#!/usr/bin/env python3
"""
split_klayout_cells.py
----------------------
Splits a gds2klayout-generated KLayout Python script into one file per cell.

Each cell file is:
  - STANDALONE: run directly in KLayout (Macros -> Run Script) to view that cell
  - IMPORTABLE: main_ihp.py imports build() from each file to assemble the hierarchy

The __name__ == "__main__" guard (like xschem's top-level-only execution) means
the standalone block is silently skipped when the file is imported by main_ihp.py.

Usage:
    python split_klayout_cells.py tt_um_tatzelreference_klayout.py

Outputs:
    cells/
        layers.py          <- layer index variables (edit this for IHP)
        shortpmos_2x.py    <- standalone + importable
        ...
    main_ihp.py            <- assembles full hierarchy
"""

import re
import sys
from pathlib import Path

CELL_MARKER = re.compile(r'^# === (.+) === *$')
LAYER_DEF    = re.compile(r'^(L_\w+)\s*=\s*layout\.layer\(')
CELL_DECL    = re.compile(r'^cell_(\w+)\s*=\s*layout\.create_cell\(')


def sanitize(name):
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)


def parse_script(path):
    with open(path) as f:
        raw = f.readlines()

    header_lines = []
    layer_lines  = []
    cell_decls   = []
    cell_bodies  = {}
    current_cell = None
    in_header    = True

    for line in raw:
        stripped = line.rstrip('\n')

        if LAYER_DEF.match(stripped):
            layer_lines.append(line)
            if in_header:
                header_lines.append(line)
            continue

        m = CELL_DECL.match(stripped)
        if m:
            cell_decls.append(m.group(1))
            if in_header:
                header_lines.append(line)
            continue

        m = CELL_MARKER.match(stripped)
        if m:
            in_header = False
            current_cell = m.group(1)
            cell_bodies.setdefault(current_cell, [])
            continue

        if in_header:
            header_lines.append(line)
            continue

        if current_cell is not None:
            # Skip bare layout.write(...) footer lines that gds2klayout appends
            import re as _re
            if not _re.match(r'^layout\.', line.strip()):
                cell_bodies[current_cell].append(line)

    return header_lines, layer_lines, cell_decls, cell_bodies


def write_layers_module(out_dir, layer_lines):
    lines = [
        "# layers.py  -  edit THIS file to remap sky130 layers to IHP sg13g2\n",
        "# Format: L_<name> = layout.layer(layer, datatype)\n",
        "#\n",
        "# sky130 -> IHP sg13g2 quick reference:\n",
        "#   nwell.drawing  (64/20)  -> NWell.drawing      (31/0)\n",
        "#   diff.drawing   (65/20)  -> Activ.drawing       (1/0)\n",
        "#   tap.drawing    (65/44)  -> Activ.drawing       (1/0)\n",
        "#   poly.drawing   (66/20)  -> GatPoly.drawing     (5/0)\n",
        "#   licon1.drawing (66/44)  -> Cont.drawing        (6/0)\n",
        "#   li1.drawing    (67/20)  -> Metal1.drawing      (8/0)  [no li1 in IHP]\n",
        "#   mcon.drawing   (67/44)  -> Via1.drawing       (19/0)\n",
        "#   met1.drawing   (68/20)  -> Metal1.drawing      (8/0)\n",
        "#   via.drawing    (68/44)  -> Via1.drawing       (19/0)\n",
        "#   met2.drawing   (69/20)  -> Metal2.drawing     (10/0)\n",
        "#   met4.drawing   (71/20)  -> Metal4.drawing     (50/0)\n",
        "#   nsdm.drawing   (93/44)  -> nSD.drawing         (7/0)\n",
        "#   psdm.drawing   (94/20)  -> pSD.drawing        (14/0)\n",
        "#\n",
        "import pya\n",
        "\n",
        "def register_layers(layout):\n",
        "    class Layers: pass\n",
        "    L = Layers()\n",
    ]
    for ll in layer_lines:
        # Verbatim emit — handles both numeric layout.layer(n, d)
        # and named layout.layer(pya.LayerInfo(n, d, "name")) forms.
        m = re.match(r'\s*(L_\w+)\s*=(.*)', ll.rstrip())
        if m:
            var, rhs = m.group(1), m.group(2)
            lines.append(f"    L.{var} ={rhs}\n")
    lines.append("    return L\n")
    (out_dir / "layers.py").write_text("".join(lines))
    print(f"  wrote {out_dir}/layers.py")


def _direct_deps(body_lines, self_safe):
    """Return list of cell names directly instantiated in body_lines."""
    deps = []
    for line in body_lines:
        m = re.search(r'cell_(\w+)\.cell_index\(\)', line)
        if m:
            ref = m.group(1)
            if ref != self_safe and ref not in deps:
                deps.append(ref)
    return deps


def _transitive_deps(cell_name, all_bodies, visited=None):
    """Return all dependencies of cell_name in topological order (leaves first)."""
    if visited is None:
        visited = []
    safe = sanitize(cell_name)
    body = all_bodies.get(cell_name, [])
    for dep in _direct_deps(body, safe):
        if dep not in visited:
            _transitive_deps(dep, all_bodies, visited)
            if dep not in visited:
                visited.append(dep)
    return visited


