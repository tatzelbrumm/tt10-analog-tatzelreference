"""Cell: flatpmos1x0_3
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers

def build(layout, L, cells):
    """Populate "flatpmos1x0_3"."""
    cell = cells["flatpmos1x0_3"]

if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["flatpmos1x0_3"] = layout.create_cell("flatpmos1x0_3")
    build(layout, L, cells)
    out = "flatpmos1x0_3.gds"
    layout.write(out)
    print("Written:", out)
