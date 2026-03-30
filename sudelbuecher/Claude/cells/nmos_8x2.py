"""Cell: nmos_8x2
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from sky130_fd_pr__nfet_01v8_BDGNGK import build as _build_sky130_fd_pr__nfet_01v8_BDGNGK

def build(layout, L, cells):
    """Populate "nmos_8x2". cells must contain: nmos_8x2, sky130_fd_pr__nfet_01v8_BDGNGK."""
    cell = cells["nmos_8x2"]
    cell.insert(pya.DCellInstArray(
        cells["sky130_fd_pr__nfet_01v8_BDGNGK"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(1.29, 4.285))))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["sky130_fd_pr__nfet_01v8_BDGNGK"] = layout.create_cell("sky130_fd_pr__nfet_01v8_BDGNGK")
    _build_sky130_fd_pr__nfet_01v8_BDGNGK(layout, L, cells)
    cells["nmos_8x2"] = layout.create_cell("nmos_8x2")
    build(layout, L, cells)
    out = "nmos_8x2.gds"
    layout.write(out)
    print("Written:", out)
