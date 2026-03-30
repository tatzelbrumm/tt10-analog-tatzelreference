"""main_ihp.py
Assembles the full layout by importing build() from each cell module.
Run in KLayout (Macros -> Run Script) or on the command line:
    python main_ihp.py
"""
import pya
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "cells"))
from layers import register_layers
from shortpmos_2x import build as build_shortpmos_2x
from shortnmos_2x import build as build_shortnmos_2x
from sky130_fd_pr__nfet_01v8_BDGNGK import build as build_sky130_fd_pr__nfet_01v8_BDGNGK
from nmos_8x2 import build as build_nmos_8x2
from flatpmos1x0_3 import build as build_flatpmos1x0_3
from ToBiasStartup import build as build_ToBiasStartup
from nmos1x20_8x import build as build_nmos1x20_8x
from nmos_1x80_2x import build as build_nmos_1x80_2x
from pmos_7x import build as build_pmos_7x
from nmos_5x import build as build_nmos_5x
from OgueyAebischer_p7_n5 import build as build_OgueyAebischer_p7_n5
from OgueyAebischerBias import build as build_OgueyAebischerBias
from reference import build as build_reference
from tatzelreference_tile import build as build_tatzelreference_tile
from tt_um_tatzelreference import build as build_tt_um_tatzelreference

layout = pya.Layout()
layout.dbu = 0.001
L = register_layers(layout)

cells = {}
cells["shortpmos_2x"] = layout.create_cell("shortpmos_2x")
cells["shortnmos_2x"] = layout.create_cell("shortnmos_2x")
cells["sky130_fd_pr__nfet_01v8_BDGNGK"] = layout.create_cell("sky130_fd_pr__nfet_01v8_BDGNGK")
cells["nmos_8x2"] = layout.create_cell("nmos_8x2")
cells["flatpmos1x0_3"] = layout.create_cell("flatpmos1x0_3")
cells["ToBiasStartup"] = layout.create_cell("ToBiasStartup")
cells["nmos1x20_8x"] = layout.create_cell("nmos1x20_8x")
cells["nmos_1x80_2x"] = layout.create_cell("nmos_1x80_2x")
cells["pmos_7x"] = layout.create_cell("pmos_7x")
cells["nmos_5x"] = layout.create_cell("nmos_5x")
cells["OgueyAebischer_p7_n5"] = layout.create_cell("OgueyAebischer_p7_n5")
cells["OgueyAebischerBias"] = layout.create_cell("OgueyAebischerBias")
cells["reference"] = layout.create_cell("reference")
cells["tatzelreference_tile"] = layout.create_cell("tatzelreference_tile")
cells["tt_um_tatzelreference"] = layout.create_cell("tt_um_tatzelreference")

# Populate in declaration order (leaf cells first)
build_shortpmos_2x(layout, L, cells)
build_shortnmos_2x(layout, L, cells)
build_sky130_fd_pr__nfet_01v8_BDGNGK(layout, L, cells)
build_nmos_8x2(layout, L, cells)
build_flatpmos1x0_3(layout, L, cells)
build_ToBiasStartup(layout, L, cells)
build_nmos1x20_8x(layout, L, cells)
build_nmos_1x80_2x(layout, L, cells)
build_pmos_7x(layout, L, cells)
build_nmos_5x(layout, L, cells)
build_OgueyAebischer_p7_n5(layout, L, cells)
build_OgueyAebischerBias(layout, L, cells)
build_reference(layout, L, cells)
build_tatzelreference_tile(layout, L, cells)
build_tt_um_tatzelreference(layout, L, cells)

layout.write("output_ihp.gds")
print("Written: output_ihp.gds")
