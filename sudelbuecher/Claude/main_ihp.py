"""main_ihp.py
Assembles the full layout from per-cell modules.
Run in KLayout via: Macros → Run Script, or from command line:
    python main_ihp.py
"""

import pya
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "cells"))

from layers import register_layers
from shortpmos_2x import build_shortpmos_2x
from shortnmos_2x import build_shortnmos_2x
from sky130_fd_pr__nfet_01v8_BDGNGK import build_sky130_fd_pr__nfet_01v8_BDGNGK
from nmos_8x2 import build_nmos_8x2
from flatpmos1x0_3 import build_flatpmos1x0_3
from ToBiasStartup import build_ToBiasStartup
from nmos1x20_8x import build_nmos1x20_8x
from nmos_1x80_2x import build_nmos_1x80_2x
from pmos_7x import build_pmos_7x
from nmos_5x import build_nmos_5x
from OgueyAebischer_p7_n5 import build_OgueyAebischer_p7_n5
from OgueyAebischerBias import build_OgueyAebischerBias
from reference import build_reference
from tatzelreference_tile import build_tatzelreference_tile
from tt_um_tatzelreference import build_tt_um_tatzelreference

# ── setup ────────────────────────────────────────────────────────────
layout = pya.Layout()
layout.dbu = 0.001
L = register_layers(layout)

# ── cell declarations ────────────────────────────────────────────────
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

# ── populate cells (leaf → top order) ───────────────────────────────
# Cells are built in declaration order; adjust if you see missing refs.
build_shortpmos_2x(cells["shortpmos_2x"], L, cells)
build_shortnmos_2x(cells["shortnmos_2x"], L, cells)
build_sky130_fd_pr__nfet_01v8_BDGNGK(cells["sky130_fd_pr__nfet_01v8_BDGNGK"], L, cells)
build_nmos_8x2(cells["nmos_8x2"], L, cells)
build_flatpmos1x0_3(cells["flatpmos1x0_3"], L, cells)
build_ToBiasStartup(cells["ToBiasStartup"], L, cells)
build_nmos1x20_8x(cells["nmos1x20_8x"], L, cells)
build_nmos_1x80_2x(cells["nmos_1x80_2x"], L, cells)
build_pmos_7x(cells["pmos_7x"], L, cells)
build_nmos_5x(cells["nmos_5x"], L, cells)
build_OgueyAebischer_p7_n5(cells["OgueyAebischer_p7_n5"], L, cells)
build_OgueyAebischerBias(cells["OgueyAebischerBias"], L, cells)
build_reference(cells["reference"], L, cells)
build_tatzelreference_tile(cells["tatzelreference_tile"], L, cells)
build_tt_um_tatzelreference(cells["tt_um_tatzelreference"], L, cells)

# ── write output ────────────────────────────────────────────────────
output_file = "output_ihp.gds"
layout.write(output_file)
print(f"Written: {output_file}")
