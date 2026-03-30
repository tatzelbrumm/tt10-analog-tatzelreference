"""Cell: tt_um_tatzelreference
Standalone : run in KLayout (Macros -> Run Script) to view just this cell.
Importable : main_ihp.py imports build() to assemble the full hierarchy.
"""
import pya
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layers import register_layers
from tatzelreference_tile import build as _build_tatzelreference_tile

def build(layout, L, cells):
    """Populate "tt_um_tatzelreference". cells must contain: tt_um_tatzelreference, tatzelreference_tile."""
    cell = cells["tt_um_tatzelreference"]
    cell.insert(pya.DCellInstArray(
        cells["tatzelreference_tile"].cell_index(),
        pya.DCplxTrans(1, 0, False,
                      pya.DVector(0, 0))))
    cell.shapes(L.L_235_4).insert(
        pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(15.03, 224.76), pya.DPoint(15.33, 224.76), pya.DPoint(15.33, 225.76), pya.DPoint(15.03, 225.76), pya.DPoint(15.03, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(17.79, 224.76), pya.DPoint(18.09, 224.76), pya.DPoint(18.09, 225.76), pya.DPoint(17.79, 225.76), pya.DPoint(17.79, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(20.55, 224.76), pya.DPoint(20.85, 224.76), pya.DPoint(20.85, 225.76), pya.DPoint(20.55, 225.76), pya.DPoint(20.55, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(23.31, 224.76), pya.DPoint(23.61, 224.76), pya.DPoint(23.61, 225.76), pya.DPoint(23.31, 225.76), pya.DPoint(23.31, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(26.07, 224.76), pya.DPoint(26.37, 224.76), pya.DPoint(26.37, 225.76), pya.DPoint(26.07, 225.76), pya.DPoint(26.07, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(28.83, 224.76), pya.DPoint(29.13, 224.76), pya.DPoint(29.13, 225.76), pya.DPoint(28.83, 225.76), pya.DPoint(28.83, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(31.59, 224.76), pya.DPoint(31.89, 224.76), pya.DPoint(31.89, 225.76), pya.DPoint(31.59, 225.76), pya.DPoint(31.59, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(34.35, 224.76), pya.DPoint(34.65, 224.76), pya.DPoint(34.65, 225.76), pya.DPoint(34.35, 225.76), pya.DPoint(34.35, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(37.11, 224.76), pya.DPoint(37.41, 224.76), pya.DPoint(37.41, 225.76), pya.DPoint(37.11, 225.76), pya.DPoint(37.11, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(39.87, 224.76), pya.DPoint(40.17, 224.76), pya.DPoint(40.17, 225.76), pya.DPoint(39.87, 225.76), pya.DPoint(39.87, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(42.63, 224.76), pya.DPoint(42.93, 224.76), pya.DPoint(42.93, 225.76), pya.DPoint(42.63, 225.76), pya.DPoint(42.63, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(45.39, 224.76), pya.DPoint(45.69, 224.76), pya.DPoint(45.69, 225.76), pya.DPoint(45.39, 225.76), pya.DPoint(45.39, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(48.15, 224.76), pya.DPoint(48.45, 224.76), pya.DPoint(48.45, 225.76), pya.DPoint(48.15, 225.76), pya.DPoint(48.15, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(50.91, 224.76), pya.DPoint(51.21, 224.76), pya.DPoint(51.21, 225.76), pya.DPoint(50.91, 225.76), pya.DPoint(50.91, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(53.67, 224.76), pya.DPoint(53.97, 224.76), pya.DPoint(53.97, 225.76), pya.DPoint(53.67, 225.76), pya.DPoint(53.67, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(56.43, 224.76), pya.DPoint(56.73, 224.76), pya.DPoint(56.73, 225.76), pya.DPoint(56.43, 225.76), pya.DPoint(56.43, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(59.19, 224.76), pya.DPoint(59.49, 224.76), pya.DPoint(59.49, 225.76), pya.DPoint(59.19, 225.76), pya.DPoint(59.19, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(61.95, 224.76), pya.DPoint(62.25, 224.76), pya.DPoint(62.25, 225.76), pya.DPoint(61.95, 225.76), pya.DPoint(61.95, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(64.71, 224.76), pya.DPoint(65.01, 224.76), pya.DPoint(65.01, 225.76), pya.DPoint(64.71, 225.76), pya.DPoint(64.71, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(67.47, 224.76), pya.DPoint(67.77, 224.76), pya.DPoint(67.77, 225.76), pya.DPoint(67.47, 225.76), pya.DPoint(67.47, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(70.23, 224.76), pya.DPoint(70.53, 224.76), pya.DPoint(70.53, 225.76), pya.DPoint(70.23, 225.76), pya.DPoint(70.23, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(72.99, 224.76), pya.DPoint(73.29, 224.76), pya.DPoint(73.29, 225.76), pya.DPoint(72.99, 225.76), pya.DPoint(72.99, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(75.75, 224.76), pya.DPoint(76.05, 224.76), pya.DPoint(76.05, 225.76), pya.DPoint(75.75, 225.76), pya.DPoint(75.75, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(78.51, 224.76), pya.DPoint(78.81, 224.76), pya.DPoint(78.81, 225.76), pya.DPoint(78.51, 225.76), pya.DPoint(78.51, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(81.27, 224.76), pya.DPoint(81.57, 224.76), pya.DPoint(81.57, 225.76), pya.DPoint(81.27, 225.76), pya.DPoint(81.27, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(84.03, 224.76), pya.DPoint(84.33, 224.76), pya.DPoint(84.33, 225.76), pya.DPoint(84.03, 225.76), pya.DPoint(84.03, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(86.79, 224.76), pya.DPoint(87.09, 224.76), pya.DPoint(87.09, 225.76), pya.DPoint(86.79, 225.76), pya.DPoint(86.79, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(89.55, 224.76), pya.DPoint(89.85, 224.76), pya.DPoint(89.85, 225.76), pya.DPoint(89.55, 225.76), pya.DPoint(89.55, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(92.31, 224.76), pya.DPoint(92.61, 224.76), pya.DPoint(92.61, 225.76), pya.DPoint(92.31, 225.76), pya.DPoint(92.31, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(95.07, 224.76), pya.DPoint(95.37, 224.76), pya.DPoint(95.37, 225.76), pya.DPoint(95.07, 225.76), pya.DPoint(95.07, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(97.83, 224.76), pya.DPoint(98.13, 224.76), pya.DPoint(98.13, 225.76), pya.DPoint(97.83, 225.76), pya.DPoint(97.83, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(100.59, 224.76), pya.DPoint(100.89, 224.76), pya.DPoint(100.89, 225.76), pya.DPoint(100.59, 225.76), pya.DPoint(100.59, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(103.35, 224.76), pya.DPoint(103.65, 224.76), pya.DPoint(103.65, 225.76), pya.DPoint(103.35, 225.76), pya.DPoint(103.35, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(106.11, 224.76), pya.DPoint(106.41, 224.76), pya.DPoint(106.41, 225.76), pya.DPoint(106.11, 225.76), pya.DPoint(106.11, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(108.87, 224.76), pya.DPoint(109.17, 224.76), pya.DPoint(109.17, 225.76), pya.DPoint(108.87, 225.76), pya.DPoint(108.87, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(111.63, 224.76), pya.DPoint(111.93, 224.76), pya.DPoint(111.93, 225.76), pya.DPoint(111.63, 225.76), pya.DPoint(111.63, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(114.39, 224.76), pya.DPoint(114.69, 224.76), pya.DPoint(114.69, 225.76), pya.DPoint(114.39, 225.76), pya.DPoint(114.39, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(117.15, 224.76), pya.DPoint(117.45, 224.76), pya.DPoint(117.45, 225.76), pya.DPoint(117.15, 225.76), pya.DPoint(117.15, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(119.91, 224.76), pya.DPoint(120.21, 224.76), pya.DPoint(120.21, 225.76), pya.DPoint(119.91, 225.76), pya.DPoint(119.91, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(122.67, 224.76), pya.DPoint(122.97, 224.76), pya.DPoint(122.97, 225.76), pya.DPoint(122.67, 225.76), pya.DPoint(122.67, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(125.43, 224.76), pya.DPoint(125.73, 224.76), pya.DPoint(125.73, 225.76), pya.DPoint(125.43, 225.76), pya.DPoint(125.43, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(128.19, 224.76), pya.DPoint(128.49, 224.76), pya.DPoint(128.49, 225.76), pya.DPoint(128.19, 225.76), pya.DPoint(128.19, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(130.95, 224.76), pya.DPoint(131.25, 224.76), pya.DPoint(131.25, 225.76), pya.DPoint(130.95, 225.76), pya.DPoint(130.95, 224.76)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(1, 5), pya.DPoint(3, 5), pya.DPoint(3, 220.76), pya.DPoint(1, 220.76), pya.DPoint(1, 5)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(4, 5), pya.DPoint(6, 5), pya.DPoint(6, 220.76), pya.DPoint(4, 220.76), pya.DPoint(4, 5)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(7, 5), pya.DPoint(9, 5), pya.DPoint(9, 220.76), pya.DPoint(7, 220.76), pya.DPoint(7, 5)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(0.93, 0), pya.DPoint(1.83, 0), pya.DPoint(1.83, 1), pya.DPoint(0.93, 1), pya.DPoint(0.93, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(20.25, 0), pya.DPoint(21.15, 0), pya.DPoint(21.15, 1), pya.DPoint(20.25, 1), pya.DPoint(20.25, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 1), pya.DPoint(39.57, 1), pya.DPoint(39.57, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 1), pya.DPoint(58.89, 1), pya.DPoint(58.89, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 1), pya.DPoint(78.21, 1), pya.DPoint(78.21, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 1), pya.DPoint(97.53, 1), pya.DPoint(97.53, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 1), pya.DPoint(116.85, 1), pya.DPoint(116.85, 0)]))
    cell.shapes(L.L_met4_drawing).insert(
        pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 1), pya.DPoint(136.17, 1), pya.DPoint(136.17, 0)]))
    _txt = pya.Text("clk",
                   pya.Trans(1, False, pya.Vector(128340, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(128.19, 224.76), pya.DPoint(128.49, 224.76), pya.DPoint(128.49, 225.76), pya.DPoint(128.19, 225.76), pya.DPoint(128.19, 224.76)]))
    _txt = pya.Text("ena",
                   pya.Trans(1, False, pya.Vector(131100, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(130.95, 224.76), pya.DPoint(131.25, 224.76), pya.DPoint(131.25, 225.76), pya.DPoint(130.95, 225.76), pya.DPoint(130.95, 224.76)]))
    _txt = pya.Text("rst_n",
                   pya.Trans(1, False, pya.Vector(125580, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(125.43, 224.76), pya.DPoint(125.73, 224.76), pya.DPoint(125.73, 225.76), pya.DPoint(125.43, 225.76), pya.DPoint(125.43, 224.76)]))
    _txt = pya.Text("ua[0]",
                   pya.Trans(0, False, pya.Vector(136620, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 1), pya.DPoint(136.17, 1), pya.DPoint(136.17, 0)]))
    _txt = pya.Text("ua[1]",
                   pya.Trans(0, False, pya.Vector(117300, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 1), pya.DPoint(116.85, 1), pya.DPoint(116.85, 0)]))
    _txt = pya.Text("ua[2]",
                   pya.Trans(0, False, pya.Vector(97980, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 1), pya.DPoint(97.53, 1), pya.DPoint(97.53, 0)]))
    _txt = pya.Text("ua[3]",
                   pya.Trans(0, False, pya.Vector(78660, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 1), pya.DPoint(78.21, 1), pya.DPoint(78.21, 0)]))
    _txt = pya.Text("ua[4]",
                   pya.Trans(0, False, pya.Vector(59340, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 1), pya.DPoint(58.89, 1), pya.DPoint(58.89, 0)]))
    _txt = pya.Text("ua[5]",
                   pya.Trans(0, False, pya.Vector(40020, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 1), pya.DPoint(39.57, 1), pya.DPoint(39.57, 0)]))
    _txt = pya.Text("ua[6]",
                   pya.Trans(0, False, pya.Vector(20700, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(20.25, 0), pya.DPoint(21.15, 0), pya.DPoint(21.15, 1), pya.DPoint(20.25, 1), pya.DPoint(20.25, 0)]))
    _txt = pya.Text("ua[7]",
                   pya.Trans(0, False, pya.Vector(1380, 500)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(0.93, 0), pya.DPoint(1.83, 0), pya.DPoint(1.83, 1), pya.DPoint(0.93, 1), pya.DPoint(0.93, 0)]))
    _txt = pya.Text("ui_in[0]",
                   pya.Trans(1, False, pya.Vector(122820, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(122.67, 224.76), pya.DPoint(122.97, 224.76), pya.DPoint(122.97, 225.76), pya.DPoint(122.67, 225.76), pya.DPoint(122.67, 224.76)]))
    _txt = pya.Text("ui_in[1]",
                   pya.Trans(1, False, pya.Vector(120060, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(119.91, 224.76), pya.DPoint(120.21, 224.76), pya.DPoint(120.21, 225.76), pya.DPoint(119.91, 225.76), pya.DPoint(119.91, 224.76)]))
    _txt = pya.Text("ui_in[2]",
                   pya.Trans(1, False, pya.Vector(117300, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(117.15, 224.76), pya.DPoint(117.45, 224.76), pya.DPoint(117.45, 225.76), pya.DPoint(117.15, 225.76), pya.DPoint(117.15, 224.76)]))
    _txt = pya.Text("ui_in[3]",
                   pya.Trans(1, False, pya.Vector(114540, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(114.39, 224.76), pya.DPoint(114.69, 224.76), pya.DPoint(114.69, 225.76), pya.DPoint(114.39, 225.76), pya.DPoint(114.39, 224.76)]))
    _txt = pya.Text("ui_in[4]",
                   pya.Trans(1, False, pya.Vector(111780, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(111.63, 224.76), pya.DPoint(111.93, 224.76), pya.DPoint(111.93, 225.76), pya.DPoint(111.63, 225.76), pya.DPoint(111.63, 224.76)]))
    _txt = pya.Text("ui_in[5]",
                   pya.Trans(1, False, pya.Vector(109020, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(108.87, 224.76), pya.DPoint(109.17, 224.76), pya.DPoint(109.17, 225.76), pya.DPoint(108.87, 225.76), pya.DPoint(108.87, 224.76)]))
    _txt = pya.Text("ui_in[6]",
                   pya.Trans(1, False, pya.Vector(106260, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(106.11, 224.76), pya.DPoint(106.41, 224.76), pya.DPoint(106.41, 225.76), pya.DPoint(106.11, 225.76), pya.DPoint(106.11, 224.76)]))
    _txt = pya.Text("ui_in[7]",
                   pya.Trans(1, False, pya.Vector(103500, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(103.35, 224.76), pya.DPoint(103.65, 224.76), pya.DPoint(103.65, 225.76), pya.DPoint(103.35, 225.76), pya.DPoint(103.35, 224.76)]))
    _txt = pya.Text("uio_in[0]",
                   pya.Trans(1, False, pya.Vector(100740, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(100.59, 224.76), pya.DPoint(100.89, 224.76), pya.DPoint(100.89, 225.76), pya.DPoint(100.59, 225.76), pya.DPoint(100.59, 224.76)]))
    _txt = pya.Text("uio_in[1]",
                   pya.Trans(1, False, pya.Vector(97980, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(97.83, 224.76), pya.DPoint(98.13, 224.76), pya.DPoint(98.13, 225.76), pya.DPoint(97.83, 225.76), pya.DPoint(97.83, 224.76)]))
    _txt = pya.Text("uio_in[2]",
                   pya.Trans(1, False, pya.Vector(95220, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(95.07, 224.76), pya.DPoint(95.37, 224.76), pya.DPoint(95.37, 225.76), pya.DPoint(95.07, 225.76), pya.DPoint(95.07, 224.76)]))
    _txt = pya.Text("uio_in[3]",
                   pya.Trans(1, False, pya.Vector(92460, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(92.31, 224.76), pya.DPoint(92.61, 224.76), pya.DPoint(92.61, 225.76), pya.DPoint(92.31, 225.76), pya.DPoint(92.31, 224.76)]))
    _txt = pya.Text("uio_in[4]",
                   pya.Trans(1, False, pya.Vector(89700, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(89.55, 224.76), pya.DPoint(89.85, 224.76), pya.DPoint(89.85, 225.76), pya.DPoint(89.55, 225.76), pya.DPoint(89.55, 224.76)]))
    _txt = pya.Text("uio_in[5]",
                   pya.Trans(1, False, pya.Vector(86940, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(86.79, 224.76), pya.DPoint(87.09, 224.76), pya.DPoint(87.09, 225.76), pya.DPoint(86.79, 225.76), pya.DPoint(86.79, 224.76)]))
    _txt = pya.Text("uio_in[6]",
                   pya.Trans(1, False, pya.Vector(84180, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(84.03, 224.76), pya.DPoint(84.33, 224.76), pya.DPoint(84.33, 225.76), pya.DPoint(84.03, 225.76), pya.DPoint(84.03, 224.76)]))
    _txt = pya.Text("uio_in[7]",
                   pya.Trans(1, False, pya.Vector(81420, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(81.27, 224.76), pya.DPoint(81.57, 224.76), pya.DPoint(81.57, 225.76), pya.DPoint(81.27, 225.76), pya.DPoint(81.27, 224.76)]))
    _txt = pya.Text("uio_oe[0]",
                   pya.Trans(1, False, pya.Vector(34500, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(34.35, 224.76), pya.DPoint(34.65, 224.76), pya.DPoint(34.65, 225.76), pya.DPoint(34.35, 225.76), pya.DPoint(34.35, 224.76)]))
    _txt = pya.Text("uio_oe[1]",
                   pya.Trans(1, False, pya.Vector(31740, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(31.59, 224.76), pya.DPoint(31.89, 224.76), pya.DPoint(31.89, 225.76), pya.DPoint(31.59, 225.76), pya.DPoint(31.59, 224.76)]))
    _txt = pya.Text("uio_oe[2]",
                   pya.Trans(1, False, pya.Vector(28980, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(28.83, 224.76), pya.DPoint(29.13, 224.76), pya.DPoint(29.13, 225.76), pya.DPoint(28.83, 225.76), pya.DPoint(28.83, 224.76)]))
    _txt = pya.Text("uio_oe[3]",
                   pya.Trans(1, False, pya.Vector(26220, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(26.07, 224.76), pya.DPoint(26.37, 224.76), pya.DPoint(26.37, 225.76), pya.DPoint(26.07, 225.76), pya.DPoint(26.07, 224.76)]))
    _txt = pya.Text("uio_oe[4]",
                   pya.Trans(1, False, pya.Vector(23460, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(23.31, 224.76), pya.DPoint(23.61, 224.76), pya.DPoint(23.61, 225.76), pya.DPoint(23.31, 225.76), pya.DPoint(23.31, 224.76)]))
    _txt = pya.Text("uio_oe[5]",
                   pya.Trans(1, False, pya.Vector(20700, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(20.55, 224.76), pya.DPoint(20.85, 224.76), pya.DPoint(20.85, 225.76), pya.DPoint(20.55, 225.76), pya.DPoint(20.55, 224.76)]))
    _txt = pya.Text("uio_oe[6]",
                   pya.Trans(1, False, pya.Vector(17940, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(17.79, 224.76), pya.DPoint(18.09, 224.76), pya.DPoint(18.09, 225.76), pya.DPoint(17.79, 225.76), pya.DPoint(17.79, 224.76)]))
    _txt = pya.Text("uio_oe[7]",
                   pya.Trans(1, False, pya.Vector(15180, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(15.03, 224.76), pya.DPoint(15.33, 224.76), pya.DPoint(15.33, 225.76), pya.DPoint(15.03, 225.76), pya.DPoint(15.03, 224.76)]))
    _txt = pya.Text("uio_out[0]",
                   pya.Trans(1, False, pya.Vector(56580, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(56.43, 224.76), pya.DPoint(56.73, 224.76), pya.DPoint(56.73, 225.76), pya.DPoint(56.43, 225.76), pya.DPoint(56.43, 224.76)]))
    _txt = pya.Text("uio_out[1]",
                   pya.Trans(1, False, pya.Vector(53820, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(53.67, 224.76), pya.DPoint(53.97, 224.76), pya.DPoint(53.97, 225.76), pya.DPoint(53.67, 225.76), pya.DPoint(53.67, 224.76)]))
    _txt = pya.Text("uio_out[2]",
                   pya.Trans(1, False, pya.Vector(51060, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(50.91, 224.76), pya.DPoint(51.21, 224.76), pya.DPoint(51.21, 225.76), pya.DPoint(50.91, 225.76), pya.DPoint(50.91, 224.76)]))
    _txt = pya.Text("uio_out[3]",
                   pya.Trans(1, False, pya.Vector(48300, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(48.15, 224.76), pya.DPoint(48.45, 224.76), pya.DPoint(48.45, 225.76), pya.DPoint(48.15, 225.76), pya.DPoint(48.15, 224.76)]))
    _txt = pya.Text("uio_out[4]",
                   pya.Trans(1, False, pya.Vector(45540, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(45.39, 224.76), pya.DPoint(45.69, 224.76), pya.DPoint(45.69, 225.76), pya.DPoint(45.39, 225.76), pya.DPoint(45.39, 224.76)]))
    _txt = pya.Text("uio_out[5]",
                   pya.Trans(1, False, pya.Vector(42780, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(42.63, 224.76), pya.DPoint(42.93, 224.76), pya.DPoint(42.93, 225.76), pya.DPoint(42.63, 225.76), pya.DPoint(42.63, 224.76)]))
    _txt = pya.Text("uio_out[6]",
                   pya.Trans(1, False, pya.Vector(40020, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(39.87, 224.76), pya.DPoint(40.17, 224.76), pya.DPoint(40.17, 225.76), pya.DPoint(39.87, 225.76), pya.DPoint(39.87, 224.76)]))
    _txt = pya.Text("uio_out[7]",
                   pya.Trans(1, False, pya.Vector(37260, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(37.11, 224.76), pya.DPoint(37.41, 224.76), pya.DPoint(37.41, 225.76), pya.DPoint(37.11, 225.76), pya.DPoint(37.11, 224.76)]))
    _txt = pya.Text("uo_out[0]",
                   pya.Trans(1, False, pya.Vector(78660, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(78.51, 224.76), pya.DPoint(78.81, 224.76), pya.DPoint(78.81, 225.76), pya.DPoint(78.51, 225.76), pya.DPoint(78.51, 224.76)]))
    _txt = pya.Text("uo_out[1]",
                   pya.Trans(1, False, pya.Vector(75900, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(75.75, 224.76), pya.DPoint(76.05, 224.76), pya.DPoint(76.05, 225.76), pya.DPoint(75.75, 225.76), pya.DPoint(75.75, 224.76)]))
    _txt = pya.Text("uo_out[2]",
                   pya.Trans(1, False, pya.Vector(73140, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(72.99, 224.76), pya.DPoint(73.29, 224.76), pya.DPoint(73.29, 225.76), pya.DPoint(72.99, 225.76), pya.DPoint(72.99, 224.76)]))
    _txt = pya.Text("uo_out[3]",
                   pya.Trans(1, False, pya.Vector(70380, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(70.23, 224.76), pya.DPoint(70.53, 224.76), pya.DPoint(70.53, 225.76), pya.DPoint(70.23, 225.76), pya.DPoint(70.23, 224.76)]))
    _txt = pya.Text("uo_out[4]",
                   pya.Trans(1, False, pya.Vector(67620, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(67.47, 224.76), pya.DPoint(67.77, 224.76), pya.DPoint(67.77, 225.76), pya.DPoint(67.47, 225.76), pya.DPoint(67.47, 224.76)]))
    _txt = pya.Text("uo_out[5]",
                   pya.Trans(1, False, pya.Vector(64860, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(64.71, 224.76), pya.DPoint(65.01, 224.76), pya.DPoint(65.01, 225.76), pya.DPoint(64.71, 225.76), pya.DPoint(64.71, 224.76)]))
    _txt = pya.Text("uo_out[6]",
                   pya.Trans(1, False, pya.Vector(62100, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(61.95, 224.76), pya.DPoint(62.25, 224.76), pya.DPoint(62.25, 225.76), pya.DPoint(61.95, 225.76), pya.DPoint(61.95, 224.76)]))
    _txt = pya.Text("uo_out[7]",
                   pya.Trans(1, False, pya.Vector(59340, 225260)))
    _txt.halign = 1
    _txt.valign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(59.19, 224.76), pya.DPoint(59.49, 224.76), pya.DPoint(59.49, 225.76), pya.DPoint(59.19, 225.76), pya.DPoint(59.19, 224.76)]))
    _txt = pya.Text("VDPWR",
                   pya.Trans(0, False, pya.Vector(2000, 112880)))
    _txt.halign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(1, 5), pya.DPoint(3, 5), pya.DPoint(3, 220.76), pya.DPoint(1, 220.76), pya.DPoint(1, 5)]))
    _txt = pya.Text("VGND",
                   pya.Trans(0, False, pya.Vector(5000, 112880)))
    _txt.halign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(4, 5), pya.DPoint(6, 5), pya.DPoint(6, 220.76), pya.DPoint(4, 220.76), pya.DPoint(4, 5)]))
    _txt = pya.Text("VAPWR",
                   pya.Trans(0, False, pya.Vector(8000, 112880)))
    _txt.halign = 1
    cell.shapes(L.L_met4_pin).insert(_txt)
    cell.shapes(L.L_met4_label).insert(
        pya.DPolygon([pya.DPoint(7, 5), pya.DPoint(9, 5), pya.DPoint(9, 220.76), pya.DPoint(7, 220.76), pya.DPoint(7, 5)]))

# Save
    layout.write("output.gds")

if __name__ == "__main__":
    # This block only runs when you open this file in KLayout and hit Run.
    # It is silently skipped when main_ihp.py imports this module.
    layout = pya.Layout()
    layout.dbu = 0.001
    L = register_layers(layout)
    cells = {}
    cells["tatzelreference_tile"] = layout.create_cell("tatzelreference_tile")
    _build_tatzelreference_tile(layout, L, cells)
    cells["tt_um_tatzelreference"] = layout.create_cell("tt_um_tatzelreference")
    build(layout, L, cells)
    out = "tt_um_tatzelreference.gds"
    layout.write(out)
    print("Written:", out)
