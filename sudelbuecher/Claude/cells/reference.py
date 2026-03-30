"""Cell: reference
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from ToBiasStartup import build as _build_ToBiasStartup
from OgueyAebischerBias import build as _build_OgueyAebischerBias

def build(layout, L, cells):
    """Populate "reference". cells must contain: reference, ToBiasStartup, OgueyAebischerBias."""
    cell = cells["reference"]
    cell.insert(pya.DCellInstArray(
        cells["ToBiasStartup"].cell_index(),
        pya.DCplxTrans(1, 180, True,
                      pya.DVector(-4.06, 0))))
    cell.insert(pya.DCellInstArray(
        cells["OgueyAebischerBias"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(0, 0))))
    _txt = pya.Text("vss",
                   pya.Trans(0, False, pya.Vector(-6275, -1290)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, -1.42), pya.DPoint(-6.14, -1.42), pya.DPoint(-6.14, -1.16), pya.DPoint(-6.41, -1.16), pya.DPoint(-6.41, -1.42)]))
    _txt = pya.Text("vdd",
                   pya.Trans(0, False, pya.Vector(-6275, 4000)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, 3.87), pya.DPoint(-6.14, 3.87), pya.DPoint(-6.14, 4.13), pya.DPoint(-6.41, 4.13), pya.DPoint(-6.41, 3.87)]))
    _txt = pya.Text("vbp",
                   pya.Trans(0, False, pya.Vector(-6275, 1940)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, 1.81), pya.DPoint(-6.14, 1.81), pya.DPoint(-6.14, 2.07), pya.DPoint(-6.41, 2.07), pya.DPoint(-6.41, 1.81)]))
    _txt = pya.Text("vbn",
                   pya.Trans(0, False, pya.Vector(-6275, 1540)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, 1.41), pya.DPoint(-6.14, 1.41), pya.DPoint(-6.14, 1.67), pya.DPoint(-6.41, 1.67), pya.DPoint(-6.41, 1.41)]))
    _txt = pya.Text("vbr",
                   pya.Trans(0, False, pya.Vector(-6275, 1140)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, 1.01), pya.DPoint(-6.14, 1.01), pya.DPoint(-6.14, 1.27), pya.DPoint(-6.41, 1.27), pya.DPoint(-6.41, 1.01)]))
    _txt = pya.Text("disable",
                   pya.Trans(0, False, pya.Vector(-6275, 740)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-6.41, 0.61), pya.DPoint(-6.14, 0.61), pya.DPoint(-6.14, 0.87), pya.DPoint(-6.41, 0.87), pya.DPoint(-6.41, 0.61)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["ToBiasStartup"] = layout.create_cell("ToBiasStartup")
    _build_ToBiasStartup(layout, L, cells)
    cells["OgueyAebischerBias"] = layout.create_cell("OgueyAebischerBias")
    _build_OgueyAebischerBias(layout, L, cells)
    cells["reference"] = layout.create_cell("reference")
    build(layout, L, cells)
    out = "reference.gds"
    layout.write(out)
    print("Written:", out)
