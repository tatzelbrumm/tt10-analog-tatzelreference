"""
split_klayout_cells.py
----------------------
Splits a gds2klayout-generated KLayout Python script into one file per cell,
plus a main_ihp.py that reassembles the layout.

Usage:
    python split_klayout_cells.py tt_um_tatzelreference_klayout.py

Outputs:
    cells/
        layers.py          <- layer index variables (edit this for IHP)
        shortpmos_2x.py
        shortnmos_2x.py
        ... (one file per cell)
    main_ihp.py            <- assembles everything, writes output.gds
"""

import re
import os
import sys
from pathlib import Path

# ── helpers ──────────────────────────────────────────────────────────────────

CELL_MARKER = re.compile(r'^# === (.+) === *$')
LAYER_DEF    = re.compile(r'^(L_\w+)\s*=\s*layout\.layer\(')
CELL_DECL    = re.compile(r'^cell_(\w+)\s*=\s*layout\.create_cell\(')
CELL_SHAPE   = re.compile(r'^(cell_(\w+))\.')
CELL_INSERT  = re.compile(r'^(cell_(\w+))\.insert\(')

def sanitize(name: str) -> str:
    """Turn a cell name into a valid Python identifier for use as filename."""
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)

def parse_script(path: str):
    """
    Returns:
        header_lines  : lines before the first cell declaration
        layer_lines   : only the L_xx_yy = layout.layer(...) lines
        cell_order    : list of cell names in declaration order
        cell_bodies   : dict  cellname -> list of body lines
    """
    with open(path) as f:
        raw = f.readlines()

    header_lines = []
    layer_lines  = []
    cell_decls   = []   # ordered list of cell names
    cell_bodies  = {}   # cellname -> [lines]

    current_cell = None
    in_header    = True

    for line in raw:
        stripped = line.rstrip('\n')

        # Collect layer definitions (can appear anywhere before first === block)
        if LAYER_DEF.match(stripped):
            layer_lines.append(line)
            if in_header:
                header_lines.append(line)
            continue

        # Cell declarations section
        m = CELL_DECL.match(stripped)
        if m:
            cname = m.group(1)
            cell_decls.append(cname)
            if in_header:
                header_lines.append(line)
            continue

        # === cell section marker ===
        m = CELL_MARKER.match(stripped)
        if m:
            in_header = False
            current_cell = m.group(1)
            # Normalise cell name to Python identifier for dict key
            cell_bodies.setdefault(current_cell, [])
            continue

        # Still in header boilerplate
        if in_header:
            header_lines.append(line)
            continue

        # Body line belonging to current cell
        if current_cell is not None:
            cell_bodies[current_cell].append(line)

    return header_lines, layer_lines, cell_decls, cell_bodies

def write_layers_module(out_dir: Path, layer_lines: list):
    """Write cells/layers.py – the single place to edit layer numbers for IHP."""
    lines = [
        "# layers.py  –  edit THIS file to remap sky130 layers to IHP sg13g2\n",
        "# Format: L_<GDS_layer>_<GDS_datatype> = layout.layer(layer, datatype)\n",
        "# Replace the (layer, datatype) pairs with IHP equivalents.\n",
        "#\n",
        "# sky130 → IHP sg13g2 mapping hints (fill in IHP numbers from sg13g2 PDK docs):\n",
        "#   64/20  nwell       → IHP NWell          (?/0)\n",
        "#   65/20  diff/active → IHP Activ           (1/0)\n",
        "#   65/44  tap         → IHP Activ           (1/0)  [same layer, no tap distinction]\n",
        "#   66/20  poly        → IHP GatPoly         (5/0)\n",
        "#   66/44  contact     → IHP Cont            (6/0)\n",
        "#   67/20  li1         → IHP (no li1 equiv – use Metal1 or merge into contact)\n",
        "#   67/44  mcon        → IHP Via1            (19/0)\n",
        "#   68/20  met1        → IHP Metal1          (8/0)\n",
        "#   68/44  via1        → IHP Via1            (19/0)\n",
        "#   69/20  met2        → IHP Metal2          (10/0)\n",
        "#   71/20  met4        → IHP Metal4          (?) – check PDK\n",
        "#   93/44  nsdm        → IHP nSD             (?) \n",
        "#   94/20  psdm        → IHP pSD             (?)\n",
        "#   81/53  areaid      → IHP prBoundary / TT keepout\n",
        "#   235/4  prBoundary  → IHP prBoundary\n",
        "#\n",
        "# NOTE: sky130 li1 (local interconnect) has no direct IHP equivalent.\n",
        "# Geometry on li1 must be re-drawn using Metal1 with IHP DRC clearances.\n",
        "\n",
        "import pya\n",
        "\n",
        "def register_layers(layout):\n",
        "    \"\"\"Call this once with your pya.Layout() instance.\n",
        "       Returns a namespace object with all layer index variables.\"\"\"\n",
        "    class Layers: pass\n",
        "    L = Layers()\n",
    ]
    for ll in layer_lines:
        # e.g.  L_64_20 = layout.layer(64, 20)
        m = re.match(r'^\s*(L_\w+)\s*=\s*layout\.layer\((\d+),\s*(\d+)\)', ll)
        if m:
            var, gds_l, gds_d = m.group(1), m.group(2), m.group(3)
            lines.append(
                f"    L.{var} = layout.layer({gds_l}, {gds_d})"
                f"  # sky130 {gds_l}/{gds_d} – TODO remap for IHP\n"
            )
    lines += [
        "    return L\n",
    ]
    (out_dir / "layers.py").write_text("".join(lines))
    print(f"  wrote {out_dir}/layers.py")

