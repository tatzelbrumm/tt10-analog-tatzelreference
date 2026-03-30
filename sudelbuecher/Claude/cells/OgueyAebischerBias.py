"""Cell: OgueyAebischerBias
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from nmos_1x80_2x import build as _build_nmos_1x80_2x
from OgueyAebischer_p7_n5 import build as _build_OgueyAebischer_p7_n5

def build(layout, L, cells):
    """Populate "OgueyAebischerBias". cells must contain: OgueyAebischerBias, nmos_1x80_2x, OgueyAebischer_p7_n5."""
    cell = cells["OgueyAebischerBias"]
    cell.insert(pya.DCellInstArray(
        cells["nmos_1x80_2x"].cell_index(),
        pya.DCplxTrans(1, 0, True,
                      pya.DVector(-1.4, -2.33))))
    cell.insert(pya.DCellInstArray(
        cells["OgueyAebischer_p7_n5"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(0, 0))))
    cell.shapes(L.L_nwell_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, 2), pya.DPoint(9.74, 2), pya.DPoint(9.74, 4.46), pya.DPoint(-1.77, 4.46), pya.DPoint(-1.77, 2)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.72, -2.03), pya.DPoint(7.6, -2.03), pya.DPoint(7.6, -1.86), pya.DPoint(6.72, -1.86), pya.DPoint(6.72, -2.03)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.99, -2.03), pya.DPoint(8.87, -2.03), pya.DPoint(8.87, -1.86), pya.DPoint(7.99, -1.86), pya.DPoint(7.99, -2.03)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(6.895, -2.03), pya.DPoint(7.065, -2.03), pya.DPoint(7.065, -1.86), pya.DPoint(6.895, -1.86), pya.DPoint(6.895, -2.03)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(7.255, -2.03), pya.DPoint(7.425, -2.03), pya.DPoint(7.425, -1.86), pya.DPoint(7.255, -1.86), pya.DPoint(7.255, -2.03)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(8.165, -2.03), pya.DPoint(8.335, -2.03), pya.DPoint(8.335, -1.86), pya.DPoint(8.165, -1.86), pya.DPoint(8.165, -2.03)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(8.525, -2.03), pya.DPoint(8.695, -2.03), pya.DPoint(8.695, -1.86), pya.DPoint(8.525, -1.86), pya.DPoint(8.525, -2.03)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.44, -1.96), pya.DPoint(-1.12, -1.96), pya.DPoint(-1.12, 1.27), pya.DPoint(-1.44, 1.27), pya.DPoint(-1.44, -1.96)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.96, -1.96), pya.DPoint(0.04, -1.96), pya.DPoint(0.04, 1.27), pya.DPoint(-0.96, 1.27), pya.DPoint(-0.96, -1.96)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.44, -2.19), pya.DPoint(0.04, -2.19), pya.DPoint(0.04, -1.96), pya.DPoint(-1.44, -1.96), pya.DPoint(-1.44, -2.19)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.44, -22.63), pya.DPoint(-1.12, -22.63), pya.DPoint(-1.12, -2.19), pya.DPoint(-1.44, -2.19), pya.DPoint(-1.44, -22.63)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.96, -2.59), pya.DPoint(0.04, -2.59), pya.DPoint(0.04, -2.19), pya.DPoint(-0.96, -2.19), pya.DPoint(-0.96, -2.59)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.31, -2.59), pya.DPoint(1.31, -2.59), pya.DPoint(1.31, -0.76), pya.DPoint(0.31, -0.76), pya.DPoint(0.31, -2.59)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, -2.59), pya.DPoint(7.66, -2.59), pya.DPoint(7.66, -1.16), pya.DPoint(6.66, -1.16), pya.DPoint(6.66, -2.59)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.93, -2.59), pya.DPoint(8.93, -2.59), pya.DPoint(8.93, -1.16), pya.DPoint(7.93, -1.16), pya.DPoint(7.93, -2.59)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.09, -22.63), pya.DPoint(9.41, -22.63), pya.DPoint(9.41, 1.27), pya.DPoint(9.09, 1.27), pya.DPoint(9.09, -22.63)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.355, 1.065), pya.DPoint(-1.205, 1.065), pya.DPoint(-1.205, 1.215), pya.DPoint(-1.355, 1.215), pya.DPoint(-1.355, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.855, 1.065), pya.DPoint(-0.705, 1.065), pya.DPoint(-0.705, 1.215), pya.DPoint(-0.855, 1.215), pya.DPoint(-0.855, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.535, 1.065), pya.DPoint(-0.385, 1.065), pya.DPoint(-0.385, 1.215), pya.DPoint(-0.535, 1.215), pya.DPoint(-0.535, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.215, 1.065), pya.DPoint(-0.065, 1.065), pya.DPoint(-0.065, 1.215), pya.DPoint(-0.215, 1.215), pya.DPoint(-0.215, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(9.175, 1.065), pya.DPoint(9.325, 1.065), pya.DPoint(9.325, 1.215), pya.DPoint(9.175, 1.215), pya.DPoint(9.175, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.415, -0.965), pya.DPoint(0.565, -0.965), pya.DPoint(0.565, -0.815), pya.DPoint(0.415, -0.815), pya.DPoint(0.415, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.735, -0.965), pya.DPoint(0.885, -0.965), pya.DPoint(0.885, -0.815), pya.DPoint(0.735, -0.815), pya.DPoint(0.735, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.055, -0.965), pya.DPoint(1.205, -0.965), pya.DPoint(1.205, -0.815), pya.DPoint(1.055, -0.815), pya.DPoint(1.055, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.765, -1.365), pya.DPoint(6.915, -1.365), pya.DPoint(6.915, -1.215), pya.DPoint(6.765, -1.215), pya.DPoint(6.765, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.085, -1.365), pya.DPoint(7.235, -1.365), pya.DPoint(7.235, -1.215), pya.DPoint(7.085, -1.215), pya.DPoint(7.085, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.405, -1.365), pya.DPoint(7.555, -1.365), pya.DPoint(7.555, -1.215), pya.DPoint(7.405, -1.215), pya.DPoint(7.405, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.035, -1.365), pya.DPoint(8.185, -1.365), pya.DPoint(8.185, -1.215), pya.DPoint(8.035, -1.215), pya.DPoint(8.035, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.355, -1.365), pya.DPoint(8.505, -1.365), pya.DPoint(8.505, -1.215), pya.DPoint(8.355, -1.215), pya.DPoint(8.355, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.675, -1.365), pya.DPoint(8.825, -1.365), pya.DPoint(8.825, -1.215), pya.DPoint(8.675, -1.215), pya.DPoint(8.675, -1.365)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, 3.87), pya.DPoint(9.74, 3.87), pya.DPoint(9.74, 4.13), pya.DPoint(-1.77, 4.13), pya.DPoint(-1.77, 3.87)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, 1.81), pya.DPoint(9.74, 1.81), pya.DPoint(9.74, 2.07), pya.DPoint(-1.77, 2.07), pya.DPoint(-1.77, 1.81)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.76, 1.41), pya.DPoint(9.74, 1.41), pya.DPoint(9.74, 1.67), pya.DPoint(-1.76, 1.67), pya.DPoint(-1.76, 1.41)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, 1.01), pya.DPoint(9.74, 1.01), pya.DPoint(9.74, 1.27), pya.DPoint(-1.77, 1.27), pya.DPoint(-1.77, 1.01)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, -1.02), pya.DPoint(9.74, -1.02), pya.DPoint(9.74, -0.76), pya.DPoint(-1.77, -0.76), pya.DPoint(-1.77, -1.02)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, -1.42), pya.DPoint(9.74, -1.42), pya.DPoint(9.74, -1.16), pya.DPoint(-1.77, -1.16), pya.DPoint(-1.77, -1.42)]))
    _txt = pya.Text("vss",
                   pya.Trans(0, False, pya.Vector(-1640, -1290)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-1.77, -1.42), pya.DPoint(-1.51, -1.42), pya.DPoint(-1.51, -1.16), pya.DPoint(-1.77, -1.16), pya.DPoint(-1.77, -1.42)]))
    _txt = pya.Text("vdd",
                   pya.Trans(0, False, pya.Vector(-1640, 4000)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-1.77, 3.87), pya.DPoint(-1.51, 3.87), pya.DPoint(-1.51, 4.13), pya.DPoint(-1.77, 4.13), pya.DPoint(-1.77, 3.87)]))
    _txt = pya.Text("vbp",
                   pya.Trans(0, False, pya.Vector(-1640, 1940)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-1.77, 1.81), pya.DPoint(-1.51, 1.81), pya.DPoint(-1.51, 2.07), pya.DPoint(-1.77, 2.07), pya.DPoint(-1.77, 1.81)]))
    _txt = pya.Text("vbn",
                   pya.Trans(0, False, pya.Vector(-1630, 1540)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-1.76, 1.41), pya.DPoint(-1.5, 1.41), pya.DPoint(-1.5, 1.67), pya.DPoint(-1.76, 1.67), pya.DPoint(-1.76, 1.41)]))
    _txt = pya.Text("vbr",
                   pya.Trans(0, False, pya.Vector(-1640, 1140)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-1.77, 1.01), pya.DPoint(-1.51, 1.01), pya.DPoint(-1.51, 1.27), pya.DPoint(-1.77, 1.27), pya.DPoint(-1.77, 1.01)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["nmos_1x80_2x"] = layout.create_cell("nmos_1x80_2x")
    _build_nmos_1x80_2x(layout, L, cells)
    cells["OgueyAebischer_p7_n5"] = layout.create_cell("OgueyAebischer_p7_n5")
    _build_OgueyAebischer_p7_n5(layout, L, cells)
    cells["OgueyAebischerBias"] = layout.create_cell("OgueyAebischerBias")
    build(layout, L, cells)
    out = "OgueyAebischerBias.gds"
    layout.write(out)
    print("Written:", out)
