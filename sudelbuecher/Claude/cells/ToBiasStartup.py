"""Cell: ToBiasStartup
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

def build(layout, L, cells):
    """Populate "ToBiasStartup". cells must contain: ToBiasStartup, shortpmos_2x, shortnmos_2x, nmos_8x2, flatpmos1x0_3."""
    cell = cells["ToBiasStartup"]
    cell.insert(pya.DCellInstArray(
        cells["shortpmos_2x"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(0.9, 3.02))))
    cell.insert(pya.DCellInstArray(
        cells["shortnmos_2x"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(0.9, -0.21))))
    cell.insert(pya.DCellInstArray(
        cells["nmos_8x2"].cell_index(),
        pya.DCplxTrans(1, 180, True,
                      pya.DVector(1.5, -19.86))))
    cell.insert(pya.DCellInstArray(
        cells["nmos_8x2"].cell_index(),
        pya.DCplxTrans(1, 180, True,
                      pya.DVector(1.5, -10.78))))
    cell.insert(pya.DCellInstArray(
        cells["flatpmos1x0_3"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(-2.86, 3.02))))
    cell.shapes(L.L_nwell_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, 2), pya.DPoint(2.35, 2), pya.DPoint(2.35, 4.46), pya.DPoint(-3.67, 4.46), pya.DPoint(-3.67, 2)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.49, 4.03), pya.DPoint(2.17, 4.03), pya.DPoint(2.17, 4.28), pya.DPoint(-3.49, 4.28), pya.DPoint(-3.49, 4.03)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.26, -1.13), pya.DPoint(2.06, -1.13), pya.DPoint(2.06, -0.92), pya.DPoint(-0.26, -0.92), pya.DPoint(-0.26, -1.13)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.56, -2.05), pya.DPoint(1.98, -2.05), pya.DPoint(1.98, -1.84), pya.DPoint(-1.56, -1.84), pya.DPoint(-1.56, -2.05)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.56, -10.92), pya.DPoint(-1.35, -10.92), pya.DPoint(-1.35, -2.05), pya.DPoint(-1.56, -2.05), pya.DPoint(-1.56, -10.92)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(1.77, -10.92), pya.DPoint(1.98, -10.92), pya.DPoint(1.98, -2.05), pya.DPoint(1.77, -2.05), pya.DPoint(1.77, -10.92)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.56, -11.13), pya.DPoint(1.98, -11.13), pya.DPoint(1.98, -10.92), pya.DPoint(-1.56, -10.92), pya.DPoint(-1.56, -11.13)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.56, -20), pya.DPoint(-1.35, -20), pya.DPoint(-1.35, -11.13), pya.DPoint(-1.56, -11.13), pya.DPoint(-1.56, -20)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(1.77, -20), pya.DPoint(1.98, -20), pya.DPoint(1.98, -11.13), pya.DPoint(1.77, -11.13), pya.DPoint(1.77, -20)]))
    cell.shapes(L.L_tap_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.56, -20.21), pya.DPoint(1.98, -20.21), pya.DPoint(1.98, -20), pya.DPoint(-1.56, -20), pya.DPoint(-1.56, -20.21)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.385, -1.255), pya.DPoint(2.185, -1.255), pya.DPoint(2.185, -0.795), pya.DPoint(-0.385, -0.795), pya.DPoint(-0.385, -1.255)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.685, -2.175), pya.DPoint(2.105, -2.175), pya.DPoint(2.105, -1.715), pya.DPoint(-1.685, -1.715), pya.DPoint(-1.685, -2.175)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.685, -10.795), pya.DPoint(-1.225, -10.795), pya.DPoint(-1.225, -2.175), pya.DPoint(-1.685, -2.175), pya.DPoint(-1.685, -10.795)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(1.645, -10.795), pya.DPoint(2.105, -10.795), pya.DPoint(2.105, -2.175), pya.DPoint(1.645, -2.175), pya.DPoint(1.645, -10.795)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.685, -11.255), pya.DPoint(2.105, -11.255), pya.DPoint(2.105, -10.795), pya.DPoint(-1.685, -10.795), pya.DPoint(-1.685, -11.255)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.685, -19.875), pya.DPoint(-1.225, -19.875), pya.DPoint(-1.225, -11.255), pya.DPoint(-1.685, -11.255), pya.DPoint(-1.685, -19.875)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(1.645, -19.875), pya.DPoint(2.105, -19.875), pya.DPoint(2.105, -11.255), pya.DPoint(1.645, -11.255), pya.DPoint(1.645, -19.875)]))
    cell.shapes(L.L_psdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.685, -20.335), pya.DPoint(2.105, -20.335), pya.DPoint(2.105, -19.875), pya.DPoint(-1.685, -19.875), pya.DPoint(-1.685, -20.335)]))
    cell.shapes(L.L_nsdm_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.615, 3.905), pya.DPoint(2.295, 3.905), pya.DPoint(2.295, 4.405), pya.DPoint(-3.615, 4.405), pya.DPoint(-3.615, 3.905)]))
    cell.shapes(L.L_poly_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.36, 2.87), pya.DPoint(-1.32, 2.87), pya.DPoint(-1.32, 3.17), pya.DPoint(-2.36, 3.17), pya.DPoint(-2.36, 2.87)]))
    cell.shapes(L.L_poly_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.82, 2.87), pya.DPoint(-0.24, 2.87), pya.DPoint(-0.24, 3.17), pya.DPoint(-0.82, 3.17), pya.DPoint(-0.82, 2.87)]))
    cell.shapes(L.L_poly_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.28, -0.36), pya.DPoint(-0.24, -0.36), pya.DPoint(-0.24, -0.06), pya.DPoint(-1.28, -0.06), pya.DPoint(-1.28, -0.36)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.285, 4.07), pya.DPoint(-3.115, 4.07), pya.DPoint(-3.115, 4.24), pya.DPoint(-3.285, 4.24), pya.DPoint(-3.285, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.945, 4.07), pya.DPoint(-2.775, 4.07), pya.DPoint(-2.775, 4.24), pya.DPoint(-2.945, 4.24), pya.DPoint(-2.945, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.605, 4.07), pya.DPoint(-2.435, 4.07), pya.DPoint(-2.435, 4.24), pya.DPoint(-2.605, 4.24), pya.DPoint(-2.605, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.035, 4.07), pya.DPoint(0.135, 4.07), pya.DPoint(0.135, 4.24), pya.DPoint(-0.035, 4.24), pya.DPoint(-0.035, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.305, 4.07), pya.DPoint(0.475, 4.07), pya.DPoint(0.475, 4.24), pya.DPoint(0.305, 4.24), pya.DPoint(0.305, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.645, 4.07), pya.DPoint(0.815, 4.07), pya.DPoint(0.815, 4.24), pya.DPoint(0.645, 4.24), pya.DPoint(0.645, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.985, 4.07), pya.DPoint(1.155, 4.07), pya.DPoint(1.155, 4.24), pya.DPoint(0.985, 4.24), pya.DPoint(0.985, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.325, 4.07), pya.DPoint(1.495, 4.07), pya.DPoint(1.495, 4.24), pya.DPoint(1.325, 4.24), pya.DPoint(1.325, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.665, 4.07), pya.DPoint(1.835, 4.07), pya.DPoint(1.835, 4.24), pya.DPoint(1.665, 4.24), pya.DPoint(1.665, 4.07)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.615, 2.935), pya.DPoint(-1.445, 2.935), pya.DPoint(-1.445, 3.105), pya.DPoint(-1.615, 3.105), pya.DPoint(-1.615, 2.935)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.695, 2.935), pya.DPoint(-0.525, 2.935), pya.DPoint(-0.525, 3.105), pya.DPoint(-0.695, 3.105), pya.DPoint(-0.695, 2.935)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.155, -0.295), pya.DPoint(-0.985, -0.295), pya.DPoint(-0.985, -0.125), pya.DPoint(-1.155, -0.125), pya.DPoint(-1.155, -0.295)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.005, -1.11), pya.DPoint(0.165, -1.11), pya.DPoint(0.165, -0.94), pya.DPoint(-0.005, -0.94), pya.DPoint(-0.005, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.335, -1.11), pya.DPoint(0.505, -1.11), pya.DPoint(0.505, -0.94), pya.DPoint(0.335, -0.94), pya.DPoint(0.335, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.295, -1.11), pya.DPoint(1.465, -1.11), pya.DPoint(1.465, -0.94), pya.DPoint(1.295, -0.94), pya.DPoint(1.295, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.635, -1.11), pya.DPoint(1.805, -1.11), pya.DPoint(1.805, -0.94), pya.DPoint(1.635, -0.94), pya.DPoint(1.635, -1.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.235, -2.03), pya.DPoint(-1.065, -2.03), pya.DPoint(-1.065, -1.86), pya.DPoint(-1.235, -1.86), pya.DPoint(-1.235, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.895, -2.03), pya.DPoint(-0.725, -2.03), pya.DPoint(-0.725, -1.86), pya.DPoint(-0.895, -1.86), pya.DPoint(-0.895, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.555, -2.03), pya.DPoint(-0.385, -2.03), pya.DPoint(-0.385, -1.86), pya.DPoint(-0.555, -1.86), pya.DPoint(-0.555, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.215, -2.03), pya.DPoint(-0.045, -2.03), pya.DPoint(-0.045, -1.86), pya.DPoint(-0.215, -1.86), pya.DPoint(-0.215, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.125, -2.03), pya.DPoint(0.295, -2.03), pya.DPoint(0.295, -1.86), pya.DPoint(0.125, -1.86), pya.DPoint(0.125, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.465, -2.03), pya.DPoint(0.635, -2.03), pya.DPoint(0.635, -1.86), pya.DPoint(0.465, -1.86), pya.DPoint(0.465, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.805, -2.03), pya.DPoint(0.975, -2.03), pya.DPoint(0.975, -1.86), pya.DPoint(0.805, -1.86), pya.DPoint(0.805, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.145, -2.03), pya.DPoint(1.315, -2.03), pya.DPoint(1.315, -1.86), pya.DPoint(1.145, -1.86), pya.DPoint(1.145, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.485, -2.03), pya.DPoint(1.655, -2.03), pya.DPoint(1.655, -1.86), pya.DPoint(1.485, -1.86), pya.DPoint(1.485, -2.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -2.49), pya.DPoint(-1.37, -2.49), pya.DPoint(-1.37, -2.32), pya.DPoint(-1.54, -2.32), pya.DPoint(-1.54, -2.49)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -2.49), pya.DPoint(1.96, -2.49), pya.DPoint(1.96, -2.32), pya.DPoint(1.79, -2.32), pya.DPoint(1.79, -2.49)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -2.83), pya.DPoint(-1.37, -2.83), pya.DPoint(-1.37, -2.66), pya.DPoint(-1.54, -2.66), pya.DPoint(-1.54, -2.83)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -2.83), pya.DPoint(1.96, -2.83), pya.DPoint(1.96, -2.66), pya.DPoint(1.79, -2.66), pya.DPoint(1.79, -2.83)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -3.17), pya.DPoint(-1.37, -3.17), pya.DPoint(-1.37, -3), pya.DPoint(-1.54, -3), pya.DPoint(-1.54, -3.17)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -3.17), pya.DPoint(1.96, -3.17), pya.DPoint(1.96, -3), pya.DPoint(1.79, -3), pya.DPoint(1.79, -3.17)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -3.51), pya.DPoint(-1.37, -3.51), pya.DPoint(-1.37, -3.34), pya.DPoint(-1.54, -3.34), pya.DPoint(-1.54, -3.51)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -3.51), pya.DPoint(1.96, -3.51), pya.DPoint(1.96, -3.34), pya.DPoint(1.79, -3.34), pya.DPoint(1.79, -3.51)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -3.85), pya.DPoint(-1.37, -3.85), pya.DPoint(-1.37, -3.68), pya.DPoint(-1.54, -3.68), pya.DPoint(-1.54, -3.85)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -3.85), pya.DPoint(1.96, -3.85), pya.DPoint(1.96, -3.68), pya.DPoint(1.79, -3.68), pya.DPoint(1.79, -3.85)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -4.19), pya.DPoint(-1.37, -4.19), pya.DPoint(-1.37, -4.02), pya.DPoint(-1.54, -4.02), pya.DPoint(-1.54, -4.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -4.19), pya.DPoint(1.96, -4.19), pya.DPoint(1.96, -4.02), pya.DPoint(1.79, -4.02), pya.DPoint(1.79, -4.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -4.53), pya.DPoint(-1.37, -4.53), pya.DPoint(-1.37, -4.36), pya.DPoint(-1.54, -4.36), pya.DPoint(-1.54, -4.53)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -4.53), pya.DPoint(1.96, -4.53), pya.DPoint(1.96, -4.36), pya.DPoint(1.79, -4.36), pya.DPoint(1.79, -4.53)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -4.87), pya.DPoint(-1.37, -4.87), pya.DPoint(-1.37, -4.7), pya.DPoint(-1.54, -4.7), pya.DPoint(-1.54, -4.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -4.87), pya.DPoint(1.96, -4.87), pya.DPoint(1.96, -4.7), pya.DPoint(1.79, -4.7), pya.DPoint(1.79, -4.87)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -5.21), pya.DPoint(-1.37, -5.21), pya.DPoint(-1.37, -5.04), pya.DPoint(-1.54, -5.04), pya.DPoint(-1.54, -5.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -5.21), pya.DPoint(1.96, -5.21), pya.DPoint(1.96, -5.04), pya.DPoint(1.79, -5.04), pya.DPoint(1.79, -5.21)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -5.55), pya.DPoint(-1.37, -5.55), pya.DPoint(-1.37, -5.38), pya.DPoint(-1.54, -5.38), pya.DPoint(-1.54, -5.55)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -5.55), pya.DPoint(1.96, -5.55), pya.DPoint(1.96, -5.38), pya.DPoint(1.79, -5.38), pya.DPoint(1.79, -5.55)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -5.89), pya.DPoint(-1.37, -5.89), pya.DPoint(-1.37, -5.72), pya.DPoint(-1.54, -5.72), pya.DPoint(-1.54, -5.89)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -5.89), pya.DPoint(1.96, -5.89), pya.DPoint(1.96, -5.72), pya.DPoint(1.79, -5.72), pya.DPoint(1.79, -5.89)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -6.23), pya.DPoint(-1.37, -6.23), pya.DPoint(-1.37, -6.06), pya.DPoint(-1.54, -6.06), pya.DPoint(-1.54, -6.23)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -6.23), pya.DPoint(1.96, -6.23), pya.DPoint(1.96, -6.06), pya.DPoint(1.79, -6.06), pya.DPoint(1.79, -6.23)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -6.57), pya.DPoint(-1.37, -6.57), pya.DPoint(-1.37, -6.4), pya.DPoint(-1.54, -6.4), pya.DPoint(-1.54, -6.57)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -6.57), pya.DPoint(1.96, -6.57), pya.DPoint(1.96, -6.4), pya.DPoint(1.79, -6.4), pya.DPoint(1.79, -6.57)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -6.91), pya.DPoint(-1.37, -6.91), pya.DPoint(-1.37, -6.74), pya.DPoint(-1.54, -6.74), pya.DPoint(-1.54, -6.91)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -6.91), pya.DPoint(1.96, -6.91), pya.DPoint(1.96, -6.74), pya.DPoint(1.79, -6.74), pya.DPoint(1.79, -6.91)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -7.25), pya.DPoint(-1.37, -7.25), pya.DPoint(-1.37, -7.08), pya.DPoint(-1.54, -7.08), pya.DPoint(-1.54, -7.25)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -7.25), pya.DPoint(1.96, -7.25), pya.DPoint(1.96, -7.08), pya.DPoint(1.79, -7.08), pya.DPoint(1.79, -7.25)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -7.59), pya.DPoint(-1.37, -7.59), pya.DPoint(-1.37, -7.42), pya.DPoint(-1.54, -7.42), pya.DPoint(-1.54, -7.59)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -7.59), pya.DPoint(1.96, -7.59), pya.DPoint(1.96, -7.42), pya.DPoint(1.79, -7.42), pya.DPoint(1.79, -7.59)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -7.93), pya.DPoint(-1.37, -7.93), pya.DPoint(-1.37, -7.76), pya.DPoint(-1.54, -7.76), pya.DPoint(-1.54, -7.93)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -7.93), pya.DPoint(1.96, -7.93), pya.DPoint(1.96, -7.76), pya.DPoint(1.79, -7.76), pya.DPoint(1.79, -7.93)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -8.27), pya.DPoint(-1.37, -8.27), pya.DPoint(-1.37, -8.1), pya.DPoint(-1.54, -8.1), pya.DPoint(-1.54, -8.27)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -8.27), pya.DPoint(1.96, -8.27), pya.DPoint(1.96, -8.1), pya.DPoint(1.79, -8.1), pya.DPoint(1.79, -8.27)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -8.61), pya.DPoint(-1.37, -8.61), pya.DPoint(-1.37, -8.44), pya.DPoint(-1.54, -8.44), pya.DPoint(-1.54, -8.61)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -8.61), pya.DPoint(1.96, -8.61), pya.DPoint(1.96, -8.44), pya.DPoint(1.79, -8.44), pya.DPoint(1.79, -8.61)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -8.95), pya.DPoint(-1.37, -8.95), pya.DPoint(-1.37, -8.78), pya.DPoint(-1.54, -8.78), pya.DPoint(-1.54, -8.95)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -8.95), pya.DPoint(1.96, -8.95), pya.DPoint(1.96, -8.78), pya.DPoint(1.79, -8.78), pya.DPoint(1.79, -8.95)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -9.29), pya.DPoint(-1.37, -9.29), pya.DPoint(-1.37, -9.12), pya.DPoint(-1.54, -9.12), pya.DPoint(-1.54, -9.29)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -9.29), pya.DPoint(1.96, -9.29), pya.DPoint(1.96, -9.12), pya.DPoint(1.79, -9.12), pya.DPoint(1.79, -9.29)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -9.63), pya.DPoint(-1.37, -9.63), pya.DPoint(-1.37, -9.46), pya.DPoint(-1.54, -9.46), pya.DPoint(-1.54, -9.63)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -9.63), pya.DPoint(1.96, -9.63), pya.DPoint(1.96, -9.46), pya.DPoint(1.79, -9.46), pya.DPoint(1.79, -9.63)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -9.97), pya.DPoint(-1.37, -9.97), pya.DPoint(-1.37, -9.8), pya.DPoint(-1.54, -9.8), pya.DPoint(-1.54, -9.97)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -9.97), pya.DPoint(1.96, -9.97), pya.DPoint(1.96, -9.8), pya.DPoint(1.79, -9.8), pya.DPoint(1.79, -9.97)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -10.31), pya.DPoint(-1.37, -10.31), pya.DPoint(-1.37, -10.14), pya.DPoint(-1.54, -10.14), pya.DPoint(-1.54, -10.31)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -10.31), pya.DPoint(1.96, -10.31), pya.DPoint(1.96, -10.14), pya.DPoint(1.79, -10.14), pya.DPoint(1.79, -10.31)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -10.65), pya.DPoint(-1.37, -10.65), pya.DPoint(-1.37, -10.48), pya.DPoint(-1.54, -10.48), pya.DPoint(-1.54, -10.65)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -10.65), pya.DPoint(1.96, -10.65), pya.DPoint(1.96, -10.48), pya.DPoint(1.79, -10.48), pya.DPoint(1.79, -10.65)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.235, -11.11), pya.DPoint(-1.065, -11.11), pya.DPoint(-1.065, -10.94), pya.DPoint(-1.235, -10.94), pya.DPoint(-1.235, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.895, -11.11), pya.DPoint(-0.725, -11.11), pya.DPoint(-0.725, -10.94), pya.DPoint(-0.895, -10.94), pya.DPoint(-0.895, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.555, -11.11), pya.DPoint(-0.385, -11.11), pya.DPoint(-0.385, -10.94), pya.DPoint(-0.555, -10.94), pya.DPoint(-0.555, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.215, -11.11), pya.DPoint(-0.045, -11.11), pya.DPoint(-0.045, -10.94), pya.DPoint(-0.215, -10.94), pya.DPoint(-0.215, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.125, -11.11), pya.DPoint(0.295, -11.11), pya.DPoint(0.295, -10.94), pya.DPoint(0.125, -10.94), pya.DPoint(0.125, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.465, -11.11), pya.DPoint(0.635, -11.11), pya.DPoint(0.635, -10.94), pya.DPoint(0.465, -10.94), pya.DPoint(0.465, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.805, -11.11), pya.DPoint(0.975, -11.11), pya.DPoint(0.975, -10.94), pya.DPoint(0.805, -10.94), pya.DPoint(0.805, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.145, -11.11), pya.DPoint(1.315, -11.11), pya.DPoint(1.315, -10.94), pya.DPoint(1.145, -10.94), pya.DPoint(1.145, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.485, -11.11), pya.DPoint(1.655, -11.11), pya.DPoint(1.655, -10.94), pya.DPoint(1.485, -10.94), pya.DPoint(1.485, -11.11)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -11.57), pya.DPoint(-1.37, -11.57), pya.DPoint(-1.37, -11.4), pya.DPoint(-1.54, -11.4), pya.DPoint(-1.54, -11.57)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -11.57), pya.DPoint(1.96, -11.57), pya.DPoint(1.96, -11.4), pya.DPoint(1.79, -11.4), pya.DPoint(1.79, -11.57)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -11.91), pya.DPoint(-1.37, -11.91), pya.DPoint(-1.37, -11.74), pya.DPoint(-1.54, -11.74), pya.DPoint(-1.54, -11.91)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -11.91), pya.DPoint(1.96, -11.91), pya.DPoint(1.96, -11.74), pya.DPoint(1.79, -11.74), pya.DPoint(1.79, -11.91)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -12.25), pya.DPoint(-1.37, -12.25), pya.DPoint(-1.37, -12.08), pya.DPoint(-1.54, -12.08), pya.DPoint(-1.54, -12.25)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -12.25), pya.DPoint(1.96, -12.25), pya.DPoint(1.96, -12.08), pya.DPoint(1.79, -12.08), pya.DPoint(1.79, -12.25)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -12.59), pya.DPoint(-1.37, -12.59), pya.DPoint(-1.37, -12.42), pya.DPoint(-1.54, -12.42), pya.DPoint(-1.54, -12.59)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -12.59), pya.DPoint(1.96, -12.59), pya.DPoint(1.96, -12.42), pya.DPoint(1.79, -12.42), pya.DPoint(1.79, -12.59)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -12.93), pya.DPoint(-1.37, -12.93), pya.DPoint(-1.37, -12.76), pya.DPoint(-1.54, -12.76), pya.DPoint(-1.54, -12.93)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -12.93), pya.DPoint(1.96, -12.93), pya.DPoint(1.96, -12.76), pya.DPoint(1.79, -12.76), pya.DPoint(1.79, -12.93)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -13.27), pya.DPoint(-1.37, -13.27), pya.DPoint(-1.37, -13.1), pya.DPoint(-1.54, -13.1), pya.DPoint(-1.54, -13.27)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -13.27), pya.DPoint(1.96, -13.27), pya.DPoint(1.96, -13.1), pya.DPoint(1.79, -13.1), pya.DPoint(1.79, -13.27)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -13.61), pya.DPoint(-1.37, -13.61), pya.DPoint(-1.37, -13.44), pya.DPoint(-1.54, -13.44), pya.DPoint(-1.54, -13.61)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -13.61), pya.DPoint(1.96, -13.61), pya.DPoint(1.96, -13.44), pya.DPoint(1.79, -13.44), pya.DPoint(1.79, -13.61)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -13.95), pya.DPoint(-1.37, -13.95), pya.DPoint(-1.37, -13.78), pya.DPoint(-1.54, -13.78), pya.DPoint(-1.54, -13.95)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -13.95), pya.DPoint(1.96, -13.95), pya.DPoint(1.96, -13.78), pya.DPoint(1.79, -13.78), pya.DPoint(1.79, -13.95)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -14.29), pya.DPoint(-1.37, -14.29), pya.DPoint(-1.37, -14.12), pya.DPoint(-1.54, -14.12), pya.DPoint(-1.54, -14.29)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -14.29), pya.DPoint(1.96, -14.29), pya.DPoint(1.96, -14.12), pya.DPoint(1.79, -14.12), pya.DPoint(1.79, -14.29)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -14.63), pya.DPoint(-1.37, -14.63), pya.DPoint(-1.37, -14.46), pya.DPoint(-1.54, -14.46), pya.DPoint(-1.54, -14.63)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -14.63), pya.DPoint(1.96, -14.63), pya.DPoint(1.96, -14.46), pya.DPoint(1.79, -14.46), pya.DPoint(1.79, -14.63)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -14.97), pya.DPoint(-1.37, -14.97), pya.DPoint(-1.37, -14.8), pya.DPoint(-1.54, -14.8), pya.DPoint(-1.54, -14.97)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -14.97), pya.DPoint(1.96, -14.97), pya.DPoint(1.96, -14.8), pya.DPoint(1.79, -14.8), pya.DPoint(1.79, -14.97)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -15.31), pya.DPoint(-1.37, -15.31), pya.DPoint(-1.37, -15.14), pya.DPoint(-1.54, -15.14), pya.DPoint(-1.54, -15.31)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -15.31), pya.DPoint(1.96, -15.31), pya.DPoint(1.96, -15.14), pya.DPoint(1.79, -15.14), pya.DPoint(1.79, -15.31)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -15.65), pya.DPoint(-1.37, -15.65), pya.DPoint(-1.37, -15.48), pya.DPoint(-1.54, -15.48), pya.DPoint(-1.54, -15.65)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -15.65), pya.DPoint(1.96, -15.65), pya.DPoint(1.96, -15.48), pya.DPoint(1.79, -15.48), pya.DPoint(1.79, -15.65)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -15.99), pya.DPoint(-1.37, -15.99), pya.DPoint(-1.37, -15.82), pya.DPoint(-1.54, -15.82), pya.DPoint(-1.54, -15.99)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -15.99), pya.DPoint(1.96, -15.99), pya.DPoint(1.96, -15.82), pya.DPoint(1.79, -15.82), pya.DPoint(1.79, -15.99)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -16.33), pya.DPoint(-1.37, -16.33), pya.DPoint(-1.37, -16.16), pya.DPoint(-1.54, -16.16), pya.DPoint(-1.54, -16.33)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -16.33), pya.DPoint(1.96, -16.33), pya.DPoint(1.96, -16.16), pya.DPoint(1.79, -16.16), pya.DPoint(1.79, -16.33)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -16.67), pya.DPoint(-1.37, -16.67), pya.DPoint(-1.37, -16.5), pya.DPoint(-1.54, -16.5), pya.DPoint(-1.54, -16.67)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -16.67), pya.DPoint(1.96, -16.67), pya.DPoint(1.96, -16.5), pya.DPoint(1.79, -16.5), pya.DPoint(1.79, -16.67)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -17.01), pya.DPoint(-1.37, -17.01), pya.DPoint(-1.37, -16.84), pya.DPoint(-1.54, -16.84), pya.DPoint(-1.54, -17.01)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -17.01), pya.DPoint(1.96, -17.01), pya.DPoint(1.96, -16.84), pya.DPoint(1.79, -16.84), pya.DPoint(1.79, -17.01)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -17.35), pya.DPoint(-1.37, -17.35), pya.DPoint(-1.37, -17.18), pya.DPoint(-1.54, -17.18), pya.DPoint(-1.54, -17.35)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -17.35), pya.DPoint(1.96, -17.35), pya.DPoint(1.96, -17.18), pya.DPoint(1.79, -17.18), pya.DPoint(1.79, -17.35)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -17.69), pya.DPoint(-1.37, -17.69), pya.DPoint(-1.37, -17.52), pya.DPoint(-1.54, -17.52), pya.DPoint(-1.54, -17.69)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -17.69), pya.DPoint(1.96, -17.69), pya.DPoint(1.96, -17.52), pya.DPoint(1.79, -17.52), pya.DPoint(1.79, -17.69)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -18.03), pya.DPoint(-1.37, -18.03), pya.DPoint(-1.37, -17.86), pya.DPoint(-1.54, -17.86), pya.DPoint(-1.54, -18.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -18.03), pya.DPoint(1.96, -18.03), pya.DPoint(1.96, -17.86), pya.DPoint(1.79, -17.86), pya.DPoint(1.79, -18.03)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -18.37), pya.DPoint(-1.37, -18.37), pya.DPoint(-1.37, -18.2), pya.DPoint(-1.54, -18.2), pya.DPoint(-1.54, -18.37)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -18.37), pya.DPoint(1.96, -18.37), pya.DPoint(1.96, -18.2), pya.DPoint(1.79, -18.2), pya.DPoint(1.79, -18.37)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -18.71), pya.DPoint(-1.37, -18.71), pya.DPoint(-1.37, -18.54), pya.DPoint(-1.54, -18.54), pya.DPoint(-1.54, -18.71)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -18.71), pya.DPoint(1.96, -18.71), pya.DPoint(1.96, -18.54), pya.DPoint(1.79, -18.54), pya.DPoint(1.79, -18.71)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -19.05), pya.DPoint(-1.37, -19.05), pya.DPoint(-1.37, -18.88), pya.DPoint(-1.54, -18.88), pya.DPoint(-1.54, -19.05)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -19.05), pya.DPoint(1.96, -19.05), pya.DPoint(1.96, -18.88), pya.DPoint(1.79, -18.88), pya.DPoint(1.79, -19.05)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -19.39), pya.DPoint(-1.37, -19.39), pya.DPoint(-1.37, -19.22), pya.DPoint(-1.54, -19.22), pya.DPoint(-1.54, -19.39)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -19.39), pya.DPoint(1.96, -19.39), pya.DPoint(1.96, -19.22), pya.DPoint(1.79, -19.22), pya.DPoint(1.79, -19.39)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -19.73), pya.DPoint(-1.37, -19.73), pya.DPoint(-1.37, -19.56), pya.DPoint(-1.54, -19.56), pya.DPoint(-1.54, -19.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -19.73), pya.DPoint(1.96, -19.73), pya.DPoint(1.96, -19.56), pya.DPoint(1.79, -19.56), pya.DPoint(1.79, -19.73)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.235, -20.19), pya.DPoint(-1.065, -20.19), pya.DPoint(-1.065, -20.02), pya.DPoint(-1.235, -20.02), pya.DPoint(-1.235, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.895, -20.19), pya.DPoint(-0.725, -20.19), pya.DPoint(-0.725, -20.02), pya.DPoint(-0.895, -20.02), pya.DPoint(-0.895, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.555, -20.19), pya.DPoint(-0.385, -20.19), pya.DPoint(-0.385, -20.02), pya.DPoint(-0.555, -20.02), pya.DPoint(-0.555, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.215, -20.19), pya.DPoint(-0.045, -20.19), pya.DPoint(-0.045, -20.02), pya.DPoint(-0.215, -20.02), pya.DPoint(-0.215, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.125, -20.19), pya.DPoint(0.295, -20.19), pya.DPoint(0.295, -20.02), pya.DPoint(0.125, -20.02), pya.DPoint(0.125, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.465, -20.19), pya.DPoint(0.635, -20.19), pya.DPoint(0.635, -20.02), pya.DPoint(0.465, -20.02), pya.DPoint(0.465, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.805, -20.19), pya.DPoint(0.975, -20.19), pya.DPoint(0.975, -20.02), pya.DPoint(0.805, -20.02), pya.DPoint(0.805, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.145, -20.19), pya.DPoint(1.315, -20.19), pya.DPoint(1.315, -20.02), pya.DPoint(1.145, -20.02), pya.DPoint(1.145, -20.19)]))
    cell.shapes(L.L_licon1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.485, -20.19), pya.DPoint(1.655, -20.19), pya.DPoint(1.655, -20.02), pya.DPoint(1.485, -20.02), pya.DPoint(1.485, -20.19)]))
    cell.shapes(L.L_npc_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.715, 2.835), pya.DPoint(-1.345, 2.835), pya.DPoint(-1.345, 3.205), pya.DPoint(-1.715, 3.205), pya.DPoint(-1.715, 2.835)]))
    cell.shapes(L.L_npc_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.795, 2.835), pya.DPoint(-0.425, 2.835), pya.DPoint(-0.425, 3.205), pya.DPoint(-0.795, 3.205), pya.DPoint(-0.795, 2.835)]))
    cell.shapes(L.L_npc_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.255, -0.395), pya.DPoint(-0.885, -0.395), pya.DPoint(-0.885, -0.025), pya.DPoint(-1.255, -0.025), pya.DPoint(-1.255, -0.395)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.38, 4.07), pya.DPoint(-2.34, 4.07), pya.DPoint(-2.34, 4.24), pya.DPoint(-3.38, 4.24), pya.DPoint(-3.38, 4.07)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.26, 4.07), pya.DPoint(2.06, 4.07), pya.DPoint(2.06, 4.24), pya.DPoint(-0.26, 4.24), pya.DPoint(-0.26, 4.07)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.66, 2.84), pya.DPoint(-1.4, 2.84), pya.DPoint(-1.4, 3.2), pya.DPoint(-1.66, 3.2), pya.DPoint(-1.66, 2.84)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.74, 2.84), pya.DPoint(-0.48, 2.84), pya.DPoint(-0.48, 3.2), pya.DPoint(-0.74, 3.2), pya.DPoint(-0.74, 2.84)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.2, -0.39), pya.DPoint(-0.94, -0.39), pya.DPoint(-0.94, -0.03), pya.DPoint(-1.2, -0.03), pya.DPoint(-1.2, -0.39)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.26, -1.11), pya.DPoint(2.06, -1.11), pya.DPoint(2.06, -0.94), pya.DPoint(-0.26, -0.94), pya.DPoint(-0.26, -1.11)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -2.03), pya.DPoint(1.96, -2.03), pya.DPoint(1.96, -1.86), pya.DPoint(-1.54, -1.86), pya.DPoint(-1.54, -2.03)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -10.94), pya.DPoint(-1.37, -10.94), pya.DPoint(-1.37, -2.03), pya.DPoint(-1.54, -2.03), pya.DPoint(-1.54, -10.94)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.02, -10.67), pya.DPoint(1.44, -10.67), pya.DPoint(1.44, -2.63), pya.DPoint(-1.02, -2.63), pya.DPoint(-1.02, -10.67)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -10.94), pya.DPoint(1.96, -10.94), pya.DPoint(1.96, -2.03), pya.DPoint(1.79, -2.03), pya.DPoint(1.79, -10.94)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -11.11), pya.DPoint(1.96, -11.11), pya.DPoint(1.96, -10.94), pya.DPoint(-1.54, -10.94), pya.DPoint(-1.54, -11.11)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -20.02), pya.DPoint(-1.37, -20.02), pya.DPoint(-1.37, -11.11), pya.DPoint(-1.54, -11.11), pya.DPoint(-1.54, -20.02)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.03, -19.75), pya.DPoint(1.43, -19.75), pya.DPoint(1.43, -11.71), pya.DPoint(-1.03, -11.71), pya.DPoint(-1.03, -19.75)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.79, -20.02), pya.DPoint(1.96, -20.02), pya.DPoint(1.96, -11.11), pya.DPoint(1.79, -11.11), pya.DPoint(1.79, -20.02)]))
    cell.shapes(L.L_li1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.54, -20.19), pya.DPoint(1.96, -20.19), pya.DPoint(1.96, -20.02), pya.DPoint(-1.54, -20.02), pya.DPoint(-1.54, -20.19)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.125, 4.07), pya.DPoint(-2.955, 4.07), pya.DPoint(-2.955, 4.24), pya.DPoint(-3.125, 4.24), pya.DPoint(-3.125, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.765, 4.07), pya.DPoint(-2.595, 4.07), pya.DPoint(-2.595, 4.24), pya.DPoint(-2.765, 4.24), pya.DPoint(-2.765, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.005, 4.07), pya.DPoint(0.165, 4.07), pya.DPoint(0.165, 4.24), pya.DPoint(-0.005, 4.24), pya.DPoint(-0.005, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.355, 4.07), pya.DPoint(0.525, 4.07), pya.DPoint(0.525, 4.24), pya.DPoint(0.355, 4.24), pya.DPoint(0.355, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.275, 4.07), pya.DPoint(1.445, 4.07), pya.DPoint(1.445, 4.24), pya.DPoint(1.275, 4.24), pya.DPoint(1.275, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.635, 4.07), pya.DPoint(1.805, 4.07), pya.DPoint(1.805, 4.24), pya.DPoint(1.635, 4.24), pya.DPoint(1.635, 4.07)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.615, 2.935), pya.DPoint(-1.445, 2.935), pya.DPoint(-1.445, 3.105), pya.DPoint(-1.615, 3.105), pya.DPoint(-1.615, 2.935)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.695, 2.935), pya.DPoint(-0.525, 2.935), pya.DPoint(-0.525, 3.105), pya.DPoint(-0.695, 3.105), pya.DPoint(-0.695, 2.935)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.155, -0.295), pya.DPoint(-0.985, -0.295), pya.DPoint(-0.985, -0.125), pya.DPoint(-1.155, -0.125), pya.DPoint(-1.155, -0.295)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.015, -1.11), pya.DPoint(0.155, -1.11), pya.DPoint(0.155, -0.94), pya.DPoint(-0.015, -0.94), pya.DPoint(-0.015, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.345, -1.11), pya.DPoint(0.515, -1.11), pya.DPoint(0.515, -0.94), pya.DPoint(0.345, -0.94), pya.DPoint(0.345, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.285, -1.11), pya.DPoint(1.455, -1.11), pya.DPoint(1.455, -0.94), pya.DPoint(1.285, -0.94), pya.DPoint(1.285, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(1.645, -1.11), pya.DPoint(1.815, -1.11), pya.DPoint(1.815, -0.94), pya.DPoint(1.645, -0.94), pya.DPoint(1.645, -1.11)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.005, -2.03), pya.DPoint(0.165, -2.03), pya.DPoint(0.165, -1.86), pya.DPoint(-0.005, -1.86), pya.DPoint(-0.005, -2.03)]))
    cell.shapes(L.L_mcon_drawing).insert(
        pya.DPolygon([pya.DPoint(0.355, -2.03), pya.DPoint(0.525, -2.03), pya.DPoint(0.525, -1.86), pya.DPoint(0.355, -1.86), pya.DPoint(0.355, -2.03)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.36, 3.2), pya.DPoint(-2.36, 3.2), pya.DPoint(-2.36, 4.28), pya.DPoint(-3.36, 4.28), pya.DPoint(-3.36, 3.2)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.68, 2.21), pya.DPoint(-2.36, 2.21), pya.DPoint(-2.36, 2.84), pya.DPoint(-2.68, 2.84), pya.DPoint(-2.68, 2.21)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.15, -11.73), pya.DPoint(-1.83, -11.73), pya.DPoint(-1.83, 4.14), pya.DPoint(-2.15, 4.14), pya.DPoint(-2.15, -11.73)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.24, 4.03), pya.DPoint(2.04, 4.03), pya.DPoint(2.04, 4.28), pya.DPoint(-0.24, 4.28), pya.DPoint(-0.24, 4.03)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.24, 3.2), pya.DPoint(0.76, 3.2), pya.DPoint(0.76, 4.03), pya.DPoint(-0.24, 4.03), pya.DPoint(-0.24, 3.2)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.04, 3.2), pya.DPoint(2.04, 3.2), pya.DPoint(2.04, 4.03), pya.DPoint(1.04, 4.03), pya.DPoint(1.04, 3.2)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.69, -11.34), pya.DPoint(-1.37, -11.34), pya.DPoint(-1.37, 3.18), pya.DPoint(-1.69, 3.18), pya.DPoint(-1.69, -11.34)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -2.65), pya.DPoint(-0.91, -2.65), pya.DPoint(-0.91, 0.87), pya.DPoint(-1.23, 0.87), pya.DPoint(-1.23, -2.65)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.77, -2.49), pya.DPoint(-0.45, -2.49), pya.DPoint(-0.45, 3.18), pya.DPoint(-0.77, 3.18), pya.DPoint(-0.77, -2.49)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(0.46, 0), pya.DPoint(0.76, 0), pya.DPoint(0.76, 2.81), pya.DPoint(0.46, 2.81), pya.DPoint(0.46, 0)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.74, 0), pya.DPoint(2.04, 0), pya.DPoint(2.04, 2.81), pya.DPoint(1.74, 2.81), pya.DPoint(1.74, 0)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.24, -2.06), pya.DPoint(0.76, -2.06), pya.DPoint(0.76, -0.39), pya.DPoint(-0.24, -0.39), pya.DPoint(-0.24, -2.06)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(1.04, -1.42), pya.DPoint(2.04, -1.42), pya.DPoint(2.04, -0.39), pya.DPoint(1.04, -0.39), pya.DPoint(1.04, -1.42)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -2.88), pya.DPoint(1.47, -2.88), pya.DPoint(1.47, -2.65), pya.DPoint(-1.23, -2.65), pya.DPoint(-1.23, -2.88)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -10.42), pya.DPoint(-0.91, -10.42), pya.DPoint(-0.91, -2.88), pya.DPoint(-1.23, -2.88), pya.DPoint(-1.23, -10.42)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -10.65), pya.DPoint(1.47, -10.65), pya.DPoint(1.47, -10.42), pya.DPoint(-1.23, -10.42), pya.DPoint(-1.23, -10.65)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.69, -11.57), pya.DPoint(1.19, -11.57), pya.DPoint(1.19, -11.34), pya.DPoint(-1.69, -11.34), pya.DPoint(-1.69, -11.57)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.15, -11.96), pya.DPoint(1.47, -11.96), pya.DPoint(1.47, -11.73), pya.DPoint(-2.15, -11.73), pya.DPoint(-2.15, -11.96)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -19.5), pya.DPoint(-0.91, -19.5), pya.DPoint(-0.91, -11.96), pya.DPoint(-1.23, -11.96), pya.DPoint(-1.23, -19.5)]))
    cell.shapes(L.L_met1_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, -19.73), pya.DPoint(1.47, -19.73), pya.DPoint(1.47, -19.5), pya.DPoint(-1.23, -19.5), pya.DPoint(-1.23, -19.73)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.255, 3.925), pya.DPoint(-3.105, 3.925), pya.DPoint(-3.105, 4.075), pya.DPoint(-3.255, 4.075), pya.DPoint(-3.255, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.935, 3.925), pya.DPoint(-2.785, 3.925), pya.DPoint(-2.785, 4.075), pya.DPoint(-2.935, 4.075), pya.DPoint(-2.935, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.615, 3.925), pya.DPoint(-2.465, 3.925), pya.DPoint(-2.465, 4.075), pya.DPoint(-2.615, 4.075), pya.DPoint(-2.615, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.065, 3.925), pya.DPoint(-1.915, 3.925), pya.DPoint(-1.915, 4.075), pya.DPoint(-2.065, 4.075), pya.DPoint(-2.065, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.135, 3.925), pya.DPoint(0.015, 3.925), pya.DPoint(0.015, 4.075), pya.DPoint(-0.135, 4.075), pya.DPoint(-0.135, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.185, 3.925), pya.DPoint(0.335, 3.925), pya.DPoint(0.335, 4.075), pya.DPoint(0.185, 4.075), pya.DPoint(0.185, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.505, 3.925), pya.DPoint(0.655, 3.925), pya.DPoint(0.655, 4.075), pya.DPoint(0.505, 4.075), pya.DPoint(0.505, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.145, 3.925), pya.DPoint(1.295, 3.925), pya.DPoint(1.295, 4.075), pya.DPoint(1.145, 4.075), pya.DPoint(1.145, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.465, 3.925), pya.DPoint(1.615, 3.925), pya.DPoint(1.615, 4.075), pya.DPoint(1.465, 4.075), pya.DPoint(1.465, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.785, 3.925), pya.DPoint(1.935, 3.925), pya.DPoint(1.935, 4.075), pya.DPoint(1.785, 4.075), pya.DPoint(1.785, 3.925)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.595, 2.265), pya.DPoint(-2.445, 2.265), pya.DPoint(-2.445, 2.415), pya.DPoint(-2.595, 2.415), pya.DPoint(-2.595, 2.265)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.685, 2.265), pya.DPoint(-0.535, 2.265), pya.DPoint(-0.535, 2.415), pya.DPoint(-0.685, 2.415), pya.DPoint(-0.685, 2.265)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.605, 1.865), pya.DPoint(-1.455, 1.865), pya.DPoint(-1.455, 2.015), pya.DPoint(-1.605, 2.015), pya.DPoint(-1.605, 1.865)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.815, 1.465), pya.DPoint(1.965, 1.465), pya.DPoint(1.965, 1.615), pya.DPoint(1.815, 1.615), pya.DPoint(1.815, 1.465)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.535, 1.065), pya.DPoint(0.685, 1.065), pya.DPoint(0.685, 1.215), pya.DPoint(0.535, 1.215), pya.DPoint(0.535, 1.065)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.145, 0.665), pya.DPoint(-0.995, 0.665), pya.DPoint(-0.995, 0.815), pya.DPoint(-1.145, 0.815), pya.DPoint(-1.145, 0.665)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(-0.135, -1.365), pya.DPoint(0.015, -1.365), pya.DPoint(0.015, -1.215), pya.DPoint(-0.135, -1.215), pya.DPoint(-0.135, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.185, -1.365), pya.DPoint(0.335, -1.365), pya.DPoint(0.335, -1.215), pya.DPoint(0.185, -1.215), pya.DPoint(0.185, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(0.505, -1.365), pya.DPoint(0.655, -1.365), pya.DPoint(0.655, -1.215), pya.DPoint(0.505, -1.215), pya.DPoint(0.505, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.145, -1.365), pya.DPoint(1.295, -1.365), pya.DPoint(1.295, -1.215), pya.DPoint(1.145, -1.215), pya.DPoint(1.145, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.465, -1.365), pya.DPoint(1.615, -1.365), pya.DPoint(1.615, -1.215), pya.DPoint(1.465, -1.215), pya.DPoint(1.465, -1.365)]))
    cell.shapes(L.L_via_drawing).insert(
        pya.DPolygon([pya.DPoint(1.785, -1.365), pya.DPoint(1.935, -1.365), pya.DPoint(1.935, -1.215), pya.DPoint(1.785, -1.215), pya.DPoint(1.785, -1.365)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, 3.87), pya.DPoint(2.35, 3.87), pya.DPoint(2.35, 4.13), pya.DPoint(-3.67, 4.13), pya.DPoint(-3.67, 3.87)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-2.68, 2.21), pya.DPoint(-0.45, 2.21), pya.DPoint(-0.45, 2.47), pya.DPoint(-2.68, 2.47), pya.DPoint(-2.68, 2.21)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.81), pya.DPoint(2.35, 1.81), pya.DPoint(2.35, 2.07), pya.DPoint(-3.67, 2.07), pya.DPoint(-3.67, 1.81)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.41), pya.DPoint(2.35, 1.41), pya.DPoint(2.35, 1.67), pya.DPoint(-3.67, 1.67), pya.DPoint(-3.67, 1.41)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.01), pya.DPoint(2.35, 1.01), pya.DPoint(2.35, 1.27), pya.DPoint(-3.67, 1.27), pya.DPoint(-3.67, 1.01)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-1.23, 0.61), pya.DPoint(2.35, 0.61), pya.DPoint(2.35, 0.87), pya.DPoint(-1.23, 0.87), pya.DPoint(-1.23, 0.61)]))
    cell.shapes(L.L_met2_drawing).insert(
        pya.DPolygon([pya.DPoint(-3.67, -1.42), pya.DPoint(2.35, -1.42), pya.DPoint(2.35, -1.16), pya.DPoint(-3.67, -1.16), pya.DPoint(-3.67, -1.42)]))
    _txt = pya.Text("vss",
                   pya.Trans(0, False, pya.Vector(-3535, -1290)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-3.67, -1.42), pya.DPoint(-3.4, -1.42), pya.DPoint(-3.4, -1.16), pya.DPoint(-3.67, -1.16), pya.DPoint(-3.67, -1.42)]))
    _txt = pya.Text("vdd",
                   pya.Trans(0, False, pya.Vector(-3535, 4000)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-3.67, 3.87), pya.DPoint(-3.4, 3.87), pya.DPoint(-3.4, 4.13), pya.DPoint(-3.67, 4.13), pya.DPoint(-3.67, 3.87)]))
    _txt = pya.Text("vbp",
                   pya.Trans(0, False, pya.Vector(-3535, 1940)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.81), pya.DPoint(-3.4, 1.81), pya.DPoint(-3.4, 2.07), pya.DPoint(-3.67, 2.07), pya.DPoint(-3.67, 1.81)]))
    _txt = pya.Text("vbn",
                   pya.Trans(0, False, pya.Vector(-3535, 1540)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.41), pya.DPoint(-3.4, 1.41), pya.DPoint(-3.4, 1.67), pya.DPoint(-3.67, 1.67), pya.DPoint(-3.67, 1.41)]))
    _txt = pya.Text("vbr",
                   pya.Trans(0, False, pya.Vector(-3535, 1140)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(-3.67, 1.01), pya.DPoint(-3.4, 1.01), pya.DPoint(-3.4, 1.27), pya.DPoint(-3.67, 1.27), pya.DPoint(-3.67, 1.01)]))
    _txt = pya.Text("disable",
                   pya.Trans(0, False, pya.Vector(2215, 740)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met2_pin).insert(_txt)
    cell.shapes(L.L_met2_label).insert(
        pya.DPolygon([pya.DPoint(2.08, 0.61), pya.DPoint(2.35, 0.61), pya.DPoint(2.35, 0.87), pya.DPoint(2.08, 0.87), pya.DPoint(2.08, 0.61)]))


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
    build(layout, L, cells)
    out = "ToBiasStartup.gds"
    layout.write(out)
    print("Written:", out)
