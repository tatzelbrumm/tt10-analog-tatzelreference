#!/usr/bin/env python3
"""
lyp2map.py — Convert a KLayout .lyp layer-properties file to a gds2klayout .map file
======================================================================================

Usage
-----
    python lyp2map.py <file.lyp> [output.map]

If output.map is omitted the result is written to <stem>.map in the same
directory as the input file.

LANGSEC DESIGN NOTES
--------------------
A .lyp file is KLayout's XML layer-properties format.  The grammar we care
about is a strict subset:

    lyp          = <layer-properties> { properties-entry } </layer-properties>
    properties-entry = <properties>
                         <source> layer_spec </source>
                         <name>   string      </name>
                         ...
                       </properties>
    layer_spec   = UINT "/" UINT [ "@" index ]   |   "*/*"   |   "*"

We extract only <source> and <name> from each <properties> block.
All other XML content is accepted but ignored (we do not need it).

Rejection rules (closed-world):
  - <source> values that are not numeric "layer/datatype" (e.g. wildcards
    "*/*", named layers, or absent values) are skipped with a warning —
    they carry no GDS layer identity.
  - <name> values whose dot-separated segments are not all valid Python
    identifiers are skipped with a warning — they would be unrepresentable
    as variable names in the generated script.
  - Duplicate (layer, datatype) entries are skipped (first wins, matching
    KLayout's own precedence rule for duplicate layer specs in a .lyp).

The parser uses Python's stdlib xml.etree.ElementTree, which is a
well-tested conformant XML parser.  We do NOT use regex on the raw XML
text — that would be shotgun parsing.

Dependencies: none (pure stdlib).
"""

import sys
import os
import re
import xml.etree.ElementTree as ET


# ---------------------------------------------------------------------------
# Grammar for layer_spec values extracted from <source>
# The format is "layer/datatype" optionally followed by "@n" (view index).
# ---------------------------------------------------------------------------
_SOURCE_RE = re.compile(r'^(\d+)/(\d+)(?:@\d+)?$')
_UINT_MAX  = 4095

# Grammar for names: dot-separated Python-identifier segments
_SEG_RE    = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')


def _valid_name(name: str) -> bool:
    """Return True if name is one or more dot-separated identifier segments."""
    if not name:
        return False
    return all(_SEG_RE.match(seg) for seg in name.split('.'))


def _sanitize_name(name: str) -> str:
    """
    Make a name safe for our map format:
      - strip leading/trailing whitespace
      - replace internal whitespace runs with underscores
      - replace slashes, colons, parens with underscores

    This handles names like "nwell (60/0)" or "met1 drawing" that appear
    in some PDK lyp files.  After sanitization the name must still pass
    _valid_name(); if not, the entry is skipped.
    """
    name = name.strip()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[/:\\(){}[\]<>!@#$%^&*+=|,;?\'"` ]', '_', name)
    # collapse multiple underscores
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name


def parse_lyp(path: str) -> list:
    """
    Parse a KLayout .lyp file and return a list of (layer, datatype, name)
    triples, in document order.

    Skips entries that have no numeric layer/datatype or no usable name.
    Skips duplicate (layer, datatype) pairs (first occurrence wins).
    """
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        raise SystemExit(f"XML parse error in {path!r}: {e}") from e

    root = tree.getroot()

    # The root may be <layer-properties> directly, or the file may wrap it.
    # Handle both.
    if root.tag == 'layer-properties':
        entries_root = root
    else:
        entries_root = root.find('layer-properties')
        if entries_root is None:
            raise SystemExit(
                f"{path!r}: no <layer-properties> element found — "
                f"is this a valid KLayout .lyp file?"
            )

    results = []
    seen    = {}   # (layer, datatype) -> first name seen

    def process_properties(elem):
        """Extract one layer entry from a <properties> element."""
        source_el = elem.find('source')
        name_el   = elem.find('name')

        if source_el is None or not (source_el.text or '').strip():
            return  # no source — skip silently
        if name_el is None or not (name_el.text or '').strip():
            return  # no name — skip silently

        source_text = source_el.text.strip()
        raw_name    = name_el.text.strip()

        # Parse source — must be "layer/datatype[@n]"
        m = _SOURCE_RE.match(source_text)
        if not m:
            # Wildcard, named layer, or other non-numeric spec — skip
            return

        layer    = int(m.group(1))
        datatype = int(m.group(2))

        if layer > _UINT_MAX or datatype > _UINT_MAX:
            print(f"  warning: skipping {source_text!r} — value exceeds GDS maximum {_UINT_MAX}",
                  file=sys.stderr)
            return

        # Sanitize and validate name
        name = _sanitize_name(raw_name)
        if not _valid_name(name):
            print(f"  warning: skipping ({layer},{datatype}) — "
                  f"name {raw_name!r} cannot be made into a valid identifier",
                  file=sys.stderr)
            return

        key = (layer, datatype)
        if key in seen:
            # Duplicate — first wins, warn
            print(f"  warning: duplicate ({layer},{datatype}): "
                  f"keeping {seen[key]!r}, ignoring {name!r}",
                  file=sys.stderr)
            return

        seen[key] = name
        results.append((layer, datatype, name))

    # Walk all <properties> elements, including those nested inside groups
    for elem in entries_root.iter('properties'):
        process_properties(elem)

    return results


def write_map(entries: list, out_path: str, source_lyp: str) -> None:
    """Write a gds2klayout-format .map file."""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# Layer map generated from: {os.path.basename(source_lyp)}\n")
        f.write(f"# {len(entries)} entries\n")
        f.write(f"# Format: <GDS layer>  <GDS datatype>  <name>\n")
        f.write(f"#\n")

        # Group by layer number for readability
        prev_layer = None
        for (layer, datatype, name) in sorted(entries, key=lambda x: (x[0], x[1])):
            if prev_layer is not None and layer != prev_layer:
                f.write('\n')
            f.write(f"{layer:<6} {datatype:<6} {name}\n")
            prev_layer = layer

    print(f"Wrote {len(entries)} entries to {out_path!r}")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.lyp> [output.map]", file=sys.stderr)
        sys.exit(1)

    lyp_path = sys.argv[1]
    if len(sys.argv) >= 3:
        map_path = sys.argv[2]
    else:
        stem     = os.path.splitext(lyp_path)[0]
        map_path = stem + '.map'

    entries = parse_lyp(lyp_path)

    if not entries:
        print(f"No usable layer entries found in {lyp_path!r} — is this a valid .lyp file?",
              file=sys.stderr)
        sys.exit(2)

    write_map(entries, map_path, lyp_path)


if __name__ == '__main__':
    main()
