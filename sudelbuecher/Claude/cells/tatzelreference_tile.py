"""Cell: tatzelreference_tile
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from shortpmos_2x import build as _build_shortpmos_2x
from shortnmos_2x import build as _build_shortnmos_2x
from sky130_fd_pr__nfet_01v8_BDGNGK import build as _build_sky130_fd_pr__nfet_01v8_BDGNGK
from nmos_8x2 import build as _build_nmos_8x2
from flatpmos1x0_3 import build as _build_flatpmos1x0_3
from ToBiasStartup import build as _build_ToBiasStartup
from nmos1x20_8x import build as _build_nmos1x20_8x
from nmos_1x80_2x import build as _build_nmos_1x80_2x
from pmos_7x import build as _build_pmos_7x
from nmos_5x import build as _build_nmos_5x
from OgueyAebischer_p7_n5 import build as _build_OgueyAebischer_p7_n5
from OgueyAebischerBias import build as _build_OgueyAebischerBias
from reference import build as _build_reference

def build(layout, L, cells):
    """Populate "tatzelreference_tile". cells must contain: tatzelreference_tile, reference."""
    cell = cells["tatzelreference_tile"]
    cell.insert(pya.DCellInstArray(
        cells["reference"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(45.33, 32.22))))
    cell.shapes(L.L_235_4).insert(
        pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
    cell.shapes(L.L_81_53).insert(
        pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 2), pya.DPoint(39.57, 2), pya.DPoint(39.57, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 2), pya.DPoint(58.89, 2), pya.DPoint(58.89, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 2), pya.DPoint(78.21, 2), pya.DPoint(78.21, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 2), pya.DPoint(97.53, 2), pya.DPoint(97.53, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 2), pya.DPoint(116.85, 2), pya.DPoint(116.85, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 2), pya.DPoint(136.17, 2), pya.DPoint(136.17, 0)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["shortpmos_2x"] = layout.create_cell("shortpmos_2x")
    _build_shortpmos_2x(layout, L, cells)
    cells["shortnmos_2x"] = layout.create_cell("shortnmos_2x")
    _build_shortnmos_2x(layout, L, cells)
    cells["sky130_fd_pr__nfet_01v8_BDGNGK"] = layout.create_cell("sky130_fd_pr__nfet_01v8_BDGNGK")
    _build_sky130_fd_pr__nfet_01v8_BDGNGK(layout, L, cells)
    cells["nmos_8x2"] = layout.create_cell("nmos_8x2")
    _build_nmos_8x2(layout, L, cells)
    cells["flatpmos1x0_3"] = layout.create_cell("flatpmos1x0_3")
    _build_flatpmos1x0_3(layout, L, cells)
    cells["ToBiasStartup"] = layout.create_cell("ToBiasStartup")
    _build_ToBiasStartup(layout, L, cells)
    cells["nmos1x20_8x"] = layout.create_cell("nmos1x20_8x")
    _build_nmos1x20_8x(layout, L, cells)
    cells["nmos_1x80_2x"] = layout.create_cell("nmos_1x80_2x")
    _build_nmos_1x80_2x(layout, L, cells)
    cells["pmos_7x"] = layout.create_cell("pmos_7x")
    _build_pmos_7x(layout, L, cells)
    cells["nmos_5x"] = layout.create_cell("nmos_5x")
    _build_nmos_5x(layout, L, cells)
    cells["OgueyAebischer_p7_n5"] = layout.create_cell("OgueyAebischer_p7_n5")
    _build_OgueyAebischer_p7_n5(layout, L, cells)
    cells["OgueyAebischerBias"] = layout.create_cell("OgueyAebischerBias")
    _build_OgueyAebischerBias(layout, L, cells)
    cells["reference"] = layout.create_cell("reference")
    _build_reference(layout, L, cells)
    cells["tatzelreference_tile"] = layout.create_cell("tatzelreference_tile")
    build(layout, L, cells)
    out = "tatzelreference_tile.gds"
    layout.write(out)
    print("Written:", out)
