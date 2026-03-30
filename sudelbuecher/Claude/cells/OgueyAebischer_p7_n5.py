"""Cell: OgueyAebischer_p7_n5
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from pmos_7x import build as _build_pmos_7x
from nmos_5x import build as _build_nmos_5x

def build(layout, L, cells):
    """Populate "OgueyAebischer_p7_n5". cells must contain: OgueyAebischer_p7_n5, pmos_7x, nmos_5x."""
    cell = cells["OgueyAebischer_p7_n5"]
    cell.insert(pya.DCellInstArray(
        cells["pmos_7x"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(4.62, 2.97))))
    cell.insert(pya.DCellInstArray(
        cells["nmos_5x"].cell_index(),
        pya.DCplxTrans(1, 180, True,
                      pya.DVector(4.62, 0.14))))
    cell.shapes(L.L_nwell_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 2), pya.DPoint(9.46, 2), pya.DPoint(9.46, 4.46), pya.DPoint(-0.22, 4.46), pya.DPoint(-0.22, 2)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(0.18, 4.03), pya.DPoint(9.06, 4.03), pya.DPoint(9.06, 4.28), pya.DPoint(0.18, 4.28), pya.DPoint(0.18, 4.03)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(0.69, -0.92), pya.DPoint(0.9, -0.92), pya.DPoint(0.9, 1.69), pya.DPoint(0.69, 1.69), pya.DPoint(0.69, -0.92)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(8.34, -0.92), pya.DPoint(8.55, -0.92), pya.DPoint(8.55, 1.69), pya.DPoint(8.34, 1.69), pya.DPoint(8.34, -0.92)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(0.69, -1.13), pya.DPoint(8.55, -1.13), pya.DPoint(8.55, -0.92), pya.DPoint(0.69, -0.92), pya.DPoint(0.69, -1.13)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(0.565, -0.795), pya.DPoint(1.025, -0.795), pya.DPoint(1.025, 2.055), pya.DPoint(0.565, 2.055), pya.DPoint(0.565, -0.795)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(8.215, -0.795), pya.DPoint(8.675, -0.795), pya.DPoint(8.675, 2.055), pya.DPoint(8.215, 2.055), pya.DPoint(8.215, -0.795)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(0.565, -1.255), pya.DPoint(8.675, -1.255), pya.DPoint(8.675, -0.795), pya.DPoint(0.565, -0.795), pya.DPoint(0.565, -1.255)]))
    cell.shapes(L.L_nsdm_drawing).insert(
        pya.DPolygon([pya.DPoint(0.055, 3.905), pya.DPoint(9.185, 3.905), pya.DPoint(9.185, 4.405), pya.DPoint(0.055, 4.405), pya.DPoint(0.055, 3.905)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.455, 4.07), pya.DPoint(0.625, 4.07), pya.DPoint(0.625, 4.24), pya.DPoint(0.455, 4.24), pya.DPoint(0.455, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.795, 4.07), pya.DPoint(0.965, 4.07), pya.DPoint(0.965, 4.24), pya.DPoint(0.795, 4.24), pya.DPoint(0.795, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.135, 4.07), pya.DPoint(1.305, 4.07), pya.DPoint(1.305, 4.24), pya.DPoint(1.135, 4.24), pya.DPoint(1.135, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.475, 4.07), pya.DPoint(1.645, 4.07), pya.DPoint(1.645, 4.24), pya.DPoint(1.475, 4.24), pya.DPoint(1.475, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.815, 4.07), pya.DPoint(1.985, 4.07), pya.DPoint(1.985, 4.24), pya.DPoint(1.815, 4.24), pya.DPoint(1.815, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.155, 4.07), pya.DPoint(2.325, 4.07), pya.DPoint(2.325, 4.24), pya.DPoint(2.155, 4.24), pya.DPoint(2.155, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.495, 4.07), pya.DPoint(2.665, 4.07), pya.DPoint(2.665, 4.24), pya.DPoint(2.495, 4.24), pya.DPoint(2.495, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.835, 4.07), pya.DPoint(3.005, 4.07), pya.DPoint(3.005, 4.24), pya.DPoint(2.835, 4.24), pya.DPoint(2.835, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.175, 4.07), pya.DPoint(3.345, 4.07), pya.DPoint(3.345, 4.24), pya.DPoint(3.175, 4.24), pya.DPoint(3.175, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.515, 4.07), pya.DPoint(3.685, 4.07), pya.DPoint(3.685, 4.24), pya.DPoint(3.515, 4.24), pya.DPoint(3.515, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.855, 4.07), pya.DPoint(4.025, 4.07), pya.DPoint(4.025, 4.24), pya.DPoint(3.855, 4.24), pya.DPoint(3.855, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.195, 4.07), pya.DPoint(4.365, 4.07), pya.DPoint(4.365, 4.24), pya.DPoint(4.195, 4.24), pya.DPoint(4.195, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.535, 4.07), pya.DPoint(4.705, 4.07), pya.DPoint(4.705, 4.24), pya.DPoint(4.535, 4.24), pya.DPoint(4.535, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.875, 4.07), pya.DPoint(5.045, 4.07), pya.DPoint(5.045, 4.24), pya.DPoint(4.875, 4.24), pya.DPoint(4.875, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.215, 4.07), pya.DPoint(5.385, 4.07), pya.DPoint(5.385, 4.24), pya.DPoint(5.215, 4.24), pya.DPoint(5.215, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.555, 4.07), pya.DPoint(5.725, 4.07), pya.DPoint(5.725, 4.24), pya.DPoint(5.555, 4.24), pya.DPoint(5.555, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.895, 4.07), pya.DPoint(6.065, 4.07), pya.DPoint(6.065, 4.24), pya.DPoint(5.895, 4.24), pya.DPoint(5.895, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.235, 4.07), pya.DPoint(6.405, 4.07), pya.DPoint(6.405, 4.24), pya.DPoint(6.235, 4.24), pya.DPoint(6.235, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.575, 4.07), pya.DPoint(6.745, 4.07), pya.DPoint(6.745, 4.24), pya.DPoint(6.575, 4.24), pya.DPoint(6.575, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.915, 4.07), pya.DPoint(7.085, 4.07), pya.DPoint(7.085, 4.24), pya.DPoint(6.915, 4.24), pya.DPoint(6.915, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.255, 4.07), pya.DPoint(7.425, 4.07), pya.DPoint(7.425, 4.24), pya.DPoint(7.255, 4.24), pya.DPoint(7.255, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.595, 4.07), pya.DPoint(7.765, 4.07), pya.DPoint(7.765, 4.24), pya.DPoint(7.595, 4.24), pya.DPoint(7.595, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.935, 4.07), pya.DPoint(8.105, 4.07), pya.DPoint(8.105, 4.24), pya.DPoint(7.935, 4.24), pya.DPoint(7.935, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.275, 4.07), pya.DPoint(8.445, 4.07), pya.DPoint(8.445, 4.24), pya.DPoint(8.275, 4.24), pya.DPoint(8.275, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.615, 4.07), pya.DPoint(8.785, 4.07), pya.DPoint(8.785, 4.24), pya.DPoint(8.615, 4.24), pya.DPoint(8.615, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, 1.3), pya.DPoint(0.88, 1.3), pya.DPoint(0.88, 1.47), pya.DPoint(0.71, 1.47), pya.DPoint(0.71, 1.3)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, 1.3), pya.DPoint(8.53, 1.3), pya.DPoint(8.53, 1.47), pya.DPoint(8.36, 1.47), pya.DPoint(8.36, 1.3)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, 0.96), pya.DPoint(0.88, 0.96), pya.DPoint(0.88, 1.13), pya.DPoint(0.71, 1.13), pya.DPoint(0.71, 0.96)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, 0.96), pya.DPoint(8.53, 0.96), pya.DPoint(8.53, 1.13), pya.DPoint(8.36, 1.13), pya.DPoint(8.36, 0.96)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, 0.62), pya.DPoint(0.88, 0.62), pya.DPoint(0.88, 0.79), pya.DPoint(0.71, 0.79), pya.DPoint(0.71, 0.62)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, 0.62), pya.DPoint(8.53, 0.62), pya.DPoint(8.53, 0.79), pya.DPoint(8.36, 0.79), pya.DPoint(8.36, 0.62)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, 0.28), pya.DPoint(0.88, 0.28), pya.DPoint(0.88, 0.45), pya.DPoint(0.71, 0.45), pya.DPoint(0.71, 0.28)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, 0.28), pya.DPoint(8.53, 0.28), pya.DPoint(8.53, 0.45), pya.DPoint(8.36, 0.45), pya.DPoint(8.36, 0.28)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, -0.06), pya.DPoint(0.88, -0.06), pya.DPoint(0.88, 0.11), pya.DPoint(0.71, 0.11), pya.DPoint(0.71, -0.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, -0.06), pya.DPoint(8.53, -0.06), pya.DPoint(8.53, 0.11), pya.DPoint(8.36, 0.11), pya.DPoint(8.36, -0.06)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, -0.4), pya.DPoint(0.88, -0.4), pya.DPoint(0.88, -0.23), pya.DPoint(0.71, -0.23), pya.DPoint(0.71, -0.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, -0.4), pya.DPoint(8.53, -0.4), pya.DPoint(8.53, -0.23), pya.DPoint(8.36, -0.23), pya.DPoint(8.36, -0.4)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, -0.74), pya.DPoint(0.88, -0.74), pya.DPoint(0.88, -0.57), pya.DPoint(0.71, -0.57), pya.DPoint(0.71, -0.74)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, -0.74), pya.DPoint(8.53, -0.74), pya.DPoint(8.53, -0.57), pya.DPoint(8.36, -0.57), pya.DPoint(8.36, -0.74)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.135, -1.11), pya.DPoint(1.305, -1.11), pya.DPoint(1.305, -0.94), pya.DPoint(1.135, -0.94), pya.DPoint(1.135, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.475, -1.11), pya.DPoint(1.645, -1.11), pya.DPoint(1.645, -0.94), pya.DPoint(1.475, -0.94), pya.DPoint(1.475, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.815, -1.11), pya.DPoint(1.985, -1.11), pya.DPoint(1.985, -0.94), pya.DPoint(1.815, -0.94), pya.DPoint(1.815, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.155, -1.11), pya.DPoint(2.325, -1.11), pya.DPoint(2.325, -0.94), pya.DPoint(2.155, -0.94), pya.DPoint(2.155, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.495, -1.11), pya.DPoint(2.665, -1.11), pya.DPoint(2.665, -0.94), pya.DPoint(2.495, -0.94), pya.DPoint(2.495, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.835, -1.11), pya.DPoint(3.005, -1.11), pya.DPoint(3.005, -0.94), pya.DPoint(2.835, -0.94), pya.DPoint(2.835, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.175, -1.11), pya.DPoint(3.345, -1.11), pya.DPoint(3.345, -0.94), pya.DPoint(3.175, -0.94), pya.DPoint(3.175, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.515, -1.11), pya.DPoint(3.685, -1.11), pya.DPoint(3.685, -0.94), pya.DPoint(3.515, -0.94), pya.DPoint(3.515, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.855, -1.11), pya.DPoint(4.025, -1.11), pya.DPoint(4.025, -0.94), pya.DPoint(3.855, -0.94), pya.DPoint(3.855, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.195, -1.11), pya.DPoint(4.365, -1.11), pya.DPoint(4.365, -0.94), pya.DPoint(4.195, -0.94), pya.DPoint(4.195, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.535, -1.11), pya.DPoint(4.705, -1.11), pya.DPoint(4.705, -0.94), pya.DPoint(4.535, -0.94), pya.DPoint(4.535, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.875, -1.11), pya.DPoint(5.045, -1.11), pya.DPoint(5.045, -0.94), pya.DPoint(4.875, -0.94), pya.DPoint(4.875, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.215, -1.11), pya.DPoint(5.385, -1.11), pya.DPoint(5.385, -0.94), pya.DPoint(5.215, -0.94), pya.DPoint(5.215, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.555, -1.11), pya.DPoint(5.725, -1.11), pya.DPoint(5.725, -0.94), pya.DPoint(5.555, -0.94), pya.DPoint(5.555, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.895, -1.11), pya.DPoint(6.065, -1.11), pya.DPoint(6.065, -0.94), pya.DPoint(5.895, -0.94), pya.DPoint(5.895, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.235, -1.11), pya.DPoint(6.405, -1.11), pya.DPoint(6.405, -0.94), pya.DPoint(6.235, -0.94), pya.DPoint(6.235, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.575, -1.11), pya.DPoint(6.745, -1.11), pya.DPoint(6.745, -0.94), pya.DPoint(6.575, -0.94), pya.DPoint(6.575, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.915, -1.11), pya.DPoint(7.085, -1.11), pya.DPoint(7.085, -0.94), pya.DPoint(6.915, -0.94), pya.DPoint(6.915, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.255, -1.11), pya.DPoint(7.425, -1.11), pya.DPoint(7.425, -0.94), pya.DPoint(7.255, -0.94), pya.DPoint(7.255, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.595, -1.11), pya.DPoint(7.765, -1.11), pya.DPoint(7.765, -0.94), pya.DPoint(7.595, -0.94), pya.DPoint(7.595, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.935, -1.11), pya.DPoint(8.105, -1.11), pya.DPoint(8.105, -0.94), pya.DPoint(7.935, -0.94), pya.DPoint(7.935, -1.11)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.29, 4.07), pya.DPoint(8.95, 4.07), pya.DPoint(8.95, 4.24), pya.DPoint(0.29, 4.24), pya.DPoint(0.29, 4.07)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.29, 3.53), pya.DPoint(8.95, 3.53), pya.DPoint(8.95, 3.7), pya.DPoint(0.29, 3.7), pya.DPoint(0.29, 3.53)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, -0.94), pya.DPoint(0.88, -0.94), pya.DPoint(0.88, 1.67), pya.DPoint(0.71, 1.67), pya.DPoint(0.71, -0.94)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.36, -0.94), pya.DPoint(8.53, -0.94), pya.DPoint(8.53, 1.67), pya.DPoint(8.36, 1.67), pya.DPoint(8.36, -0.94)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.71, -1.11), pya.DPoint(8.53, -1.11), pya.DPoint(8.53, -0.94), pya.DPoint(0.71, -0.94), pya.DPoint(0.71, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.545, 4.07), pya.DPoint(0.715, 4.07), pya.DPoint(0.715, 4.24), pya.DPoint(0.545, 4.24), pya.DPoint(0.545, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.905, 4.07), pya.DPoint(1.075, 4.07), pya.DPoint(1.075, 4.24), pya.DPoint(0.905, 4.24), pya.DPoint(0.905, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.815, 4.07), pya.DPoint(1.985, 4.07), pya.DPoint(1.985, 4.24), pya.DPoint(1.815, 4.24), pya.DPoint(1.815, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(2.175, 4.07), pya.DPoint(2.345, 4.07), pya.DPoint(2.345, 4.24), pya.DPoint(2.175, 4.24), pya.DPoint(2.175, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(3.085, 4.07), pya.DPoint(3.255, 4.07), pya.DPoint(3.255, 4.24), pya.DPoint(3.085, 4.24), pya.DPoint(3.085, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(3.445, 4.07), pya.DPoint(3.615, 4.07), pya.DPoint(3.615, 4.24), pya.DPoint(3.445, 4.24), pya.DPoint(3.445, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(4.355, 4.07), pya.DPoint(4.525, 4.07), pya.DPoint(4.525, 4.24), pya.DPoint(4.355, 4.24), pya.DPoint(4.355, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(4.715, 4.07), pya.DPoint(4.885, 4.07), pya.DPoint(4.885, 4.24), pya.DPoint(4.715, 4.24), pya.DPoint(4.715, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(5.625, 4.07), pya.DPoint(5.795, 4.07), pya.DPoint(5.795, 4.24), pya.DPoint(5.625, 4.24), pya.DPoint(5.625, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(5.985, 4.07), pya.DPoint(6.155, 4.07), pya.DPoint(6.155, 4.24), pya.DPoint(5.985, 4.24), pya.DPoint(5.985, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(6.895, 4.07), pya.DPoint(7.065, 4.07), pya.DPoint(7.065, 4.24), pya.DPoint(6.895, 4.24), pya.DPoint(6.895, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(7.255, 4.07), pya.DPoint(7.425, 4.07), pya.DPoint(7.425, 4.24), pya.DPoint(7.255, 4.24), pya.DPoint(7.255, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(8.165, 4.07), pya.DPoint(8.335, 4.07), pya.DPoint(8.335, 4.24), pya.DPoint(8.165, 4.24), pya.DPoint(8.165, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(8.525, 4.07), pya.DPoint(8.695, 4.07), pya.DPoint(8.695, 4.24), pya.DPoint(8.525, 4.24), pya.DPoint(8.525, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(4.355, -1.11), pya.DPoint(4.525, -1.11), pya.DPoint(4.525, -0.94), pya.DPoint(4.355, -0.94), pya.DPoint(4.355, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(4.715, -1.11), pya.DPoint(4.885, -1.11), pya.DPoint(4.885, -0.94), pya.DPoint(4.715, -0.94), pya.DPoint(4.715, -1.11)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.31, 3.73), pya.DPoint(1.31, 3.73), pya.DPoint(1.31, 4.28), pya.DPoint(0.31, 4.28), pya.DPoint(0.31, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.58, 3.73), pya.DPoint(2.58, 3.73), pya.DPoint(2.58, 4.28), pya.DPoint(1.58, 4.28), pya.DPoint(1.58, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.85, 3.73), pya.DPoint(3.85, 3.73), pya.DPoint(3.85, 4.28), pya.DPoint(2.85, 4.28), pya.DPoint(2.85, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.12, 3.73), pya.DPoint(5.12, 3.73), pya.DPoint(5.12, 4.28), pya.DPoint(4.12, 4.28), pya.DPoint(4.12, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.39, 3.73), pya.DPoint(6.39, 3.73), pya.DPoint(6.39, 4.28), pya.DPoint(5.39, 4.28), pya.DPoint(5.39, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, 3.73), pya.DPoint(7.66, 3.73), pya.DPoint(7.66, 4.28), pya.DPoint(6.66, 4.28), pya.DPoint(6.66, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.93, 3.73), pya.DPoint(8.93, 3.73), pya.DPoint(8.93, 4.28), pya.DPoint(7.93, 4.28), pya.DPoint(7.93, 3.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.31, 3.5), pya.DPoint(8.93, 3.5), pya.DPoint(8.93, 3.73), pya.DPoint(0.31, 3.73), pya.DPoint(0.31, 3.5)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 1.81), pya.DPoint(0.1, 1.81), pya.DPoint(0.1, 3.48), pya.DPoint(-0.22, 3.48), pya.DPoint(-0.22, 1.81)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.31, 1.01), pya.DPoint(0.63, 1.01), pya.DPoint(0.63, 2.44), pya.DPoint(0.31, 2.44), pya.DPoint(0.31, 1.01)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.1, -0.37), pya.DPoint(1.42, -0.37), pya.DPoint(1.42, 1.67), pya.DPoint(1.1, 1.67), pya.DPoint(1.1, -0.37)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.58, 1.41), pya.DPoint(1.9, 1.41), pya.DPoint(1.9, 2.44), pya.DPoint(1.58, 2.44), pya.DPoint(1.58, 1.41)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.26, 0.67), pya.DPoint(2.58, 0.67), pya.DPoint(2.58, 2.07), pya.DPoint(2.26, 2.07), pya.DPoint(2.26, 0.67)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.85, 1.41), pya.DPoint(3.17, 1.41), pya.DPoint(3.17, 2.44), pya.DPoint(2.85, 2.44), pya.DPoint(2.85, 1.41)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.53, 0.67), pya.DPoint(3.85, 0.67), pya.DPoint(3.85, 2.07), pya.DPoint(3.53, 2.07), pya.DPoint(3.53, 0.67)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.12, 1.81), pya.DPoint(4.44, 1.81), pya.DPoint(4.44, 2.44), pya.DPoint(4.12, 2.44), pya.DPoint(4.12, 1.81)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.8, 0.67), pya.DPoint(5.12, 0.67), pya.DPoint(5.12, 1.67), pya.DPoint(4.8, 1.67), pya.DPoint(4.8, 0.67)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.39, 1.41), pya.DPoint(5.71, 1.41), pya.DPoint(5.71, 2.44), pya.DPoint(5.39, 2.44), pya.DPoint(5.39, 1.41)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.07, 0.67), pya.DPoint(6.39, 0.67), pya.DPoint(6.39, 2.07), pya.DPoint(6.07, 2.07), pya.DPoint(6.07, 0.67)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, 1.41), pya.DPoint(6.98, 1.41), pya.DPoint(6.98, 2.44), pya.DPoint(6.66, 2.44), pya.DPoint(6.66, 1.41)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.34, 0.67), pya.DPoint(7.66, 0.67), pya.DPoint(7.66, 2.07), pya.DPoint(7.34, 2.07), pya.DPoint(7.34, 0.67)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(7.82, -0.37), pya.DPoint(8.14, -0.37), pya.DPoint(8.14, 1.67), pya.DPoint(7.82, 1.67), pya.DPoint(7.82, -0.37)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(8.61, 1.01), pya.DPoint(8.93, 1.01), pya.DPoint(8.93, 2.44), pya.DPoint(8.61, 2.44), pya.DPoint(8.61, 1.01)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(9.14, 1.81), pya.DPoint(9.46, 1.81), pya.DPoint(9.46, 3.48), pya.DPoint(9.14, 3.48), pya.DPoint(9.14, 1.81)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(2.26, -1.02), pya.DPoint(2.58, -1.02), pya.DPoint(2.58, -0.39), pya.DPoint(2.26, -0.39), pya.DPoint(2.26, -1.02)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(3.53, -1.02), pya.DPoint(3.85, -1.02), pya.DPoint(3.85, -0.39), pya.DPoint(3.53, -0.39), pya.DPoint(3.53, -1.02)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(4.12, -1.42), pya.DPoint(5.12, -1.42), pya.DPoint(5.12, -0.39), pya.DPoint(4.12, -0.39), pya.DPoint(4.12, -1.42)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(5.39, -1.02), pya.DPoint(5.71, -1.02), pya.DPoint(5.71, -0.39), pya.DPoint(5.39, -0.39), pya.DPoint(5.39, -1.02)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(6.66, -1.02), pya.DPoint(6.98, -1.02), pya.DPoint(6.98, -0.39), pya.DPoint(6.66, -0.39), pya.DPoint(6.66, -1.02)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.415, 3.925), pya.DPoint(0.565, 3.925), pya.DPoint(0.565, 4.075), pya.DPoint(0.415, 4.075), pya.DPoint(0.415, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.735, 3.925), pya.DPoint(0.885, 3.925), pya.DPoint(0.885, 4.075), pya.DPoint(0.735, 4.075), pya.DPoint(0.735, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.055, 3.925), pya.DPoint(1.205, 3.925), pya.DPoint(1.205, 4.075), pya.DPoint(1.055, 4.075), pya.DPoint(1.055, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.685, 3.925), pya.DPoint(1.835, 3.925), pya.DPoint(1.835, 4.075), pya.DPoint(1.685, 4.075), pya.DPoint(1.685, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.005, 3.925), pya.DPoint(2.155, 3.925), pya.DPoint(2.155, 4.075), pya.DPoint(2.005, 4.075), pya.DPoint(2.005, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.325, 3.925), pya.DPoint(2.475, 3.925), pya.DPoint(2.475, 4.075), pya.DPoint(2.325, 4.075), pya.DPoint(2.325, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.955, 3.925), pya.DPoint(3.105, 3.925), pya.DPoint(3.105, 4.075), pya.DPoint(2.955, 4.075), pya.DPoint(2.955, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(3.275, 3.925), pya.DPoint(3.425, 3.925), pya.DPoint(3.425, 4.075), pya.DPoint(3.275, 4.075), pya.DPoint(3.275, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(3.595, 3.925), pya.DPoint(3.745, 3.925), pya.DPoint(3.745, 4.075), pya.DPoint(3.595, 4.075), pya.DPoint(3.595, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.225, 3.925), pya.DPoint(4.375, 3.925), pya.DPoint(4.375, 4.075), pya.DPoint(4.225, 4.075), pya.DPoint(4.225, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.545, 3.925), pya.DPoint(4.695, 3.925), pya.DPoint(4.695, 4.075), pya.DPoint(4.545, 4.075), pya.DPoint(4.545, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.865, 3.925), pya.DPoint(5.015, 3.925), pya.DPoint(5.015, 4.075), pya.DPoint(4.865, 4.075), pya.DPoint(4.865, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(5.495, 3.925), pya.DPoint(5.645, 3.925), pya.DPoint(5.645, 4.075), pya.DPoint(5.495, 4.075), pya.DPoint(5.495, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(5.815, 3.925), pya.DPoint(5.965, 3.925), pya.DPoint(5.965, 4.075), pya.DPoint(5.815, 4.075), pya.DPoint(5.815, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.135, 3.925), pya.DPoint(6.285, 3.925), pya.DPoint(6.285, 4.075), pya.DPoint(6.135, 4.075), pya.DPoint(6.135, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.765, 3.925), pya.DPoint(6.915, 3.925), pya.DPoint(6.915, 4.075), pya.DPoint(6.765, 4.075), pya.DPoint(6.765, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.085, 3.925), pya.DPoint(7.235, 3.925), pya.DPoint(7.235, 4.075), pya.DPoint(7.085, 4.075), pya.DPoint(7.085, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.405, 3.925), pya.DPoint(7.555, 3.925), pya.DPoint(7.555, 4.075), pya.DPoint(7.405, 4.075), pya.DPoint(7.405, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.035, 3.925), pya.DPoint(8.185, 3.925), pya.DPoint(8.185, 4.075), pya.DPoint(8.035, 4.075), pya.DPoint(8.035, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.355, 3.925), pya.DPoint(8.505, 3.925), pya.DPoint(8.505, 4.075), pya.DPoint(8.355, 4.075), pya.DPoint(8.355, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.675, 3.925), pya.DPoint(8.825, 3.925), pya.DPoint(8.825, 4.075), pya.DPoint(8.675, 4.075), pya.DPoint(8.675, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.135, 1.865), pya.DPoint(0.015, 1.865), pya.DPoint(0.015, 2.015), pya.DPoint(-0.135, 2.015), pya.DPoint(-0.135, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.345, 1.865), pya.DPoint(2.495, 1.865), pya.DPoint(2.495, 2.015), pya.DPoint(2.345, 2.015), pya.DPoint(2.345, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(3.615, 1.865), pya.DPoint(3.765, 1.865), pya.DPoint(3.765, 2.015), pya.DPoint(3.615, 2.015), pya.DPoint(3.615, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.205, 1.865), pya.DPoint(4.355, 1.865), pya.DPoint(4.355, 2.015), pya.DPoint(4.205, 2.015), pya.DPoint(4.205, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.155, 1.865), pya.DPoint(6.305, 1.865), pya.DPoint(6.305, 2.015), pya.DPoint(6.155, 2.015), pya.DPoint(6.155, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.425, 1.865), pya.DPoint(7.575, 1.865), pya.DPoint(7.575, 2.015), pya.DPoint(7.425, 2.015), pya.DPoint(7.425, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(9.225, 1.865), pya.DPoint(9.375, 1.865), pya.DPoint(9.375, 2.015), pya.DPoint(9.225, 2.015), pya.DPoint(9.225, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.185, 1.465), pya.DPoint(1.335, 1.465), pya.DPoint(1.335, 1.615), pya.DPoint(1.185, 1.615), pya.DPoint(1.185, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.665, 1.465), pya.DPoint(1.815, 1.465), pya.DPoint(1.815, 1.615), pya.DPoint(1.665, 1.615), pya.DPoint(1.665, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.935, 1.465), pya.DPoint(3.085, 1.465), pya.DPoint(3.085, 1.615), pya.DPoint(2.935, 1.615), pya.DPoint(2.935, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.885, 1.465), pya.DPoint(5.035, 1.465), pya.DPoint(5.035, 1.615), pya.DPoint(4.885, 1.615), pya.DPoint(4.885, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(5.475, 1.465), pya.DPoint(5.625, 1.465), pya.DPoint(5.625, 1.615), pya.DPoint(5.475, 1.615), pya.DPoint(5.475, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.745, 1.465), pya.DPoint(6.895, 1.465), pya.DPoint(6.895, 1.615), pya.DPoint(6.745, 1.615), pya.DPoint(6.745, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(7.905, 1.465), pya.DPoint(8.055, 1.465), pya.DPoint(8.055, 1.615), pya.DPoint(7.905, 1.615), pya.DPoint(7.905, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.395, 1.065), pya.DPoint(0.545, 1.065), pya.DPoint(0.545, 1.215), pya.DPoint(0.395, 1.215), pya.DPoint(0.395, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(8.695, 1.065), pya.DPoint(8.845, 1.065), pya.DPoint(8.845, 1.215), pya.DPoint(8.695, 1.215), pya.DPoint(8.695, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(2.345, -0.965), pya.DPoint(2.495, -0.965), pya.DPoint(2.495, -0.815), pya.DPoint(2.345, -0.815), pya.DPoint(2.345, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(3.615, -0.965), pya.DPoint(3.765, -0.965), pya.DPoint(3.765, -0.815), pya.DPoint(3.615, -0.815), pya.DPoint(3.615, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(5.475, -0.965), pya.DPoint(5.625, -0.965), pya.DPoint(5.625, -0.815), pya.DPoint(5.475, -0.815), pya.DPoint(5.475, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(6.745, -0.965), pya.DPoint(6.895, -0.965), pya.DPoint(6.895, -0.815), pya.DPoint(6.745, -0.815), pya.DPoint(6.745, -0.965)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.225, -1.365), pya.DPoint(4.375, -1.365), pya.DPoint(4.375, -1.215), pya.DPoint(4.225, -1.215), pya.DPoint(4.225, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.545, -1.365), pya.DPoint(4.695, -1.365), pya.DPoint(4.695, -1.215), pya.DPoint(4.545, -1.215), pya.DPoint(4.545, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(4.865, -1.365), pya.DPoint(5.015, -1.365), pya.DPoint(5.015, -1.215), pya.DPoint(4.865, -1.215), pya.DPoint(4.865, -1.365)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 3.87), pya.DPoint(9.46, 3.87), pya.DPoint(9.46, 4.13), pya.DPoint(-0.22, 4.13), pya.DPoint(-0.22, 3.87)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 1.81), pya.DPoint(9.46, 1.81), pya.DPoint(9.46, 2.07), pya.DPoint(-0.22, 2.07), pya.DPoint(-0.22, 1.81)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 1.41), pya.DPoint(9.46, 1.41), pya.DPoint(9.46, 1.67), pya.DPoint(-0.22, 1.67), pya.DPoint(-0.22, 1.41)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, 1.01), pya.DPoint(9.46, 1.01), pya.DPoint(9.46, 1.27), pya.DPoint(-0.22, 1.27), pya.DPoint(-0.22, 1.01)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, -1.02), pya.DPoint(9.46, -1.02), pya.DPoint(9.46, -0.76), pya.DPoint(-0.22, -0.76), pya.DPoint(-0.22, -1.02)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.22, -1.42), pya.DPoint(9.46, -1.42), pya.DPoint(9.46, -1.16), pya.DPoint(-0.22, -1.16), pya.DPoint(-0.22, -1.42)]))


if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["pmos_7x"] = layout.create_cell("pmos_7x")
    _build_pmos_7x(layout, L, cells)
    cells["nmos_5x"] = layout.create_cell("nmos_5x")
    _build_nmos_5x(layout, L, cells)
    cells["OgueyAebischer_p7_n5"] = layout.create_cell("OgueyAebischer_p7_n5")
    build(layout, L, cells)
    out = "OgueyAebischer_p7_n5.gds"
    layout.write(out)
    print("Written:", out)
