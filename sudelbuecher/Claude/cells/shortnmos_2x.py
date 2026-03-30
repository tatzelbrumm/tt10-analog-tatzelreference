"""Cell: shortnmos_2x
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers

def build(layout, L, cells):
    """Populate "shortnmos_2x"."""
    cell = cells["shortnmos_2x"]
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.14, -0.44), pya.DPoint(-0.14, -0.44), pya.DPoint(-0.14, 0.44), pya.DPoint(-1.14, 0.44), pya.DPoint(-1.14, -0.44)]))
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(0.14, -0.44), pya.DPoint(1.14, -0.44), pya.DPoint(1.14, 0.44), pya.DPoint(0.14, 0.44), pya.DPoint(0.14, -0.44)]))
    cell.shapes(L.L_nsdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.265, -0.565), pya.DPoint(1.265, -0.565), pya.DPoint(1.265, 0.565), pya.DPoint(-1.265, 0.565), pya.DPoint(-1.265, -0.565)]))
    cell.shapes(L.L_poly_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.27, -0.15), pya.DPoint(1.27, -0.15), pya.DPoint(1.27, 0.15), pya.DPoint(-1.27, 0.15), pya.DPoint(-1.27, -0.15)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.065, 0.21), pya.DPoint(-0.895, 0.21), pya.DPoint(-0.895, 0.38), pya.DPoint(-1.065, 0.38), pya.DPoint(-1.065, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.725, 0.21), pya.DPoint(-0.555, 0.21), pya.DPoint(-0.555, 0.38), pya.DPoint(-0.725, 0.38), pya.DPoint(-0.725, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.385, 0.21), pya.DPoint(-0.215, 0.21), pya.DPoint(-0.215, 0.38), pya.DPoint(-0.385, 0.38), pya.DPoint(-0.385, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.215, 0.21), pya.DPoint(0.385, 0.21), pya.DPoint(0.385, 0.38), pya.DPoint(0.215, 0.38), pya.DPoint(0.215, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.555, 0.21), pya.DPoint(0.725, 0.21), pya.DPoint(0.725, 0.38), pya.DPoint(0.555, 0.38), pya.DPoint(0.555, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.895, 0.21), pya.DPoint(1.065, 0.21), pya.DPoint(1.065, 0.38), pya.DPoint(0.895, 0.38), pya.DPoint(0.895, 0.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.065, -0.38), pya.DPoint(-0.895, -0.38), pya.DPoint(-0.895, -0.21), pya.DPoint(-1.065, -0.21), pya.DPoint(-1.065, -0.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.725, -0.38), pya.DPoint(-0.555, -0.38), pya.DPoint(-0.555, -0.21), pya.DPoint(-0.725, -0.21), pya.DPoint(-0.725, -0.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.385, -0.38), pya.DPoint(-0.215, -0.38), pya.DPoint(-0.215, -0.21), pya.DPoint(-0.385, -0.21), pya.DPoint(-0.385, -0.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.215, -0.38), pya.DPoint(0.385, -0.38), pya.DPoint(0.385, -0.21), pya.DPoint(0.215, -0.21), pya.DPoint(0.215, -0.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.555, -0.38), pya.DPoint(0.725, -0.38), pya.DPoint(0.725, -0.21), pya.DPoint(0.555, -0.21), pya.DPoint(0.555, -0.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.895, -0.38), pya.DPoint(1.065, -0.38), pya.DPoint(1.065, -0.21), pya.DPoint(0.895, -0.21), pya.DPoint(0.895, -0.38)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.16, 0.21), pya.DPoint(-0.12, 0.21), pya.DPoint(-0.12, 0.38), pya.DPoint(-1.16, 0.38), pya.DPoint(-1.16, 0.21)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.12, 0.21), pya.DPoint(1.16, 0.21), pya.DPoint(1.16, 0.38), pya.DPoint(0.12, 0.38), pya.DPoint(0.12, 0.21)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.16, -0.38), pya.DPoint(1.16, -0.38), pya.DPoint(1.16, -0.21), pya.DPoint(-1.16, -0.21), pya.DPoint(-1.16, -0.38)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.905, 0.21), pya.DPoint(-0.735, 0.21), pya.DPoint(-0.735, 0.38), pya.DPoint(-0.905, 0.38), pya.DPoint(-0.905, 0.21)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.545, 0.21), pya.DPoint(-0.375, 0.21), pya.DPoint(-0.375, 0.38), pya.DPoint(-0.545, 0.38), pya.DPoint(-0.545, 0.21)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.375, 0.21), pya.DPoint(0.545, 0.21), pya.DPoint(0.545, 0.38), pya.DPoint(0.375, 0.38), pya.DPoint(0.375, 0.21)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.735, 0.21), pya.DPoint(0.905, 0.21), pya.DPoint(0.905, 0.38), pya.DPoint(0.735, 0.38), pya.DPoint(0.735, 0.21)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.905, -0.38), pya.DPoint(-0.735, -0.38), pya.DPoint(-0.735, -0.21), pya.DPoint(-0.905, -0.21), pya.DPoint(-0.905, -0.38)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.545, -0.38), pya.DPoint(-0.375, -0.38), pya.DPoint(-0.375, -0.21), pya.DPoint(-0.545, -0.21), pya.DPoint(-0.545, -0.38)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.375, -0.38), pya.DPoint(0.545, -0.38), pya.DPoint(0.545, -0.21), pya.DPoint(0.375, -0.21), pya.DPoint(0.375, -0.38)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.735, -0.38), pya.DPoint(0.905, -0.38), pya.DPoint(0.905, -0.21), pya.DPoint(0.735, -0.21), pya.DPoint(0.735, -0.38)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.14, 0.18), pya.DPoint(-0.14, 0.18), pya.DPoint(-0.14, 0.41), pya.DPoint(-1.14, 0.41), pya.DPoint(-1.14, 0.18)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.14, 0.18), pya.DPoint(1.14, 0.18), pya.DPoint(1.14, 0.41), pya.DPoint(0.14, 0.41), pya.DPoint(0.14, 0.18)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.14, -0.41), pya.DPoint(1.14, -0.41), pya.DPoint(1.14, -0.18), pya.DPoint(-1.14, -0.18), pya.DPoint(-1.14, -0.41)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["shortnmos_2x"] = layout.create_cell("shortnmos_2x")
    build(layout, L, cells)
    out = "shortnmos_2x.gds"
    layout.write(out)
    print("Written:", out)
