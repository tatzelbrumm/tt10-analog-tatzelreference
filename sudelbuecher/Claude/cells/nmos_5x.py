"""Cell: nmos_5x
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers

def build(layout, L, cells):
    """Populate "nmos_5x"."""
    cell = cells["nmos_5x"]
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.04, -0.79), pya.DPoint(-2.04, -0.79), pya.DPoint(-2.04, 0.79), pya.DPoint(-3.04, 0.79), pya.DPoint(-3.04, -0.79)]))
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, -0.79), pya.DPoint(-0.77, -0.79), pya.DPoint(-0.77, 0.79), pya.DPoint(-1.77, 0.79), pya.DPoint(-1.77, -0.79)]))
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.5, -0.79), pya.DPoint(0.5, -0.79), pya.DPoint(0.5, 0.79), pya.DPoint(-0.5, 0.79), pya.DPoint(-0.5, -0.79)]))
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(0.77, -0.79), pya.DPoint(1.77, -0.79), pya.DPoint(1.77, 0.79), pya.DPoint(0.77, 0.79), pya.DPoint(0.77, -0.79)]))
    cell.shapes(L.L_diff_drawing).insert(
        pya.DPolygon([pya.DPoint(2.04, -0.79), pya.DPoint(3.04, -0.79), pya.DPoint(3.04, 0.79), pya.DPoint(2.04, 0.79), pya.DPoint(2.04, -0.79)]))
    cell.shapes(L.L_nsdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.165, -0.915), pya.DPoint(3.165, -0.915), pya.DPoint(3.165, 0.915), pya.DPoint(-3.165, 0.915), pya.DPoint(-3.165, -0.915)]))
    cell.shapes(L.L_poly_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.48, -0.5), pya.DPoint(3.48, -0.5), pya.DPoint(3.48, 0.5), pya.DPoint(-3.48, 0.5), pya.DPoint(-3.48, -0.5)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.965, 0.56), pya.DPoint(-2.795, 0.56), pya.DPoint(-2.795, 0.73), pya.DPoint(-2.965, 0.73), pya.DPoint(-2.965, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.625, 0.56), pya.DPoint(-2.455, 0.56), pya.DPoint(-2.455, 0.73), pya.DPoint(-2.625, 0.73), pya.DPoint(-2.625, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.285, 0.56), pya.DPoint(-2.115, 0.56), pya.DPoint(-2.115, 0.73), pya.DPoint(-2.285, 0.73), pya.DPoint(-2.285, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.695, 0.56), pya.DPoint(-1.525, 0.56), pya.DPoint(-1.525, 0.73), pya.DPoint(-1.695, 0.73), pya.DPoint(-1.695, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.355, 0.56), pya.DPoint(-1.185, 0.56), pya.DPoint(-1.185, 0.73), pya.DPoint(-1.355, 0.73), pya.DPoint(-1.355, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.015, 0.56), pya.DPoint(-0.845, 0.56), pya.DPoint(-0.845, 0.73), pya.DPoint(-1.015, 0.73), pya.DPoint(-1.015, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.425, 0.56), pya.DPoint(-0.255, 0.56), pya.DPoint(-0.255, 0.73), pya.DPoint(-0.425, 0.73), pya.DPoint(-0.425, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.085, 0.56), pya.DPoint(0.085, 0.56), pya.DPoint(0.085, 0.73), pya.DPoint(-0.085, 0.73), pya.DPoint(-0.085, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.255, 0.56), pya.DPoint(0.425, 0.56), pya.DPoint(0.425, 0.73), pya.DPoint(0.255, 0.73), pya.DPoint(0.255, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.845, 0.56), pya.DPoint(1.015, 0.56), pya.DPoint(1.015, 0.73), pya.DPoint(0.845, 0.73), pya.DPoint(0.845, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.185, 0.56), pya.DPoint(1.355, 0.56), pya.DPoint(1.355, 0.73), pya.DPoint(1.185, 0.73), pya.DPoint(1.185, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.525, 0.56), pya.DPoint(1.695, 0.56), pya.DPoint(1.695, 0.73), pya.DPoint(1.525, 0.73), pya.DPoint(1.525, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.115, 0.56), pya.DPoint(2.285, 0.56), pya.DPoint(2.285, 0.73), pya.DPoint(2.115, 0.73), pya.DPoint(2.115, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.455, 0.56), pya.DPoint(2.625, 0.56), pya.DPoint(2.625, 0.73), pya.DPoint(2.455, 0.73), pya.DPoint(2.455, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.795, 0.56), pya.DPoint(2.965, 0.56), pya.DPoint(2.965, 0.73), pya.DPoint(2.795, 0.73), pya.DPoint(2.795, 0.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, 0.255), pya.DPoint(-3.23, 0.255), pya.DPoint(-3.23, 0.425), pya.DPoint(-3.4, 0.425), pya.DPoint(-3.4, 0.255)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, 0.255), pya.DPoint(3.4, 0.255), pya.DPoint(3.4, 0.425), pya.DPoint(3.23, 0.425), pya.DPoint(3.23, 0.255)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, -0.085), pya.DPoint(-3.23, -0.085), pya.DPoint(-3.23, 0.085), pya.DPoint(-3.4, 0.085), pya.DPoint(-3.4, -0.085)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, -0.085), pya.DPoint(3.4, -0.085), pya.DPoint(3.4, 0.085), pya.DPoint(3.23, 0.085), pya.DPoint(3.23, -0.085)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, -0.425), pya.DPoint(-3.23, -0.425), pya.DPoint(-3.23, -0.255), pya.DPoint(-3.4, -0.255), pya.DPoint(-3.4, -0.425)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, -0.425), pya.DPoint(3.4, -0.425), pya.DPoint(3.4, -0.255), pya.DPoint(3.23, -0.255), pya.DPoint(3.23, -0.425)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.965, -0.73), pya.DPoint(-2.795, -0.73), pya.DPoint(-2.795, -0.56), pya.DPoint(-2.965, -0.56), pya.DPoint(-2.965, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.625, -0.73), pya.DPoint(-2.455, -0.73), pya.DPoint(-2.455, -0.56), pya.DPoint(-2.625, -0.56), pya.DPoint(-2.625, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.285, -0.73), pya.DPoint(-2.115, -0.73), pya.DPoint(-2.115, -0.56), pya.DPoint(-2.285, -0.56), pya.DPoint(-2.285, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.695, -0.73), pya.DPoint(-1.525, -0.73), pya.DPoint(-1.525, -0.56), pya.DPoint(-1.695, -0.56), pya.DPoint(-1.695, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.355, -0.73), pya.DPoint(-1.185, -0.73), pya.DPoint(-1.185, -0.56), pya.DPoint(-1.355, -0.56), pya.DPoint(-1.355, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.015, -0.73), pya.DPoint(-0.845, -0.73), pya.DPoint(-0.845, -0.56), pya.DPoint(-1.015, -0.56), pya.DPoint(-1.015, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.425, -0.73), pya.DPoint(-0.255, -0.73), pya.DPoint(-0.255, -0.56), pya.DPoint(-0.425, -0.56), pya.DPoint(-0.425, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.085, -0.73), pya.DPoint(0.085, -0.73), pya.DPoint(0.085, -0.56), pya.DPoint(-0.085, -0.56), pya.DPoint(-0.085, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.255, -0.73), pya.DPoint(0.425, -0.73), pya.DPoint(0.425, -0.56), pya.DPoint(0.255, -0.56), pya.DPoint(0.255, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.845, -0.73), pya.DPoint(1.015, -0.73), pya.DPoint(1.015, -0.56), pya.DPoint(0.845, -0.56), pya.DPoint(0.845, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.185, -0.73), pya.DPoint(1.355, -0.73), pya.DPoint(1.355, -0.56), pya.DPoint(1.185, -0.56), pya.DPoint(1.185, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.525, -0.73), pya.DPoint(1.695, -0.73), pya.DPoint(1.695, -0.56), pya.DPoint(1.525, -0.56), pya.DPoint(1.525, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.115, -0.73), pya.DPoint(2.285, -0.73), pya.DPoint(2.285, -0.56), pya.DPoint(2.115, -0.56), pya.DPoint(2.115, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.455, -0.73), pya.DPoint(2.625, -0.73), pya.DPoint(2.625, -0.56), pya.DPoint(2.455, -0.56), pya.DPoint(2.455, -0.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.795, -0.73), pya.DPoint(2.965, -0.73), pya.DPoint(2.965, -0.56), pya.DPoint(2.795, -0.56), pya.DPoint(2.795, -0.73)]))
    cell.shapes(L.L_npc_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.5, -0.525), pya.DPoint(-3.13, -0.525), pya.DPoint(-3.13, 0.525), pya.DPoint(-3.5, 0.525), pya.DPoint(-3.5, -0.525)]))
    cell.shapes(L.L_npc_drawing).insert(
        pya.DPolygon([pya.DPoint(3.13, -0.525), pya.DPoint(3.5, -0.525), pya.DPoint(3.5, 0.525), pya.DPoint(3.13, 0.525), pya.DPoint(3.13, -0.525)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.06, 0.56), pya.DPoint(-2.02, 0.56), pya.DPoint(-2.02, 0.73), pya.DPoint(-3.06, 0.73), pya.DPoint(-3.06, 0.56)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.79, 0.56), pya.DPoint(-0.75, 0.56), pya.DPoint(-0.75, 0.73), pya.DPoint(-1.79, 0.73), pya.DPoint(-1.79, 0.56)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.52, 0.56), pya.DPoint(0.52, 0.56), pya.DPoint(0.52, 0.73), pya.DPoint(-0.52, 0.73), pya.DPoint(-0.52, 0.56)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.75, 0.56), pya.DPoint(1.79, 0.56), pya.DPoint(1.79, 0.73), pya.DPoint(0.75, 0.73), pya.DPoint(0.75, 0.56)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.02, 0.56), pya.DPoint(3.06, 0.56), pya.DPoint(3.06, 0.73), pya.DPoint(2.02, 0.73), pya.DPoint(2.02, 0.56)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, -0.53), pya.DPoint(-3.23, -0.53), pya.DPoint(-3.23, 0.53), pya.DPoint(-3.4, 0.53), pya.DPoint(-3.4, -0.53)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, -0.53), pya.DPoint(3.4, -0.53), pya.DPoint(3.4, 0.53), pya.DPoint(3.23, 0.53), pya.DPoint(3.23, -0.53)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.06, -0.73), pya.DPoint(-2.02, -0.73), pya.DPoint(-2.02, -0.56), pya.DPoint(-3.06, -0.56), pya.DPoint(-3.06, -0.73)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.79, -0.73), pya.DPoint(-0.75, -0.73), pya.DPoint(-0.75, -0.56), pya.DPoint(-1.79, -0.56), pya.DPoint(-1.79, -0.73)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.52, -0.73), pya.DPoint(0.52, -0.73), pya.DPoint(0.52, -0.56), pya.DPoint(-0.52, -0.56), pya.DPoint(-0.52, -0.73)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.75, -0.73), pya.DPoint(1.79, -0.73), pya.DPoint(1.79, -0.56), pya.DPoint(0.75, -0.56), pya.DPoint(0.75, -0.73)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.02, -0.73), pya.DPoint(3.06, -0.73), pya.DPoint(3.06, -0.56), pya.DPoint(2.02, -0.56), pya.DPoint(2.02, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.805, 0.56), pya.DPoint(-2.635, 0.56), pya.DPoint(-2.635, 0.73), pya.DPoint(-2.805, 0.73), pya.DPoint(-2.805, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.445, 0.56), pya.DPoint(-2.275, 0.56), pya.DPoint(-2.275, 0.73), pya.DPoint(-2.445, 0.73), pya.DPoint(-2.445, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.535, 0.56), pya.DPoint(-1.365, 0.56), pya.DPoint(-1.365, 0.73), pya.DPoint(-1.535, 0.73), pya.DPoint(-1.535, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.175, 0.56), pya.DPoint(-1.005, 0.56), pya.DPoint(-1.005, 0.73), pya.DPoint(-1.175, 0.73), pya.DPoint(-1.175, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.265, 0.56), pya.DPoint(-0.095, 0.56), pya.DPoint(-0.095, 0.73), pya.DPoint(-0.265, 0.73), pya.DPoint(-0.265, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.095, 0.56), pya.DPoint(0.265, 0.56), pya.DPoint(0.265, 0.73), pya.DPoint(0.095, 0.73), pya.DPoint(0.095, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.005, 0.56), pya.DPoint(1.175, 0.56), pya.DPoint(1.175, 0.73), pya.DPoint(1.005, 0.73), pya.DPoint(1.005, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.365, 0.56), pya.DPoint(1.535, 0.56), pya.DPoint(1.535, 0.73), pya.DPoint(1.365, 0.73), pya.DPoint(1.365, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(2.275, 0.56), pya.DPoint(2.445, 0.56), pya.DPoint(2.445, 0.73), pya.DPoint(2.275, 0.73), pya.DPoint(2.275, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(2.635, 0.56), pya.DPoint(2.805, 0.56), pya.DPoint(2.805, 0.73), pya.DPoint(2.635, 0.73), pya.DPoint(2.635, 0.56)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, 0.275), pya.DPoint(-3.23, 0.275), pya.DPoint(-3.23, 0.445), pya.DPoint(-3.4, 0.445), pya.DPoint(-3.4, 0.275)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, 0.275), pya.DPoint(3.4, 0.275), pya.DPoint(3.4, 0.445), pya.DPoint(3.23, 0.445), pya.DPoint(3.23, 0.275)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, -0.085), pya.DPoint(-3.23, -0.085), pya.DPoint(-3.23, 0.085), pya.DPoint(-3.4, 0.085), pya.DPoint(-3.4, -0.085)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, -0.085), pya.DPoint(3.4, -0.085), pya.DPoint(3.4, 0.085), pya.DPoint(3.23, 0.085), pya.DPoint(3.23, -0.085)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.4, -0.445), pya.DPoint(-3.23, -0.445), pya.DPoint(-3.23, -0.275), pya.DPoint(-3.4, -0.275), pya.DPoint(-3.4, -0.445)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(3.23, -0.445), pya.DPoint(3.4, -0.445), pya.DPoint(3.4, -0.275), pya.DPoint(3.23, -0.275), pya.DPoint(3.23, -0.445)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.805, -0.73), pya.DPoint(-2.635, -0.73), pya.DPoint(-2.635, -0.56), pya.DPoint(-2.805, -0.56), pya.DPoint(-2.805, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.445, -0.73), pya.DPoint(-2.275, -0.73), pya.DPoint(-2.275, -0.56), pya.DPoint(-2.445, -0.56), pya.DPoint(-2.445, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.535, -0.73), pya.DPoint(-1.365, -0.73), pya.DPoint(-1.365, -0.56), pya.DPoint(-1.535, -0.56), pya.DPoint(-1.535, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.175, -0.73), pya.DPoint(-1.005, -0.73), pya.DPoint(-1.005, -0.56), pya.DPoint(-1.175, -0.56), pya.DPoint(-1.175, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.265, -0.73), pya.DPoint(-0.095, -0.73), pya.DPoint(-0.095, -0.56), pya.DPoint(-0.265, -0.56), pya.DPoint(-0.265, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.095, -0.73), pya.DPoint(0.265, -0.73), pya.DPoint(0.265, -0.56), pya.DPoint(0.095, -0.56), pya.DPoint(0.095, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.005, -0.73), pya.DPoint(1.175, -0.73), pya.DPoint(1.175, -0.56), pya.DPoint(1.005, -0.56), pya.DPoint(1.005, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.365, -0.73), pya.DPoint(1.535, -0.73), pya.DPoint(1.535, -0.56), pya.DPoint(1.365, -0.56), pya.DPoint(1.365, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(2.275, -0.73), pya.DPoint(2.445, -0.73), pya.DPoint(2.445, -0.56), pya.DPoint(2.275, -0.56), pya.DPoint(2.275, -0.73)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(2.635, -0.73), pya.DPoint(2.805, -0.73), pya.DPoint(2.805, -0.56), pya.DPoint(2.635, -0.56), pya.DPoint(2.635, -0.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.04, 0.53), pya.DPoint(-2.04, 0.53), pya.DPoint(-2.04, 0.76), pya.DPoint(-3.04, 0.76), pya.DPoint(-3.04, 0.53)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, 0.53), pya.DPoint(-0.77, 0.53), pya.DPoint(-0.77, 0.76), pya.DPoint(-1.77, 0.76), pya.DPoint(-1.77, 0.53)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.5, 0.53), pya.DPoint(0.5, 0.53), pya.DPoint(0.5, 0.76), pya.DPoint(-0.5, 0.76), pya.DPoint(-0.5, 0.53)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.77, 0.53), pya.DPoint(1.77, 0.53), pya.DPoint(1.77, 0.76), pya.DPoint(0.77, 0.76), pya.DPoint(0.77, 0.53)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.04, 0.53), pya.DPoint(3.04, 0.53), pya.DPoint(3.04, 0.76), pya.DPoint(2.04, 0.76), pya.DPoint(2.04, 0.53)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.43, -0.51), pya.DPoint(-3.2, -0.51), pya.DPoint(-3.2, 0.51), pya.DPoint(-3.43, 0.51), pya.DPoint(-3.43, -0.51)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.2, -0.51), pya.DPoint(3.43, -0.51), pya.DPoint(3.43, 0.51), pya.DPoint(3.2, 0.51), pya.DPoint(3.2, -0.51)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.04, -0.76), pya.DPoint(-2.04, -0.76), pya.DPoint(-2.04, -0.53), pya.DPoint(-3.04, -0.53), pya.DPoint(-3.04, -0.76)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.77, -0.76), pya.DPoint(-0.77, -0.76), pya.DPoint(-0.77, -0.53), pya.DPoint(-1.77, -0.53), pya.DPoint(-1.77, -0.76)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.5, -0.76), pya.DPoint(0.5, -0.76), pya.DPoint(0.5, -0.53), pya.DPoint(-0.5, -0.53), pya.DPoint(-0.5, -0.76)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.77, -0.76), pya.DPoint(1.77, -0.76), pya.DPoint(1.77, -0.53), pya.DPoint(0.77, -0.53), pya.DPoint(0.77, -0.76)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.04, -0.76), pya.DPoint(3.04, -0.76), pya.DPoint(3.04, -0.53), pya.DPoint(2.04, -0.53), pya.DPoint(2.04, -0.76)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["nmos_5x"] = layout.create_cell("nmos_5x")
    build(layout, L, cells)
    out = "nmos_5x.gds"
    layout.write(out)
    print("Written:", out)
