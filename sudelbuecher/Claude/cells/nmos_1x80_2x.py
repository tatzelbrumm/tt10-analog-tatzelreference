"""Cell: nmos_1x80_2x
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from nmos1x20_8x import build as _build_nmos1x20_8x

def build(layout, L, cells):
    """Populate "nmos_1x80_2x". cells must contain: nmos_1x80_2x, nmos1x20_8x."""
    cell = cells["nmos_1x80_2x"]
    cell.insert(pya.DCellInstArray(
        cells["nmos1x20_8x"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(4.75, 10.29))))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.37, 20.85), pya.DPoint(11.14, 20.85), pya.DPoint(11.14, 21.06), pya.DPoint(-0.37, 21.06), pya.DPoint(-0.37, 20.85)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.37, -0.28), pya.DPoint(-0.16, -0.28), pya.DPoint(-0.16, 20.85), pya.DPoint(-0.37, 20.85), pya.DPoint(-0.37, -0.28)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(10.93, -0.28), pya.DPoint(11.14, -0.28), pya.DPoint(11.14, 20.85), pya.DPoint(10.93, 20.85), pya.DPoint(10.93, -0.28)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.37, -0.49), pya.DPoint(11.14, -0.49), pya.DPoint(11.14, -0.28), pya.DPoint(-0.37, -0.28), pya.DPoint(-0.37, -0.49)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.495, 20.725), pya.DPoint(11.265, 20.725), pya.DPoint(11.265, 21.185), pya.DPoint(-0.495, 21.185), pya.DPoint(-0.495, 20.725)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.495, -0.155), pya.DPoint(-0.035, -0.155), pya.DPoint(-0.035, 20.725), pya.DPoint(-0.495, 20.725), pya.DPoint(-0.495, -0.155)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(10.805, -0.155), pya.DPoint(11.265, -0.155), pya.DPoint(11.265, 20.725), pya.DPoint(10.805, 20.725), pya.DPoint(10.805, -0.155)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.495, -0.615), pya.DPoint(11.265, -0.615), pya.DPoint(11.265, -0.155), pya.DPoint(-0.495, -0.155), pya.DPoint(-0.495, -0.615)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.14, 20.87), pya.DPoint(0.03, 20.87), pya.DPoint(0.03, 21.04), pya.DPoint(-0.14, 21.04), pya.DPoint(-0.14, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.2, 20.87), pya.DPoint(0.37, 20.87), pya.DPoint(0.37, 21.04), pya.DPoint(0.2, 21.04), pya.DPoint(0.2, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.54, 20.87), pya.DPoint(0.71, 20.87), pya.DPoint(0.71, 21.04), pya.DPoint(0.54, 21.04), pya.DPoint(0.54, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.88, 20.87), pya.DPoint(1.05, 20.87), pya.DPoint(1.05, 21.04), pya.DPoint(0.88, 21.04), pya.DPoint(0.88, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.22, 20.87), pya.DPoint(1.39, 20.87), pya.DPoint(1.39, 21.04), pya.DPoint(1.22, 21.04), pya.DPoint(1.22, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.56, 20.87), pya.DPoint(1.73, 20.87), pya.DPoint(1.73, 21.04), pya.DPoint(1.56, 21.04), pya.DPoint(1.56, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.9, 20.87), pya.DPoint(2.07, 20.87), pya.DPoint(2.07, 21.04), pya.DPoint(1.9, 21.04), pya.DPoint(1.9, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.24, 20.87), pya.DPoint(2.41, 20.87), pya.DPoint(2.41, 21.04), pya.DPoint(2.24, 21.04), pya.DPoint(2.24, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.58, 20.87), pya.DPoint(2.75, 20.87), pya.DPoint(2.75, 21.04), pya.DPoint(2.58, 21.04), pya.DPoint(2.58, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.92, 20.87), pya.DPoint(3.09, 20.87), pya.DPoint(3.09, 21.04), pya.DPoint(2.92, 21.04), pya.DPoint(2.92, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.26, 20.87), pya.DPoint(3.43, 20.87), pya.DPoint(3.43, 21.04), pya.DPoint(3.26, 21.04), pya.DPoint(3.26, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.6, 20.87), pya.DPoint(3.77, 20.87), pya.DPoint(3.77, 21.04), pya.DPoint(3.6, 21.04), pya.DPoint(3.6, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.94, 20.87), pya.DPoint(4.11, 20.87), pya.DPoint(4.11, 21.04), pya.DPoint(3.94, 21.04), pya.DPoint(3.94, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.28, 20.87), pya.DPoint(4.45, 20.87), pya.DPoint(4.45, 21.04), pya.DPoint(4.28, 21.04), pya.DPoint(4.28, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.62, 20.87), pya.DPoint(4.79, 20.87), pya.DPoint(4.79, 21.04), pya.DPoint(4.62, 21.04), pya.DPoint(4.62, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.96, 20.87), pya.DPoint(5.13, 20.87), pya.DPoint(5.13, 21.04), pya.DPoint(4.96, 21.04), pya.DPoint(4.96, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.3, 20.87), pya.DPoint(5.47, 20.87), pya.DPoint(5.47, 21.04), pya.DPoint(5.3, 21.04), pya.DPoint(5.3, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.64, 20.87), pya.DPoint(5.81, 20.87), pya.DPoint(5.81, 21.04), pya.DPoint(5.64, 21.04), pya.DPoint(5.64, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.98, 20.87), pya.DPoint(6.15, 20.87), pya.DPoint(6.15, 21.04), pya.DPoint(5.98, 21.04), pya.DPoint(5.98, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.32, 20.87), pya.DPoint(6.49, 20.87), pya.DPoint(6.49, 21.04), pya.DPoint(6.32, 21.04), pya.DPoint(6.32, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, 20.87), pya.DPoint(6.83, 20.87), pya.DPoint(6.83, 21.04), pya.DPoint(6.66, 21.04), pya.DPoint(6.66, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7, 20.87), pya.DPoint(7.17, 20.87), pya.DPoint(7.17, 21.04), pya.DPoint(7, 21.04), pya.DPoint(7, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.34, 20.87), pya.DPoint(7.51, 20.87), pya.DPoint(7.51, 21.04), pya.DPoint(7.34, 21.04), pya.DPoint(7.34, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.68, 20.87), pya.DPoint(7.85, 20.87), pya.DPoint(7.85, 21.04), pya.DPoint(7.68, 21.04), pya.DPoint(7.68, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.02, 20.87), pya.DPoint(8.19, 20.87), pya.DPoint(8.19, 21.04), pya.DPoint(8.02, 21.04), pya.DPoint(8.02, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, 20.87), pya.DPoint(8.53, 20.87), pya.DPoint(8.53, 21.04), pya.DPoint(8.36, 21.04), pya.DPoint(8.36, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.7, 20.87), pya.DPoint(8.87, 20.87), pya.DPoint(8.87, 21.04), pya.DPoint(8.7, 21.04), pya.DPoint(8.7, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.04, 20.87), pya.DPoint(9.21, 20.87), pya.DPoint(9.21, 21.04), pya.DPoint(9.04, 21.04), pya.DPoint(9.04, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.38, 20.87), pya.DPoint(9.55, 20.87), pya.DPoint(9.55, 21.04), pya.DPoint(9.38, 21.04), pya.DPoint(9.38, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.72, 20.87), pya.DPoint(9.89, 20.87), pya.DPoint(9.89, 21.04), pya.DPoint(9.72, 21.04), pya.DPoint(9.72, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.06, 20.87), pya.DPoint(10.23, 20.87), pya.DPoint(10.23, 21.04), pya.DPoint(10.06, 21.04), pya.DPoint(10.06, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.4, 20.87), pya.DPoint(10.57, 20.87), pya.DPoint(10.57, 21.04), pya.DPoint(10.4, 21.04), pya.DPoint(10.4, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.74, 20.87), pya.DPoint(10.91, 20.87), pya.DPoint(10.91, 21.04), pya.DPoint(10.74, 21.04), pya.DPoint(10.74, 20.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 20.4), pya.DPoint(-0.18, 20.4), pya.DPoint(-0.18, 20.57), pya.DPoint(-0.35, 20.57), pya.DPoint(-0.35, 20.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 20.4), pya.DPoint(11.12, 20.4), pya.DPoint(11.12, 20.57), pya.DPoint(10.95, 20.57), pya.DPoint(10.95, 20.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 20.06), pya.DPoint(-0.18, 20.06), pya.DPoint(-0.18, 20.23), pya.DPoint(-0.35, 20.23), pya.DPoint(-0.35, 20.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 20.06), pya.DPoint(11.12, 20.06), pya.DPoint(11.12, 20.23), pya.DPoint(10.95, 20.23), pya.DPoint(10.95, 20.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 19.72), pya.DPoint(-0.18, 19.72), pya.DPoint(-0.18, 19.89), pya.DPoint(-0.35, 19.89), pya.DPoint(-0.35, 19.72)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 19.72), pya.DPoint(11.12, 19.72), pya.DPoint(11.12, 19.89), pya.DPoint(10.95, 19.89), pya.DPoint(10.95, 19.72)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 19.38), pya.DPoint(-0.18, 19.38), pya.DPoint(-0.18, 19.55), pya.DPoint(-0.35, 19.55), pya.DPoint(-0.35, 19.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 19.38), pya.DPoint(11.12, 19.38), pya.DPoint(11.12, 19.55), pya.DPoint(10.95, 19.55), pya.DPoint(10.95, 19.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 19.04), pya.DPoint(-0.18, 19.04), pya.DPoint(-0.18, 19.21), pya.DPoint(-0.35, 19.21), pya.DPoint(-0.35, 19.04)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 19.04), pya.DPoint(11.12, 19.04), pya.DPoint(11.12, 19.21), pya.DPoint(10.95, 19.21), pya.DPoint(10.95, 19.04)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 18.7), pya.DPoint(-0.18, 18.7), pya.DPoint(-0.18, 18.87), pya.DPoint(-0.35, 18.87), pya.DPoint(-0.35, 18.7)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 18.7), pya.DPoint(11.12, 18.7), pya.DPoint(11.12, 18.87), pya.DPoint(10.95, 18.87), pya.DPoint(10.95, 18.7)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 18.36), pya.DPoint(-0.18, 18.36), pya.DPoint(-0.18, 18.53), pya.DPoint(-0.35, 18.53), pya.DPoint(-0.35, 18.36)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 18.36), pya.DPoint(11.12, 18.36), pya.DPoint(11.12, 18.53), pya.DPoint(10.95, 18.53), pya.DPoint(10.95, 18.36)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 18.02), pya.DPoint(-0.18, 18.02), pya.DPoint(-0.18, 18.19), pya.DPoint(-0.35, 18.19), pya.DPoint(-0.35, 18.02)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 18.02), pya.DPoint(11.12, 18.02), pya.DPoint(11.12, 18.19), pya.DPoint(10.95, 18.19), pya.DPoint(10.95, 18.02)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 17.68), pya.DPoint(-0.18, 17.68), pya.DPoint(-0.18, 17.85), pya.DPoint(-0.35, 17.85), pya.DPoint(-0.35, 17.68)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 17.68), pya.DPoint(11.12, 17.68), pya.DPoint(11.12, 17.85), pya.DPoint(10.95, 17.85), pya.DPoint(10.95, 17.68)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 17.34), pya.DPoint(-0.18, 17.34), pya.DPoint(-0.18, 17.51), pya.DPoint(-0.35, 17.51), pya.DPoint(-0.35, 17.34)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 17.34), pya.DPoint(11.12, 17.34), pya.DPoint(11.12, 17.51), pya.DPoint(10.95, 17.51), pya.DPoint(10.95, 17.34)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 17), pya.DPoint(-0.18, 17), pya.DPoint(-0.18, 17.17), pya.DPoint(-0.35, 17.17), pya.DPoint(-0.35, 17)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 17), pya.DPoint(11.12, 17), pya.DPoint(11.12, 17.17), pya.DPoint(10.95, 17.17), pya.DPoint(10.95, 17)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 16.66), pya.DPoint(-0.18, 16.66), pya.DPoint(-0.18, 16.83), pya.DPoint(-0.35, 16.83), pya.DPoint(-0.35, 16.66)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 16.66), pya.DPoint(11.12, 16.66), pya.DPoint(11.12, 16.83), pya.DPoint(10.95, 16.83), pya.DPoint(10.95, 16.66)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 16.32), pya.DPoint(-0.18, 16.32), pya.DPoint(-0.18, 16.49), pya.DPoint(-0.35, 16.49), pya.DPoint(-0.35, 16.32)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 16.32), pya.DPoint(11.12, 16.32), pya.DPoint(11.12, 16.49), pya.DPoint(10.95, 16.49), pya.DPoint(10.95, 16.32)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 15.98), pya.DPoint(-0.18, 15.98), pya.DPoint(-0.18, 16.15), pya.DPoint(-0.35, 16.15), pya.DPoint(-0.35, 15.98)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 15.98), pya.DPoint(11.12, 15.98), pya.DPoint(11.12, 16.15), pya.DPoint(10.95, 16.15), pya.DPoint(10.95, 15.98)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 15.64), pya.DPoint(-0.18, 15.64), pya.DPoint(-0.18, 15.81), pya.DPoint(-0.35, 15.81), pya.DPoint(-0.35, 15.64)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 15.64), pya.DPoint(11.12, 15.64), pya.DPoint(11.12, 15.81), pya.DPoint(10.95, 15.81), pya.DPoint(10.95, 15.64)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 15.3), pya.DPoint(-0.18, 15.3), pya.DPoint(-0.18, 15.47), pya.DPoint(-0.35, 15.47), pya.DPoint(-0.35, 15.3)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 15.3), pya.DPoint(11.12, 15.3), pya.DPoint(11.12, 15.47), pya.DPoint(10.95, 15.47), pya.DPoint(10.95, 15.3)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 14.96), pya.DPoint(-0.18, 14.96), pya.DPoint(-0.18, 15.13), pya.DPoint(-0.35, 15.13), pya.DPoint(-0.35, 14.96)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 14.96), pya.DPoint(11.12, 14.96), pya.DPoint(11.12, 15.13), pya.DPoint(10.95, 15.13), pya.DPoint(10.95, 14.96)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 14.62), pya.DPoint(-0.18, 14.62), pya.DPoint(-0.18, 14.79), pya.DPoint(-0.35, 14.79), pya.DPoint(-0.35, 14.62)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 14.62), pya.DPoint(11.12, 14.62), pya.DPoint(11.12, 14.79), pya.DPoint(10.95, 14.79), pya.DPoint(10.95, 14.62)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 14.28), pya.DPoint(-0.18, 14.28), pya.DPoint(-0.18, 14.45), pya.DPoint(-0.35, 14.45), pya.DPoint(-0.35, 14.28)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 14.28), pya.DPoint(11.12, 14.28), pya.DPoint(11.12, 14.45), pya.DPoint(10.95, 14.45), pya.DPoint(10.95, 14.28)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 13.94), pya.DPoint(-0.18, 13.94), pya.DPoint(-0.18, 14.11), pya.DPoint(-0.35, 14.11), pya.DPoint(-0.35, 13.94)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 13.94), pya.DPoint(11.12, 13.94), pya.DPoint(11.12, 14.11), pya.DPoint(10.95, 14.11), pya.DPoint(10.95, 13.94)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 13.6), pya.DPoint(-0.18, 13.6), pya.DPoint(-0.18, 13.77), pya.DPoint(-0.35, 13.77), pya.DPoint(-0.35, 13.6)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 13.6), pya.DPoint(11.12, 13.6), pya.DPoint(11.12, 13.77), pya.DPoint(10.95, 13.77), pya.DPoint(10.95, 13.6)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 13.26), pya.DPoint(-0.18, 13.26), pya.DPoint(-0.18, 13.43), pya.DPoint(-0.35, 13.43), pya.DPoint(-0.35, 13.26)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 13.26), pya.DPoint(11.12, 13.26), pya.DPoint(11.12, 13.43), pya.DPoint(10.95, 13.43), pya.DPoint(10.95, 13.26)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 12.92), pya.DPoint(-0.18, 12.92), pya.DPoint(-0.18, 13.09), pya.DPoint(-0.35, 13.09), pya.DPoint(-0.35, 12.92)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 12.92), pya.DPoint(11.12, 12.92), pya.DPoint(11.12, 13.09), pya.DPoint(10.95, 13.09), pya.DPoint(10.95, 12.92)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 12.58), pya.DPoint(-0.18, 12.58), pya.DPoint(-0.18, 12.75), pya.DPoint(-0.35, 12.75), pya.DPoint(-0.35, 12.58)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 12.58), pya.DPoint(11.12, 12.58), pya.DPoint(11.12, 12.75), pya.DPoint(10.95, 12.75), pya.DPoint(10.95, 12.58)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 12.24), pya.DPoint(-0.18, 12.24), pya.DPoint(-0.18, 12.41), pya.DPoint(-0.35, 12.41), pya.DPoint(-0.35, 12.24)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 12.24), pya.DPoint(11.12, 12.24), pya.DPoint(11.12, 12.41), pya.DPoint(10.95, 12.41), pya.DPoint(10.95, 12.24)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 11.9), pya.DPoint(-0.18, 11.9), pya.DPoint(-0.18, 12.07), pya.DPoint(-0.35, 12.07), pya.DPoint(-0.35, 11.9)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 11.9), pya.DPoint(11.12, 11.9), pya.DPoint(11.12, 12.07), pya.DPoint(10.95, 12.07), pya.DPoint(10.95, 11.9)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 11.56), pya.DPoint(-0.18, 11.56), pya.DPoint(-0.18, 11.73), pya.DPoint(-0.35, 11.73), pya.DPoint(-0.35, 11.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 11.56), pya.DPoint(11.12, 11.56), pya.DPoint(11.12, 11.73), pya.DPoint(10.95, 11.73), pya.DPoint(10.95, 11.56)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 11.22), pya.DPoint(-0.18, 11.22), pya.DPoint(-0.18, 11.39), pya.DPoint(-0.35, 11.39), pya.DPoint(-0.35, 11.22)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 11.22), pya.DPoint(11.12, 11.22), pya.DPoint(11.12, 11.39), pya.DPoint(10.95, 11.39), pya.DPoint(10.95, 11.22)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 10.88), pya.DPoint(-0.18, 10.88), pya.DPoint(-0.18, 11.05), pya.DPoint(-0.35, 11.05), pya.DPoint(-0.35, 10.88)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 10.88), pya.DPoint(11.12, 10.88), pya.DPoint(11.12, 11.05), pya.DPoint(10.95, 11.05), pya.DPoint(10.95, 10.88)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 10.54), pya.DPoint(-0.18, 10.54), pya.DPoint(-0.18, 10.71), pya.DPoint(-0.35, 10.71), pya.DPoint(-0.35, 10.54)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 10.54), pya.DPoint(11.12, 10.54), pya.DPoint(11.12, 10.71), pya.DPoint(10.95, 10.71), pya.DPoint(10.95, 10.54)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 10.2), pya.DPoint(-0.18, 10.2), pya.DPoint(-0.18, 10.37), pya.DPoint(-0.35, 10.37), pya.DPoint(-0.35, 10.2)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 10.2), pya.DPoint(11.12, 10.2), pya.DPoint(11.12, 10.37), pya.DPoint(10.95, 10.37), pya.DPoint(10.95, 10.2)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 9.86), pya.DPoint(-0.18, 9.86), pya.DPoint(-0.18, 10.03), pya.DPoint(-0.35, 10.03), pya.DPoint(-0.35, 9.86)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 9.86), pya.DPoint(11.12, 9.86), pya.DPoint(11.12, 10.03), pya.DPoint(10.95, 10.03), pya.DPoint(10.95, 9.86)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 9.52), pya.DPoint(-0.18, 9.52), pya.DPoint(-0.18, 9.69), pya.DPoint(-0.35, 9.69), pya.DPoint(-0.35, 9.52)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 9.52), pya.DPoint(11.12, 9.52), pya.DPoint(11.12, 9.69), pya.DPoint(10.95, 9.69), pya.DPoint(10.95, 9.52)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 9.18), pya.DPoint(-0.18, 9.18), pya.DPoint(-0.18, 9.35), pya.DPoint(-0.35, 9.35), pya.DPoint(-0.35, 9.18)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 9.18), pya.DPoint(11.12, 9.18), pya.DPoint(11.12, 9.35), pya.DPoint(10.95, 9.35), pya.DPoint(10.95, 9.18)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 8.84), pya.DPoint(-0.18, 8.84), pya.DPoint(-0.18, 9.01), pya.DPoint(-0.35, 9.01), pya.DPoint(-0.35, 8.84)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 8.84), pya.DPoint(11.12, 8.84), pya.DPoint(11.12, 9.01), pya.DPoint(10.95, 9.01), pya.DPoint(10.95, 8.84)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 8.5), pya.DPoint(-0.18, 8.5), pya.DPoint(-0.18, 8.67), pya.DPoint(-0.35, 8.67), pya.DPoint(-0.35, 8.5)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 8.5), pya.DPoint(11.12, 8.5), pya.DPoint(11.12, 8.67), pya.DPoint(10.95, 8.67), pya.DPoint(10.95, 8.5)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 8.16), pya.DPoint(-0.18, 8.16), pya.DPoint(-0.18, 8.33), pya.DPoint(-0.35, 8.33), pya.DPoint(-0.35, 8.16)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 8.16), pya.DPoint(11.12, 8.16), pya.DPoint(11.12, 8.33), pya.DPoint(10.95, 8.33), pya.DPoint(10.95, 8.16)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 7.82), pya.DPoint(-0.18, 7.82), pya.DPoint(-0.18, 7.99), pya.DPoint(-0.35, 7.99), pya.DPoint(-0.35, 7.82)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 7.82), pya.DPoint(11.12, 7.82), pya.DPoint(11.12, 7.99), pya.DPoint(10.95, 7.99), pya.DPoint(10.95, 7.82)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 7.48), pya.DPoint(-0.18, 7.48), pya.DPoint(-0.18, 7.65), pya.DPoint(-0.35, 7.65), pya.DPoint(-0.35, 7.48)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 7.48), pya.DPoint(11.12, 7.48), pya.DPoint(11.12, 7.65), pya.DPoint(10.95, 7.65), pya.DPoint(10.95, 7.48)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 7.14), pya.DPoint(-0.18, 7.14), pya.DPoint(-0.18, 7.31), pya.DPoint(-0.35, 7.31), pya.DPoint(-0.35, 7.14)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 7.14), pya.DPoint(11.12, 7.14), pya.DPoint(11.12, 7.31), pya.DPoint(10.95, 7.31), pya.DPoint(10.95, 7.14)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 6.8), pya.DPoint(-0.18, 6.8), pya.DPoint(-0.18, 6.97), pya.DPoint(-0.35, 6.97), pya.DPoint(-0.35, 6.8)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 6.8), pya.DPoint(11.12, 6.8), pya.DPoint(11.12, 6.97), pya.DPoint(10.95, 6.97), pya.DPoint(10.95, 6.8)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 6.46), pya.DPoint(-0.18, 6.46), pya.DPoint(-0.18, 6.63), pya.DPoint(-0.35, 6.63), pya.DPoint(-0.35, 6.46)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 6.46), pya.DPoint(11.12, 6.46), pya.DPoint(11.12, 6.63), pya.DPoint(10.95, 6.63), pya.DPoint(10.95, 6.46)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 6.12), pya.DPoint(-0.18, 6.12), pya.DPoint(-0.18, 6.29), pya.DPoint(-0.35, 6.29), pya.DPoint(-0.35, 6.12)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 6.12), pya.DPoint(11.12, 6.12), pya.DPoint(11.12, 6.29), pya.DPoint(10.95, 6.29), pya.DPoint(10.95, 6.12)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 5.78), pya.DPoint(-0.18, 5.78), pya.DPoint(-0.18, 5.95), pya.DPoint(-0.35, 5.95), pya.DPoint(-0.35, 5.78)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 5.78), pya.DPoint(11.12, 5.78), pya.DPoint(11.12, 5.95), pya.DPoint(10.95, 5.95), pya.DPoint(10.95, 5.78)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 5.44), pya.DPoint(-0.18, 5.44), pya.DPoint(-0.18, 5.61), pya.DPoint(-0.35, 5.61), pya.DPoint(-0.35, 5.44)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 5.44), pya.DPoint(11.12, 5.44), pya.DPoint(11.12, 5.61), pya.DPoint(10.95, 5.61), pya.DPoint(10.95, 5.44)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 5.1), pya.DPoint(-0.18, 5.1), pya.DPoint(-0.18, 5.27), pya.DPoint(-0.35, 5.27), pya.DPoint(-0.35, 5.1)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 5.1), pya.DPoint(11.12, 5.1), pya.DPoint(11.12, 5.27), pya.DPoint(10.95, 5.27), pya.DPoint(10.95, 5.1)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 4.76), pya.DPoint(-0.18, 4.76), pya.DPoint(-0.18, 4.93), pya.DPoint(-0.35, 4.93), pya.DPoint(-0.35, 4.76)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 4.76), pya.DPoint(11.12, 4.76), pya.DPoint(11.12, 4.93), pya.DPoint(10.95, 4.93), pya.DPoint(10.95, 4.76)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 4.42), pya.DPoint(-0.18, 4.42), pya.DPoint(-0.18, 4.59), pya.DPoint(-0.35, 4.59), pya.DPoint(-0.35, 4.42)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 4.42), pya.DPoint(11.12, 4.42), pya.DPoint(11.12, 4.59), pya.DPoint(10.95, 4.59), pya.DPoint(10.95, 4.42)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 4.08), pya.DPoint(-0.18, 4.08), pya.DPoint(-0.18, 4.25), pya.DPoint(-0.35, 4.25), pya.DPoint(-0.35, 4.08)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 4.08), pya.DPoint(11.12, 4.08), pya.DPoint(11.12, 4.25), pya.DPoint(10.95, 4.25), pya.DPoint(10.95, 4.08)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 3.74), pya.DPoint(-0.18, 3.74), pya.DPoint(-0.18, 3.91), pya.DPoint(-0.35, 3.91), pya.DPoint(-0.35, 3.74)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 3.74), pya.DPoint(11.12, 3.74), pya.DPoint(11.12, 3.91), pya.DPoint(10.95, 3.91), pya.DPoint(10.95, 3.74)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 3.4), pya.DPoint(-0.18, 3.4), pya.DPoint(-0.18, 3.57), pya.DPoint(-0.35, 3.57), pya.DPoint(-0.35, 3.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 3.4), pya.DPoint(11.12, 3.4), pya.DPoint(11.12, 3.57), pya.DPoint(10.95, 3.57), pya.DPoint(10.95, 3.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 3.06), pya.DPoint(-0.18, 3.06), pya.DPoint(-0.18, 3.23), pya.DPoint(-0.35, 3.23), pya.DPoint(-0.35, 3.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 3.06), pya.DPoint(11.12, 3.06), pya.DPoint(11.12, 3.23), pya.DPoint(10.95, 3.23), pya.DPoint(10.95, 3.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 2.72), pya.DPoint(-0.18, 2.72), pya.DPoint(-0.18, 2.89), pya.DPoint(-0.35, 2.89), pya.DPoint(-0.35, 2.72)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 2.72), pya.DPoint(11.12, 2.72), pya.DPoint(11.12, 2.89), pya.DPoint(10.95, 2.89), pya.DPoint(10.95, 2.72)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 2.38), pya.DPoint(-0.18, 2.38), pya.DPoint(-0.18, 2.55), pya.DPoint(-0.35, 2.55), pya.DPoint(-0.35, 2.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 2.38), pya.DPoint(11.12, 2.38), pya.DPoint(11.12, 2.55), pya.DPoint(10.95, 2.55), pya.DPoint(10.95, 2.38)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 2.04), pya.DPoint(-0.18, 2.04), pya.DPoint(-0.18, 2.21), pya.DPoint(-0.35, 2.21), pya.DPoint(-0.35, 2.04)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 2.04), pya.DPoint(11.12, 2.04), pya.DPoint(11.12, 2.21), pya.DPoint(10.95, 2.21), pya.DPoint(10.95, 2.04)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 1.7), pya.DPoint(-0.18, 1.7), pya.DPoint(-0.18, 1.87), pya.DPoint(-0.35, 1.87), pya.DPoint(-0.35, 1.7)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 1.7), pya.DPoint(11.12, 1.7), pya.DPoint(11.12, 1.87), pya.DPoint(10.95, 1.87), pya.DPoint(10.95, 1.7)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 1.36), pya.DPoint(-0.18, 1.36), pya.DPoint(-0.18, 1.53), pya.DPoint(-0.35, 1.53), pya.DPoint(-0.35, 1.36)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 1.36), pya.DPoint(11.12, 1.36), pya.DPoint(11.12, 1.53), pya.DPoint(10.95, 1.53), pya.DPoint(10.95, 1.36)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 1.02), pya.DPoint(-0.18, 1.02), pya.DPoint(-0.18, 1.19), pya.DPoint(-0.35, 1.19), pya.DPoint(-0.35, 1.02)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 1.02), pya.DPoint(11.12, 1.02), pya.DPoint(11.12, 1.19), pya.DPoint(10.95, 1.19), pya.DPoint(10.95, 1.02)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 0.68), pya.DPoint(-0.18, 0.68), pya.DPoint(-0.18, 0.85), pya.DPoint(-0.35, 0.85), pya.DPoint(-0.35, 0.68)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 0.68), pya.DPoint(11.12, 0.68), pya.DPoint(11.12, 0.85), pya.DPoint(10.95, 0.85), pya.DPoint(10.95, 0.68)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 0.34), pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 0.51), pya.DPoint(-0.35, 0.51), pya.DPoint(-0.35, 0.34)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 0.34), pya.DPoint(11.12, 0.34), pya.DPoint(11.12, 0.51), pya.DPoint(10.95, 0.51), pya.DPoint(10.95, 0.34)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 0), pya.DPoint(-0.18, 0), pya.DPoint(-0.18, 0.17), pya.DPoint(-0.35, 0.17), pya.DPoint(-0.35, 0)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, 0), pya.DPoint(11.12, 0), pya.DPoint(11.12, 0.17), pya.DPoint(10.95, 0.17), pya.DPoint(10.95, 0)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.14, -0.47), pya.DPoint(0.03, -0.47), pya.DPoint(0.03, -0.3), pya.DPoint(-0.14, -0.3), pya.DPoint(-0.14, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.2, -0.47), pya.DPoint(0.37, -0.47), pya.DPoint(0.37, -0.3), pya.DPoint(0.2, -0.3), pya.DPoint(0.2, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.54, -0.47), pya.DPoint(0.71, -0.47), pya.DPoint(0.71, -0.3), pya.DPoint(0.54, -0.3), pya.DPoint(0.54, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.88, -0.47), pya.DPoint(1.05, -0.47), pya.DPoint(1.05, -0.3), pya.DPoint(0.88, -0.3), pya.DPoint(0.88, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.22, -0.47), pya.DPoint(1.39, -0.47), pya.DPoint(1.39, -0.3), pya.DPoint(1.22, -0.3), pya.DPoint(1.22, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.56, -0.47), pya.DPoint(1.73, -0.47), pya.DPoint(1.73, -0.3), pya.DPoint(1.56, -0.3), pya.DPoint(1.56, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.9, -0.47), pya.DPoint(2.07, -0.47), pya.DPoint(2.07, -0.3), pya.DPoint(1.9, -0.3), pya.DPoint(1.9, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.24, -0.47), pya.DPoint(2.41, -0.47), pya.DPoint(2.41, -0.3), pya.DPoint(2.24, -0.3), pya.DPoint(2.24, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.58, -0.47), pya.DPoint(2.75, -0.47), pya.DPoint(2.75, -0.3), pya.DPoint(2.58, -0.3), pya.DPoint(2.58, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.92, -0.47), pya.DPoint(3.09, -0.47), pya.DPoint(3.09, -0.3), pya.DPoint(2.92, -0.3), pya.DPoint(2.92, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.26, -0.47), pya.DPoint(3.43, -0.47), pya.DPoint(3.43, -0.3), pya.DPoint(3.26, -0.3), pya.DPoint(3.26, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.6, -0.47), pya.DPoint(3.77, -0.47), pya.DPoint(3.77, -0.3), pya.DPoint(3.6, -0.3), pya.DPoint(3.6, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.94, -0.47), pya.DPoint(4.11, -0.47), pya.DPoint(4.11, -0.3), pya.DPoint(3.94, -0.3), pya.DPoint(3.94, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.28, -0.47), pya.DPoint(4.45, -0.47), pya.DPoint(4.45, -0.3), pya.DPoint(4.28, -0.3), pya.DPoint(4.28, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.62, -0.47), pya.DPoint(4.79, -0.47), pya.DPoint(4.79, -0.3), pya.DPoint(4.62, -0.3), pya.DPoint(4.62, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.96, -0.47), pya.DPoint(5.13, -0.47), pya.DPoint(5.13, -0.3), pya.DPoint(4.96, -0.3), pya.DPoint(4.96, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.3, -0.47), pya.DPoint(5.47, -0.47), pya.DPoint(5.47, -0.3), pya.DPoint(5.3, -0.3), pya.DPoint(5.3, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.64, -0.47), pya.DPoint(5.81, -0.47), pya.DPoint(5.81, -0.3), pya.DPoint(5.64, -0.3), pya.DPoint(5.64, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.98, -0.47), pya.DPoint(6.15, -0.47), pya.DPoint(6.15, -0.3), pya.DPoint(5.98, -0.3), pya.DPoint(5.98, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.32, -0.47), pya.DPoint(6.49, -0.47), pya.DPoint(6.49, -0.3), pya.DPoint(6.32, -0.3), pya.DPoint(6.32, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, -0.47), pya.DPoint(6.83, -0.47), pya.DPoint(6.83, -0.3), pya.DPoint(6.66, -0.3), pya.DPoint(6.66, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7, -0.47), pya.DPoint(7.17, -0.47), pya.DPoint(7.17, -0.3), pya.DPoint(7, -0.3), pya.DPoint(7, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.34, -0.47), pya.DPoint(7.51, -0.47), pya.DPoint(7.51, -0.3), pya.DPoint(7.34, -0.3), pya.DPoint(7.34, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.68, -0.47), pya.DPoint(7.85, -0.47), pya.DPoint(7.85, -0.3), pya.DPoint(7.68, -0.3), pya.DPoint(7.68, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.02, -0.47), pya.DPoint(8.19, -0.47), pya.DPoint(8.19, -0.3), pya.DPoint(8.02, -0.3), pya.DPoint(8.02, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, -0.47), pya.DPoint(8.53, -0.47), pya.DPoint(8.53, -0.3), pya.DPoint(8.36, -0.3), pya.DPoint(8.36, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.7, -0.47), pya.DPoint(8.87, -0.47), pya.DPoint(8.87, -0.3), pya.DPoint(8.7, -0.3), pya.DPoint(8.7, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.04, -0.47), pya.DPoint(9.21, -0.47), pya.DPoint(9.21, -0.3), pya.DPoint(9.04, -0.3), pya.DPoint(9.04, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.38, -0.47), pya.DPoint(9.55, -0.47), pya.DPoint(9.55, -0.3), pya.DPoint(9.38, -0.3), pya.DPoint(9.38, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.72, -0.47), pya.DPoint(9.89, -0.47), pya.DPoint(9.89, -0.3), pya.DPoint(9.72, -0.3), pya.DPoint(9.72, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.06, -0.47), pya.DPoint(10.23, -0.47), pya.DPoint(10.23, -0.3), pya.DPoint(10.06, -0.3), pya.DPoint(10.06, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.4, -0.47), pya.DPoint(10.57, -0.47), pya.DPoint(10.57, -0.3), pya.DPoint(10.4, -0.3), pya.DPoint(10.4, -0.47)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.74, -0.47), pya.DPoint(10.91, -0.47), pya.DPoint(10.91, -0.3), pya.DPoint(10.74, -0.3), pya.DPoint(10.74, -0.47)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, 20.87), pya.DPoint(11.12, 20.87), pya.DPoint(11.12, 21.04), pya.DPoint(-0.35, 21.04), pya.DPoint(-0.35, 20.87)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, -0.3), pya.DPoint(-0.18, -0.3), pya.DPoint(-0.18, 20.87), pya.DPoint(-0.35, 20.87), pya.DPoint(-0.35, -0.3)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.95, -0.3), pya.DPoint(11.12, -0.3), pya.DPoint(11.12, 20.87), pya.DPoint(10.95, 20.87), pya.DPoint(10.95, -0.3)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.35, -0.47), pya.DPoint(11.12, -0.47), pya.DPoint(11.12, -0.3), pya.DPoint(-0.35, -0.3), pya.DPoint(-0.35, -0.47)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.44, 21.09), pya.DPoint(5.25, 21.09), pya.DPoint(5.25, 21.35), pya.DPoint(0.44, 21.35), pya.DPoint(0.44, 21.09)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.44, 20.32), pya.DPoint(1.44, 20.32), pya.DPoint(1.44, 21.09), pya.DPoint(0.44, 21.09), pya.DPoint(0.44, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.71, 20.69), pya.DPoint(3.98, 20.69), pya.DPoint(3.98, 20.95), pya.DPoint(1.71, 20.95), pya.DPoint(1.71, 20.69)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.71, 20.32), pya.DPoint(2.71, 20.32), pya.DPoint(2.71, 20.69), pya.DPoint(1.71, 20.69), pya.DPoint(1.71, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.98, 20.32), pya.DPoint(3.98, 20.32), pya.DPoint(3.98, 20.69), pya.DPoint(2.98, 20.69), pya.DPoint(2.98, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.25, 20.32), pya.DPoint(5.25, 20.32), pya.DPoint(5.25, 21.09), pya.DPoint(4.25, 21.09), pya.DPoint(4.25, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.52, 21.09), pya.DPoint(10.33, 21.09), pya.DPoint(10.33, 21.35), pya.DPoint(5.52, 21.35), pya.DPoint(5.52, 21.09)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.52, 20.32), pya.DPoint(6.52, 20.32), pya.DPoint(6.52, 21.09), pya.DPoint(5.52, 21.09), pya.DPoint(5.52, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.79, 20.69), pya.DPoint(9.06, 20.69), pya.DPoint(9.06, 20.95), pya.DPoint(6.79, 20.95), pya.DPoint(6.79, 20.69)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.79, 20.32), pya.DPoint(7.79, 20.32), pya.DPoint(7.79, 20.69), pya.DPoint(6.79, 20.69), pya.DPoint(6.79, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.06, 20.32), pya.DPoint(9.06, 20.32), pya.DPoint(9.06, 20.69), pya.DPoint(8.06, 20.69), pya.DPoint(8.06, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.33, 20.32), pya.DPoint(10.33, 20.32), pya.DPoint(10.33, 21.09), pya.DPoint(9.33, 21.09), pya.DPoint(9.33, 20.32)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.04, 0.28), pya.DPoint(0.28, 0.28), pya.DPoint(0.28, 20.3), pya.DPoint(-0.04, 20.3), pya.DPoint(-0.04, 0.28)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(10.49, 0.28), pya.DPoint(10.81, 0.28), pya.DPoint(10.81, 20.3), pya.DPoint(10.49, 20.3), pya.DPoint(10.49, 0.28)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.98, -0.51), pya.DPoint(3.98, -0.51), pya.DPoint(3.98, 0.26), pya.DPoint(2.98, 0.26), pya.DPoint(2.98, -0.51)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.25, -0.11), pya.DPoint(5.25, -0.11), pya.DPoint(5.25, 0.26), pya.DPoint(4.25, 0.26), pya.DPoint(4.25, -0.11)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.52, -0.11), pya.DPoint(6.52, -0.11), pya.DPoint(6.52, 0.26), pya.DPoint(5.52, 0.26), pya.DPoint(5.52, -0.11)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.25, -0.37), pya.DPoint(6.52, -0.37), pya.DPoint(6.52, -0.11), pya.DPoint(4.25, -0.11), pya.DPoint(4.25, -0.37)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.79, -0.51), pya.DPoint(7.79, -0.51), pya.DPoint(7.79, 0.26), pya.DPoint(6.79, 0.26), pya.DPoint(6.79, -0.51)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.98, -0.77), pya.DPoint(7.79, -0.77), pya.DPoint(7.79, -0.51), pya.DPoint(2.98, -0.51), pya.DPoint(2.98, -0.77)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["nmos1x20_8x"] = layout.create_cell("nmos1x20_8x")
    _build_nmos1x20_8x(layout, L, cells)
    cells["nmos_1x80_2x"] = layout.create_cell("nmos_1x80_2x")
    build(layout, L, cells)
    out = "nmos_1x80_2x.gds"
    layout.write(out)
    print("Written:", out)