def write_cell_module(out_dir: Path, cell_name: str, body_lines: list, all_cells: list):
    """Write one cells/<cell>.py file."""
    safe = sanitize(cell_name)
    fname = out_dir / f"{safe}.py"

    # Detect which other cells this cell references (for the import comment)
    referenced = []
    for line in body_lines:
        m = re.search(r'cell_(\w+)\.cell_index\(\)', line)
        if m:
            ref = m.group(1)
            if ref != safe and ref not in referenced:
                referenced.append(ref)

    lines = [
        f'"""Cell: {cell_name}"""\n',
        "# Auto-generated by split_klayout_cells.py\n",
        "# Edit geometry here after layer remapping.\n",
    ]
    if referenced:
        lines += [
            f"# This cell instantiates: {', '.join(referenced)}\n",
        ]
    lines += ["\nimport pya\n\n"]

    lines.append(f"def build_{safe}(cell, L, cells):\n")
    lines.append(f'    """Populate cell "{cell_name}" with shapes and sub-cell instances.\n')
    lines.append(f'    Args:\n')
    lines.append(f'        cell  – pya.Cell for "{cell_name}"\n')
    lines.append(f'        L     – layers namespace from layers.register_layers()\n')
    lines.append(f'        cells – dict of all cell objects keyed by cell name\n')
    lines.append(f'    """\n')

    # Rewrite body lines: replace bare `cell_foo` references
    for raw_line in body_lines:
        if raw_line.strip() == "" or raw_line.strip().startswith("#"):
            lines.append(raw_line)
            continue

        # Replace cell_<thisname> with cell (the function parameter)
        rewritten = re.sub(
            rf'\bcell_{re.escape(safe)}\b',
            'cell',
            raw_line
        )
        # Replace remaining cell_<othername> with cells["othername"]
        # Negative lookbehind for '.' to avoid matching .cell_index() etc.
        def replace_other(m):
            other = m.group(1)
            return f'cells["{other}"]'
        rewritten = re.sub(r'(?<!\.)\bcell_(\w+)\b', replace_other, rewritten)
        # Replace bare layer variables L_xx_yy with L.L_xx_yy
        rewritten = re.sub(r'\b(L_\w+)\b', r'L.\1', rewritten)
        lines.append("    " + rewritten)

    (fname).write_text("".join(lines))
    print(f"  wrote {fname}")

def write_main(out_path: Path, cell_order: list, layer_lines: list):
    """Write main_ihp.py that imports all cell modules and writes output.gds."""
    safenames = [(c, sanitize(c)) for c in cell_order]

    lines = [
        '"""main_ihp.py\n',
        'Assembles the full layout from per-cell modules.\n',
        'Run in KLayout via: Macros → Run Script, or from command line:\n',
        '    python main_ihp.py\n',
        '"""\n\n',
        'import pya\n',
        'import sys, os\n',
        'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "cells"))\n\n',
        'from layers import register_layers\n',
    ]
    for cname, safe in safenames:
        lines.append(f'from {safe} import build_{safe}\n')

    lines += [
        '\n# ── setup ────────────────────────────────────────────────────────────\n',
        'layout = pya.Layout()\n',
        'layout.dbu = 0.001\n',
        'L = register_layers(layout)\n\n',
        '# ── cell declarations ────────────────────────────────────────────────\n',
        'cells = {}\n',
    ]
    for cname, safe in safenames:
        lines.append(f'cells["{cname}"] = layout.create_cell("{cname}")\n')

    lines += [
        '\n# ── populate cells (leaf → top order) ───────────────────────────────\n',
        '# Cells are built in declaration order; adjust if you see missing refs.\n',
    ]
    for cname, safe in safenames:
        lines.append(f'build_{safe}(cells["{cname}"], L, cells)\n')

    lines += [
        '\n# ── write output ────────────────────────────────────────────────────\n',
        'output_file = "output_ihp.gds"\n',
        'layout.write(output_file)\n',
        'print(f"Written: {output_file}")\n',
    ]
    out_path.write_text("".join(lines))
    print(f"  wrote {out_path}")

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python split_klayout_cells.py <input_klayout_script.py>")
        sys.exit(1)

    src = sys.argv[1]
    print(f"Parsing {src} ...")
    header_lines, layer_lines, cell_order, cell_bodies = parse_script(src)

    out_dir = Path("cells")
    out_dir.mkdir(exist_ok=True)

    print("Writing layer module ...")
    write_layers_module(out_dir, layer_lines)

    print("Writing cell modules ...")
    for cname in cell_order:
        body = cell_bodies.get(cname, [])
        write_cell_module(out_dir, cname, body, cell_order)

    print("Writing main_ihp.py ...")
    write_main(Path("main_ihp.py"), cell_order, layer_lines)

    print(f"\nDone. {len(cell_order)} cells split into cells/")
    print("Next steps:")
    print("  1. Edit cells/layers.py  – fill in IHP sg13g2 layer numbers")
    print("  2. Replace sky130_fd_pr__nfet_01v8_BDGNGK with IHP NFET PCell")
    print("  3. Run main_ihp.py in KLayout, then DRC with sg13g2 deck")
    print("  4. Fix DRC violations cell by cell, starting with the leaf cells")

if __name__ == "__main__":
    main()