def write_cell_module(out_dir, cell_name, body_lines, all_bodies):
    """Write one cells/<cell>.py - standalone runnable AND importable."""
    safe = sanitize(cell_name)
    fname = out_dir / f"{safe}.py"

    # Direct deps (for imports at top of file)
    referenced = _direct_deps(body_lines, safe)
    # Full transitive deps (for standalone block — must create entire sub-tree)
    all_deps = _transitive_deps(cell_name, all_bodies)

    out = []
    w = out.append

    w(f'"""Cell: {cell_name}\n')
    w(f'Standalone : run in KLayout (Macros -> Run Script) to view just this cell.\n')
    w(f'Importable : main_ihp.py imports build() to assemble the full hierarchy.\n')
    w(f'"""\n')
    w('import pya\n')
    w('import sys, os\n')
    w('sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n')
    w('from layers import register_layers\n')
    for ref in all_deps:
        w(f'from {ref} import build as _build_{ref}\n')
    w('\n')

    # build() function — called by both standalone block and main_ihp.py
    w('def build(layout, L, cells):\n')
    if referenced:
        w(f'    """Populate "{cell_name}". cells must contain: {cell_name}, {", ".join(referenced)}."""\n')
    else:
        w(f'    """Populate "{cell_name}"."""\n')
    w(f'    cell = cells["{cell_name}"]\n')

    for raw_line in body_lines:
        if raw_line.strip() == "" or raw_line.strip().startswith("#"):
            out.append(raw_line)
            continue
        # Replace this cell's var with 'cell'
        rewritten = re.sub(rf'\bcell_{re.escape(safe)}\b', 'cell', raw_line)
        # Replace other cell vars with cells["name"]
        rewritten = re.sub(r'(?<!\.)\bcell_(\w+)\b',
                           lambda m: f'cells["{m.group(1)}"]', rewritten)
        # Replace layer vars with L.L_xx_yy
        rewritten = re.sub(r'\b(L_\w+)\b', r'L.\1', rewritten)
        out.append("    " + rewritten)

    # Standalone block — skipped on import, only runs when file is executed directly
    w('\n')
    w('if __name__ == "__main__":\n')
    w('    # This block only runs when you open this file in KLayout and hit Run.\n')
    w('    # It is silently skipped when main_ihp.py imports this module.\n')
    w('    layout = pya.Layout()\n')
    w('    layout.dbu = 0.001\n')
    w('    L = register_layers(layout)\n')
    w('    cells = {}\n')
    # Build entire sub-tree first (topological order, leaves first)
    for ref in all_deps:
        w(f'    cells["{ref}"] = layout.create_cell("{ref}")\n')
        w(f'    _build_{ref}(layout, L, cells)\n')
    w(f'    cells["{cell_name}"] = layout.create_cell("{cell_name}")\n')
    w('    build(layout, L, cells)\n')
    w(f'    out = "{safe}.gds"\n')
    w('    layout.write(out)\n')
    w('    print("Written:", out)\n')

    fname.write_text("".join(out))
    print(f"  wrote {fname}")


def write_main(out_path, cell_order):
    """Write main_ihp.py — imports build() from each cell module."""
    safenames = [(c, sanitize(c)) for c in cell_order]

    out = []
    w = out.append

    w('"""main_ihp.py\n')
    w('Assembles the full layout by importing build() from each cell module.\n')
    w('Run in KLayout (Macros -> Run Script) or on the command line:\n')
    w('    python main_ihp.py\n')
    w('"""\n')
    w('import pya\n')
    w('import sys, os\n')
    w('sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "cells"))\n')
    w('from layers import register_layers\n')
    for cname, safe in safenames:
        w(f'from {safe} import build as build_{safe}\n')
    w('\n')
    w('layout = pya.Layout()\n')
    w('layout.dbu = 0.001\n')
    w('L = register_layers(layout)\n')
    w('\n')
    w('cells = {}\n')
    for cname, safe in safenames:
        w(f'cells["{cname}"] = layout.create_cell("{cname}")\n')
    w('\n')
    w('# Populate in declaration order (leaf cells first)\n')
    for cname, safe in safenames:
        w(f'build_{safe}(layout, L, cells)\n')
    w('\n')
    w('layout.write("output_ihp.gds")\n')
    w('print("Written: output_ihp.gds")\n')

    out_path.write_text("".join(out))
    print(f"  wrote {out_path}")


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
        write_cell_module(out_dir, cname, cell_bodies.get(cname, []), cell_bodies)

    print("Writing main_ihp.py ...")
    write_main(Path("main_ihp.py"), cell_order)

    print(f"\nDone. {len(cell_order)} cells split into cells/")
    print("Each cell file is standalone (run in KLayout) AND importable by main_ihp.py.")
    print("The if __name__ == '__main__' guard keeps them separate — no code duplication.")

if __name__ == "__main__":
    main()
