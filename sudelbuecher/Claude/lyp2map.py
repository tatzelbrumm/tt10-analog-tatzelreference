#!/usr/bin/env python3
"""
lyp2map.py — Convert a KLayout .lyp layer-properties file to a gds2klayout .map file
======================================================================================

Usage
-----
    python lyp2map.py <file.lyp> [output.map]

If output.map is omitted the result is written to <stem>.map alongside the input.

LANGSEC DESIGN NOTES
--------------------
A .lyp file is KLayout's XML layer-properties format.  The grammar we care
about is a strict subset of valid .lyp XML:

    lyp_file     = <layer-properties> { properties-entry } </layer-properties>
    properties-entry = <properties>
                         <source> layer_spec </source>
                         <n>   n_string   </n>
                         { any-other-element }
                       </properties>
    layer_spec   = UINT "/" UINT [ "@" DIGIT+ ]
    n_string     = segment { "." segment }
    segment      = LETTER_OR_UNDERSCORE { LETTER_OR_DIGIT_OR_UNDERSCORE }

Only <source> and <n> are extracted; all other XML content is ignored.

REJECTION RULES (closed-world, no silent mangling):

  1. Root element MUST be <layer-properties>.  Any other root is an error.
     We do NOT fall back to searching children — that would silently accept
     .lyt files and other XML documents.

  2. <source> MUST match layer_spec exactly (anchored regex).
     Wildcards, named layers, missing text -> SKIP WITH WARNING.

  3. <n> MUST match n_string exactly (anchored regex).  Names containing
     spaces, parens, slashes, or other non-identifier characters are REJECTED
     WITH A WARNING.  We do NOT sanitize/mangle names: "nwell (60/0)" mangled
     to "nwell_60_0" could silently collide with a different layer.
     LangSec: reject malformed input; do not guess at its intent.

  4. Layer and datatype must be in [0, 4095] (GDS 12-bit limit).

  5. Duplicate (layer, datatype): first wins; subsequent emit a warning.

The XML is parsed with stdlib xml.etree.ElementTree — a conformant parser.
We do NOT regex the raw XML bytes (that would be shotgun parsing).

Dependencies: none (pure stdlib).
"""

import sys
import os
import re
import xml.etree.ElementTree as ET


# ---------------------------------------------------------------------------
# Grammar terminals
# ---------------------------------------------------------------------------

# layer_spec: "digits/digits" optionally followed by "@digits"
_SOURCE_RE = re.compile(r'^(?P<layer>\d+)/(?P<datatype>\d+)(?:@\d+)?$')

# n_string: one or more dot-separated Python-identifier segments
_SEGMENT   = r'[A-Za-z_][A-Za-z0-9_]*'
_NAME_RE   = re.compile(r'^' + _SEGMENT + r'(?:\.' + _SEGMENT + r')*$')

_UINT_MAX  = 4095   # GDS layer/datatype are 12-bit fields (Calma spec section 2.5)


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_lyp(path: str) -> list:
    """
    Parse a KLayout .lyp file and return [(layer, datatype, name), ...].

    Prints warnings to stderr for skipped entries.
    Raises SystemExit on structural errors (bad XML, wrong root element).
    """
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        raise SystemExit(f"ERROR: XML parse error in {path!r}: {e}") from e

    root = tree.getroot()

    # Rule 1: root MUST be <layer-properties>.
    if root.tag != 'layer-properties':
        raise SystemExit(
            f"ERROR: {path!r}: root element is <{root.tag}>, "
            f"expected <layer-properties>.  "
            f"Is this a standalone .lyp file rather than a .lyt?"
        )

    results = []
    seen    = {}   # (layer, datatype) -> name of first accepted entry

    for elem in root.iter('properties'):
        _process(elem, results, seen)

    return results


def _process(elem, results: list, seen: dict) -> None:
    """Extract one (layer, datatype, name) triple from a <properties> element."""

    source_el = elem.find('source')
    name_el   = elem.find('name')

    # Missing <source>: skip silently (group/header entries have none).
    if source_el is None or not (source_el.text or '').strip():
        return

    source_text = source_el.text.strip()

    # Rule 2: source must match layer_spec grammar.
    m = _SOURCE_RE.match(source_text)
    if not m:
        print(f"  skip: source {source_text!r} — not a numeric layer/datatype",
              file=sys.stderr)
        return

    layer    = int(m.group('layer'))
    datatype = int(m.group('datatype'))

    # Rule 4: range check.
    if layer > _UINT_MAX:
        print(f"  skip: layer {layer} exceeds GDS maximum {_UINT_MAX}", file=sys.stderr)
        return
    if datatype > _UINT_MAX:
        print(f"  skip: datatype {datatype} on layer {layer} "
              f"exceeds GDS maximum {_UINT_MAX}", file=sys.stderr)
        return

    # Missing <n>: skip with warning (no PDK name to emit).
    if name_el is None or not (name_el.text or '').strip():
        print(f"  skip: ({layer},{datatype}) has no <n> element", file=sys.stderr)
        return

    raw_name = name_el.text.strip()

    # Rule 3: name must satisfy n_string grammar — reject, do not mangle.
    if not _NAME_RE.match(raw_name):
        print(f"  skip: ({layer},{datatype}) name {raw_name!r} "
              f"does not match grammar (dot-separated identifiers only). "
              f"Rename it in the .lyp file if you need this layer.",
              file=sys.stderr)
        return

    key = (layer, datatype)

    # Rule 5: duplicates — first wins.
    if key in seen:
        print(f"  skip: ({layer},{datatype}) duplicate — "
              f"keeping {seen[key]!r}, ignoring {raw_name!r}", file=sys.stderr)
        return

    seen[key] = raw_name
    results.append((layer, datatype, raw_name))


# ---------------------------------------------------------------------------
# Writer
# ---------------------------------------------------------------------------

def write_map(entries: list, out_path: str, source_lyp: str) -> None:
    """Write a gds2klayout-format .map file."""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# Layer map generated from: {os.path.basename(source_lyp)}\n")
        f.write(f"# {len(entries)} entries\n")
        f.write("# Format: <GDS layer>  <GDS datatype>  <n>\n")
        f.write("#\n")
        prev_layer = None
        for (layer, datatype, name) in sorted(entries, key=lambda x: (x[0], x[1])):
            if prev_layer is not None and layer != prev_layer:
                f.write('\n')
            f.write(f"{layer:<6} {datatype:<6} {name}\n")
            prev_layer = layer
    print(f"Wrote {len(entries)} entries -> {out_path!r}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.lyp> [output.map]", file=sys.stderr)
        sys.exit(1)

    lyp_path = sys.argv[1]
    map_path = sys.argv[2] if len(sys.argv) >= 3 else (
        os.path.splitext(lyp_path)[0] + '.map'
    )

    entries = parse_lyp(lyp_path)

    if not entries:
        print(f"No usable entries in {lyp_path!r}. Check stderr for details.",
              file=sys.stderr)
        sys.exit(2)

    write_map(entries, map_path, lyp_path)


if __name__ == '__main__':
    main()
