import pya

layout = pya.Layout()

layout.dbu = 0.001

# --- layer index variables ---
L_nwell_drawing = layout.layer(pya.LayerInfo(64, 20, "nwell.drawing"))
L_diff_drawing = layout.layer(pya.LayerInfo(65, 20, "diff.drawing"))
L_tap_drawing = layout.layer(pya.LayerInfo(65, 44, "tap.drawing"))
L_poly_drawing = layout.layer(pya.LayerInfo(66, 20, "poly.drawing"))
L_licon1_drawing = layout.layer(pya.LayerInfo(66, 44, "licon1.drawing"))
L_li1_drawing = layout.layer(pya.LayerInfo(67, 20, "li1.drawing"))
L_mcon_drawing = layout.layer(pya.LayerInfo(67, 44, "mcon.drawing"))
L_met1_drawing = layout.layer(pya.LayerInfo(68, 20, "met1.drawing"))
L_via_drawing = layout.layer(pya.LayerInfo(68, 44, "via.drawing"))
L_met2_pin = layout.layer(pya.LayerInfo(69, 5, "met2.pin"))
L_met2_label = layout.layer(pya.LayerInfo(69, 16, "met2.label"))
L_met2_drawing = layout.layer(pya.LayerInfo(69, 20, "met2.drawing"))
L_met4_pin = layout.layer(pya.LayerInfo(71, 5, "met4.pin"))
L_met4_label = layout.layer(pya.LayerInfo(71, 16, "met4.label"))
L_met4_drawing = layout.layer(pya.LayerInfo(71, 20, "met4.drawing"))
L_81_53 = layout.layer(81, 53)
L_nsdm_drawing = layout.layer(pya.LayerInfo(93, 44, "nsdm.drawing"))
L_psdm_drawing = layout.layer(pya.LayerInfo(94, 20, "psdm.drawing"))
L_npc_drawing = layout.layer(pya.LayerInfo(95, 20, "npc.drawing"))
L_235_4 = layout.layer(235, 4)

# --- cell declarations ---
cell_shortpmos_2x = layout.create_cell("shortpmos_2x")
cell_shortnmos_2x = layout.create_cell("shortnmos_2x")
cell_sky130_fd_pr__nfet_01v8_BDGNGK = layout.create_cell("sky130_fd_pr__nfet_01v8_BDGNGK")
cell_nmos_8x2 = layout.create_cell("nmos_8x2")
cell_flatpmos1x0_3 = layout.create_cell("flatpmos1x0.3")
cell_ToBiasStartup = layout.create_cell("ToBiasStartup")
cell_nmos1x20_8x = layout.create_cell("nmos1x20_8x")
cell_nmos_1x80_2x = layout.create_cell("nmos_1x80_2x")
cell_pmos_7x = layout.create_cell("pmos_7x")
cell_nmos_5x = layout.create_cell("nmos_5x")
cell_OgueyAebischer_p7_n5 = layout.create_cell("OgueyAebischer_p7_n5")
cell_OgueyAebischerBias = layout.create_cell("OgueyAebischerBias")
cell_reference = layout.create_cell("reference")
cell_tatzelreference_tile = layout.create_cell("tatzelreference_tile")
cell_tt_um_tatzelreference = layout.create_cell("tt_um_tatzelreference")

# === shortpmos_2x ===
cell_shortpmos_2x.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.45, -0.62), pya.DPoint(1.45, -0.62), pya.DPoint(1.45, 0.62), pya.DPoint(-1.45, 0.62), pya.DPoint(-1.45, -0.62)]))
cell_shortpmos_2x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, -0.44), pya.DPoint(-0.14, -0.44), pya.DPoint(-0.14, 0.44), pya.DPoint(-1.14, 0.44), pya.DPoint(-1.14, -0.44)]))
cell_shortpmos_2x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(0.14, -0.44), pya.DPoint(1.14, -0.44), pya.DPoint(1.14, 0.44), pya.DPoint(0.14, 0.44), pya.DPoint(0.14, -0.44)]))
cell_shortpmos_2x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.265, -0.565), pya.DPoint(1.265, -0.565), pya.DPoint(1.265, 0.565), pya.DPoint(-1.265, 0.565), pya.DPoint(-1.265, -0.565)]))
cell_shortpmos_2x.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.27, -0.15), pya.DPoint(1.27, -0.15), pya.DPoint(1.27, 0.15), pya.DPoint(-1.27, 0.15), pya.DPoint(-1.27, -0.15)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.065, 0.21), pya.DPoint(-0.895, 0.21), pya.DPoint(-0.895, 0.38), pya.DPoint(-1.065, 0.38), pya.DPoint(-1.065, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.725, 0.21), pya.DPoint(-0.555, 0.21), pya.DPoint(-0.555, 0.38), pya.DPoint(-0.725, 0.38), pya.DPoint(-0.725, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.385, 0.21), pya.DPoint(-0.215, 0.21), pya.DPoint(-0.215, 0.38), pya.DPoint(-0.385, 0.38), pya.DPoint(-0.385, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.215, 0.21), pya.DPoint(0.385, 0.21), pya.DPoint(0.385, 0.38), pya.DPoint(0.215, 0.38), pya.DPoint(0.215, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.555, 0.21), pya.DPoint(0.725, 0.21), pya.DPoint(0.725, 0.38), pya.DPoint(0.555, 0.38), pya.DPoint(0.555, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.895, 0.21), pya.DPoint(1.065, 0.21), pya.DPoint(1.065, 0.38), pya.DPoint(0.895, 0.38), pya.DPoint(0.895, 0.21)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.065, -0.38), pya.DPoint(-0.895, -0.38), pya.DPoint(-0.895, -0.21), pya.DPoint(-1.065, -0.21), pya.DPoint(-1.065, -0.38)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.725, -0.38), pya.DPoint(-0.555, -0.38), pya.DPoint(-0.555, -0.21), pya.DPoint(-0.725, -0.21), pya.DPoint(-0.725, -0.38)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.385, -0.38), pya.DPoint(-0.215, -0.38), pya.DPoint(-0.215, -0.21), pya.DPoint(-0.385, -0.21), pya.DPoint(-0.385, -0.38)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.215, -0.38), pya.DPoint(0.385, -0.38), pya.DPoint(0.385, -0.21), pya.DPoint(0.215, -0.21), pya.DPoint(0.215, -0.38)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.555, -0.38), pya.DPoint(0.725, -0.38), pya.DPoint(0.725, -0.21), pya.DPoint(0.555, -0.21), pya.DPoint(0.555, -0.38)]))
cell_shortpmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.895, -0.38), pya.DPoint(1.065, -0.38), pya.DPoint(1.065, -0.21), pya.DPoint(0.895, -0.21), pya.DPoint(0.895, -0.38)]))
cell_shortpmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.16, 0.21), pya.DPoint(1.16, 0.21), pya.DPoint(1.16, 0.38), pya.DPoint(-1.16, 0.38), pya.DPoint(-1.16, 0.21)]))
cell_shortpmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.16, -0.38), pya.DPoint(-0.12, -0.38), pya.DPoint(-0.12, -0.21), pya.DPoint(-1.16, -0.21), pya.DPoint(-1.16, -0.38)]))
cell_shortpmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.12, -0.38), pya.DPoint(1.16, -0.38), pya.DPoint(1.16, -0.21), pya.DPoint(0.12, -0.21), pya.DPoint(0.12, -0.38)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.905, 0.21), pya.DPoint(-0.735, 0.21), pya.DPoint(-0.735, 0.38), pya.DPoint(-0.905, 0.38), pya.DPoint(-0.905, 0.21)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.545, 0.21), pya.DPoint(-0.375, 0.21), pya.DPoint(-0.375, 0.38), pya.DPoint(-0.545, 0.38), pya.DPoint(-0.545, 0.21)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.375, 0.21), pya.DPoint(0.545, 0.21), pya.DPoint(0.545, 0.38), pya.DPoint(0.375, 0.38), pya.DPoint(0.375, 0.21)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, 0.21), pya.DPoint(0.905, 0.21), pya.DPoint(0.905, 0.38), pya.DPoint(0.735, 0.38), pya.DPoint(0.735, 0.21)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.905, -0.38), pya.DPoint(-0.735, -0.38), pya.DPoint(-0.735, -0.21), pya.DPoint(-0.905, -0.21), pya.DPoint(-0.905, -0.38)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.545, -0.38), pya.DPoint(-0.375, -0.38), pya.DPoint(-0.375, -0.21), pya.DPoint(-0.545, -0.21), pya.DPoint(-0.545, -0.38)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.375, -0.38), pya.DPoint(0.545, -0.38), pya.DPoint(0.545, -0.21), pya.DPoint(0.375, -0.21), pya.DPoint(0.375, -0.38)]))
cell_shortpmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, -0.38), pya.DPoint(0.905, -0.38), pya.DPoint(0.905, -0.21), pya.DPoint(0.735, -0.21), pya.DPoint(0.735, -0.38)]))
cell_shortpmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, 0.18), pya.DPoint(1.14, 0.18), pya.DPoint(1.14, 0.41), pya.DPoint(-1.14, 0.41), pya.DPoint(-1.14, 0.18)]))
cell_shortpmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, -0.41), pya.DPoint(-0.14, -0.41), pya.DPoint(-0.14, -0.18), pya.DPoint(-1.14, -0.18), pya.DPoint(-1.14, -0.41)]))
cell_shortpmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.14, -0.41), pya.DPoint(1.14, -0.41), pya.DPoint(1.14, -0.18), pya.DPoint(0.14, -0.18), pya.DPoint(0.14, -0.41)]))

# === shortnmos_2x ===
cell_shortnmos_2x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, -0.44), pya.DPoint(-0.14, -0.44), pya.DPoint(-0.14, 0.44), pya.DPoint(-1.14, 0.44), pya.DPoint(-1.14, -0.44)]))
cell_shortnmos_2x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(0.14, -0.44), pya.DPoint(1.14, -0.44), pya.DPoint(1.14, 0.44), pya.DPoint(0.14, 0.44), pya.DPoint(0.14, -0.44)]))
cell_shortnmos_2x.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.265, -0.565), pya.DPoint(1.265, -0.565), pya.DPoint(1.265, 0.565), pya.DPoint(-1.265, 0.565), pya.DPoint(-1.265, -0.565)]))
cell_shortnmos_2x.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.27, -0.15), pya.DPoint(1.27, -0.15), pya.DPoint(1.27, 0.15), pya.DPoint(-1.27, 0.15), pya.DPoint(-1.27, -0.15)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.065, 0.21), pya.DPoint(-0.895, 0.21), pya.DPoint(-0.895, 0.38), pya.DPoint(-1.065, 0.38), pya.DPoint(-1.065, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.725, 0.21), pya.DPoint(-0.555, 0.21), pya.DPoint(-0.555, 0.38), pya.DPoint(-0.725, 0.38), pya.DPoint(-0.725, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.385, 0.21), pya.DPoint(-0.215, 0.21), pya.DPoint(-0.215, 0.38), pya.DPoint(-0.385, 0.38), pya.DPoint(-0.385, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.215, 0.21), pya.DPoint(0.385, 0.21), pya.DPoint(0.385, 0.38), pya.DPoint(0.215, 0.38), pya.DPoint(0.215, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.555, 0.21), pya.DPoint(0.725, 0.21), pya.DPoint(0.725, 0.38), pya.DPoint(0.555, 0.38), pya.DPoint(0.555, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.895, 0.21), pya.DPoint(1.065, 0.21), pya.DPoint(1.065, 0.38), pya.DPoint(0.895, 0.38), pya.DPoint(0.895, 0.21)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.065, -0.38), pya.DPoint(-0.895, -0.38), pya.DPoint(-0.895, -0.21), pya.DPoint(-1.065, -0.21), pya.DPoint(-1.065, -0.38)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.725, -0.38), pya.DPoint(-0.555, -0.38), pya.DPoint(-0.555, -0.21), pya.DPoint(-0.725, -0.21), pya.DPoint(-0.725, -0.38)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.385, -0.38), pya.DPoint(-0.215, -0.38), pya.DPoint(-0.215, -0.21), pya.DPoint(-0.385, -0.21), pya.DPoint(-0.385, -0.38)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.215, -0.38), pya.DPoint(0.385, -0.38), pya.DPoint(0.385, -0.21), pya.DPoint(0.215, -0.21), pya.DPoint(0.215, -0.38)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.555, -0.38), pya.DPoint(0.725, -0.38), pya.DPoint(0.725, -0.21), pya.DPoint(0.555, -0.21), pya.DPoint(0.555, -0.38)]))
cell_shortnmos_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.895, -0.38), pya.DPoint(1.065, -0.38), pya.DPoint(1.065, -0.21), pya.DPoint(0.895, -0.21), pya.DPoint(0.895, -0.38)]))
cell_shortnmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.16, 0.21), pya.DPoint(-0.12, 0.21), pya.DPoint(-0.12, 0.38), pya.DPoint(-1.16, 0.38), pya.DPoint(-1.16, 0.21)]))
cell_shortnmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.12, 0.21), pya.DPoint(1.16, 0.21), pya.DPoint(1.16, 0.38), pya.DPoint(0.12, 0.38), pya.DPoint(0.12, 0.21)]))
cell_shortnmos_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.16, -0.38), pya.DPoint(1.16, -0.38), pya.DPoint(1.16, -0.21), pya.DPoint(-1.16, -0.21), pya.DPoint(-1.16, -0.38)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.905, 0.21), pya.DPoint(-0.735, 0.21), pya.DPoint(-0.735, 0.38), pya.DPoint(-0.905, 0.38), pya.DPoint(-0.905, 0.21)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.545, 0.21), pya.DPoint(-0.375, 0.21), pya.DPoint(-0.375, 0.38), pya.DPoint(-0.545, 0.38), pya.DPoint(-0.545, 0.21)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.375, 0.21), pya.DPoint(0.545, 0.21), pya.DPoint(0.545, 0.38), pya.DPoint(0.375, 0.38), pya.DPoint(0.375, 0.21)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, 0.21), pya.DPoint(0.905, 0.21), pya.DPoint(0.905, 0.38), pya.DPoint(0.735, 0.38), pya.DPoint(0.735, 0.21)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.905, -0.38), pya.DPoint(-0.735, -0.38), pya.DPoint(-0.735, -0.21), pya.DPoint(-0.905, -0.21), pya.DPoint(-0.905, -0.38)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.545, -0.38), pya.DPoint(-0.375, -0.38), pya.DPoint(-0.375, -0.21), pya.DPoint(-0.545, -0.21), pya.DPoint(-0.545, -0.38)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.375, -0.38), pya.DPoint(0.545, -0.38), pya.DPoint(0.545, -0.21), pya.DPoint(0.375, -0.21), pya.DPoint(0.375, -0.38)]))
cell_shortnmos_2x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, -0.38), pya.DPoint(0.905, -0.38), pya.DPoint(0.905, -0.21), pya.DPoint(0.735, -0.21), pya.DPoint(0.735, -0.38)]))
cell_shortnmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, 0.18), pya.DPoint(-0.14, 0.18), pya.DPoint(-0.14, 0.41), pya.DPoint(-1.14, 0.41), pya.DPoint(-1.14, 0.18)]))
cell_shortnmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.14, 0.18), pya.DPoint(1.14, 0.18), pya.DPoint(1.14, 0.41), pya.DPoint(0.14, 0.41), pya.DPoint(0.14, 0.18)]))
cell_shortnmos_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.14, -0.41), pya.DPoint(1.14, -0.41), pya.DPoint(1.14, -0.18), pya.DPoint(-1.14, -0.18), pya.DPoint(-1.14, -0.41)]))

# === sky130_fd_pr__nfet_01v8_BDGNGK ===
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.29, -4.155), pya.DPoint(1.29, -4.155), pya.DPoint(1.29, 3.845), pya.DPoint(-1.29, 3.845), pya.DPoint(-1.29, -4.155)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.415, -4.28), pya.DPoint(1.415, -4.28), pya.DPoint(1.415, 3.97), pya.DPoint(-1.415, 3.97), pya.DPoint(-1.415, -4.28)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-1, -4.285), pya.DPoint(1, -4.285), pya.DPoint(1, 4.285), pya.DPoint(-1, 4.285), pya.DPoint(-1, -4.285)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.765, 4.035), pya.DPoint(-0.595, 4.035), pya.DPoint(-0.595, 4.205), pya.DPoint(-0.765, 4.205), pya.DPoint(-0.765, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, 4.035), pya.DPoint(-0.255, 4.035), pya.DPoint(-0.255, 4.205), pya.DPoint(-0.425, 4.205), pya.DPoint(-0.425, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 4.035), pya.DPoint(0.085, 4.035), pya.DPoint(0.085, 4.205), pya.DPoint(-0.085, 4.205), pya.DPoint(-0.085, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, 4.035), pya.DPoint(0.425, 4.035), pya.DPoint(0.425, 4.205), pya.DPoint(0.255, 4.205), pya.DPoint(0.255, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.595, 4.035), pya.DPoint(0.765, 4.035), pya.DPoint(0.765, 4.205), pya.DPoint(0.595, 4.205), pya.DPoint(0.595, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 3.5), pya.DPoint(-1.06, 3.5), pya.DPoint(-1.06, 3.67), pya.DPoint(-1.23, 3.67), pya.DPoint(-1.23, 3.5)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 3.5), pya.DPoint(1.23, 3.5), pya.DPoint(1.23, 3.67), pya.DPoint(1.06, 3.67), pya.DPoint(1.06, 3.5)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 3.16), pya.DPoint(-1.06, 3.16), pya.DPoint(-1.06, 3.33), pya.DPoint(-1.23, 3.33), pya.DPoint(-1.23, 3.16)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 3.16), pya.DPoint(1.23, 3.16), pya.DPoint(1.23, 3.33), pya.DPoint(1.06, 3.33), pya.DPoint(1.06, 3.16)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.82), pya.DPoint(-1.06, 2.82), pya.DPoint(-1.06, 2.99), pya.DPoint(-1.23, 2.99), pya.DPoint(-1.23, 2.82)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.82), pya.DPoint(1.23, 2.82), pya.DPoint(1.23, 2.99), pya.DPoint(1.06, 2.99), pya.DPoint(1.06, 2.82)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.48), pya.DPoint(-1.06, 2.48), pya.DPoint(-1.06, 2.65), pya.DPoint(-1.23, 2.65), pya.DPoint(-1.23, 2.48)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.48), pya.DPoint(1.23, 2.48), pya.DPoint(1.23, 2.65), pya.DPoint(1.06, 2.65), pya.DPoint(1.06, 2.48)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.14), pya.DPoint(-1.06, 2.14), pya.DPoint(-1.06, 2.31), pya.DPoint(-1.23, 2.31), pya.DPoint(-1.23, 2.14)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.14), pya.DPoint(1.23, 2.14), pya.DPoint(1.23, 2.31), pya.DPoint(1.06, 2.31), pya.DPoint(1.06, 2.14)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.8), pya.DPoint(-1.06, 1.8), pya.DPoint(-1.06, 1.97), pya.DPoint(-1.23, 1.97), pya.DPoint(-1.23, 1.8)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.8), pya.DPoint(1.23, 1.8), pya.DPoint(1.23, 1.97), pya.DPoint(1.06, 1.97), pya.DPoint(1.06, 1.8)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.46), pya.DPoint(-1.06, 1.46), pya.DPoint(-1.06, 1.63), pya.DPoint(-1.23, 1.63), pya.DPoint(-1.23, 1.46)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.46), pya.DPoint(1.23, 1.46), pya.DPoint(1.23, 1.63), pya.DPoint(1.06, 1.63), pya.DPoint(1.06, 1.46)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.12), pya.DPoint(-1.06, 1.12), pya.DPoint(-1.06, 1.29), pya.DPoint(-1.23, 1.29), pya.DPoint(-1.23, 1.12)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.12), pya.DPoint(1.23, 1.12), pya.DPoint(1.23, 1.29), pya.DPoint(1.06, 1.29), pya.DPoint(1.06, 1.12)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.78), pya.DPoint(-1.06, 0.78), pya.DPoint(-1.06, 0.95), pya.DPoint(-1.23, 0.95), pya.DPoint(-1.23, 0.78)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 0.78), pya.DPoint(1.23, 0.78), pya.DPoint(1.23, 0.95), pya.DPoint(1.06, 0.95), pya.DPoint(1.06, 0.78)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.44), pya.DPoint(-1.06, 0.44), pya.DPoint(-1.06, 0.61), pya.DPoint(-1.23, 0.61), pya.DPoint(-1.23, 0.44)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 0.44), pya.DPoint(1.23, 0.44), pya.DPoint(1.23, 0.61), pya.DPoint(1.06, 0.61), pya.DPoint(1.06, 0.44)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.1), pya.DPoint(-1.06, 0.1), pya.DPoint(-1.06, 0.27), pya.DPoint(-1.23, 0.27), pya.DPoint(-1.23, 0.1)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 0.1), pya.DPoint(1.23, 0.1), pya.DPoint(1.23, 0.27), pya.DPoint(1.06, 0.27), pya.DPoint(1.06, 0.1)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.24), pya.DPoint(-1.06, -0.24), pya.DPoint(-1.06, -0.07), pya.DPoint(-1.23, -0.07), pya.DPoint(-1.23, -0.24)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.24), pya.DPoint(1.23, -0.24), pya.DPoint(1.23, -0.07), pya.DPoint(1.06, -0.07), pya.DPoint(1.06, -0.24)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.58), pya.DPoint(-1.06, -0.58), pya.DPoint(-1.06, -0.41), pya.DPoint(-1.23, -0.41), pya.DPoint(-1.23, -0.58)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.58), pya.DPoint(1.23, -0.58), pya.DPoint(1.23, -0.41), pya.DPoint(1.06, -0.41), pya.DPoint(1.06, -0.58)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.92), pya.DPoint(-1.06, -0.92), pya.DPoint(-1.06, -0.75), pya.DPoint(-1.23, -0.75), pya.DPoint(-1.23, -0.92)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.92), pya.DPoint(1.23, -0.92), pya.DPoint(1.23, -0.75), pya.DPoint(1.06, -0.75), pya.DPoint(1.06, -0.92)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.26), pya.DPoint(-1.06, -1.26), pya.DPoint(-1.06, -1.09), pya.DPoint(-1.23, -1.09), pya.DPoint(-1.23, -1.26)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.26), pya.DPoint(1.23, -1.26), pya.DPoint(1.23, -1.09), pya.DPoint(1.06, -1.09), pya.DPoint(1.06, -1.26)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.6), pya.DPoint(-1.06, -1.6), pya.DPoint(-1.06, -1.43), pya.DPoint(-1.23, -1.43), pya.DPoint(-1.23, -1.6)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.6), pya.DPoint(1.23, -1.6), pya.DPoint(1.23, -1.43), pya.DPoint(1.06, -1.43), pya.DPoint(1.06, -1.6)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.94), pya.DPoint(-1.06, -1.94), pya.DPoint(-1.06, -1.77), pya.DPoint(-1.23, -1.77), pya.DPoint(-1.23, -1.94)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.94), pya.DPoint(1.23, -1.94), pya.DPoint(1.23, -1.77), pya.DPoint(1.06, -1.77), pya.DPoint(1.06, -1.94)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.28), pya.DPoint(-1.06, -2.28), pya.DPoint(-1.06, -2.11), pya.DPoint(-1.23, -2.11), pya.DPoint(-1.23, -2.28)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.28), pya.DPoint(1.23, -2.28), pya.DPoint(1.23, -2.11), pya.DPoint(1.06, -2.11), pya.DPoint(1.06, -2.28)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.62), pya.DPoint(-1.06, -2.62), pya.DPoint(-1.06, -2.45), pya.DPoint(-1.23, -2.45), pya.DPoint(-1.23, -2.62)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.62), pya.DPoint(1.23, -2.62), pya.DPoint(1.23, -2.45), pya.DPoint(1.06, -2.45), pya.DPoint(1.06, -2.62)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.96), pya.DPoint(-1.06, -2.96), pya.DPoint(-1.06, -2.79), pya.DPoint(-1.23, -2.79), pya.DPoint(-1.23, -2.96)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.96), pya.DPoint(1.23, -2.96), pya.DPoint(1.23, -2.79), pya.DPoint(1.06, -2.79), pya.DPoint(1.06, -2.96)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -3.3), pya.DPoint(-1.06, -3.3), pya.DPoint(-1.06, -3.13), pya.DPoint(-1.23, -3.13), pya.DPoint(-1.23, -3.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -3.3), pya.DPoint(1.23, -3.3), pya.DPoint(1.23, -3.13), pya.DPoint(1.06, -3.13), pya.DPoint(1.06, -3.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -3.64), pya.DPoint(-1.06, -3.64), pya.DPoint(-1.06, -3.47), pya.DPoint(-1.23, -3.47), pya.DPoint(-1.23, -3.64)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -3.64), pya.DPoint(1.23, -3.64), pya.DPoint(1.23, -3.47), pya.DPoint(1.06, -3.47), pya.DPoint(1.06, -3.64)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -3.98), pya.DPoint(-1.06, -3.98), pya.DPoint(-1.06, -3.81), pya.DPoint(-1.23, -3.81), pya.DPoint(-1.23, -3.98)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -3.98), pya.DPoint(1.23, -3.98), pya.DPoint(1.23, -3.81), pya.DPoint(1.06, -3.81), pya.DPoint(1.06, -3.98)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.865, 3.935), pya.DPoint(0.865, 3.935), pya.DPoint(0.865, 4.305), pya.DPoint(-0.865, 4.305), pya.DPoint(-0.865, 3.935)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1, 4.035), pya.DPoint(1, 4.035), pya.DPoint(1, 4.205), pya.DPoint(-1, 4.205), pya.DPoint(-1, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -4.175), pya.DPoint(-1.06, -4.175), pya.DPoint(-1.06, 3.865), pya.DPoint(-1.23, 3.865), pya.DPoint(-1.23, -4.175)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -4.175), pya.DPoint(1.23, -4.175), pya.DPoint(1.23, 3.865), pya.DPoint(1.06, 3.865), pya.DPoint(1.06, -4.175)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.805, 4.035), pya.DPoint(-0.635, 4.035), pya.DPoint(-0.635, 4.205), pya.DPoint(-0.805, 4.205), pya.DPoint(-0.805, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.445, 4.035), pya.DPoint(-0.275, 4.035), pya.DPoint(-0.275, 4.205), pya.DPoint(-0.445, 4.205), pya.DPoint(-0.445, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 4.035), pya.DPoint(0.085, 4.035), pya.DPoint(0.085, 4.205), pya.DPoint(-0.085, 4.205), pya.DPoint(-0.085, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.275, 4.035), pya.DPoint(0.445, 4.035), pya.DPoint(0.445, 4.205), pya.DPoint(0.275, 4.205), pya.DPoint(0.275, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.635, 4.035), pya.DPoint(0.805, 4.035), pya.DPoint(0.805, 4.205), pya.DPoint(0.635, 4.205), pya.DPoint(0.635, 4.035)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 3.54), pya.DPoint(-1.06, 3.54), pya.DPoint(-1.06, 3.71), pya.DPoint(-1.23, 3.71), pya.DPoint(-1.23, 3.54)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 3.54), pya.DPoint(1.23, 3.54), pya.DPoint(1.23, 3.71), pya.DPoint(1.06, 3.71), pya.DPoint(1.06, 3.54)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 3.18), pya.DPoint(-1.06, 3.18), pya.DPoint(-1.06, 3.35), pya.DPoint(-1.23, 3.35), pya.DPoint(-1.23, 3.18)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 3.18), pya.DPoint(1.23, 3.18), pya.DPoint(1.23, 3.35), pya.DPoint(1.06, 3.35), pya.DPoint(1.06, 3.18)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.82), pya.DPoint(-1.06, 2.82), pya.DPoint(-1.06, 2.99), pya.DPoint(-1.23, 2.99), pya.DPoint(-1.23, 2.82)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.82), pya.DPoint(1.23, 2.82), pya.DPoint(1.23, 2.99), pya.DPoint(1.06, 2.99), pya.DPoint(1.06, 2.82)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.46), pya.DPoint(-1.06, 2.46), pya.DPoint(-1.06, 2.63), pya.DPoint(-1.23, 2.63), pya.DPoint(-1.23, 2.46)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.46), pya.DPoint(1.23, 2.46), pya.DPoint(1.23, 2.63), pya.DPoint(1.06, 2.63), pya.DPoint(1.06, 2.46)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 2.1), pya.DPoint(-1.06, 2.1), pya.DPoint(-1.06, 2.27), pya.DPoint(-1.23, 2.27), pya.DPoint(-1.23, 2.1)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 2.1), pya.DPoint(1.23, 2.1), pya.DPoint(1.23, 2.27), pya.DPoint(1.06, 2.27), pya.DPoint(1.06, 2.1)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.74), pya.DPoint(-1.06, 1.74), pya.DPoint(-1.06, 1.91), pya.DPoint(-1.23, 1.91), pya.DPoint(-1.23, 1.74)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.74), pya.DPoint(1.23, 1.74), pya.DPoint(1.23, 1.91), pya.DPoint(1.06, 1.91), pya.DPoint(1.06, 1.74)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.38), pya.DPoint(-1.06, 1.38), pya.DPoint(-1.06, 1.55), pya.DPoint(-1.23, 1.55), pya.DPoint(-1.23, 1.38)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.38), pya.DPoint(1.23, 1.38), pya.DPoint(1.23, 1.55), pya.DPoint(1.06, 1.55), pya.DPoint(1.06, 1.38)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 1.02), pya.DPoint(-1.06, 1.02), pya.DPoint(-1.06, 1.19), pya.DPoint(-1.23, 1.19), pya.DPoint(-1.23, 1.02)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 1.02), pya.DPoint(1.23, 1.02), pya.DPoint(1.23, 1.19), pya.DPoint(1.06, 1.19), pya.DPoint(1.06, 1.02)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.66), pya.DPoint(-1.06, 0.66), pya.DPoint(-1.06, 0.83), pya.DPoint(-1.23, 0.83), pya.DPoint(-1.23, 0.66)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 0.66), pya.DPoint(1.23, 0.66), pya.DPoint(1.23, 0.83), pya.DPoint(1.06, 0.83), pya.DPoint(1.06, 0.66)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.3), pya.DPoint(-1.06, 0.3), pya.DPoint(-1.06, 0.47), pya.DPoint(-1.23, 0.47), pya.DPoint(-1.23, 0.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, 0.3), pya.DPoint(1.23, 0.3), pya.DPoint(1.23, 0.47), pya.DPoint(1.06, 0.47), pya.DPoint(1.06, 0.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.06), pya.DPoint(-1.06, -0.06), pya.DPoint(-1.06, 0.11), pya.DPoint(-1.23, 0.11), pya.DPoint(-1.23, -0.06)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.06), pya.DPoint(1.23, -0.06), pya.DPoint(1.23, 0.11), pya.DPoint(1.06, 0.11), pya.DPoint(1.06, -0.06)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.42), pya.DPoint(-1.06, -0.42), pya.DPoint(-1.06, -0.25), pya.DPoint(-1.23, -0.25), pya.DPoint(-1.23, -0.42)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.42), pya.DPoint(1.23, -0.42), pya.DPoint(1.23, -0.25), pya.DPoint(1.06, -0.25), pya.DPoint(1.06, -0.42)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -0.78), pya.DPoint(-1.06, -0.78), pya.DPoint(-1.06, -0.61), pya.DPoint(-1.23, -0.61), pya.DPoint(-1.23, -0.78)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -0.78), pya.DPoint(1.23, -0.78), pya.DPoint(1.23, -0.61), pya.DPoint(1.06, -0.61), pya.DPoint(1.06, -0.78)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.14), pya.DPoint(-1.06, -1.14), pya.DPoint(-1.06, -0.97), pya.DPoint(-1.23, -0.97), pya.DPoint(-1.23, -1.14)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.14), pya.DPoint(1.23, -1.14), pya.DPoint(1.23, -0.97), pya.DPoint(1.06, -0.97), pya.DPoint(1.06, -1.14)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.5), pya.DPoint(-1.06, -1.5), pya.DPoint(-1.06, -1.33), pya.DPoint(-1.23, -1.33), pya.DPoint(-1.23, -1.5)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.5), pya.DPoint(1.23, -1.5), pya.DPoint(1.23, -1.33), pya.DPoint(1.06, -1.33), pya.DPoint(1.06, -1.5)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -1.86), pya.DPoint(-1.06, -1.86), pya.DPoint(-1.06, -1.69), pya.DPoint(-1.23, -1.69), pya.DPoint(-1.23, -1.86)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -1.86), pya.DPoint(1.23, -1.86), pya.DPoint(1.23, -1.69), pya.DPoint(1.06, -1.69), pya.DPoint(1.06, -1.86)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.22), pya.DPoint(-1.06, -2.22), pya.DPoint(-1.06, -2.05), pya.DPoint(-1.23, -2.05), pya.DPoint(-1.23, -2.22)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.22), pya.DPoint(1.23, -2.22), pya.DPoint(1.23, -2.05), pya.DPoint(1.06, -2.05), pya.DPoint(1.06, -2.22)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.58), pya.DPoint(-1.06, -2.58), pya.DPoint(-1.06, -2.41), pya.DPoint(-1.23, -2.41), pya.DPoint(-1.23, -2.58)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.58), pya.DPoint(1.23, -2.58), pya.DPoint(1.23, -2.41), pya.DPoint(1.06, -2.41), pya.DPoint(1.06, -2.58)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.94), pya.DPoint(-1.06, -2.94), pya.DPoint(-1.06, -2.77), pya.DPoint(-1.23, -2.77), pya.DPoint(-1.23, -2.94)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -2.94), pya.DPoint(1.23, -2.94), pya.DPoint(1.23, -2.77), pya.DPoint(1.06, -2.77), pya.DPoint(1.06, -2.94)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -3.3), pya.DPoint(-1.06, -3.3), pya.DPoint(-1.06, -3.13), pya.DPoint(-1.23, -3.13), pya.DPoint(-1.23, -3.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -3.3), pya.DPoint(1.23, -3.3), pya.DPoint(1.23, -3.13), pya.DPoint(1.06, -3.13), pya.DPoint(1.06, -3.3)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -3.66), pya.DPoint(-1.06, -3.66), pya.DPoint(-1.06, -3.49), pya.DPoint(-1.23, -3.49), pya.DPoint(-1.23, -3.66)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -3.66), pya.DPoint(1.23, -3.66), pya.DPoint(1.23, -3.49), pya.DPoint(1.06, -3.49), pya.DPoint(1.06, -3.66)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -4.02), pya.DPoint(-1.06, -4.02), pya.DPoint(-1.06, -3.85), pya.DPoint(-1.23, -3.85), pya.DPoint(-1.23, -4.02)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.06, -4.02), pya.DPoint(1.23, -4.02), pya.DPoint(1.23, -3.85), pya.DPoint(1.06, -3.85), pya.DPoint(1.06, -4.02)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.98, 4.005), pya.DPoint(0.98, 4.005), pya.DPoint(0.98, 4.235), pya.DPoint(-0.98, 4.235), pya.DPoint(-0.98, 4.005)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.26, -4.155), pya.DPoint(-1.03, -4.155), pya.DPoint(-1.03, 3.845), pya.DPoint(-1.26, 3.845), pya.DPoint(-1.26, -4.155)]))
cell_sky130_fd_pr__nfet_01v8_BDGNGK.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.03, -4.155), pya.DPoint(1.26, -4.155), pya.DPoint(1.26, 3.845), pya.DPoint(1.03, 3.845), pya.DPoint(1.03, -4.155)]))

# === nmos_8x2 ===
cell_nmos_8x2.insert(pya.DCellInstArray(
    cell_sky130_fd_pr__nfet_01v8_BDGNGK.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.29, 4.285))))

# === flatpmos1x0.3 ===
cell_flatpmos1x0_3.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.81, -0.62), pya.DPoint(0.81, -0.62), pya.DPoint(0.81, 0.62), pya.DPoint(-0.81, 0.62), pya.DPoint(-0.81, -0.62)]))
cell_flatpmos1x0_3.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.44), pya.DPoint(0.5, -0.44), pya.DPoint(0.5, 0.44), pya.DPoint(-0.5, 0.44), pya.DPoint(-0.5, -0.44)]))
cell_flatpmos1x0_3.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.625, -0.565), pya.DPoint(0.625, -0.565), pya.DPoint(0.625, 0.565), pya.DPoint(-0.625, 0.565), pya.DPoint(-0.625, -0.565)]))
cell_flatpmos1x0_3.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.63, -0.15), pya.DPoint(0.63, -0.15), pya.DPoint(0.63, 0.15), pya.DPoint(-0.63, 0.15), pya.DPoint(-0.63, -0.15)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, 0.21), pya.DPoint(-0.255, 0.21), pya.DPoint(-0.255, 0.38), pya.DPoint(-0.425, 0.38), pya.DPoint(-0.425, 0.21)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 0.21), pya.DPoint(0.085, 0.21), pya.DPoint(0.085, 0.38), pya.DPoint(-0.085, 0.38), pya.DPoint(-0.085, 0.21)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, 0.21), pya.DPoint(0.425, 0.21), pya.DPoint(0.425, 0.38), pya.DPoint(0.255, 0.38), pya.DPoint(0.255, 0.21)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, -0.38), pya.DPoint(-0.255, -0.38), pya.DPoint(-0.255, -0.21), pya.DPoint(-0.425, -0.21), pya.DPoint(-0.425, -0.38)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, -0.38), pya.DPoint(0.085, -0.38), pya.DPoint(0.085, -0.21), pya.DPoint(-0.085, -0.21), pya.DPoint(-0.085, -0.38)]))
cell_flatpmos1x0_3.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, -0.38), pya.DPoint(0.425, -0.38), pya.DPoint(0.425, -0.21), pya.DPoint(0.255, -0.21), pya.DPoint(0.255, -0.38)]))
cell_flatpmos1x0_3.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, 0.21), pya.DPoint(0.52, 0.21), pya.DPoint(0.52, 0.38), pya.DPoint(-0.52, 0.38), pya.DPoint(-0.52, 0.21)]))
cell_flatpmos1x0_3.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, -0.38), pya.DPoint(0.52, -0.38), pya.DPoint(0.52, -0.21), pya.DPoint(-0.52, -0.21), pya.DPoint(-0.52, -0.38)]))
cell_flatpmos1x0_3.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, 0.21), pya.DPoint(-0.095, 0.21), pya.DPoint(-0.095, 0.38), pya.DPoint(-0.265, 0.38), pya.DPoint(-0.265, 0.21)]))
cell_flatpmos1x0_3.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, 0.21), pya.DPoint(0.265, 0.21), pya.DPoint(0.265, 0.38), pya.DPoint(0.095, 0.38), pya.DPoint(0.095, 0.21)]))
cell_flatpmos1x0_3.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, -0.38), pya.DPoint(-0.095, -0.38), pya.DPoint(-0.095, -0.21), pya.DPoint(-0.265, -0.21), pya.DPoint(-0.265, -0.38)]))
cell_flatpmos1x0_3.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, -0.38), pya.DPoint(0.265, -0.38), pya.DPoint(0.265, -0.21), pya.DPoint(0.095, -0.21), pya.DPoint(0.095, -0.38)]))
cell_flatpmos1x0_3.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, 0.18), pya.DPoint(0.5, 0.18), pya.DPoint(0.5, 0.41), pya.DPoint(-0.5, 0.41), pya.DPoint(-0.5, 0.18)]))
cell_flatpmos1x0_3.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.41), pya.DPoint(0.5, -0.41), pya.DPoint(0.5, -0.18), pya.DPoint(-0.5, -0.18), pya.DPoint(-0.5, -0.41)]))

# === ToBiasStartup ===
cell_ToBiasStartup.insert(pya.DCellInstArray(
    cell_shortpmos_2x.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.9, 3.02))))
cell_ToBiasStartup.insert(pya.DCellInstArray(
    cell_shortnmos_2x.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.9, -0.21))))
cell_ToBiasStartup.insert(pya.DCellInstArray(
    cell_nmos_8x2.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(1.5, -19.86))))
cell_ToBiasStartup.insert(pya.DCellInstArray(
    cell_nmos_8x2.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(1.5, -10.78))))
cell_ToBiasStartup.insert(pya.DCellInstArray(
    cell_flatpmos1x0_3.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-2.86, 3.02))))
cell_ToBiasStartup.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, 2), pya.DPoint(2.35, 2), pya.DPoint(2.35, 4.46), pya.DPoint(-3.67, 4.46), pya.DPoint(-3.67, 2)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.49, 4.03), pya.DPoint(2.17, 4.03), pya.DPoint(2.17, 4.28), pya.DPoint(-3.49, 4.28), pya.DPoint(-3.49, 4.03)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.26, -1.13), pya.DPoint(2.06, -1.13), pya.DPoint(2.06, -0.92), pya.DPoint(-0.26, -0.92), pya.DPoint(-0.26, -1.13)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.56, -2.05), pya.DPoint(1.98, -2.05), pya.DPoint(1.98, -1.84), pya.DPoint(-1.56, -1.84), pya.DPoint(-1.56, -2.05)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.56, -10.92), pya.DPoint(-1.35, -10.92), pya.DPoint(-1.35, -2.05), pya.DPoint(-1.56, -2.05), pya.DPoint(-1.56, -10.92)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(1.77, -10.92), pya.DPoint(1.98, -10.92), pya.DPoint(1.98, -2.05), pya.DPoint(1.77, -2.05), pya.DPoint(1.77, -10.92)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.56, -11.13), pya.DPoint(1.98, -11.13), pya.DPoint(1.98, -10.92), pya.DPoint(-1.56, -10.92), pya.DPoint(-1.56, -11.13)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.56, -20), pya.DPoint(-1.35, -20), pya.DPoint(-1.35, -11.13), pya.DPoint(-1.56, -11.13), pya.DPoint(-1.56, -20)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(1.77, -20), pya.DPoint(1.98, -20), pya.DPoint(1.98, -11.13), pya.DPoint(1.77, -11.13), pya.DPoint(1.77, -20)]))
cell_ToBiasStartup.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.56, -20.21), pya.DPoint(1.98, -20.21), pya.DPoint(1.98, -20), pya.DPoint(-1.56, -20), pya.DPoint(-1.56, -20.21)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.385, -1.255), pya.DPoint(2.185, -1.255), pya.DPoint(2.185, -0.795), pya.DPoint(-0.385, -0.795), pya.DPoint(-0.385, -1.255)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.685, -2.175), pya.DPoint(2.105, -2.175), pya.DPoint(2.105, -1.715), pya.DPoint(-1.685, -1.715), pya.DPoint(-1.685, -2.175)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.685, -10.795), pya.DPoint(-1.225, -10.795), pya.DPoint(-1.225, -2.175), pya.DPoint(-1.685, -2.175), pya.DPoint(-1.685, -10.795)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(1.645, -10.795), pya.DPoint(2.105, -10.795), pya.DPoint(2.105, -2.175), pya.DPoint(1.645, -2.175), pya.DPoint(1.645, -10.795)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.685, -11.255), pya.DPoint(2.105, -11.255), pya.DPoint(2.105, -10.795), pya.DPoint(-1.685, -10.795), pya.DPoint(-1.685, -11.255)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.685, -19.875), pya.DPoint(-1.225, -19.875), pya.DPoint(-1.225, -11.255), pya.DPoint(-1.685, -11.255), pya.DPoint(-1.685, -19.875)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(1.645, -19.875), pya.DPoint(2.105, -19.875), pya.DPoint(2.105, -11.255), pya.DPoint(1.645, -11.255), pya.DPoint(1.645, -19.875)]))
cell_ToBiasStartup.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.685, -20.335), pya.DPoint(2.105, -20.335), pya.DPoint(2.105, -19.875), pya.DPoint(-1.685, -19.875), pya.DPoint(-1.685, -20.335)]))
cell_ToBiasStartup.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.615, 3.905), pya.DPoint(2.295, 3.905), pya.DPoint(2.295, 4.405), pya.DPoint(-3.615, 4.405), pya.DPoint(-3.615, 3.905)]))
cell_ToBiasStartup.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.36, 2.87), pya.DPoint(-1.32, 2.87), pya.DPoint(-1.32, 3.17), pya.DPoint(-2.36, 3.17), pya.DPoint(-2.36, 2.87)]))
cell_ToBiasStartup.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.82, 2.87), pya.DPoint(-0.24, 2.87), pya.DPoint(-0.24, 3.17), pya.DPoint(-0.82, 3.17), pya.DPoint(-0.82, 2.87)]))
cell_ToBiasStartup.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.28, -0.36), pya.DPoint(-0.24, -0.36), pya.DPoint(-0.24, -0.06), pya.DPoint(-1.28, -0.06), pya.DPoint(-1.28, -0.36)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.285, 4.07), pya.DPoint(-3.115, 4.07), pya.DPoint(-3.115, 4.24), pya.DPoint(-3.285, 4.24), pya.DPoint(-3.285, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.945, 4.07), pya.DPoint(-2.775, 4.07), pya.DPoint(-2.775, 4.24), pya.DPoint(-2.945, 4.24), pya.DPoint(-2.945, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.605, 4.07), pya.DPoint(-2.435, 4.07), pya.DPoint(-2.435, 4.24), pya.DPoint(-2.605, 4.24), pya.DPoint(-2.605, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.035, 4.07), pya.DPoint(0.135, 4.07), pya.DPoint(0.135, 4.24), pya.DPoint(-0.035, 4.24), pya.DPoint(-0.035, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.305, 4.07), pya.DPoint(0.475, 4.07), pya.DPoint(0.475, 4.24), pya.DPoint(0.305, 4.24), pya.DPoint(0.305, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.645, 4.07), pya.DPoint(0.815, 4.07), pya.DPoint(0.815, 4.24), pya.DPoint(0.645, 4.24), pya.DPoint(0.645, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.985, 4.07), pya.DPoint(1.155, 4.07), pya.DPoint(1.155, 4.24), pya.DPoint(0.985, 4.24), pya.DPoint(0.985, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.325, 4.07), pya.DPoint(1.495, 4.07), pya.DPoint(1.495, 4.24), pya.DPoint(1.325, 4.24), pya.DPoint(1.325, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.665, 4.07), pya.DPoint(1.835, 4.07), pya.DPoint(1.835, 4.24), pya.DPoint(1.665, 4.24), pya.DPoint(1.665, 4.07)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.615, 2.935), pya.DPoint(-1.445, 2.935), pya.DPoint(-1.445, 3.105), pya.DPoint(-1.615, 3.105), pya.DPoint(-1.615, 2.935)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.695, 2.935), pya.DPoint(-0.525, 2.935), pya.DPoint(-0.525, 3.105), pya.DPoint(-0.695, 3.105), pya.DPoint(-0.695, 2.935)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.155, -0.295), pya.DPoint(-0.985, -0.295), pya.DPoint(-0.985, -0.125), pya.DPoint(-1.155, -0.125), pya.DPoint(-1.155, -0.295)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.005, -1.11), pya.DPoint(0.165, -1.11), pya.DPoint(0.165, -0.94), pya.DPoint(-0.005, -0.94), pya.DPoint(-0.005, -1.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.335, -1.11), pya.DPoint(0.505, -1.11), pya.DPoint(0.505, -0.94), pya.DPoint(0.335, -0.94), pya.DPoint(0.335, -1.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.295, -1.11), pya.DPoint(1.465, -1.11), pya.DPoint(1.465, -0.94), pya.DPoint(1.295, -0.94), pya.DPoint(1.295, -1.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.635, -1.11), pya.DPoint(1.805, -1.11), pya.DPoint(1.805, -0.94), pya.DPoint(1.635, -0.94), pya.DPoint(1.635, -1.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.235, -2.03), pya.DPoint(-1.065, -2.03), pya.DPoint(-1.065, -1.86), pya.DPoint(-1.235, -1.86), pya.DPoint(-1.235, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.895, -2.03), pya.DPoint(-0.725, -2.03), pya.DPoint(-0.725, -1.86), pya.DPoint(-0.895, -1.86), pya.DPoint(-0.895, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.555, -2.03), pya.DPoint(-0.385, -2.03), pya.DPoint(-0.385, -1.86), pya.DPoint(-0.555, -1.86), pya.DPoint(-0.555, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.215, -2.03), pya.DPoint(-0.045, -2.03), pya.DPoint(-0.045, -1.86), pya.DPoint(-0.215, -1.86), pya.DPoint(-0.215, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.125, -2.03), pya.DPoint(0.295, -2.03), pya.DPoint(0.295, -1.86), pya.DPoint(0.125, -1.86), pya.DPoint(0.125, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.465, -2.03), pya.DPoint(0.635, -2.03), pya.DPoint(0.635, -1.86), pya.DPoint(0.465, -1.86), pya.DPoint(0.465, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.805, -2.03), pya.DPoint(0.975, -2.03), pya.DPoint(0.975, -1.86), pya.DPoint(0.805, -1.86), pya.DPoint(0.805, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.145, -2.03), pya.DPoint(1.315, -2.03), pya.DPoint(1.315, -1.86), pya.DPoint(1.145, -1.86), pya.DPoint(1.145, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.485, -2.03), pya.DPoint(1.655, -2.03), pya.DPoint(1.655, -1.86), pya.DPoint(1.485, -1.86), pya.DPoint(1.485, -2.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -2.49), pya.DPoint(-1.37, -2.49), pya.DPoint(-1.37, -2.32), pya.DPoint(-1.54, -2.32), pya.DPoint(-1.54, -2.49)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -2.49), pya.DPoint(1.96, -2.49), pya.DPoint(1.96, -2.32), pya.DPoint(1.79, -2.32), pya.DPoint(1.79, -2.49)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -2.83), pya.DPoint(-1.37, -2.83), pya.DPoint(-1.37, -2.66), pya.DPoint(-1.54, -2.66), pya.DPoint(-1.54, -2.83)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -2.83), pya.DPoint(1.96, -2.83), pya.DPoint(1.96, -2.66), pya.DPoint(1.79, -2.66), pya.DPoint(1.79, -2.83)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -3.17), pya.DPoint(-1.37, -3.17), pya.DPoint(-1.37, -3), pya.DPoint(-1.54, -3), pya.DPoint(-1.54, -3.17)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -3.17), pya.DPoint(1.96, -3.17), pya.DPoint(1.96, -3), pya.DPoint(1.79, -3), pya.DPoint(1.79, -3.17)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -3.51), pya.DPoint(-1.37, -3.51), pya.DPoint(-1.37, -3.34), pya.DPoint(-1.54, -3.34), pya.DPoint(-1.54, -3.51)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -3.51), pya.DPoint(1.96, -3.51), pya.DPoint(1.96, -3.34), pya.DPoint(1.79, -3.34), pya.DPoint(1.79, -3.51)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -3.85), pya.DPoint(-1.37, -3.85), pya.DPoint(-1.37, -3.68), pya.DPoint(-1.54, -3.68), pya.DPoint(-1.54, -3.85)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -3.85), pya.DPoint(1.96, -3.85), pya.DPoint(1.96, -3.68), pya.DPoint(1.79, -3.68), pya.DPoint(1.79, -3.85)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -4.19), pya.DPoint(-1.37, -4.19), pya.DPoint(-1.37, -4.02), pya.DPoint(-1.54, -4.02), pya.DPoint(-1.54, -4.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -4.19), pya.DPoint(1.96, -4.19), pya.DPoint(1.96, -4.02), pya.DPoint(1.79, -4.02), pya.DPoint(1.79, -4.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -4.53), pya.DPoint(-1.37, -4.53), pya.DPoint(-1.37, -4.36), pya.DPoint(-1.54, -4.36), pya.DPoint(-1.54, -4.53)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -4.53), pya.DPoint(1.96, -4.53), pya.DPoint(1.96, -4.36), pya.DPoint(1.79, -4.36), pya.DPoint(1.79, -4.53)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -4.87), pya.DPoint(-1.37, -4.87), pya.DPoint(-1.37, -4.7), pya.DPoint(-1.54, -4.7), pya.DPoint(-1.54, -4.87)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -4.87), pya.DPoint(1.96, -4.87), pya.DPoint(1.96, -4.7), pya.DPoint(1.79, -4.7), pya.DPoint(1.79, -4.87)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -5.21), pya.DPoint(-1.37, -5.21), pya.DPoint(-1.37, -5.04), pya.DPoint(-1.54, -5.04), pya.DPoint(-1.54, -5.21)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -5.21), pya.DPoint(1.96, -5.21), pya.DPoint(1.96, -5.04), pya.DPoint(1.79, -5.04), pya.DPoint(1.79, -5.21)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -5.55), pya.DPoint(-1.37, -5.55), pya.DPoint(-1.37, -5.38), pya.DPoint(-1.54, -5.38), pya.DPoint(-1.54, -5.55)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -5.55), pya.DPoint(1.96, -5.55), pya.DPoint(1.96, -5.38), pya.DPoint(1.79, -5.38), pya.DPoint(1.79, -5.55)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -5.89), pya.DPoint(-1.37, -5.89), pya.DPoint(-1.37, -5.72), pya.DPoint(-1.54, -5.72), pya.DPoint(-1.54, -5.89)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -5.89), pya.DPoint(1.96, -5.89), pya.DPoint(1.96, -5.72), pya.DPoint(1.79, -5.72), pya.DPoint(1.79, -5.89)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -6.23), pya.DPoint(-1.37, -6.23), pya.DPoint(-1.37, -6.06), pya.DPoint(-1.54, -6.06), pya.DPoint(-1.54, -6.23)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -6.23), pya.DPoint(1.96, -6.23), pya.DPoint(1.96, -6.06), pya.DPoint(1.79, -6.06), pya.DPoint(1.79, -6.23)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -6.57), pya.DPoint(-1.37, -6.57), pya.DPoint(-1.37, -6.4), pya.DPoint(-1.54, -6.4), pya.DPoint(-1.54, -6.57)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -6.57), pya.DPoint(1.96, -6.57), pya.DPoint(1.96, -6.4), pya.DPoint(1.79, -6.4), pya.DPoint(1.79, -6.57)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -6.91), pya.DPoint(-1.37, -6.91), pya.DPoint(-1.37, -6.74), pya.DPoint(-1.54, -6.74), pya.DPoint(-1.54, -6.91)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -6.91), pya.DPoint(1.96, -6.91), pya.DPoint(1.96, -6.74), pya.DPoint(1.79, -6.74), pya.DPoint(1.79, -6.91)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -7.25), pya.DPoint(-1.37, -7.25), pya.DPoint(-1.37, -7.08), pya.DPoint(-1.54, -7.08), pya.DPoint(-1.54, -7.25)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -7.25), pya.DPoint(1.96, -7.25), pya.DPoint(1.96, -7.08), pya.DPoint(1.79, -7.08), pya.DPoint(1.79, -7.25)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -7.59), pya.DPoint(-1.37, -7.59), pya.DPoint(-1.37, -7.42), pya.DPoint(-1.54, -7.42), pya.DPoint(-1.54, -7.59)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -7.59), pya.DPoint(1.96, -7.59), pya.DPoint(1.96, -7.42), pya.DPoint(1.79, -7.42), pya.DPoint(1.79, -7.59)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -7.93), pya.DPoint(-1.37, -7.93), pya.DPoint(-1.37, -7.76), pya.DPoint(-1.54, -7.76), pya.DPoint(-1.54, -7.93)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -7.93), pya.DPoint(1.96, -7.93), pya.DPoint(1.96, -7.76), pya.DPoint(1.79, -7.76), pya.DPoint(1.79, -7.93)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -8.27), pya.DPoint(-1.37, -8.27), pya.DPoint(-1.37, -8.1), pya.DPoint(-1.54, -8.1), pya.DPoint(-1.54, -8.27)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -8.27), pya.DPoint(1.96, -8.27), pya.DPoint(1.96, -8.1), pya.DPoint(1.79, -8.1), pya.DPoint(1.79, -8.27)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -8.61), pya.DPoint(-1.37, -8.61), pya.DPoint(-1.37, -8.44), pya.DPoint(-1.54, -8.44), pya.DPoint(-1.54, -8.61)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -8.61), pya.DPoint(1.96, -8.61), pya.DPoint(1.96, -8.44), pya.DPoint(1.79, -8.44), pya.DPoint(1.79, -8.61)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -8.95), pya.DPoint(-1.37, -8.95), pya.DPoint(-1.37, -8.78), pya.DPoint(-1.54, -8.78), pya.DPoint(-1.54, -8.95)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -8.95), pya.DPoint(1.96, -8.95), pya.DPoint(1.96, -8.78), pya.DPoint(1.79, -8.78), pya.DPoint(1.79, -8.95)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -9.29), pya.DPoint(-1.37, -9.29), pya.DPoint(-1.37, -9.12), pya.DPoint(-1.54, -9.12), pya.DPoint(-1.54, -9.29)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -9.29), pya.DPoint(1.96, -9.29), pya.DPoint(1.96, -9.12), pya.DPoint(1.79, -9.12), pya.DPoint(1.79, -9.29)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -9.63), pya.DPoint(-1.37, -9.63), pya.DPoint(-1.37, -9.46), pya.DPoint(-1.54, -9.46), pya.DPoint(-1.54, -9.63)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -9.63), pya.DPoint(1.96, -9.63), pya.DPoint(1.96, -9.46), pya.DPoint(1.79, -9.46), pya.DPoint(1.79, -9.63)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -9.97), pya.DPoint(-1.37, -9.97), pya.DPoint(-1.37, -9.8), pya.DPoint(-1.54, -9.8), pya.DPoint(-1.54, -9.97)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -9.97), pya.DPoint(1.96, -9.97), pya.DPoint(1.96, -9.8), pya.DPoint(1.79, -9.8), pya.DPoint(1.79, -9.97)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -10.31), pya.DPoint(-1.37, -10.31), pya.DPoint(-1.37, -10.14), pya.DPoint(-1.54, -10.14), pya.DPoint(-1.54, -10.31)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -10.31), pya.DPoint(1.96, -10.31), pya.DPoint(1.96, -10.14), pya.DPoint(1.79, -10.14), pya.DPoint(1.79, -10.31)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -10.65), pya.DPoint(-1.37, -10.65), pya.DPoint(-1.37, -10.48), pya.DPoint(-1.54, -10.48), pya.DPoint(-1.54, -10.65)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -10.65), pya.DPoint(1.96, -10.65), pya.DPoint(1.96, -10.48), pya.DPoint(1.79, -10.48), pya.DPoint(1.79, -10.65)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.235, -11.11), pya.DPoint(-1.065, -11.11), pya.DPoint(-1.065, -10.94), pya.DPoint(-1.235, -10.94), pya.DPoint(-1.235, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.895, -11.11), pya.DPoint(-0.725, -11.11), pya.DPoint(-0.725, -10.94), pya.DPoint(-0.895, -10.94), pya.DPoint(-0.895, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.555, -11.11), pya.DPoint(-0.385, -11.11), pya.DPoint(-0.385, -10.94), pya.DPoint(-0.555, -10.94), pya.DPoint(-0.555, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.215, -11.11), pya.DPoint(-0.045, -11.11), pya.DPoint(-0.045, -10.94), pya.DPoint(-0.215, -10.94), pya.DPoint(-0.215, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.125, -11.11), pya.DPoint(0.295, -11.11), pya.DPoint(0.295, -10.94), pya.DPoint(0.125, -10.94), pya.DPoint(0.125, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.465, -11.11), pya.DPoint(0.635, -11.11), pya.DPoint(0.635, -10.94), pya.DPoint(0.465, -10.94), pya.DPoint(0.465, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.805, -11.11), pya.DPoint(0.975, -11.11), pya.DPoint(0.975, -10.94), pya.DPoint(0.805, -10.94), pya.DPoint(0.805, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.145, -11.11), pya.DPoint(1.315, -11.11), pya.DPoint(1.315, -10.94), pya.DPoint(1.145, -10.94), pya.DPoint(1.145, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.485, -11.11), pya.DPoint(1.655, -11.11), pya.DPoint(1.655, -10.94), pya.DPoint(1.485, -10.94), pya.DPoint(1.485, -11.11)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -11.57), pya.DPoint(-1.37, -11.57), pya.DPoint(-1.37, -11.4), pya.DPoint(-1.54, -11.4), pya.DPoint(-1.54, -11.57)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -11.57), pya.DPoint(1.96, -11.57), pya.DPoint(1.96, -11.4), pya.DPoint(1.79, -11.4), pya.DPoint(1.79, -11.57)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -11.91), pya.DPoint(-1.37, -11.91), pya.DPoint(-1.37, -11.74), pya.DPoint(-1.54, -11.74), pya.DPoint(-1.54, -11.91)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -11.91), pya.DPoint(1.96, -11.91), pya.DPoint(1.96, -11.74), pya.DPoint(1.79, -11.74), pya.DPoint(1.79, -11.91)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -12.25), pya.DPoint(-1.37, -12.25), pya.DPoint(-1.37, -12.08), pya.DPoint(-1.54, -12.08), pya.DPoint(-1.54, -12.25)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -12.25), pya.DPoint(1.96, -12.25), pya.DPoint(1.96, -12.08), pya.DPoint(1.79, -12.08), pya.DPoint(1.79, -12.25)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -12.59), pya.DPoint(-1.37, -12.59), pya.DPoint(-1.37, -12.42), pya.DPoint(-1.54, -12.42), pya.DPoint(-1.54, -12.59)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -12.59), pya.DPoint(1.96, -12.59), pya.DPoint(1.96, -12.42), pya.DPoint(1.79, -12.42), pya.DPoint(1.79, -12.59)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -12.93), pya.DPoint(-1.37, -12.93), pya.DPoint(-1.37, -12.76), pya.DPoint(-1.54, -12.76), pya.DPoint(-1.54, -12.93)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -12.93), pya.DPoint(1.96, -12.93), pya.DPoint(1.96, -12.76), pya.DPoint(1.79, -12.76), pya.DPoint(1.79, -12.93)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -13.27), pya.DPoint(-1.37, -13.27), pya.DPoint(-1.37, -13.1), pya.DPoint(-1.54, -13.1), pya.DPoint(-1.54, -13.27)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -13.27), pya.DPoint(1.96, -13.27), pya.DPoint(1.96, -13.1), pya.DPoint(1.79, -13.1), pya.DPoint(1.79, -13.27)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -13.61), pya.DPoint(-1.37, -13.61), pya.DPoint(-1.37, -13.44), pya.DPoint(-1.54, -13.44), pya.DPoint(-1.54, -13.61)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -13.61), pya.DPoint(1.96, -13.61), pya.DPoint(1.96, -13.44), pya.DPoint(1.79, -13.44), pya.DPoint(1.79, -13.61)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -13.95), pya.DPoint(-1.37, -13.95), pya.DPoint(-1.37, -13.78), pya.DPoint(-1.54, -13.78), pya.DPoint(-1.54, -13.95)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -13.95), pya.DPoint(1.96, -13.95), pya.DPoint(1.96, -13.78), pya.DPoint(1.79, -13.78), pya.DPoint(1.79, -13.95)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -14.29), pya.DPoint(-1.37, -14.29), pya.DPoint(-1.37, -14.12), pya.DPoint(-1.54, -14.12), pya.DPoint(-1.54, -14.29)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -14.29), pya.DPoint(1.96, -14.29), pya.DPoint(1.96, -14.12), pya.DPoint(1.79, -14.12), pya.DPoint(1.79, -14.29)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -14.63), pya.DPoint(-1.37, -14.63), pya.DPoint(-1.37, -14.46), pya.DPoint(-1.54, -14.46), pya.DPoint(-1.54, -14.63)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -14.63), pya.DPoint(1.96, -14.63), pya.DPoint(1.96, -14.46), pya.DPoint(1.79, -14.46), pya.DPoint(1.79, -14.63)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -14.97), pya.DPoint(-1.37, -14.97), pya.DPoint(-1.37, -14.8), pya.DPoint(-1.54, -14.8), pya.DPoint(-1.54, -14.97)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -14.97), pya.DPoint(1.96, -14.97), pya.DPoint(1.96, -14.8), pya.DPoint(1.79, -14.8), pya.DPoint(1.79, -14.97)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -15.31), pya.DPoint(-1.37, -15.31), pya.DPoint(-1.37, -15.14), pya.DPoint(-1.54, -15.14), pya.DPoint(-1.54, -15.31)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -15.31), pya.DPoint(1.96, -15.31), pya.DPoint(1.96, -15.14), pya.DPoint(1.79, -15.14), pya.DPoint(1.79, -15.31)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -15.65), pya.DPoint(-1.37, -15.65), pya.DPoint(-1.37, -15.48), pya.DPoint(-1.54, -15.48), pya.DPoint(-1.54, -15.65)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -15.65), pya.DPoint(1.96, -15.65), pya.DPoint(1.96, -15.48), pya.DPoint(1.79, -15.48), pya.DPoint(1.79, -15.65)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -15.99), pya.DPoint(-1.37, -15.99), pya.DPoint(-1.37, -15.82), pya.DPoint(-1.54, -15.82), pya.DPoint(-1.54, -15.99)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -15.99), pya.DPoint(1.96, -15.99), pya.DPoint(1.96, -15.82), pya.DPoint(1.79, -15.82), pya.DPoint(1.79, -15.99)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -16.33), pya.DPoint(-1.37, -16.33), pya.DPoint(-1.37, -16.16), pya.DPoint(-1.54, -16.16), pya.DPoint(-1.54, -16.33)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -16.33), pya.DPoint(1.96, -16.33), pya.DPoint(1.96, -16.16), pya.DPoint(1.79, -16.16), pya.DPoint(1.79, -16.33)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -16.67), pya.DPoint(-1.37, -16.67), pya.DPoint(-1.37, -16.5), pya.DPoint(-1.54, -16.5), pya.DPoint(-1.54, -16.67)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -16.67), pya.DPoint(1.96, -16.67), pya.DPoint(1.96, -16.5), pya.DPoint(1.79, -16.5), pya.DPoint(1.79, -16.67)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -17.01), pya.DPoint(-1.37, -17.01), pya.DPoint(-1.37, -16.84), pya.DPoint(-1.54, -16.84), pya.DPoint(-1.54, -17.01)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -17.01), pya.DPoint(1.96, -17.01), pya.DPoint(1.96, -16.84), pya.DPoint(1.79, -16.84), pya.DPoint(1.79, -17.01)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -17.35), pya.DPoint(-1.37, -17.35), pya.DPoint(-1.37, -17.18), pya.DPoint(-1.54, -17.18), pya.DPoint(-1.54, -17.35)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -17.35), pya.DPoint(1.96, -17.35), pya.DPoint(1.96, -17.18), pya.DPoint(1.79, -17.18), pya.DPoint(1.79, -17.35)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -17.69), pya.DPoint(-1.37, -17.69), pya.DPoint(-1.37, -17.52), pya.DPoint(-1.54, -17.52), pya.DPoint(-1.54, -17.69)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -17.69), pya.DPoint(1.96, -17.69), pya.DPoint(1.96, -17.52), pya.DPoint(1.79, -17.52), pya.DPoint(1.79, -17.69)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -18.03), pya.DPoint(-1.37, -18.03), pya.DPoint(-1.37, -17.86), pya.DPoint(-1.54, -17.86), pya.DPoint(-1.54, -18.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -18.03), pya.DPoint(1.96, -18.03), pya.DPoint(1.96, -17.86), pya.DPoint(1.79, -17.86), pya.DPoint(1.79, -18.03)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -18.37), pya.DPoint(-1.37, -18.37), pya.DPoint(-1.37, -18.2), pya.DPoint(-1.54, -18.2), pya.DPoint(-1.54, -18.37)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -18.37), pya.DPoint(1.96, -18.37), pya.DPoint(1.96, -18.2), pya.DPoint(1.79, -18.2), pya.DPoint(1.79, -18.37)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -18.71), pya.DPoint(-1.37, -18.71), pya.DPoint(-1.37, -18.54), pya.DPoint(-1.54, -18.54), pya.DPoint(-1.54, -18.71)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -18.71), pya.DPoint(1.96, -18.71), pya.DPoint(1.96, -18.54), pya.DPoint(1.79, -18.54), pya.DPoint(1.79, -18.71)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -19.05), pya.DPoint(-1.37, -19.05), pya.DPoint(-1.37, -18.88), pya.DPoint(-1.54, -18.88), pya.DPoint(-1.54, -19.05)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -19.05), pya.DPoint(1.96, -19.05), pya.DPoint(1.96, -18.88), pya.DPoint(1.79, -18.88), pya.DPoint(1.79, -19.05)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -19.39), pya.DPoint(-1.37, -19.39), pya.DPoint(-1.37, -19.22), pya.DPoint(-1.54, -19.22), pya.DPoint(-1.54, -19.39)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -19.39), pya.DPoint(1.96, -19.39), pya.DPoint(1.96, -19.22), pya.DPoint(1.79, -19.22), pya.DPoint(1.79, -19.39)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -19.73), pya.DPoint(-1.37, -19.73), pya.DPoint(-1.37, -19.56), pya.DPoint(-1.54, -19.56), pya.DPoint(-1.54, -19.73)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -19.73), pya.DPoint(1.96, -19.73), pya.DPoint(1.96, -19.56), pya.DPoint(1.79, -19.56), pya.DPoint(1.79, -19.73)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.235, -20.19), pya.DPoint(-1.065, -20.19), pya.DPoint(-1.065, -20.02), pya.DPoint(-1.235, -20.02), pya.DPoint(-1.235, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.895, -20.19), pya.DPoint(-0.725, -20.19), pya.DPoint(-0.725, -20.02), pya.DPoint(-0.895, -20.02), pya.DPoint(-0.895, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.555, -20.19), pya.DPoint(-0.385, -20.19), pya.DPoint(-0.385, -20.02), pya.DPoint(-0.555, -20.02), pya.DPoint(-0.555, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.215, -20.19), pya.DPoint(-0.045, -20.19), pya.DPoint(-0.045, -20.02), pya.DPoint(-0.215, -20.02), pya.DPoint(-0.215, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.125, -20.19), pya.DPoint(0.295, -20.19), pya.DPoint(0.295, -20.02), pya.DPoint(0.125, -20.02), pya.DPoint(0.125, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.465, -20.19), pya.DPoint(0.635, -20.19), pya.DPoint(0.635, -20.02), pya.DPoint(0.465, -20.02), pya.DPoint(0.465, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.805, -20.19), pya.DPoint(0.975, -20.19), pya.DPoint(0.975, -20.02), pya.DPoint(0.805, -20.02), pya.DPoint(0.805, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.145, -20.19), pya.DPoint(1.315, -20.19), pya.DPoint(1.315, -20.02), pya.DPoint(1.145, -20.02), pya.DPoint(1.145, -20.19)]))
cell_ToBiasStartup.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.485, -20.19), pya.DPoint(1.655, -20.19), pya.DPoint(1.655, -20.02), pya.DPoint(1.485, -20.02), pya.DPoint(1.485, -20.19)]))
cell_ToBiasStartup.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.715, 2.835), pya.DPoint(-1.345, 2.835), pya.DPoint(-1.345, 3.205), pya.DPoint(-1.715, 3.205), pya.DPoint(-1.715, 2.835)]))
cell_ToBiasStartup.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.795, 2.835), pya.DPoint(-0.425, 2.835), pya.DPoint(-0.425, 3.205), pya.DPoint(-0.795, 3.205), pya.DPoint(-0.795, 2.835)]))
cell_ToBiasStartup.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.255, -0.395), pya.DPoint(-0.885, -0.395), pya.DPoint(-0.885, -0.025), pya.DPoint(-1.255, -0.025), pya.DPoint(-1.255, -0.395)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.38, 4.07), pya.DPoint(-2.34, 4.07), pya.DPoint(-2.34, 4.24), pya.DPoint(-3.38, 4.24), pya.DPoint(-3.38, 4.07)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.26, 4.07), pya.DPoint(2.06, 4.07), pya.DPoint(2.06, 4.24), pya.DPoint(-0.26, 4.24), pya.DPoint(-0.26, 4.07)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.66, 2.84), pya.DPoint(-1.4, 2.84), pya.DPoint(-1.4, 3.2), pya.DPoint(-1.66, 3.2), pya.DPoint(-1.66, 2.84)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.74, 2.84), pya.DPoint(-0.48, 2.84), pya.DPoint(-0.48, 3.2), pya.DPoint(-0.74, 3.2), pya.DPoint(-0.74, 2.84)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.2, -0.39), pya.DPoint(-0.94, -0.39), pya.DPoint(-0.94, -0.03), pya.DPoint(-1.2, -0.03), pya.DPoint(-1.2, -0.39)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.26, -1.11), pya.DPoint(2.06, -1.11), pya.DPoint(2.06, -0.94), pya.DPoint(-0.26, -0.94), pya.DPoint(-0.26, -1.11)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -2.03), pya.DPoint(1.96, -2.03), pya.DPoint(1.96, -1.86), pya.DPoint(-1.54, -1.86), pya.DPoint(-1.54, -2.03)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -10.94), pya.DPoint(-1.37, -10.94), pya.DPoint(-1.37, -2.03), pya.DPoint(-1.54, -2.03), pya.DPoint(-1.54, -10.94)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.02, -10.67), pya.DPoint(1.44, -10.67), pya.DPoint(1.44, -2.63), pya.DPoint(-1.02, -2.63), pya.DPoint(-1.02, -10.67)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -10.94), pya.DPoint(1.96, -10.94), pya.DPoint(1.96, -2.03), pya.DPoint(1.79, -2.03), pya.DPoint(1.79, -10.94)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -11.11), pya.DPoint(1.96, -11.11), pya.DPoint(1.96, -10.94), pya.DPoint(-1.54, -10.94), pya.DPoint(-1.54, -11.11)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -20.02), pya.DPoint(-1.37, -20.02), pya.DPoint(-1.37, -11.11), pya.DPoint(-1.54, -11.11), pya.DPoint(-1.54, -20.02)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.03, -19.75), pya.DPoint(1.43, -19.75), pya.DPoint(1.43, -11.71), pya.DPoint(-1.03, -11.71), pya.DPoint(-1.03, -19.75)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.79, -20.02), pya.DPoint(1.96, -20.02), pya.DPoint(1.96, -11.11), pya.DPoint(1.79, -11.11), pya.DPoint(1.79, -20.02)]))
cell_ToBiasStartup.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.54, -20.19), pya.DPoint(1.96, -20.19), pya.DPoint(1.96, -20.02), pya.DPoint(-1.54, -20.02), pya.DPoint(-1.54, -20.19)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.125, 4.07), pya.DPoint(-2.955, 4.07), pya.DPoint(-2.955, 4.24), pya.DPoint(-3.125, 4.24), pya.DPoint(-3.125, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.765, 4.07), pya.DPoint(-2.595, 4.07), pya.DPoint(-2.595, 4.24), pya.DPoint(-2.765, 4.24), pya.DPoint(-2.765, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.005, 4.07), pya.DPoint(0.165, 4.07), pya.DPoint(0.165, 4.24), pya.DPoint(-0.005, 4.24), pya.DPoint(-0.005, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.355, 4.07), pya.DPoint(0.525, 4.07), pya.DPoint(0.525, 4.24), pya.DPoint(0.355, 4.24), pya.DPoint(0.355, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.275, 4.07), pya.DPoint(1.445, 4.07), pya.DPoint(1.445, 4.24), pya.DPoint(1.275, 4.24), pya.DPoint(1.275, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.635, 4.07), pya.DPoint(1.805, 4.07), pya.DPoint(1.805, 4.24), pya.DPoint(1.635, 4.24), pya.DPoint(1.635, 4.07)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.615, 2.935), pya.DPoint(-1.445, 2.935), pya.DPoint(-1.445, 3.105), pya.DPoint(-1.615, 3.105), pya.DPoint(-1.615, 2.935)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.695, 2.935), pya.DPoint(-0.525, 2.935), pya.DPoint(-0.525, 3.105), pya.DPoint(-0.695, 3.105), pya.DPoint(-0.695, 2.935)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.155, -0.295), pya.DPoint(-0.985, -0.295), pya.DPoint(-0.985, -0.125), pya.DPoint(-1.155, -0.125), pya.DPoint(-1.155, -0.295)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.015, -1.11), pya.DPoint(0.155, -1.11), pya.DPoint(0.155, -0.94), pya.DPoint(-0.015, -0.94), pya.DPoint(-0.015, -1.11)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.345, -1.11), pya.DPoint(0.515, -1.11), pya.DPoint(0.515, -0.94), pya.DPoint(0.345, -0.94), pya.DPoint(0.345, -1.11)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.285, -1.11), pya.DPoint(1.455, -1.11), pya.DPoint(1.455, -0.94), pya.DPoint(1.285, -0.94), pya.DPoint(1.285, -1.11)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.645, -1.11), pya.DPoint(1.815, -1.11), pya.DPoint(1.815, -0.94), pya.DPoint(1.645, -0.94), pya.DPoint(1.645, -1.11)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.005, -2.03), pya.DPoint(0.165, -2.03), pya.DPoint(0.165, -1.86), pya.DPoint(-0.005, -1.86), pya.DPoint(-0.005, -2.03)]))
cell_ToBiasStartup.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.355, -2.03), pya.DPoint(0.525, -2.03), pya.DPoint(0.525, -1.86), pya.DPoint(0.355, -1.86), pya.DPoint(0.355, -2.03)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.36, 3.2), pya.DPoint(-2.36, 3.2), pya.DPoint(-2.36, 4.28), pya.DPoint(-3.36, 4.28), pya.DPoint(-3.36, 3.2)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.68, 2.21), pya.DPoint(-2.36, 2.21), pya.DPoint(-2.36, 2.84), pya.DPoint(-2.68, 2.84), pya.DPoint(-2.68, 2.21)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.15, -11.73), pya.DPoint(-1.83, -11.73), pya.DPoint(-1.83, 4.14), pya.DPoint(-2.15, 4.14), pya.DPoint(-2.15, -11.73)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.24, 4.03), pya.DPoint(2.04, 4.03), pya.DPoint(2.04, 4.28), pya.DPoint(-0.24, 4.28), pya.DPoint(-0.24, 4.03)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.24, 3.2), pya.DPoint(0.76, 3.2), pya.DPoint(0.76, 4.03), pya.DPoint(-0.24, 4.03), pya.DPoint(-0.24, 3.2)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.04, 3.2), pya.DPoint(2.04, 3.2), pya.DPoint(2.04, 4.03), pya.DPoint(1.04, 4.03), pya.DPoint(1.04, 3.2)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.69, -11.34), pya.DPoint(-1.37, -11.34), pya.DPoint(-1.37, 3.18), pya.DPoint(-1.69, 3.18), pya.DPoint(-1.69, -11.34)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.65), pya.DPoint(-0.91, -2.65), pya.DPoint(-0.91, 0.87), pya.DPoint(-1.23, 0.87), pya.DPoint(-1.23, -2.65)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.77, -2.49), pya.DPoint(-0.45, -2.49), pya.DPoint(-0.45, 3.18), pya.DPoint(-0.77, 3.18), pya.DPoint(-0.77, -2.49)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.46, 0), pya.DPoint(0.76, 0), pya.DPoint(0.76, 2.81), pya.DPoint(0.46, 2.81), pya.DPoint(0.46, 0)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.74, 0), pya.DPoint(2.04, 0), pya.DPoint(2.04, 2.81), pya.DPoint(1.74, 2.81), pya.DPoint(1.74, 0)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.24, -2.06), pya.DPoint(0.76, -2.06), pya.DPoint(0.76, -0.39), pya.DPoint(-0.24, -0.39), pya.DPoint(-0.24, -2.06)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.04, -1.42), pya.DPoint(2.04, -1.42), pya.DPoint(2.04, -0.39), pya.DPoint(1.04, -0.39), pya.DPoint(1.04, -1.42)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -2.88), pya.DPoint(1.47, -2.88), pya.DPoint(1.47, -2.65), pya.DPoint(-1.23, -2.65), pya.DPoint(-1.23, -2.88)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -10.42), pya.DPoint(-0.91, -10.42), pya.DPoint(-0.91, -2.88), pya.DPoint(-1.23, -2.88), pya.DPoint(-1.23, -10.42)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -10.65), pya.DPoint(1.47, -10.65), pya.DPoint(1.47, -10.42), pya.DPoint(-1.23, -10.42), pya.DPoint(-1.23, -10.65)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.69, -11.57), pya.DPoint(1.19, -11.57), pya.DPoint(1.19, -11.34), pya.DPoint(-1.69, -11.34), pya.DPoint(-1.69, -11.57)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.15, -11.96), pya.DPoint(1.47, -11.96), pya.DPoint(1.47, -11.73), pya.DPoint(-2.15, -11.73), pya.DPoint(-2.15, -11.96)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -19.5), pya.DPoint(-0.91, -19.5), pya.DPoint(-0.91, -11.96), pya.DPoint(-1.23, -11.96), pya.DPoint(-1.23, -19.5)]))
cell_ToBiasStartup.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, -19.73), pya.DPoint(1.47, -19.73), pya.DPoint(1.47, -19.5), pya.DPoint(-1.23, -19.5), pya.DPoint(-1.23, -19.73)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.255, 3.925), pya.DPoint(-3.105, 3.925), pya.DPoint(-3.105, 4.075), pya.DPoint(-3.255, 4.075), pya.DPoint(-3.255, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.935, 3.925), pya.DPoint(-2.785, 3.925), pya.DPoint(-2.785, 4.075), pya.DPoint(-2.935, 4.075), pya.DPoint(-2.935, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.615, 3.925), pya.DPoint(-2.465, 3.925), pya.DPoint(-2.465, 4.075), pya.DPoint(-2.615, 4.075), pya.DPoint(-2.615, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.065, 3.925), pya.DPoint(-1.915, 3.925), pya.DPoint(-1.915, 4.075), pya.DPoint(-2.065, 4.075), pya.DPoint(-2.065, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.135, 3.925), pya.DPoint(0.015, 3.925), pya.DPoint(0.015, 4.075), pya.DPoint(-0.135, 4.075), pya.DPoint(-0.135, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.185, 3.925), pya.DPoint(0.335, 3.925), pya.DPoint(0.335, 4.075), pya.DPoint(0.185, 4.075), pya.DPoint(0.185, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.505, 3.925), pya.DPoint(0.655, 3.925), pya.DPoint(0.655, 4.075), pya.DPoint(0.505, 4.075), pya.DPoint(0.505, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.145, 3.925), pya.DPoint(1.295, 3.925), pya.DPoint(1.295, 4.075), pya.DPoint(1.145, 4.075), pya.DPoint(1.145, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.465, 3.925), pya.DPoint(1.615, 3.925), pya.DPoint(1.615, 4.075), pya.DPoint(1.465, 4.075), pya.DPoint(1.465, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.785, 3.925), pya.DPoint(1.935, 3.925), pya.DPoint(1.935, 4.075), pya.DPoint(1.785, 4.075), pya.DPoint(1.785, 3.925)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.595, 2.265), pya.DPoint(-2.445, 2.265), pya.DPoint(-2.445, 2.415), pya.DPoint(-2.595, 2.415), pya.DPoint(-2.595, 2.265)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.685, 2.265), pya.DPoint(-0.535, 2.265), pya.DPoint(-0.535, 2.415), pya.DPoint(-0.685, 2.415), pya.DPoint(-0.685, 2.265)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.605, 1.865), pya.DPoint(-1.455, 1.865), pya.DPoint(-1.455, 2.015), pya.DPoint(-1.605, 2.015), pya.DPoint(-1.605, 1.865)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.815, 1.465), pya.DPoint(1.965, 1.465), pya.DPoint(1.965, 1.615), pya.DPoint(1.815, 1.615), pya.DPoint(1.815, 1.465)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.535, 1.065), pya.DPoint(0.685, 1.065), pya.DPoint(0.685, 1.215), pya.DPoint(0.535, 1.215), pya.DPoint(0.535, 1.065)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.145, 0.665), pya.DPoint(-0.995, 0.665), pya.DPoint(-0.995, 0.815), pya.DPoint(-1.145, 0.815), pya.DPoint(-1.145, 0.665)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.135, -1.365), pya.DPoint(0.015, -1.365), pya.DPoint(0.015, -1.215), pya.DPoint(-0.135, -1.215), pya.DPoint(-0.135, -1.365)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.185, -1.365), pya.DPoint(0.335, -1.365), pya.DPoint(0.335, -1.215), pya.DPoint(0.185, -1.215), pya.DPoint(0.185, -1.365)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.505, -1.365), pya.DPoint(0.655, -1.365), pya.DPoint(0.655, -1.215), pya.DPoint(0.505, -1.215), pya.DPoint(0.505, -1.365)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.145, -1.365), pya.DPoint(1.295, -1.365), pya.DPoint(1.295, -1.215), pya.DPoint(1.145, -1.215), pya.DPoint(1.145, -1.365)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.465, -1.365), pya.DPoint(1.615, -1.365), pya.DPoint(1.615, -1.215), pya.DPoint(1.465, -1.215), pya.DPoint(1.465, -1.365)]))
cell_ToBiasStartup.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.785, -1.365), pya.DPoint(1.935, -1.365), pya.DPoint(1.935, -1.215), pya.DPoint(1.785, -1.215), pya.DPoint(1.785, -1.365)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, 3.87), pya.DPoint(2.35, 3.87), pya.DPoint(2.35, 4.13), pya.DPoint(-3.67, 4.13), pya.DPoint(-3.67, 3.87)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.68, 2.21), pya.DPoint(-0.45, 2.21), pya.DPoint(-0.45, 2.47), pya.DPoint(-2.68, 2.47), pya.DPoint(-2.68, 2.21)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.81), pya.DPoint(2.35, 1.81), pya.DPoint(2.35, 2.07), pya.DPoint(-3.67, 2.07), pya.DPoint(-3.67, 1.81)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.41), pya.DPoint(2.35, 1.41), pya.DPoint(2.35, 1.67), pya.DPoint(-3.67, 1.67), pya.DPoint(-3.67, 1.41)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.01), pya.DPoint(2.35, 1.01), pya.DPoint(2.35, 1.27), pya.DPoint(-3.67, 1.27), pya.DPoint(-3.67, 1.01)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.23, 0.61), pya.DPoint(2.35, 0.61), pya.DPoint(2.35, 0.87), pya.DPoint(-1.23, 0.87), pya.DPoint(-1.23, 0.61)]))
cell_ToBiasStartup.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.67, -1.42), pya.DPoint(2.35, -1.42), pya.DPoint(2.35, -1.16), pya.DPoint(-3.67, -1.16), pya.DPoint(-3.67, -1.42)]))
_txt = pya.Text("vss",
               pya.Trans(0, False, pya.Vector(-3535, -1290)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-3.67, -1.42), pya.DPoint(-3.4, -1.42), pya.DPoint(-3.4, -1.16), pya.DPoint(-3.67, -1.16), pya.DPoint(-3.67, -1.42)]))
_txt = pya.Text("vdd",
               pya.Trans(0, False, pya.Vector(-3535, 4000)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-3.67, 3.87), pya.DPoint(-3.4, 3.87), pya.DPoint(-3.4, 4.13), pya.DPoint(-3.67, 4.13), pya.DPoint(-3.67, 3.87)]))
_txt = pya.Text("vbp",
               pya.Trans(0, False, pya.Vector(-3535, 1940)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.81), pya.DPoint(-3.4, 1.81), pya.DPoint(-3.4, 2.07), pya.DPoint(-3.67, 2.07), pya.DPoint(-3.67, 1.81)]))
_txt = pya.Text("vbn",
               pya.Trans(0, False, pya.Vector(-3535, 1540)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.41), pya.DPoint(-3.4, 1.41), pya.DPoint(-3.4, 1.67), pya.DPoint(-3.67, 1.67), pya.DPoint(-3.67, 1.41)]))
_txt = pya.Text("vbr",
               pya.Trans(0, False, pya.Vector(-3535, 1140)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-3.67, 1.01), pya.DPoint(-3.4, 1.01), pya.DPoint(-3.4, 1.27), pya.DPoint(-3.67, 1.27), pya.DPoint(-3.67, 1.01)]))
_txt = pya.Text("disable",
               pya.Trans(0, False, pya.Vector(2215, 740)))
_txt.halign = 1
_txt.valign = 1
cell_ToBiasStartup.shapes(L_met2_pin).insert(_txt)
cell_ToBiasStartup.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(2.08, 0.61), pya.DPoint(2.35, 0.61), pya.DPoint(2.35, 0.87), pya.DPoint(2.08, 0.87), pya.DPoint(2.08, 0.61)]))

# === nmos1x20_8x ===
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, -10.29), pya.DPoint(-3.31, -10.29), pya.DPoint(-3.31, 10.29), pya.DPoint(-4.31, 10.29), pya.DPoint(-4.31, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -10.29), pya.DPoint(-2.04, -10.29), pya.DPoint(-2.04, 10.29), pya.DPoint(-3.04, 10.29), pya.DPoint(-3.04, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -10.29), pya.DPoint(-0.77, -10.29), pya.DPoint(-0.77, 10.29), pya.DPoint(-1.77, 10.29), pya.DPoint(-1.77, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -10.29), pya.DPoint(0.5, -10.29), pya.DPoint(0.5, 10.29), pya.DPoint(-0.5, 10.29), pya.DPoint(-0.5, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -10.29), pya.DPoint(1.77, -10.29), pya.DPoint(1.77, 10.29), pya.DPoint(0.77, 10.29), pya.DPoint(0.77, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -10.29), pya.DPoint(3.04, -10.29), pya.DPoint(3.04, 10.29), pya.DPoint(2.04, 10.29), pya.DPoint(2.04, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, -10.29), pya.DPoint(4.31, -10.29), pya.DPoint(4.31, 10.29), pya.DPoint(3.31, 10.29), pya.DPoint(3.31, -10.29)]))
cell_nmos1x20_8x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(4.58, -10.29), pya.DPoint(5.58, -10.29), pya.DPoint(5.58, 10.29), pya.DPoint(4.58, 10.29), pya.DPoint(4.58, -10.29)]))
cell_nmos1x20_8x.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.435, -10.415), pya.DPoint(5.705, -10.415), pya.DPoint(5.705, 10.415), pya.DPoint(-4.435, 10.415), pya.DPoint(-4.435, -10.415)]))
cell_nmos1x20_8x.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.75, -10), pya.DPoint(6.03, -10), pya.DPoint(6.03, 10), pya.DPoint(-4.75, 10), pya.DPoint(-4.75, -10)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.235, 10.06), pya.DPoint(-4.065, 10.06), pya.DPoint(-4.065, 10.23), pya.DPoint(-4.235, 10.23), pya.DPoint(-4.235, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.895, 10.06), pya.DPoint(-3.725, 10.06), pya.DPoint(-3.725, 10.23), pya.DPoint(-3.895, 10.23), pya.DPoint(-3.895, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.555, 10.06), pya.DPoint(-3.385, 10.06), pya.DPoint(-3.385, 10.23), pya.DPoint(-3.555, 10.23), pya.DPoint(-3.555, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, 10.06), pya.DPoint(-2.795, 10.06), pya.DPoint(-2.795, 10.23), pya.DPoint(-2.965, 10.23), pya.DPoint(-2.965, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, 10.06), pya.DPoint(-2.455, 10.06), pya.DPoint(-2.455, 10.23), pya.DPoint(-2.625, 10.23), pya.DPoint(-2.625, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, 10.06), pya.DPoint(-2.115, 10.06), pya.DPoint(-2.115, 10.23), pya.DPoint(-2.285, 10.23), pya.DPoint(-2.285, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, 10.06), pya.DPoint(-1.525, 10.06), pya.DPoint(-1.525, 10.23), pya.DPoint(-1.695, 10.23), pya.DPoint(-1.695, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, 10.06), pya.DPoint(-1.185, 10.06), pya.DPoint(-1.185, 10.23), pya.DPoint(-1.355, 10.23), pya.DPoint(-1.355, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, 10.06), pya.DPoint(-0.845, 10.06), pya.DPoint(-0.845, 10.23), pya.DPoint(-1.015, 10.23), pya.DPoint(-1.015, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, 10.06), pya.DPoint(-0.255, 10.06), pya.DPoint(-0.255, 10.23), pya.DPoint(-0.425, 10.23), pya.DPoint(-0.425, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 10.06), pya.DPoint(0.085, 10.06), pya.DPoint(0.085, 10.23), pya.DPoint(-0.085, 10.23), pya.DPoint(-0.085, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, 10.06), pya.DPoint(0.425, 10.06), pya.DPoint(0.425, 10.23), pya.DPoint(0.255, 10.23), pya.DPoint(0.255, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, 10.06), pya.DPoint(1.015, 10.06), pya.DPoint(1.015, 10.23), pya.DPoint(0.845, 10.23), pya.DPoint(0.845, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, 10.06), pya.DPoint(1.355, 10.06), pya.DPoint(1.355, 10.23), pya.DPoint(1.185, 10.23), pya.DPoint(1.185, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, 10.06), pya.DPoint(1.695, 10.06), pya.DPoint(1.695, 10.23), pya.DPoint(1.525, 10.23), pya.DPoint(1.525, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, 10.06), pya.DPoint(2.285, 10.06), pya.DPoint(2.285, 10.23), pya.DPoint(2.115, 10.23), pya.DPoint(2.115, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, 10.06), pya.DPoint(2.625, 10.06), pya.DPoint(2.625, 10.23), pya.DPoint(2.455, 10.23), pya.DPoint(2.455, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, 10.06), pya.DPoint(2.965, 10.06), pya.DPoint(2.965, 10.23), pya.DPoint(2.795, 10.23), pya.DPoint(2.795, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.385, 10.06), pya.DPoint(3.555, 10.06), pya.DPoint(3.555, 10.23), pya.DPoint(3.385, 10.23), pya.DPoint(3.385, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.725, 10.06), pya.DPoint(3.895, 10.06), pya.DPoint(3.895, 10.23), pya.DPoint(3.725, 10.23), pya.DPoint(3.725, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.065, 10.06), pya.DPoint(4.235, 10.06), pya.DPoint(4.235, 10.23), pya.DPoint(4.065, 10.23), pya.DPoint(4.065, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.655, 10.06), pya.DPoint(4.825, 10.06), pya.DPoint(4.825, 10.23), pya.DPoint(4.655, 10.23), pya.DPoint(4.655, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.995, 10.06), pya.DPoint(5.165, 10.06), pya.DPoint(5.165, 10.23), pya.DPoint(4.995, 10.23), pya.DPoint(4.995, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.335, 10.06), pya.DPoint(5.505, 10.06), pya.DPoint(5.505, 10.23), pya.DPoint(5.335, 10.23), pya.DPoint(5.335, 10.06)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 9.775), pya.DPoint(-4.5, 9.775), pya.DPoint(-4.5, 9.945), pya.DPoint(-4.67, 9.945), pya.DPoint(-4.67, 9.775)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 9.775), pya.DPoint(5.94, 9.775), pya.DPoint(5.94, 9.945), pya.DPoint(5.77, 9.945), pya.DPoint(5.77, 9.775)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 9.435), pya.DPoint(-4.5, 9.435), pya.DPoint(-4.5, 9.605), pya.DPoint(-4.67, 9.605), pya.DPoint(-4.67, 9.435)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 9.435), pya.DPoint(5.94, 9.435), pya.DPoint(5.94, 9.605), pya.DPoint(5.77, 9.605), pya.DPoint(5.77, 9.435)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 9.095), pya.DPoint(-4.5, 9.095), pya.DPoint(-4.5, 9.265), pya.DPoint(-4.67, 9.265), pya.DPoint(-4.67, 9.095)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 9.095), pya.DPoint(5.94, 9.095), pya.DPoint(5.94, 9.265), pya.DPoint(5.77, 9.265), pya.DPoint(5.77, 9.095)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.755), pya.DPoint(-4.5, 8.755), pya.DPoint(-4.5, 8.925), pya.DPoint(-4.67, 8.925), pya.DPoint(-4.67, 8.755)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.755), pya.DPoint(5.94, 8.755), pya.DPoint(5.94, 8.925), pya.DPoint(5.77, 8.925), pya.DPoint(5.77, 8.755)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.415), pya.DPoint(-4.5, 8.415), pya.DPoint(-4.5, 8.585), pya.DPoint(-4.67, 8.585), pya.DPoint(-4.67, 8.415)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.415), pya.DPoint(5.94, 8.415), pya.DPoint(5.94, 8.585), pya.DPoint(5.77, 8.585), pya.DPoint(5.77, 8.415)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.075), pya.DPoint(-4.5, 8.075), pya.DPoint(-4.5, 8.245), pya.DPoint(-4.67, 8.245), pya.DPoint(-4.67, 8.075)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.075), pya.DPoint(5.94, 8.075), pya.DPoint(5.94, 8.245), pya.DPoint(5.77, 8.245), pya.DPoint(5.77, 8.075)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.735), pya.DPoint(-4.5, 7.735), pya.DPoint(-4.5, 7.905), pya.DPoint(-4.67, 7.905), pya.DPoint(-4.67, 7.735)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.735), pya.DPoint(5.94, 7.735), pya.DPoint(5.94, 7.905), pya.DPoint(5.77, 7.905), pya.DPoint(5.77, 7.735)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.395), pya.DPoint(-4.5, 7.395), pya.DPoint(-4.5, 7.565), pya.DPoint(-4.67, 7.565), pya.DPoint(-4.67, 7.395)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.395), pya.DPoint(5.94, 7.395), pya.DPoint(5.94, 7.565), pya.DPoint(5.77, 7.565), pya.DPoint(5.77, 7.395)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.055), pya.DPoint(-4.5, 7.055), pya.DPoint(-4.5, 7.225), pya.DPoint(-4.67, 7.225), pya.DPoint(-4.67, 7.055)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.055), pya.DPoint(5.94, 7.055), pya.DPoint(5.94, 7.225), pya.DPoint(5.77, 7.225), pya.DPoint(5.77, 7.055)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.715), pya.DPoint(-4.5, 6.715), pya.DPoint(-4.5, 6.885), pya.DPoint(-4.67, 6.885), pya.DPoint(-4.67, 6.715)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.715), pya.DPoint(5.94, 6.715), pya.DPoint(5.94, 6.885), pya.DPoint(5.77, 6.885), pya.DPoint(5.77, 6.715)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.375), pya.DPoint(-4.5, 6.375), pya.DPoint(-4.5, 6.545), pya.DPoint(-4.67, 6.545), pya.DPoint(-4.67, 6.375)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.375), pya.DPoint(5.94, 6.375), pya.DPoint(5.94, 6.545), pya.DPoint(5.77, 6.545), pya.DPoint(5.77, 6.375)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.035), pya.DPoint(-4.5, 6.035), pya.DPoint(-4.5, 6.205), pya.DPoint(-4.67, 6.205), pya.DPoint(-4.67, 6.035)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.035), pya.DPoint(5.94, 6.035), pya.DPoint(5.94, 6.205), pya.DPoint(5.77, 6.205), pya.DPoint(5.77, 6.035)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 5.695), pya.DPoint(-4.5, 5.695), pya.DPoint(-4.5, 5.865), pya.DPoint(-4.67, 5.865), pya.DPoint(-4.67, 5.695)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 5.695), pya.DPoint(5.94, 5.695), pya.DPoint(5.94, 5.865), pya.DPoint(5.77, 5.865), pya.DPoint(5.77, 5.695)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 5.355), pya.DPoint(-4.5, 5.355), pya.DPoint(-4.5, 5.525), pya.DPoint(-4.67, 5.525), pya.DPoint(-4.67, 5.355)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 5.355), pya.DPoint(5.94, 5.355), pya.DPoint(5.94, 5.525), pya.DPoint(5.77, 5.525), pya.DPoint(5.77, 5.355)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 5.015), pya.DPoint(-4.5, 5.015), pya.DPoint(-4.5, 5.185), pya.DPoint(-4.67, 5.185), pya.DPoint(-4.67, 5.015)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 5.015), pya.DPoint(5.94, 5.015), pya.DPoint(5.94, 5.185), pya.DPoint(5.77, 5.185), pya.DPoint(5.77, 5.015)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 4.675), pya.DPoint(-4.5, 4.675), pya.DPoint(-4.5, 4.845), pya.DPoint(-4.67, 4.845), pya.DPoint(-4.67, 4.675)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 4.675), pya.DPoint(5.94, 4.675), pya.DPoint(5.94, 4.845), pya.DPoint(5.77, 4.845), pya.DPoint(5.77, 4.675)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 4.335), pya.DPoint(-4.5, 4.335), pya.DPoint(-4.5, 4.505), pya.DPoint(-4.67, 4.505), pya.DPoint(-4.67, 4.335)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 4.335), pya.DPoint(5.94, 4.335), pya.DPoint(5.94, 4.505), pya.DPoint(5.77, 4.505), pya.DPoint(5.77, 4.335)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.995), pya.DPoint(-4.5, 3.995), pya.DPoint(-4.5, 4.165), pya.DPoint(-4.67, 4.165), pya.DPoint(-4.67, 3.995)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.995), pya.DPoint(5.94, 3.995), pya.DPoint(5.94, 4.165), pya.DPoint(5.77, 4.165), pya.DPoint(5.77, 3.995)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.655), pya.DPoint(-4.5, 3.655), pya.DPoint(-4.5, 3.825), pya.DPoint(-4.67, 3.825), pya.DPoint(-4.67, 3.655)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.655), pya.DPoint(5.94, 3.655), pya.DPoint(5.94, 3.825), pya.DPoint(5.77, 3.825), pya.DPoint(5.77, 3.655)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.315), pya.DPoint(-4.5, 3.315), pya.DPoint(-4.5, 3.485), pya.DPoint(-4.67, 3.485), pya.DPoint(-4.67, 3.315)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.315), pya.DPoint(5.94, 3.315), pya.DPoint(5.94, 3.485), pya.DPoint(5.77, 3.485), pya.DPoint(5.77, 3.315)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.975), pya.DPoint(-4.5, 2.975), pya.DPoint(-4.5, 3.145), pya.DPoint(-4.67, 3.145), pya.DPoint(-4.67, 2.975)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.975), pya.DPoint(5.94, 2.975), pya.DPoint(5.94, 3.145), pya.DPoint(5.77, 3.145), pya.DPoint(5.77, 2.975)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.635), pya.DPoint(-4.5, 2.635), pya.DPoint(-4.5, 2.805), pya.DPoint(-4.67, 2.805), pya.DPoint(-4.67, 2.635)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.635), pya.DPoint(5.94, 2.635), pya.DPoint(5.94, 2.805), pya.DPoint(5.77, 2.805), pya.DPoint(5.77, 2.635)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.295), pya.DPoint(-4.5, 2.295), pya.DPoint(-4.5, 2.465), pya.DPoint(-4.67, 2.465), pya.DPoint(-4.67, 2.295)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.295), pya.DPoint(5.94, 2.295), pya.DPoint(5.94, 2.465), pya.DPoint(5.77, 2.465), pya.DPoint(5.77, 2.295)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 1.955), pya.DPoint(-4.5, 1.955), pya.DPoint(-4.5, 2.125), pya.DPoint(-4.67, 2.125), pya.DPoint(-4.67, 1.955)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 1.955), pya.DPoint(5.94, 1.955), pya.DPoint(5.94, 2.125), pya.DPoint(5.77, 2.125), pya.DPoint(5.77, 1.955)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 1.615), pya.DPoint(-4.5, 1.615), pya.DPoint(-4.5, 1.785), pya.DPoint(-4.67, 1.785), pya.DPoint(-4.67, 1.615)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 1.615), pya.DPoint(5.94, 1.615), pya.DPoint(5.94, 1.785), pya.DPoint(5.77, 1.785), pya.DPoint(5.77, 1.615)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 1.275), pya.DPoint(-4.5, 1.275), pya.DPoint(-4.5, 1.445), pya.DPoint(-4.67, 1.445), pya.DPoint(-4.67, 1.275)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 1.275), pya.DPoint(5.94, 1.275), pya.DPoint(5.94, 1.445), pya.DPoint(5.77, 1.445), pya.DPoint(5.77, 1.275)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.935), pya.DPoint(-4.5, 0.935), pya.DPoint(-4.5, 1.105), pya.DPoint(-4.67, 1.105), pya.DPoint(-4.67, 0.935)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.935), pya.DPoint(5.94, 0.935), pya.DPoint(5.94, 1.105), pya.DPoint(5.77, 1.105), pya.DPoint(5.77, 0.935)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.595), pya.DPoint(-4.5, 0.595), pya.DPoint(-4.5, 0.765), pya.DPoint(-4.67, 0.765), pya.DPoint(-4.67, 0.595)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.595), pya.DPoint(5.94, 0.595), pya.DPoint(5.94, 0.765), pya.DPoint(5.77, 0.765), pya.DPoint(5.77, 0.595)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.255), pya.DPoint(-4.5, 0.255), pya.DPoint(-4.5, 0.425), pya.DPoint(-4.67, 0.425), pya.DPoint(-4.67, 0.255)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.255), pya.DPoint(5.94, 0.255), pya.DPoint(5.94, 0.425), pya.DPoint(5.77, 0.425), pya.DPoint(5.77, 0.255)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.085), pya.DPoint(-4.5, -0.085), pya.DPoint(-4.5, 0.085), pya.DPoint(-4.67, 0.085), pya.DPoint(-4.67, -0.085)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.085), pya.DPoint(5.94, -0.085), pya.DPoint(5.94, 0.085), pya.DPoint(5.77, 0.085), pya.DPoint(5.77, -0.085)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.425), pya.DPoint(-4.5, -0.425), pya.DPoint(-4.5, -0.255), pya.DPoint(-4.67, -0.255), pya.DPoint(-4.67, -0.425)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.425), pya.DPoint(5.94, -0.425), pya.DPoint(5.94, -0.255), pya.DPoint(5.77, -0.255), pya.DPoint(5.77, -0.425)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.765), pya.DPoint(-4.5, -0.765), pya.DPoint(-4.5, -0.595), pya.DPoint(-4.67, -0.595), pya.DPoint(-4.67, -0.765)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.765), pya.DPoint(5.94, -0.765), pya.DPoint(5.94, -0.595), pya.DPoint(5.77, -0.595), pya.DPoint(5.77, -0.765)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.105), pya.DPoint(-4.5, -1.105), pya.DPoint(-4.5, -0.935), pya.DPoint(-4.67, -0.935), pya.DPoint(-4.67, -1.105)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.105), pya.DPoint(5.94, -1.105), pya.DPoint(5.94, -0.935), pya.DPoint(5.77, -0.935), pya.DPoint(5.77, -1.105)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.445), pya.DPoint(-4.5, -1.445), pya.DPoint(-4.5, -1.275), pya.DPoint(-4.67, -1.275), pya.DPoint(-4.67, -1.445)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.445), pya.DPoint(5.94, -1.445), pya.DPoint(5.94, -1.275), pya.DPoint(5.77, -1.275), pya.DPoint(5.77, -1.445)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.785), pya.DPoint(-4.5, -1.785), pya.DPoint(-4.5, -1.615), pya.DPoint(-4.67, -1.615), pya.DPoint(-4.67, -1.785)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.785), pya.DPoint(5.94, -1.785), pya.DPoint(5.94, -1.615), pya.DPoint(5.77, -1.615), pya.DPoint(5.77, -1.785)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.125), pya.DPoint(-4.5, -2.125), pya.DPoint(-4.5, -1.955), pya.DPoint(-4.67, -1.955), pya.DPoint(-4.67, -2.125)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.125), pya.DPoint(5.94, -2.125), pya.DPoint(5.94, -1.955), pya.DPoint(5.77, -1.955), pya.DPoint(5.77, -2.125)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.465), pya.DPoint(-4.5, -2.465), pya.DPoint(-4.5, -2.295), pya.DPoint(-4.67, -2.295), pya.DPoint(-4.67, -2.465)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.465), pya.DPoint(5.94, -2.465), pya.DPoint(5.94, -2.295), pya.DPoint(5.77, -2.295), pya.DPoint(5.77, -2.465)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.805), pya.DPoint(-4.5, -2.805), pya.DPoint(-4.5, -2.635), pya.DPoint(-4.67, -2.635), pya.DPoint(-4.67, -2.805)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.805), pya.DPoint(5.94, -2.805), pya.DPoint(5.94, -2.635), pya.DPoint(5.77, -2.635), pya.DPoint(5.77, -2.805)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -3.145), pya.DPoint(-4.5, -3.145), pya.DPoint(-4.5, -2.975), pya.DPoint(-4.67, -2.975), pya.DPoint(-4.67, -3.145)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -3.145), pya.DPoint(5.94, -3.145), pya.DPoint(5.94, -2.975), pya.DPoint(5.77, -2.975), pya.DPoint(5.77, -3.145)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -3.485), pya.DPoint(-4.5, -3.485), pya.DPoint(-4.5, -3.315), pya.DPoint(-4.67, -3.315), pya.DPoint(-4.67, -3.485)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -3.485), pya.DPoint(5.94, -3.485), pya.DPoint(5.94, -3.315), pya.DPoint(5.77, -3.315), pya.DPoint(5.77, -3.485)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -3.825), pya.DPoint(-4.5, -3.825), pya.DPoint(-4.5, -3.655), pya.DPoint(-4.67, -3.655), pya.DPoint(-4.67, -3.825)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -3.825), pya.DPoint(5.94, -3.825), pya.DPoint(5.94, -3.655), pya.DPoint(5.77, -3.655), pya.DPoint(5.77, -3.825)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.165), pya.DPoint(-4.5, -4.165), pya.DPoint(-4.5, -3.995), pya.DPoint(-4.67, -3.995), pya.DPoint(-4.67, -4.165)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.165), pya.DPoint(5.94, -4.165), pya.DPoint(5.94, -3.995), pya.DPoint(5.77, -3.995), pya.DPoint(5.77, -4.165)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.505), pya.DPoint(-4.5, -4.505), pya.DPoint(-4.5, -4.335), pya.DPoint(-4.67, -4.335), pya.DPoint(-4.67, -4.505)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.505), pya.DPoint(5.94, -4.505), pya.DPoint(5.94, -4.335), pya.DPoint(5.77, -4.335), pya.DPoint(5.77, -4.505)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.845), pya.DPoint(-4.5, -4.845), pya.DPoint(-4.5, -4.675), pya.DPoint(-4.67, -4.675), pya.DPoint(-4.67, -4.845)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.845), pya.DPoint(5.94, -4.845), pya.DPoint(5.94, -4.675), pya.DPoint(5.77, -4.675), pya.DPoint(5.77, -4.845)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.185), pya.DPoint(-4.5, -5.185), pya.DPoint(-4.5, -5.015), pya.DPoint(-4.67, -5.015), pya.DPoint(-4.67, -5.185)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.185), pya.DPoint(5.94, -5.185), pya.DPoint(5.94, -5.015), pya.DPoint(5.77, -5.015), pya.DPoint(5.77, -5.185)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.525), pya.DPoint(-4.5, -5.525), pya.DPoint(-4.5, -5.355), pya.DPoint(-4.67, -5.355), pya.DPoint(-4.67, -5.525)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.525), pya.DPoint(5.94, -5.525), pya.DPoint(5.94, -5.355), pya.DPoint(5.77, -5.355), pya.DPoint(5.77, -5.525)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.865), pya.DPoint(-4.5, -5.865), pya.DPoint(-4.5, -5.695), pya.DPoint(-4.67, -5.695), pya.DPoint(-4.67, -5.865)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.865), pya.DPoint(5.94, -5.865), pya.DPoint(5.94, -5.695), pya.DPoint(5.77, -5.695), pya.DPoint(5.77, -5.865)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.205), pya.DPoint(-4.5, -6.205), pya.DPoint(-4.5, -6.035), pya.DPoint(-4.67, -6.035), pya.DPoint(-4.67, -6.205)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.205), pya.DPoint(5.94, -6.205), pya.DPoint(5.94, -6.035), pya.DPoint(5.77, -6.035), pya.DPoint(5.77, -6.205)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.545), pya.DPoint(-4.5, -6.545), pya.DPoint(-4.5, -6.375), pya.DPoint(-4.67, -6.375), pya.DPoint(-4.67, -6.545)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.545), pya.DPoint(5.94, -6.545), pya.DPoint(5.94, -6.375), pya.DPoint(5.77, -6.375), pya.DPoint(5.77, -6.545)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.885), pya.DPoint(-4.5, -6.885), pya.DPoint(-4.5, -6.715), pya.DPoint(-4.67, -6.715), pya.DPoint(-4.67, -6.885)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.885), pya.DPoint(5.94, -6.885), pya.DPoint(5.94, -6.715), pya.DPoint(5.77, -6.715), pya.DPoint(5.77, -6.885)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -7.225), pya.DPoint(-4.5, -7.225), pya.DPoint(-4.5, -7.055), pya.DPoint(-4.67, -7.055), pya.DPoint(-4.67, -7.225)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -7.225), pya.DPoint(5.94, -7.225), pya.DPoint(5.94, -7.055), pya.DPoint(5.77, -7.055), pya.DPoint(5.77, -7.225)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -7.565), pya.DPoint(-4.5, -7.565), pya.DPoint(-4.5, -7.395), pya.DPoint(-4.67, -7.395), pya.DPoint(-4.67, -7.565)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -7.565), pya.DPoint(5.94, -7.565), pya.DPoint(5.94, -7.395), pya.DPoint(5.77, -7.395), pya.DPoint(5.77, -7.565)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -7.905), pya.DPoint(-4.5, -7.905), pya.DPoint(-4.5, -7.735), pya.DPoint(-4.67, -7.735), pya.DPoint(-4.67, -7.905)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -7.905), pya.DPoint(5.94, -7.905), pya.DPoint(5.94, -7.735), pya.DPoint(5.77, -7.735), pya.DPoint(5.77, -7.905)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.245), pya.DPoint(-4.5, -8.245), pya.DPoint(-4.5, -8.075), pya.DPoint(-4.67, -8.075), pya.DPoint(-4.67, -8.245)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.245), pya.DPoint(5.94, -8.245), pya.DPoint(5.94, -8.075), pya.DPoint(5.77, -8.075), pya.DPoint(5.77, -8.245)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.585), pya.DPoint(-4.5, -8.585), pya.DPoint(-4.5, -8.415), pya.DPoint(-4.67, -8.415), pya.DPoint(-4.67, -8.585)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.585), pya.DPoint(5.94, -8.585), pya.DPoint(5.94, -8.415), pya.DPoint(5.77, -8.415), pya.DPoint(5.77, -8.585)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.925), pya.DPoint(-4.5, -8.925), pya.DPoint(-4.5, -8.755), pya.DPoint(-4.67, -8.755), pya.DPoint(-4.67, -8.925)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.925), pya.DPoint(5.94, -8.925), pya.DPoint(5.94, -8.755), pya.DPoint(5.77, -8.755), pya.DPoint(5.77, -8.925)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.265), pya.DPoint(-4.5, -9.265), pya.DPoint(-4.5, -9.095), pya.DPoint(-4.67, -9.095), pya.DPoint(-4.67, -9.265)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.265), pya.DPoint(5.94, -9.265), pya.DPoint(5.94, -9.095), pya.DPoint(5.77, -9.095), pya.DPoint(5.77, -9.265)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.605), pya.DPoint(-4.5, -9.605), pya.DPoint(-4.5, -9.435), pya.DPoint(-4.67, -9.435), pya.DPoint(-4.67, -9.605)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.605), pya.DPoint(5.94, -9.605), pya.DPoint(5.94, -9.435), pya.DPoint(5.77, -9.435), pya.DPoint(5.77, -9.605)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.945), pya.DPoint(-4.5, -9.945), pya.DPoint(-4.5, -9.775), pya.DPoint(-4.67, -9.775), pya.DPoint(-4.67, -9.945)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.945), pya.DPoint(5.94, -9.945), pya.DPoint(5.94, -9.775), pya.DPoint(5.77, -9.775), pya.DPoint(5.77, -9.945)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.235, -10.23), pya.DPoint(-4.065, -10.23), pya.DPoint(-4.065, -10.06), pya.DPoint(-4.235, -10.06), pya.DPoint(-4.235, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.895, -10.23), pya.DPoint(-3.725, -10.23), pya.DPoint(-3.725, -10.06), pya.DPoint(-3.895, -10.06), pya.DPoint(-3.895, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.555, -10.23), pya.DPoint(-3.385, -10.23), pya.DPoint(-3.385, -10.06), pya.DPoint(-3.555, -10.06), pya.DPoint(-3.555, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, -10.23), pya.DPoint(-2.795, -10.23), pya.DPoint(-2.795, -10.06), pya.DPoint(-2.965, -10.06), pya.DPoint(-2.965, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, -10.23), pya.DPoint(-2.455, -10.23), pya.DPoint(-2.455, -10.06), pya.DPoint(-2.625, -10.06), pya.DPoint(-2.625, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, -10.23), pya.DPoint(-2.115, -10.23), pya.DPoint(-2.115, -10.06), pya.DPoint(-2.285, -10.06), pya.DPoint(-2.285, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, -10.23), pya.DPoint(-1.525, -10.23), pya.DPoint(-1.525, -10.06), pya.DPoint(-1.695, -10.06), pya.DPoint(-1.695, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, -10.23), pya.DPoint(-1.185, -10.23), pya.DPoint(-1.185, -10.06), pya.DPoint(-1.355, -10.06), pya.DPoint(-1.355, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, -10.23), pya.DPoint(-0.845, -10.23), pya.DPoint(-0.845, -10.06), pya.DPoint(-1.015, -10.06), pya.DPoint(-1.015, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, -10.23), pya.DPoint(-0.255, -10.23), pya.DPoint(-0.255, -10.06), pya.DPoint(-0.425, -10.06), pya.DPoint(-0.425, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, -10.23), pya.DPoint(0.085, -10.23), pya.DPoint(0.085, -10.06), pya.DPoint(-0.085, -10.06), pya.DPoint(-0.085, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, -10.23), pya.DPoint(0.425, -10.23), pya.DPoint(0.425, -10.06), pya.DPoint(0.255, -10.06), pya.DPoint(0.255, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, -10.23), pya.DPoint(1.015, -10.23), pya.DPoint(1.015, -10.06), pya.DPoint(0.845, -10.06), pya.DPoint(0.845, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, -10.23), pya.DPoint(1.355, -10.23), pya.DPoint(1.355, -10.06), pya.DPoint(1.185, -10.06), pya.DPoint(1.185, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, -10.23), pya.DPoint(1.695, -10.23), pya.DPoint(1.695, -10.06), pya.DPoint(1.525, -10.06), pya.DPoint(1.525, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, -10.23), pya.DPoint(2.285, -10.23), pya.DPoint(2.285, -10.06), pya.DPoint(2.115, -10.06), pya.DPoint(2.115, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, -10.23), pya.DPoint(2.625, -10.23), pya.DPoint(2.625, -10.06), pya.DPoint(2.455, -10.06), pya.DPoint(2.455, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, -10.23), pya.DPoint(2.965, -10.23), pya.DPoint(2.965, -10.06), pya.DPoint(2.795, -10.06), pya.DPoint(2.795, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.385, -10.23), pya.DPoint(3.555, -10.23), pya.DPoint(3.555, -10.06), pya.DPoint(3.385, -10.06), pya.DPoint(3.385, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.725, -10.23), pya.DPoint(3.895, -10.23), pya.DPoint(3.895, -10.06), pya.DPoint(3.725, -10.06), pya.DPoint(3.725, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.065, -10.23), pya.DPoint(4.235, -10.23), pya.DPoint(4.235, -10.06), pya.DPoint(4.065, -10.06), pya.DPoint(4.065, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.655, -10.23), pya.DPoint(4.825, -10.23), pya.DPoint(4.825, -10.06), pya.DPoint(4.655, -10.06), pya.DPoint(4.655, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.995, -10.23), pya.DPoint(5.165, -10.23), pya.DPoint(5.165, -10.06), pya.DPoint(4.995, -10.06), pya.DPoint(4.995, -10.23)]))
cell_nmos1x20_8x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.335, -10.23), pya.DPoint(5.505, -10.23), pya.DPoint(5.505, -10.06), pya.DPoint(5.335, -10.06), pya.DPoint(5.335, -10.23)]))
cell_nmos1x20_8x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.77, -10.045), pya.DPoint(-4.4, -10.045), pya.DPoint(-4.4, 10.045), pya.DPoint(-4.77, 10.045), pya.DPoint(-4.77, -10.045)]))
cell_nmos1x20_8x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(5.67, -10.045), pya.DPoint(6.04, -10.045), pya.DPoint(6.04, 10.045), pya.DPoint(5.67, 10.045), pya.DPoint(5.67, -10.045)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.33, 10.06), pya.DPoint(-3.29, 10.06), pya.DPoint(-3.29, 10.23), pya.DPoint(-4.33, 10.23), pya.DPoint(-4.33, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, 10.06), pya.DPoint(-2.02, 10.06), pya.DPoint(-2.02, 10.23), pya.DPoint(-3.06, 10.23), pya.DPoint(-3.06, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, 10.06), pya.DPoint(-0.75, 10.06), pya.DPoint(-0.75, 10.23), pya.DPoint(-1.79, 10.23), pya.DPoint(-1.79, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, 10.06), pya.DPoint(0.52, 10.06), pya.DPoint(0.52, 10.23), pya.DPoint(-0.52, 10.23), pya.DPoint(-0.52, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, 10.06), pya.DPoint(1.79, 10.06), pya.DPoint(1.79, 10.23), pya.DPoint(0.75, 10.23), pya.DPoint(0.75, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, 10.06), pya.DPoint(3.06, 10.06), pya.DPoint(3.06, 10.23), pya.DPoint(2.02, 10.23), pya.DPoint(2.02, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.29, 10.06), pya.DPoint(4.33, 10.06), pya.DPoint(4.33, 10.23), pya.DPoint(3.29, 10.23), pya.DPoint(3.29, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.56, 10.06), pya.DPoint(5.6, 10.06), pya.DPoint(5.6, 10.23), pya.DPoint(4.56, 10.23), pya.DPoint(4.56, 10.06)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -10.03), pya.DPoint(-4.5, -10.03), pya.DPoint(-4.5, 10.03), pya.DPoint(-4.67, 10.03), pya.DPoint(-4.67, -10.03)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -10.03), pya.DPoint(5.94, -10.03), pya.DPoint(5.94, 10.03), pya.DPoint(5.77, 10.03), pya.DPoint(5.77, -10.03)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.33, -10.23), pya.DPoint(-3.29, -10.23), pya.DPoint(-3.29, -10.06), pya.DPoint(-4.33, -10.06), pya.DPoint(-4.33, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, -10.23), pya.DPoint(-2.02, -10.23), pya.DPoint(-2.02, -10.06), pya.DPoint(-3.06, -10.06), pya.DPoint(-3.06, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, -10.23), pya.DPoint(-0.75, -10.23), pya.DPoint(-0.75, -10.06), pya.DPoint(-1.79, -10.06), pya.DPoint(-1.79, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, -10.23), pya.DPoint(0.52, -10.23), pya.DPoint(0.52, -10.06), pya.DPoint(-0.52, -10.06), pya.DPoint(-0.52, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, -10.23), pya.DPoint(1.79, -10.23), pya.DPoint(1.79, -10.06), pya.DPoint(0.75, -10.06), pya.DPoint(0.75, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, -10.23), pya.DPoint(3.06, -10.23), pya.DPoint(3.06, -10.06), pya.DPoint(2.02, -10.06), pya.DPoint(2.02, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.29, -10.23), pya.DPoint(4.33, -10.23), pya.DPoint(4.33, -10.06), pya.DPoint(3.29, -10.06), pya.DPoint(3.29, -10.23)]))
cell_nmos1x20_8x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.56, -10.23), pya.DPoint(5.6, -10.23), pya.DPoint(5.6, -10.06), pya.DPoint(4.56, -10.06), pya.DPoint(4.56, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.075, 10.06), pya.DPoint(-3.905, 10.06), pya.DPoint(-3.905, 10.23), pya.DPoint(-4.075, 10.23), pya.DPoint(-4.075, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.715, 10.06), pya.DPoint(-3.545, 10.06), pya.DPoint(-3.545, 10.23), pya.DPoint(-3.715, 10.23), pya.DPoint(-3.715, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, 10.06), pya.DPoint(-2.635, 10.06), pya.DPoint(-2.635, 10.23), pya.DPoint(-2.805, 10.23), pya.DPoint(-2.805, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, 10.06), pya.DPoint(-2.275, 10.06), pya.DPoint(-2.275, 10.23), pya.DPoint(-2.445, 10.23), pya.DPoint(-2.445, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, 10.06), pya.DPoint(-1.365, 10.06), pya.DPoint(-1.365, 10.23), pya.DPoint(-1.535, 10.23), pya.DPoint(-1.535, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, 10.06), pya.DPoint(-1.005, 10.06), pya.DPoint(-1.005, 10.23), pya.DPoint(-1.175, 10.23), pya.DPoint(-1.175, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, 10.06), pya.DPoint(-0.095, 10.06), pya.DPoint(-0.095, 10.23), pya.DPoint(-0.265, 10.23), pya.DPoint(-0.265, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, 10.06), pya.DPoint(0.265, 10.06), pya.DPoint(0.265, 10.23), pya.DPoint(0.095, 10.23), pya.DPoint(0.095, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, 10.06), pya.DPoint(1.175, 10.06), pya.DPoint(1.175, 10.23), pya.DPoint(1.005, 10.23), pya.DPoint(1.005, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, 10.06), pya.DPoint(1.535, 10.06), pya.DPoint(1.535, 10.23), pya.DPoint(1.365, 10.23), pya.DPoint(1.365, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, 10.06), pya.DPoint(2.445, 10.06), pya.DPoint(2.445, 10.23), pya.DPoint(2.275, 10.23), pya.DPoint(2.275, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, 10.06), pya.DPoint(2.805, 10.06), pya.DPoint(2.805, 10.23), pya.DPoint(2.635, 10.23), pya.DPoint(2.635, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.545, 10.06), pya.DPoint(3.715, 10.06), pya.DPoint(3.715, 10.23), pya.DPoint(3.545, 10.23), pya.DPoint(3.545, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.905, 10.06), pya.DPoint(4.075, 10.06), pya.DPoint(4.075, 10.23), pya.DPoint(3.905, 10.23), pya.DPoint(3.905, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.815, 10.06), pya.DPoint(4.985, 10.06), pya.DPoint(4.985, 10.23), pya.DPoint(4.815, 10.23), pya.DPoint(4.815, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.175, 10.06), pya.DPoint(5.345, 10.06), pya.DPoint(5.345, 10.23), pya.DPoint(5.175, 10.23), pya.DPoint(5.175, 10.06)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 9.635), pya.DPoint(-4.5, 9.635), pya.DPoint(-4.5, 9.805), pya.DPoint(-4.67, 9.805), pya.DPoint(-4.67, 9.635)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 9.635), pya.DPoint(5.94, 9.635), pya.DPoint(5.94, 9.805), pya.DPoint(5.77, 9.805), pya.DPoint(5.77, 9.635)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 9.275), pya.DPoint(-4.5, 9.275), pya.DPoint(-4.5, 9.445), pya.DPoint(-4.67, 9.445), pya.DPoint(-4.67, 9.275)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 9.275), pya.DPoint(5.94, 9.275), pya.DPoint(5.94, 9.445), pya.DPoint(5.77, 9.445), pya.DPoint(5.77, 9.275)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.915), pya.DPoint(-4.5, 8.915), pya.DPoint(-4.5, 9.085), pya.DPoint(-4.67, 9.085), pya.DPoint(-4.67, 8.915)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.915), pya.DPoint(5.94, 8.915), pya.DPoint(5.94, 9.085), pya.DPoint(5.77, 9.085), pya.DPoint(5.77, 8.915)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.555), pya.DPoint(-4.5, 8.555), pya.DPoint(-4.5, 8.725), pya.DPoint(-4.67, 8.725), pya.DPoint(-4.67, 8.555)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.555), pya.DPoint(5.94, 8.555), pya.DPoint(5.94, 8.725), pya.DPoint(5.77, 8.725), pya.DPoint(5.77, 8.555)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 8.195), pya.DPoint(-4.5, 8.195), pya.DPoint(-4.5, 8.365), pya.DPoint(-4.67, 8.365), pya.DPoint(-4.67, 8.195)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 8.195), pya.DPoint(5.94, 8.195), pya.DPoint(5.94, 8.365), pya.DPoint(5.77, 8.365), pya.DPoint(5.77, 8.195)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.835), pya.DPoint(-4.5, 7.835), pya.DPoint(-4.5, 8.005), pya.DPoint(-4.67, 8.005), pya.DPoint(-4.67, 7.835)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.835), pya.DPoint(5.94, 7.835), pya.DPoint(5.94, 8.005), pya.DPoint(5.77, 8.005), pya.DPoint(5.77, 7.835)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.475), pya.DPoint(-4.5, 7.475), pya.DPoint(-4.5, 7.645), pya.DPoint(-4.67, 7.645), pya.DPoint(-4.67, 7.475)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.475), pya.DPoint(5.94, 7.475), pya.DPoint(5.94, 7.645), pya.DPoint(5.77, 7.645), pya.DPoint(5.77, 7.475)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 7.115), pya.DPoint(-4.5, 7.115), pya.DPoint(-4.5, 7.285), pya.DPoint(-4.67, 7.285), pya.DPoint(-4.67, 7.115)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 7.115), pya.DPoint(5.94, 7.115), pya.DPoint(5.94, 7.285), pya.DPoint(5.77, 7.285), pya.DPoint(5.77, 7.115)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.755), pya.DPoint(-4.5, 6.755), pya.DPoint(-4.5, 6.925), pya.DPoint(-4.67, 6.925), pya.DPoint(-4.67, 6.755)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.755), pya.DPoint(5.94, 6.755), pya.DPoint(5.94, 6.925), pya.DPoint(5.77, 6.925), pya.DPoint(5.77, 6.755)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.395), pya.DPoint(-4.5, 6.395), pya.DPoint(-4.5, 6.565), pya.DPoint(-4.67, 6.565), pya.DPoint(-4.67, 6.395)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.395), pya.DPoint(5.94, 6.395), pya.DPoint(5.94, 6.565), pya.DPoint(5.77, 6.565), pya.DPoint(5.77, 6.395)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 6.035), pya.DPoint(-4.5, 6.035), pya.DPoint(-4.5, 6.205), pya.DPoint(-4.67, 6.205), pya.DPoint(-4.67, 6.035)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 6.035), pya.DPoint(5.94, 6.035), pya.DPoint(5.94, 6.205), pya.DPoint(5.77, 6.205), pya.DPoint(5.77, 6.035)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 5.675), pya.DPoint(-4.5, 5.675), pya.DPoint(-4.5, 5.845), pya.DPoint(-4.67, 5.845), pya.DPoint(-4.67, 5.675)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 5.675), pya.DPoint(5.94, 5.675), pya.DPoint(5.94, 5.845), pya.DPoint(5.77, 5.845), pya.DPoint(5.77, 5.675)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 5.315), pya.DPoint(-4.5, 5.315), pya.DPoint(-4.5, 5.485), pya.DPoint(-4.67, 5.485), pya.DPoint(-4.67, 5.315)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 5.315), pya.DPoint(5.94, 5.315), pya.DPoint(5.94, 5.485), pya.DPoint(5.77, 5.485), pya.DPoint(5.77, 5.315)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 4.955), pya.DPoint(-4.5, 4.955), pya.DPoint(-4.5, 5.125), pya.DPoint(-4.67, 5.125), pya.DPoint(-4.67, 4.955)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 4.955), pya.DPoint(5.94, 4.955), pya.DPoint(5.94, 5.125), pya.DPoint(5.77, 5.125), pya.DPoint(5.77, 4.955)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 4.595), pya.DPoint(-4.5, 4.595), pya.DPoint(-4.5, 4.765), pya.DPoint(-4.67, 4.765), pya.DPoint(-4.67, 4.595)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 4.595), pya.DPoint(5.94, 4.595), pya.DPoint(5.94, 4.765), pya.DPoint(5.77, 4.765), pya.DPoint(5.77, 4.595)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 4.235), pya.DPoint(-4.5, 4.235), pya.DPoint(-4.5, 4.405), pya.DPoint(-4.67, 4.405), pya.DPoint(-4.67, 4.235)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 4.235), pya.DPoint(5.94, 4.235), pya.DPoint(5.94, 4.405), pya.DPoint(5.77, 4.405), pya.DPoint(5.77, 4.235)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.875), pya.DPoint(-4.5, 3.875), pya.DPoint(-4.5, 4.045), pya.DPoint(-4.67, 4.045), pya.DPoint(-4.67, 3.875)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.875), pya.DPoint(5.94, 3.875), pya.DPoint(5.94, 4.045), pya.DPoint(5.77, 4.045), pya.DPoint(5.77, 3.875)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.515), pya.DPoint(-4.5, 3.515), pya.DPoint(-4.5, 3.685), pya.DPoint(-4.67, 3.685), pya.DPoint(-4.67, 3.515)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.515), pya.DPoint(5.94, 3.515), pya.DPoint(5.94, 3.685), pya.DPoint(5.77, 3.685), pya.DPoint(5.77, 3.515)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 3.155), pya.DPoint(-4.5, 3.155), pya.DPoint(-4.5, 3.325), pya.DPoint(-4.67, 3.325), pya.DPoint(-4.67, 3.155)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 3.155), pya.DPoint(5.94, 3.155), pya.DPoint(5.94, 3.325), pya.DPoint(5.77, 3.325), pya.DPoint(5.77, 3.155)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.795), pya.DPoint(-4.5, 2.795), pya.DPoint(-4.5, 2.965), pya.DPoint(-4.67, 2.965), pya.DPoint(-4.67, 2.795)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.795), pya.DPoint(5.94, 2.795), pya.DPoint(5.94, 2.965), pya.DPoint(5.77, 2.965), pya.DPoint(5.77, 2.795)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.435), pya.DPoint(-4.5, 2.435), pya.DPoint(-4.5, 2.605), pya.DPoint(-4.67, 2.605), pya.DPoint(-4.67, 2.435)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.435), pya.DPoint(5.94, 2.435), pya.DPoint(5.94, 2.605), pya.DPoint(5.77, 2.605), pya.DPoint(5.77, 2.435)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 2.075), pya.DPoint(-4.5, 2.075), pya.DPoint(-4.5, 2.245), pya.DPoint(-4.67, 2.245), pya.DPoint(-4.67, 2.075)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 2.075), pya.DPoint(5.94, 2.075), pya.DPoint(5.94, 2.245), pya.DPoint(5.77, 2.245), pya.DPoint(5.77, 2.075)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 1.715), pya.DPoint(-4.5, 1.715), pya.DPoint(-4.5, 1.885), pya.DPoint(-4.67, 1.885), pya.DPoint(-4.67, 1.715)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 1.715), pya.DPoint(5.94, 1.715), pya.DPoint(5.94, 1.885), pya.DPoint(5.77, 1.885), pya.DPoint(5.77, 1.715)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 1.355), pya.DPoint(-4.5, 1.355), pya.DPoint(-4.5, 1.525), pya.DPoint(-4.67, 1.525), pya.DPoint(-4.67, 1.355)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 1.355), pya.DPoint(5.94, 1.355), pya.DPoint(5.94, 1.525), pya.DPoint(5.77, 1.525), pya.DPoint(5.77, 1.355)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.995), pya.DPoint(-4.5, 0.995), pya.DPoint(-4.5, 1.165), pya.DPoint(-4.67, 1.165), pya.DPoint(-4.67, 0.995)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.995), pya.DPoint(5.94, 0.995), pya.DPoint(5.94, 1.165), pya.DPoint(5.77, 1.165), pya.DPoint(5.77, 0.995)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.635), pya.DPoint(-4.5, 0.635), pya.DPoint(-4.5, 0.805), pya.DPoint(-4.67, 0.805), pya.DPoint(-4.67, 0.635)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.635), pya.DPoint(5.94, 0.635), pya.DPoint(5.94, 0.805), pya.DPoint(5.77, 0.805), pya.DPoint(5.77, 0.635)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, 0.275), pya.DPoint(-4.5, 0.275), pya.DPoint(-4.5, 0.445), pya.DPoint(-4.67, 0.445), pya.DPoint(-4.67, 0.275)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, 0.275), pya.DPoint(5.94, 0.275), pya.DPoint(5.94, 0.445), pya.DPoint(5.77, 0.445), pya.DPoint(5.77, 0.275)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.085), pya.DPoint(-4.5, -0.085), pya.DPoint(-4.5, 0.085), pya.DPoint(-4.67, 0.085), pya.DPoint(-4.67, -0.085)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.085), pya.DPoint(5.94, -0.085), pya.DPoint(5.94, 0.085), pya.DPoint(5.77, 0.085), pya.DPoint(5.77, -0.085)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.445), pya.DPoint(-4.5, -0.445), pya.DPoint(-4.5, -0.275), pya.DPoint(-4.67, -0.275), pya.DPoint(-4.67, -0.445)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.445), pya.DPoint(5.94, -0.445), pya.DPoint(5.94, -0.275), pya.DPoint(5.77, -0.275), pya.DPoint(5.77, -0.445)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -0.805), pya.DPoint(-4.5, -0.805), pya.DPoint(-4.5, -0.635), pya.DPoint(-4.67, -0.635), pya.DPoint(-4.67, -0.805)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -0.805), pya.DPoint(5.94, -0.805), pya.DPoint(5.94, -0.635), pya.DPoint(5.77, -0.635), pya.DPoint(5.77, -0.805)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.165), pya.DPoint(-4.5, -1.165), pya.DPoint(-4.5, -0.995), pya.DPoint(-4.67, -0.995), pya.DPoint(-4.67, -1.165)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.165), pya.DPoint(5.94, -1.165), pya.DPoint(5.94, -0.995), pya.DPoint(5.77, -0.995), pya.DPoint(5.77, -1.165)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.525), pya.DPoint(-4.5, -1.525), pya.DPoint(-4.5, -1.355), pya.DPoint(-4.67, -1.355), pya.DPoint(-4.67, -1.525)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.525), pya.DPoint(5.94, -1.525), pya.DPoint(5.94, -1.355), pya.DPoint(5.77, -1.355), pya.DPoint(5.77, -1.525)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -1.885), pya.DPoint(-4.5, -1.885), pya.DPoint(-4.5, -1.715), pya.DPoint(-4.67, -1.715), pya.DPoint(-4.67, -1.885)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -1.885), pya.DPoint(5.94, -1.885), pya.DPoint(5.94, -1.715), pya.DPoint(5.77, -1.715), pya.DPoint(5.77, -1.885)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.245), pya.DPoint(-4.5, -2.245), pya.DPoint(-4.5, -2.075), pya.DPoint(-4.67, -2.075), pya.DPoint(-4.67, -2.245)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.245), pya.DPoint(5.94, -2.245), pya.DPoint(5.94, -2.075), pya.DPoint(5.77, -2.075), pya.DPoint(5.77, -2.245)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.605), pya.DPoint(-4.5, -2.605), pya.DPoint(-4.5, -2.435), pya.DPoint(-4.67, -2.435), pya.DPoint(-4.67, -2.605)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.605), pya.DPoint(5.94, -2.605), pya.DPoint(5.94, -2.435), pya.DPoint(5.77, -2.435), pya.DPoint(5.77, -2.605)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -2.965), pya.DPoint(-4.5, -2.965), pya.DPoint(-4.5, -2.795), pya.DPoint(-4.67, -2.795), pya.DPoint(-4.67, -2.965)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -2.965), pya.DPoint(5.94, -2.965), pya.DPoint(5.94, -2.795), pya.DPoint(5.77, -2.795), pya.DPoint(5.77, -2.965)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -3.325), pya.DPoint(-4.5, -3.325), pya.DPoint(-4.5, -3.155), pya.DPoint(-4.67, -3.155), pya.DPoint(-4.67, -3.325)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -3.325), pya.DPoint(5.94, -3.325), pya.DPoint(5.94, -3.155), pya.DPoint(5.77, -3.155), pya.DPoint(5.77, -3.325)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -3.685), pya.DPoint(-4.5, -3.685), pya.DPoint(-4.5, -3.515), pya.DPoint(-4.67, -3.515), pya.DPoint(-4.67, -3.685)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -3.685), pya.DPoint(5.94, -3.685), pya.DPoint(5.94, -3.515), pya.DPoint(5.77, -3.515), pya.DPoint(5.77, -3.685)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.045), pya.DPoint(-4.5, -4.045), pya.DPoint(-4.5, -3.875), pya.DPoint(-4.67, -3.875), pya.DPoint(-4.67, -4.045)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.045), pya.DPoint(5.94, -4.045), pya.DPoint(5.94, -3.875), pya.DPoint(5.77, -3.875), pya.DPoint(5.77, -4.045)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.405), pya.DPoint(-4.5, -4.405), pya.DPoint(-4.5, -4.235), pya.DPoint(-4.67, -4.235), pya.DPoint(-4.67, -4.405)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.405), pya.DPoint(5.94, -4.405), pya.DPoint(5.94, -4.235), pya.DPoint(5.77, -4.235), pya.DPoint(5.77, -4.405)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -4.765), pya.DPoint(-4.5, -4.765), pya.DPoint(-4.5, -4.595), pya.DPoint(-4.67, -4.595), pya.DPoint(-4.67, -4.765)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -4.765), pya.DPoint(5.94, -4.765), pya.DPoint(5.94, -4.595), pya.DPoint(5.77, -4.595), pya.DPoint(5.77, -4.765)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.125), pya.DPoint(-4.5, -5.125), pya.DPoint(-4.5, -4.955), pya.DPoint(-4.67, -4.955), pya.DPoint(-4.67, -5.125)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.125), pya.DPoint(5.94, -5.125), pya.DPoint(5.94, -4.955), pya.DPoint(5.77, -4.955), pya.DPoint(5.77, -5.125)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.485), pya.DPoint(-4.5, -5.485), pya.DPoint(-4.5, -5.315), pya.DPoint(-4.67, -5.315), pya.DPoint(-4.67, -5.485)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.485), pya.DPoint(5.94, -5.485), pya.DPoint(5.94, -5.315), pya.DPoint(5.77, -5.315), pya.DPoint(5.77, -5.485)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -5.845), pya.DPoint(-4.5, -5.845), pya.DPoint(-4.5, -5.675), pya.DPoint(-4.67, -5.675), pya.DPoint(-4.67, -5.845)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -5.845), pya.DPoint(5.94, -5.845), pya.DPoint(5.94, -5.675), pya.DPoint(5.77, -5.675), pya.DPoint(5.77, -5.845)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.205), pya.DPoint(-4.5, -6.205), pya.DPoint(-4.5, -6.035), pya.DPoint(-4.67, -6.035), pya.DPoint(-4.67, -6.205)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.205), pya.DPoint(5.94, -6.205), pya.DPoint(5.94, -6.035), pya.DPoint(5.77, -6.035), pya.DPoint(5.77, -6.205)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.565), pya.DPoint(-4.5, -6.565), pya.DPoint(-4.5, -6.395), pya.DPoint(-4.67, -6.395), pya.DPoint(-4.67, -6.565)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.565), pya.DPoint(5.94, -6.565), pya.DPoint(5.94, -6.395), pya.DPoint(5.77, -6.395), pya.DPoint(5.77, -6.565)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -6.925), pya.DPoint(-4.5, -6.925), pya.DPoint(-4.5, -6.755), pya.DPoint(-4.67, -6.755), pya.DPoint(-4.67, -6.925)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -6.925), pya.DPoint(5.94, -6.925), pya.DPoint(5.94, -6.755), pya.DPoint(5.77, -6.755), pya.DPoint(5.77, -6.925)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -7.285), pya.DPoint(-4.5, -7.285), pya.DPoint(-4.5, -7.115), pya.DPoint(-4.67, -7.115), pya.DPoint(-4.67, -7.285)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -7.285), pya.DPoint(5.94, -7.285), pya.DPoint(5.94, -7.115), pya.DPoint(5.77, -7.115), pya.DPoint(5.77, -7.285)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -7.645), pya.DPoint(-4.5, -7.645), pya.DPoint(-4.5, -7.475), pya.DPoint(-4.67, -7.475), pya.DPoint(-4.67, -7.645)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -7.645), pya.DPoint(5.94, -7.645), pya.DPoint(5.94, -7.475), pya.DPoint(5.77, -7.475), pya.DPoint(5.77, -7.645)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.005), pya.DPoint(-4.5, -8.005), pya.DPoint(-4.5, -7.835), pya.DPoint(-4.67, -7.835), pya.DPoint(-4.67, -8.005)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.005), pya.DPoint(5.94, -8.005), pya.DPoint(5.94, -7.835), pya.DPoint(5.77, -7.835), pya.DPoint(5.77, -8.005)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.365), pya.DPoint(-4.5, -8.365), pya.DPoint(-4.5, -8.195), pya.DPoint(-4.67, -8.195), pya.DPoint(-4.67, -8.365)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.365), pya.DPoint(5.94, -8.365), pya.DPoint(5.94, -8.195), pya.DPoint(5.77, -8.195), pya.DPoint(5.77, -8.365)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -8.725), pya.DPoint(-4.5, -8.725), pya.DPoint(-4.5, -8.555), pya.DPoint(-4.67, -8.555), pya.DPoint(-4.67, -8.725)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -8.725), pya.DPoint(5.94, -8.725), pya.DPoint(5.94, -8.555), pya.DPoint(5.77, -8.555), pya.DPoint(5.77, -8.725)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.085), pya.DPoint(-4.5, -9.085), pya.DPoint(-4.5, -8.915), pya.DPoint(-4.67, -8.915), pya.DPoint(-4.67, -9.085)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.085), pya.DPoint(5.94, -9.085), pya.DPoint(5.94, -8.915), pya.DPoint(5.77, -8.915), pya.DPoint(5.77, -9.085)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.445), pya.DPoint(-4.5, -9.445), pya.DPoint(-4.5, -9.275), pya.DPoint(-4.67, -9.275), pya.DPoint(-4.67, -9.445)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.445), pya.DPoint(5.94, -9.445), pya.DPoint(5.94, -9.275), pya.DPoint(5.77, -9.275), pya.DPoint(5.77, -9.445)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.67, -9.805), pya.DPoint(-4.5, -9.805), pya.DPoint(-4.5, -9.635), pya.DPoint(-4.67, -9.635), pya.DPoint(-4.67, -9.805)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.77, -9.805), pya.DPoint(5.94, -9.805), pya.DPoint(5.94, -9.635), pya.DPoint(5.77, -9.635), pya.DPoint(5.77, -9.805)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.075, -10.23), pya.DPoint(-3.905, -10.23), pya.DPoint(-3.905, -10.06), pya.DPoint(-4.075, -10.06), pya.DPoint(-4.075, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.715, -10.23), pya.DPoint(-3.545, -10.23), pya.DPoint(-3.545, -10.06), pya.DPoint(-3.715, -10.06), pya.DPoint(-3.715, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, -10.23), pya.DPoint(-2.635, -10.23), pya.DPoint(-2.635, -10.06), pya.DPoint(-2.805, -10.06), pya.DPoint(-2.805, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, -10.23), pya.DPoint(-2.275, -10.23), pya.DPoint(-2.275, -10.06), pya.DPoint(-2.445, -10.06), pya.DPoint(-2.445, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, -10.23), pya.DPoint(-1.365, -10.23), pya.DPoint(-1.365, -10.06), pya.DPoint(-1.535, -10.06), pya.DPoint(-1.535, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, -10.23), pya.DPoint(-1.005, -10.23), pya.DPoint(-1.005, -10.06), pya.DPoint(-1.175, -10.06), pya.DPoint(-1.175, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, -10.23), pya.DPoint(-0.095, -10.23), pya.DPoint(-0.095, -10.06), pya.DPoint(-0.265, -10.06), pya.DPoint(-0.265, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, -10.23), pya.DPoint(0.265, -10.23), pya.DPoint(0.265, -10.06), pya.DPoint(0.095, -10.06), pya.DPoint(0.095, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, -10.23), pya.DPoint(1.175, -10.23), pya.DPoint(1.175, -10.06), pya.DPoint(1.005, -10.06), pya.DPoint(1.005, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, -10.23), pya.DPoint(1.535, -10.23), pya.DPoint(1.535, -10.06), pya.DPoint(1.365, -10.06), pya.DPoint(1.365, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, -10.23), pya.DPoint(2.445, -10.23), pya.DPoint(2.445, -10.06), pya.DPoint(2.275, -10.06), pya.DPoint(2.275, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, -10.23), pya.DPoint(2.805, -10.23), pya.DPoint(2.805, -10.06), pya.DPoint(2.635, -10.06), pya.DPoint(2.635, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.545, -10.23), pya.DPoint(3.715, -10.23), pya.DPoint(3.715, -10.06), pya.DPoint(3.545, -10.06), pya.DPoint(3.545, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.905, -10.23), pya.DPoint(4.075, -10.23), pya.DPoint(4.075, -10.06), pya.DPoint(3.905, -10.06), pya.DPoint(3.905, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.815, -10.23), pya.DPoint(4.985, -10.23), pya.DPoint(4.985, -10.06), pya.DPoint(4.815, -10.06), pya.DPoint(4.815, -10.23)]))
cell_nmos1x20_8x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.175, -10.23), pya.DPoint(5.345, -10.23), pya.DPoint(5.345, -10.06), pya.DPoint(5.175, -10.06), pya.DPoint(5.175, -10.23)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, 10.03), pya.DPoint(-3.31, 10.03), pya.DPoint(-3.31, 10.26), pya.DPoint(-4.31, 10.26), pya.DPoint(-4.31, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, 10.03), pya.DPoint(-2.04, 10.03), pya.DPoint(-2.04, 10.26), pya.DPoint(-3.04, 10.26), pya.DPoint(-3.04, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 10.03), pya.DPoint(-0.77, 10.03), pya.DPoint(-0.77, 10.26), pya.DPoint(-1.77, 10.26), pya.DPoint(-1.77, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, 10.03), pya.DPoint(0.5, 10.03), pya.DPoint(0.5, 10.26), pya.DPoint(-0.5, 10.26), pya.DPoint(-0.5, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, 10.03), pya.DPoint(1.77, 10.03), pya.DPoint(1.77, 10.26), pya.DPoint(0.77, 10.26), pya.DPoint(0.77, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, 10.03), pya.DPoint(3.04, 10.03), pya.DPoint(3.04, 10.26), pya.DPoint(2.04, 10.26), pya.DPoint(2.04, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, 10.03), pya.DPoint(4.31, 10.03), pya.DPoint(4.31, 10.26), pya.DPoint(3.31, 10.26), pya.DPoint(3.31, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.58, 10.03), pya.DPoint(5.58, 10.03), pya.DPoint(5.58, 10.26), pya.DPoint(4.58, 10.26), pya.DPoint(4.58, 10.03)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.7, -10.01), pya.DPoint(-4.47, -10.01), pya.DPoint(-4.47, 10.01), pya.DPoint(-4.7, 10.01), pya.DPoint(-4.7, -10.01)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.74, -10.01), pya.DPoint(5.97, -10.01), pya.DPoint(5.97, 10.01), pya.DPoint(5.74, 10.01), pya.DPoint(5.74, -10.01)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, -10.26), pya.DPoint(-3.31, -10.26), pya.DPoint(-3.31, -10.03), pya.DPoint(-4.31, -10.03), pya.DPoint(-4.31, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -10.26), pya.DPoint(-2.04, -10.26), pya.DPoint(-2.04, -10.03), pya.DPoint(-3.04, -10.03), pya.DPoint(-3.04, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -10.26), pya.DPoint(-0.77, -10.26), pya.DPoint(-0.77, -10.03), pya.DPoint(-1.77, -10.03), pya.DPoint(-1.77, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -10.26), pya.DPoint(0.5, -10.26), pya.DPoint(0.5, -10.03), pya.DPoint(-0.5, -10.03), pya.DPoint(-0.5, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -10.26), pya.DPoint(1.77, -10.26), pya.DPoint(1.77, -10.03), pya.DPoint(0.77, -10.03), pya.DPoint(0.77, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -10.26), pya.DPoint(3.04, -10.26), pya.DPoint(3.04, -10.03), pya.DPoint(2.04, -10.03), pya.DPoint(2.04, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, -10.26), pya.DPoint(4.31, -10.26), pya.DPoint(4.31, -10.03), pya.DPoint(3.31, -10.03), pya.DPoint(3.31, -10.26)]))
cell_nmos1x20_8x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.58, -10.26), pya.DPoint(5.58, -10.26), pya.DPoint(5.58, -10.03), pya.DPoint(4.58, -10.03), pya.DPoint(4.58, -10.26)]))

# === nmos_1x80_2x ===
cell_nmos_1x80_2x.insert(pya.DCellInstArray(
    cell_nmos1x20_8x.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.75, 10.29))))
cell_nmos_1x80_2x.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.37, 20.85), pya.DPoint(11.14, 20.85), pya.DPoint(11.14, 21.06), pya.DPoint(-0.37, 21.06), pya.DPoint(-0.37, 20.85)]))
cell_nmos_1x80_2x.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.37, -0.28), pya.DPoint(-0.16, -0.28), pya.DPoint(-0.16, 20.85), pya.DPoint(-0.37, 20.85), pya.DPoint(-0.37, -0.28)]))
cell_nmos_1x80_2x.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(10.93, -0.28), pya.DPoint(11.14, -0.28), pya.DPoint(11.14, 20.85), pya.DPoint(10.93, 20.85), pya.DPoint(10.93, -0.28)]))
cell_nmos_1x80_2x.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.37, -0.49), pya.DPoint(11.14, -0.49), pya.DPoint(11.14, -0.28), pya.DPoint(-0.37, -0.28), pya.DPoint(-0.37, -0.49)]))
cell_nmos_1x80_2x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.495, 20.725), pya.DPoint(11.265, 20.725), pya.DPoint(11.265, 21.185), pya.DPoint(-0.495, 21.185), pya.DPoint(-0.495, 20.725)]))
cell_nmos_1x80_2x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.495, -0.155), pya.DPoint(-0.035, -0.155), pya.DPoint(-0.035, 20.725), pya.DPoint(-0.495, 20.725), pya.DPoint(-0.495, -0.155)]))
cell_nmos_1x80_2x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(10.805, -0.155), pya.DPoint(11.265, -0.155), pya.DPoint(11.265, 20.725), pya.DPoint(10.805, 20.725), pya.DPoint(10.805, -0.155)]))
cell_nmos_1x80_2x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.495, -0.615), pya.DPoint(11.265, -0.615), pya.DPoint(11.265, -0.155), pya.DPoint(-0.495, -0.155), pya.DPoint(-0.495, -0.615)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.14, 20.87), pya.DPoint(0.03, 20.87), pya.DPoint(0.03, 21.04), pya.DPoint(-0.14, 21.04), pya.DPoint(-0.14, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.2, 20.87), pya.DPoint(0.37, 20.87), pya.DPoint(0.37, 21.04), pya.DPoint(0.2, 21.04), pya.DPoint(0.2, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.54, 20.87), pya.DPoint(0.71, 20.87), pya.DPoint(0.71, 21.04), pya.DPoint(0.54, 21.04), pya.DPoint(0.54, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.88, 20.87), pya.DPoint(1.05, 20.87), pya.DPoint(1.05, 21.04), pya.DPoint(0.88, 21.04), pya.DPoint(0.88, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.22, 20.87), pya.DPoint(1.39, 20.87), pya.DPoint(1.39, 21.04), pya.DPoint(1.22, 21.04), pya.DPoint(1.22, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.56, 20.87), pya.DPoint(1.73, 20.87), pya.DPoint(1.73, 21.04), pya.DPoint(1.56, 21.04), pya.DPoint(1.56, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.9, 20.87), pya.DPoint(2.07, 20.87), pya.DPoint(2.07, 21.04), pya.DPoint(1.9, 21.04), pya.DPoint(1.9, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.24, 20.87), pya.DPoint(2.41, 20.87), pya.DPoint(2.41, 21.04), pya.DPoint(2.24, 21.04), pya.DPoint(2.24, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.58, 20.87), pya.DPoint(2.75, 20.87), pya.DPoint(2.75, 21.04), pya.DPoint(2.58, 21.04), pya.DPoint(2.58, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.92, 20.87), pya.DPoint(3.09, 20.87), pya.DPoint(3.09, 21.04), pya.DPoint(2.92, 21.04), pya.DPoint(2.92, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.26, 20.87), pya.DPoint(3.43, 20.87), pya.DPoint(3.43, 21.04), pya.DPoint(3.26, 21.04), pya.DPoint(3.26, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.6, 20.87), pya.DPoint(3.77, 20.87), pya.DPoint(3.77, 21.04), pya.DPoint(3.6, 21.04), pya.DPoint(3.6, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.94, 20.87), pya.DPoint(4.11, 20.87), pya.DPoint(4.11, 21.04), pya.DPoint(3.94, 21.04), pya.DPoint(3.94, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.28, 20.87), pya.DPoint(4.45, 20.87), pya.DPoint(4.45, 21.04), pya.DPoint(4.28, 21.04), pya.DPoint(4.28, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.62, 20.87), pya.DPoint(4.79, 20.87), pya.DPoint(4.79, 21.04), pya.DPoint(4.62, 21.04), pya.DPoint(4.62, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.96, 20.87), pya.DPoint(5.13, 20.87), pya.DPoint(5.13, 21.04), pya.DPoint(4.96, 21.04), pya.DPoint(4.96, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.3, 20.87), pya.DPoint(5.47, 20.87), pya.DPoint(5.47, 21.04), pya.DPoint(5.3, 21.04), pya.DPoint(5.3, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.64, 20.87), pya.DPoint(5.81, 20.87), pya.DPoint(5.81, 21.04), pya.DPoint(5.64, 21.04), pya.DPoint(5.64, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.98, 20.87), pya.DPoint(6.15, 20.87), pya.DPoint(6.15, 21.04), pya.DPoint(5.98, 21.04), pya.DPoint(5.98, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.32, 20.87), pya.DPoint(6.49, 20.87), pya.DPoint(6.49, 21.04), pya.DPoint(6.32, 21.04), pya.DPoint(6.32, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, 20.87), pya.DPoint(6.83, 20.87), pya.DPoint(6.83, 21.04), pya.DPoint(6.66, 21.04), pya.DPoint(6.66, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7, 20.87), pya.DPoint(7.17, 20.87), pya.DPoint(7.17, 21.04), pya.DPoint(7, 21.04), pya.DPoint(7, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.34, 20.87), pya.DPoint(7.51, 20.87), pya.DPoint(7.51, 21.04), pya.DPoint(7.34, 21.04), pya.DPoint(7.34, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.68, 20.87), pya.DPoint(7.85, 20.87), pya.DPoint(7.85, 21.04), pya.DPoint(7.68, 21.04), pya.DPoint(7.68, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.02, 20.87), pya.DPoint(8.19, 20.87), pya.DPoint(8.19, 21.04), pya.DPoint(8.02, 21.04), pya.DPoint(8.02, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, 20.87), pya.DPoint(8.53, 20.87), pya.DPoint(8.53, 21.04), pya.DPoint(8.36, 21.04), pya.DPoint(8.36, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.7, 20.87), pya.DPoint(8.87, 20.87), pya.DPoint(8.87, 21.04), pya.DPoint(8.7, 21.04), pya.DPoint(8.7, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.04, 20.87), pya.DPoint(9.21, 20.87), pya.DPoint(9.21, 21.04), pya.DPoint(9.04, 21.04), pya.DPoint(9.04, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.38, 20.87), pya.DPoint(9.55, 20.87), pya.DPoint(9.55, 21.04), pya.DPoint(9.38, 21.04), pya.DPoint(9.38, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.72, 20.87), pya.DPoint(9.89, 20.87), pya.DPoint(9.89, 21.04), pya.DPoint(9.72, 21.04), pya.DPoint(9.72, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.06, 20.87), pya.DPoint(10.23, 20.87), pya.DPoint(10.23, 21.04), pya.DPoint(10.06, 21.04), pya.DPoint(10.06, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.4, 20.87), pya.DPoint(10.57, 20.87), pya.DPoint(10.57, 21.04), pya.DPoint(10.4, 21.04), pya.DPoint(10.4, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.74, 20.87), pya.DPoint(10.91, 20.87), pya.DPoint(10.91, 21.04), pya.DPoint(10.74, 21.04), pya.DPoint(10.74, 20.87)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 20.4), pya.DPoint(-0.18, 20.4), pya.DPoint(-0.18, 20.57), pya.DPoint(-0.35, 20.57), pya.DPoint(-0.35, 20.4)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 20.4), pya.DPoint(11.12, 20.4), pya.DPoint(11.12, 20.57), pya.DPoint(10.95, 20.57), pya.DPoint(10.95, 20.4)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 20.06), pya.DPoint(-0.18, 20.06), pya.DPoint(-0.18, 20.23), pya.DPoint(-0.35, 20.23), pya.DPoint(-0.35, 20.06)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 20.06), pya.DPoint(11.12, 20.06), pya.DPoint(11.12, 20.23), pya.DPoint(10.95, 20.23), pya.DPoint(10.95, 20.06)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 19.72), pya.DPoint(-0.18, 19.72), pya.DPoint(-0.18, 19.89), pya.DPoint(-0.35, 19.89), pya.DPoint(-0.35, 19.72)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 19.72), pya.DPoint(11.12, 19.72), pya.DPoint(11.12, 19.89), pya.DPoint(10.95, 19.89), pya.DPoint(10.95, 19.72)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 19.38), pya.DPoint(-0.18, 19.38), pya.DPoint(-0.18, 19.55), pya.DPoint(-0.35, 19.55), pya.DPoint(-0.35, 19.38)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 19.38), pya.DPoint(11.12, 19.38), pya.DPoint(11.12, 19.55), pya.DPoint(10.95, 19.55), pya.DPoint(10.95, 19.38)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 19.04), pya.DPoint(-0.18, 19.04), pya.DPoint(-0.18, 19.21), pya.DPoint(-0.35, 19.21), pya.DPoint(-0.35, 19.04)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 19.04), pya.DPoint(11.12, 19.04), pya.DPoint(11.12, 19.21), pya.DPoint(10.95, 19.21), pya.DPoint(10.95, 19.04)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 18.7), pya.DPoint(-0.18, 18.7), pya.DPoint(-0.18, 18.87), pya.DPoint(-0.35, 18.87), pya.DPoint(-0.35, 18.7)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 18.7), pya.DPoint(11.12, 18.7), pya.DPoint(11.12, 18.87), pya.DPoint(10.95, 18.87), pya.DPoint(10.95, 18.7)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 18.36), pya.DPoint(-0.18, 18.36), pya.DPoint(-0.18, 18.53), pya.DPoint(-0.35, 18.53), pya.DPoint(-0.35, 18.36)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 18.36), pya.DPoint(11.12, 18.36), pya.DPoint(11.12, 18.53), pya.DPoint(10.95, 18.53), pya.DPoint(10.95, 18.36)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 18.02), pya.DPoint(-0.18, 18.02), pya.DPoint(-0.18, 18.19), pya.DPoint(-0.35, 18.19), pya.DPoint(-0.35, 18.02)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 18.02), pya.DPoint(11.12, 18.02), pya.DPoint(11.12, 18.19), pya.DPoint(10.95, 18.19), pya.DPoint(10.95, 18.02)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 17.68), pya.DPoint(-0.18, 17.68), pya.DPoint(-0.18, 17.85), pya.DPoint(-0.35, 17.85), pya.DPoint(-0.35, 17.68)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 17.68), pya.DPoint(11.12, 17.68), pya.DPoint(11.12, 17.85), pya.DPoint(10.95, 17.85), pya.DPoint(10.95, 17.68)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 17.34), pya.DPoint(-0.18, 17.34), pya.DPoint(-0.18, 17.51), pya.DPoint(-0.35, 17.51), pya.DPoint(-0.35, 17.34)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 17.34), pya.DPoint(11.12, 17.34), pya.DPoint(11.12, 17.51), pya.DPoint(10.95, 17.51), pya.DPoint(10.95, 17.34)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 17), pya.DPoint(-0.18, 17), pya.DPoint(-0.18, 17.17), pya.DPoint(-0.35, 17.17), pya.DPoint(-0.35, 17)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 17), pya.DPoint(11.12, 17), pya.DPoint(11.12, 17.17), pya.DPoint(10.95, 17.17), pya.DPoint(10.95, 17)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 16.66), pya.DPoint(-0.18, 16.66), pya.DPoint(-0.18, 16.83), pya.DPoint(-0.35, 16.83), pya.DPoint(-0.35, 16.66)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 16.66), pya.DPoint(11.12, 16.66), pya.DPoint(11.12, 16.83), pya.DPoint(10.95, 16.83), pya.DPoint(10.95, 16.66)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 16.32), pya.DPoint(-0.18, 16.32), pya.DPoint(-0.18, 16.49), pya.DPoint(-0.35, 16.49), pya.DPoint(-0.35, 16.32)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 16.32), pya.DPoint(11.12, 16.32), pya.DPoint(11.12, 16.49), pya.DPoint(10.95, 16.49), pya.DPoint(10.95, 16.32)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 15.98), pya.DPoint(-0.18, 15.98), pya.DPoint(-0.18, 16.15), pya.DPoint(-0.35, 16.15), pya.DPoint(-0.35, 15.98)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 15.98), pya.DPoint(11.12, 15.98), pya.DPoint(11.12, 16.15), pya.DPoint(10.95, 16.15), pya.DPoint(10.95, 15.98)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 15.64), pya.DPoint(-0.18, 15.64), pya.DPoint(-0.18, 15.81), pya.DPoint(-0.35, 15.81), pya.DPoint(-0.35, 15.64)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 15.64), pya.DPoint(11.12, 15.64), pya.DPoint(11.12, 15.81), pya.DPoint(10.95, 15.81), pya.DPoint(10.95, 15.64)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 15.3), pya.DPoint(-0.18, 15.3), pya.DPoint(-0.18, 15.47), pya.DPoint(-0.35, 15.47), pya.DPoint(-0.35, 15.3)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 15.3), pya.DPoint(11.12, 15.3), pya.DPoint(11.12, 15.47), pya.DPoint(10.95, 15.47), pya.DPoint(10.95, 15.3)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 14.96), pya.DPoint(-0.18, 14.96), pya.DPoint(-0.18, 15.13), pya.DPoint(-0.35, 15.13), pya.DPoint(-0.35, 14.96)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 14.96), pya.DPoint(11.12, 14.96), pya.DPoint(11.12, 15.13), pya.DPoint(10.95, 15.13), pya.DPoint(10.95, 14.96)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 14.62), pya.DPoint(-0.18, 14.62), pya.DPoint(-0.18, 14.79), pya.DPoint(-0.35, 14.79), pya.DPoint(-0.35, 14.62)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 14.62), pya.DPoint(11.12, 14.62), pya.DPoint(11.12, 14.79), pya.DPoint(10.95, 14.79), pya.DPoint(10.95, 14.62)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 14.28), pya.DPoint(-0.18, 14.28), pya.DPoint(-0.18, 14.45), pya.DPoint(-0.35, 14.45), pya.DPoint(-0.35, 14.28)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 14.28), pya.DPoint(11.12, 14.28), pya.DPoint(11.12, 14.45), pya.DPoint(10.95, 14.45), pya.DPoint(10.95, 14.28)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 13.94), pya.DPoint(-0.18, 13.94), pya.DPoint(-0.18, 14.11), pya.DPoint(-0.35, 14.11), pya.DPoint(-0.35, 13.94)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 13.94), pya.DPoint(11.12, 13.94), pya.DPoint(11.12, 14.11), pya.DPoint(10.95, 14.11), pya.DPoint(10.95, 13.94)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 13.6), pya.DPoint(-0.18, 13.6), pya.DPoint(-0.18, 13.77), pya.DPoint(-0.35, 13.77), pya.DPoint(-0.35, 13.6)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 13.6), pya.DPoint(11.12, 13.6), pya.DPoint(11.12, 13.77), pya.DPoint(10.95, 13.77), pya.DPoint(10.95, 13.6)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 13.26), pya.DPoint(-0.18, 13.26), pya.DPoint(-0.18, 13.43), pya.DPoint(-0.35, 13.43), pya.DPoint(-0.35, 13.26)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 13.26), pya.DPoint(11.12, 13.26), pya.DPoint(11.12, 13.43), pya.DPoint(10.95, 13.43), pya.DPoint(10.95, 13.26)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 12.92), pya.DPoint(-0.18, 12.92), pya.DPoint(-0.18, 13.09), pya.DPoint(-0.35, 13.09), pya.DPoint(-0.35, 12.92)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 12.92), pya.DPoint(11.12, 12.92), pya.DPoint(11.12, 13.09), pya.DPoint(10.95, 13.09), pya.DPoint(10.95, 12.92)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 12.58), pya.DPoint(-0.18, 12.58), pya.DPoint(-0.18, 12.75), pya.DPoint(-0.35, 12.75), pya.DPoint(-0.35, 12.58)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 12.58), pya.DPoint(11.12, 12.58), pya.DPoint(11.12, 12.75), pya.DPoint(10.95, 12.75), pya.DPoint(10.95, 12.58)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 12.24), pya.DPoint(-0.18, 12.24), pya.DPoint(-0.18, 12.41), pya.DPoint(-0.35, 12.41), pya.DPoint(-0.35, 12.24)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 12.24), pya.DPoint(11.12, 12.24), pya.DPoint(11.12, 12.41), pya.DPoint(10.95, 12.41), pya.DPoint(10.95, 12.24)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 11.9), pya.DPoint(-0.18, 11.9), pya.DPoint(-0.18, 12.07), pya.DPoint(-0.35, 12.07), pya.DPoint(-0.35, 11.9)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 11.9), pya.DPoint(11.12, 11.9), pya.DPoint(11.12, 12.07), pya.DPoint(10.95, 12.07), pya.DPoint(10.95, 11.9)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 11.56), pya.DPoint(-0.18, 11.56), pya.DPoint(-0.18, 11.73), pya.DPoint(-0.35, 11.73), pya.DPoint(-0.35, 11.56)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 11.56), pya.DPoint(11.12, 11.56), pya.DPoint(11.12, 11.73), pya.DPoint(10.95, 11.73), pya.DPoint(10.95, 11.56)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 11.22), pya.DPoint(-0.18, 11.22), pya.DPoint(-0.18, 11.39), pya.DPoint(-0.35, 11.39), pya.DPoint(-0.35, 11.22)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 11.22), pya.DPoint(11.12, 11.22), pya.DPoint(11.12, 11.39), pya.DPoint(10.95, 11.39), pya.DPoint(10.95, 11.22)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 10.88), pya.DPoint(-0.18, 10.88), pya.DPoint(-0.18, 11.05), pya.DPoint(-0.35, 11.05), pya.DPoint(-0.35, 10.88)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 10.88), pya.DPoint(11.12, 10.88), pya.DPoint(11.12, 11.05), pya.DPoint(10.95, 11.05), pya.DPoint(10.95, 10.88)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 10.54), pya.DPoint(-0.18, 10.54), pya.DPoint(-0.18, 10.71), pya.DPoint(-0.35, 10.71), pya.DPoint(-0.35, 10.54)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 10.54), pya.DPoint(11.12, 10.54), pya.DPoint(11.12, 10.71), pya.DPoint(10.95, 10.71), pya.DPoint(10.95, 10.54)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 10.2), pya.DPoint(-0.18, 10.2), pya.DPoint(-0.18, 10.37), pya.DPoint(-0.35, 10.37), pya.DPoint(-0.35, 10.2)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 10.2), pya.DPoint(11.12, 10.2), pya.DPoint(11.12, 10.37), pya.DPoint(10.95, 10.37), pya.DPoint(10.95, 10.2)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 9.86), pya.DPoint(-0.18, 9.86), pya.DPoint(-0.18, 10.03), pya.DPoint(-0.35, 10.03), pya.DPoint(-0.35, 9.86)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 9.86), pya.DPoint(11.12, 9.86), pya.DPoint(11.12, 10.03), pya.DPoint(10.95, 10.03), pya.DPoint(10.95, 9.86)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 9.52), pya.DPoint(-0.18, 9.52), pya.DPoint(-0.18, 9.69), pya.DPoint(-0.35, 9.69), pya.DPoint(-0.35, 9.52)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 9.52), pya.DPoint(11.12, 9.52), pya.DPoint(11.12, 9.69), pya.DPoint(10.95, 9.69), pya.DPoint(10.95, 9.52)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 9.18), pya.DPoint(-0.18, 9.18), pya.DPoint(-0.18, 9.35), pya.DPoint(-0.35, 9.35), pya.DPoint(-0.35, 9.18)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 9.18), pya.DPoint(11.12, 9.18), pya.DPoint(11.12, 9.35), pya.DPoint(10.95, 9.35), pya.DPoint(10.95, 9.18)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 8.84), pya.DPoint(-0.18, 8.84), pya.DPoint(-0.18, 9.01), pya.DPoint(-0.35, 9.01), pya.DPoint(-0.35, 8.84)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 8.84), pya.DPoint(11.12, 8.84), pya.DPoint(11.12, 9.01), pya.DPoint(10.95, 9.01), pya.DPoint(10.95, 8.84)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 8.5), pya.DPoint(-0.18, 8.5), pya.DPoint(-0.18, 8.67), pya.DPoint(-0.35, 8.67), pya.DPoint(-0.35, 8.5)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 8.5), pya.DPoint(11.12, 8.5), pya.DPoint(11.12, 8.67), pya.DPoint(10.95, 8.67), pya.DPoint(10.95, 8.5)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 8.16), pya.DPoint(-0.18, 8.16), pya.DPoint(-0.18, 8.33), pya.DPoint(-0.35, 8.33), pya.DPoint(-0.35, 8.16)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 8.16), pya.DPoint(11.12, 8.16), pya.DPoint(11.12, 8.33), pya.DPoint(10.95, 8.33), pya.DPoint(10.95, 8.16)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 7.82), pya.DPoint(-0.18, 7.82), pya.DPoint(-0.18, 7.99), pya.DPoint(-0.35, 7.99), pya.DPoint(-0.35, 7.82)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 7.82), pya.DPoint(11.12, 7.82), pya.DPoint(11.12, 7.99), pya.DPoint(10.95, 7.99), pya.DPoint(10.95, 7.82)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 7.48), pya.DPoint(-0.18, 7.48), pya.DPoint(-0.18, 7.65), pya.DPoint(-0.35, 7.65), pya.DPoint(-0.35, 7.48)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 7.48), pya.DPoint(11.12, 7.48), pya.DPoint(11.12, 7.65), pya.DPoint(10.95, 7.65), pya.DPoint(10.95, 7.48)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 7.14), pya.DPoint(-0.18, 7.14), pya.DPoint(-0.18, 7.31), pya.DPoint(-0.35, 7.31), pya.DPoint(-0.35, 7.14)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 7.14), pya.DPoint(11.12, 7.14), pya.DPoint(11.12, 7.31), pya.DPoint(10.95, 7.31), pya.DPoint(10.95, 7.14)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 6.8), pya.DPoint(-0.18, 6.8), pya.DPoint(-0.18, 6.97), pya.DPoint(-0.35, 6.97), pya.DPoint(-0.35, 6.8)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 6.8), pya.DPoint(11.12, 6.8), pya.DPoint(11.12, 6.97), pya.DPoint(10.95, 6.97), pya.DPoint(10.95, 6.8)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 6.46), pya.DPoint(-0.18, 6.46), pya.DPoint(-0.18, 6.63), pya.DPoint(-0.35, 6.63), pya.DPoint(-0.35, 6.46)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 6.46), pya.DPoint(11.12, 6.46), pya.DPoint(11.12, 6.63), pya.DPoint(10.95, 6.63), pya.DPoint(10.95, 6.46)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 6.12), pya.DPoint(-0.18, 6.12), pya.DPoint(-0.18, 6.29), pya.DPoint(-0.35, 6.29), pya.DPoint(-0.35, 6.12)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 6.12), pya.DPoint(11.12, 6.12), pya.DPoint(11.12, 6.29), pya.DPoint(10.95, 6.29), pya.DPoint(10.95, 6.12)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 5.78), pya.DPoint(-0.18, 5.78), pya.DPoint(-0.18, 5.95), pya.DPoint(-0.35, 5.95), pya.DPoint(-0.35, 5.78)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 5.78), pya.DPoint(11.12, 5.78), pya.DPoint(11.12, 5.95), pya.DPoint(10.95, 5.95), pya.DPoint(10.95, 5.78)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 5.44), pya.DPoint(-0.18, 5.44), pya.DPoint(-0.18, 5.61), pya.DPoint(-0.35, 5.61), pya.DPoint(-0.35, 5.44)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 5.44), pya.DPoint(11.12, 5.44), pya.DPoint(11.12, 5.61), pya.DPoint(10.95, 5.61), pya.DPoint(10.95, 5.44)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 5.1), pya.DPoint(-0.18, 5.1), pya.DPoint(-0.18, 5.27), pya.DPoint(-0.35, 5.27), pya.DPoint(-0.35, 5.1)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 5.1), pya.DPoint(11.12, 5.1), pya.DPoint(11.12, 5.27), pya.DPoint(10.95, 5.27), pya.DPoint(10.95, 5.1)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 4.76), pya.DPoint(-0.18, 4.76), pya.DPoint(-0.18, 4.93), pya.DPoint(-0.35, 4.93), pya.DPoint(-0.35, 4.76)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 4.76), pya.DPoint(11.12, 4.76), pya.DPoint(11.12, 4.93), pya.DPoint(10.95, 4.93), pya.DPoint(10.95, 4.76)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 4.42), pya.DPoint(-0.18, 4.42), pya.DPoint(-0.18, 4.59), pya.DPoint(-0.35, 4.59), pya.DPoint(-0.35, 4.42)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 4.42), pya.DPoint(11.12, 4.42), pya.DPoint(11.12, 4.59), pya.DPoint(10.95, 4.59), pya.DPoint(10.95, 4.42)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 4.08), pya.DPoint(-0.18, 4.08), pya.DPoint(-0.18, 4.25), pya.DPoint(-0.35, 4.25), pya.DPoint(-0.35, 4.08)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 4.08), pya.DPoint(11.12, 4.08), pya.DPoint(11.12, 4.25), pya.DPoint(10.95, 4.25), pya.DPoint(10.95, 4.08)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 3.74), pya.DPoint(-0.18, 3.74), pya.DPoint(-0.18, 3.91), pya.DPoint(-0.35, 3.91), pya.DPoint(-0.35, 3.74)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 3.74), pya.DPoint(11.12, 3.74), pya.DPoint(11.12, 3.91), pya.DPoint(10.95, 3.91), pya.DPoint(10.95, 3.74)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 3.4), pya.DPoint(-0.18, 3.4), pya.DPoint(-0.18, 3.57), pya.DPoint(-0.35, 3.57), pya.DPoint(-0.35, 3.4)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 3.4), pya.DPoint(11.12, 3.4), pya.DPoint(11.12, 3.57), pya.DPoint(10.95, 3.57), pya.DPoint(10.95, 3.4)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 3.06), pya.DPoint(-0.18, 3.06), pya.DPoint(-0.18, 3.23), pya.DPoint(-0.35, 3.23), pya.DPoint(-0.35, 3.06)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 3.06), pya.DPoint(11.12, 3.06), pya.DPoint(11.12, 3.23), pya.DPoint(10.95, 3.23), pya.DPoint(10.95, 3.06)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 2.72), pya.DPoint(-0.18, 2.72), pya.DPoint(-0.18, 2.89), pya.DPoint(-0.35, 2.89), pya.DPoint(-0.35, 2.72)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 2.72), pya.DPoint(11.12, 2.72), pya.DPoint(11.12, 2.89), pya.DPoint(10.95, 2.89), pya.DPoint(10.95, 2.72)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 2.38), pya.DPoint(-0.18, 2.38), pya.DPoint(-0.18, 2.55), pya.DPoint(-0.35, 2.55), pya.DPoint(-0.35, 2.38)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 2.38), pya.DPoint(11.12, 2.38), pya.DPoint(11.12, 2.55), pya.DPoint(10.95, 2.55), pya.DPoint(10.95, 2.38)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 2.04), pya.DPoint(-0.18, 2.04), pya.DPoint(-0.18, 2.21), pya.DPoint(-0.35, 2.21), pya.DPoint(-0.35, 2.04)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 2.04), pya.DPoint(11.12, 2.04), pya.DPoint(11.12, 2.21), pya.DPoint(10.95, 2.21), pya.DPoint(10.95, 2.04)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 1.7), pya.DPoint(-0.18, 1.7), pya.DPoint(-0.18, 1.87), pya.DPoint(-0.35, 1.87), pya.DPoint(-0.35, 1.7)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 1.7), pya.DPoint(11.12, 1.7), pya.DPoint(11.12, 1.87), pya.DPoint(10.95, 1.87), pya.DPoint(10.95, 1.7)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 1.36), pya.DPoint(-0.18, 1.36), pya.DPoint(-0.18, 1.53), pya.DPoint(-0.35, 1.53), pya.DPoint(-0.35, 1.36)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 1.36), pya.DPoint(11.12, 1.36), pya.DPoint(11.12, 1.53), pya.DPoint(10.95, 1.53), pya.DPoint(10.95, 1.36)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 1.02), pya.DPoint(-0.18, 1.02), pya.DPoint(-0.18, 1.19), pya.DPoint(-0.35, 1.19), pya.DPoint(-0.35, 1.02)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 1.02), pya.DPoint(11.12, 1.02), pya.DPoint(11.12, 1.19), pya.DPoint(10.95, 1.19), pya.DPoint(10.95, 1.02)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 0.68), pya.DPoint(-0.18, 0.68), pya.DPoint(-0.18, 0.85), pya.DPoint(-0.35, 0.85), pya.DPoint(-0.35, 0.68)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 0.68), pya.DPoint(11.12, 0.68), pya.DPoint(11.12, 0.85), pya.DPoint(10.95, 0.85), pya.DPoint(10.95, 0.68)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 0.34), pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 0.51), pya.DPoint(-0.35, 0.51), pya.DPoint(-0.35, 0.34)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 0.34), pya.DPoint(11.12, 0.34), pya.DPoint(11.12, 0.51), pya.DPoint(10.95, 0.51), pya.DPoint(10.95, 0.34)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 0), pya.DPoint(-0.18, 0), pya.DPoint(-0.18, 0.17), pya.DPoint(-0.35, 0.17), pya.DPoint(-0.35, 0)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, 0), pya.DPoint(11.12, 0), pya.DPoint(11.12, 0.17), pya.DPoint(10.95, 0.17), pya.DPoint(10.95, 0)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.14, -0.47), pya.DPoint(0.03, -0.47), pya.DPoint(0.03, -0.3), pya.DPoint(-0.14, -0.3), pya.DPoint(-0.14, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.2, -0.47), pya.DPoint(0.37, -0.47), pya.DPoint(0.37, -0.3), pya.DPoint(0.2, -0.3), pya.DPoint(0.2, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.54, -0.47), pya.DPoint(0.71, -0.47), pya.DPoint(0.71, -0.3), pya.DPoint(0.54, -0.3), pya.DPoint(0.54, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.88, -0.47), pya.DPoint(1.05, -0.47), pya.DPoint(1.05, -0.3), pya.DPoint(0.88, -0.3), pya.DPoint(0.88, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.22, -0.47), pya.DPoint(1.39, -0.47), pya.DPoint(1.39, -0.3), pya.DPoint(1.22, -0.3), pya.DPoint(1.22, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.56, -0.47), pya.DPoint(1.73, -0.47), pya.DPoint(1.73, -0.3), pya.DPoint(1.56, -0.3), pya.DPoint(1.56, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.9, -0.47), pya.DPoint(2.07, -0.47), pya.DPoint(2.07, -0.3), pya.DPoint(1.9, -0.3), pya.DPoint(1.9, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.24, -0.47), pya.DPoint(2.41, -0.47), pya.DPoint(2.41, -0.3), pya.DPoint(2.24, -0.3), pya.DPoint(2.24, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.58, -0.47), pya.DPoint(2.75, -0.47), pya.DPoint(2.75, -0.3), pya.DPoint(2.58, -0.3), pya.DPoint(2.58, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.92, -0.47), pya.DPoint(3.09, -0.47), pya.DPoint(3.09, -0.3), pya.DPoint(2.92, -0.3), pya.DPoint(2.92, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.26, -0.47), pya.DPoint(3.43, -0.47), pya.DPoint(3.43, -0.3), pya.DPoint(3.26, -0.3), pya.DPoint(3.26, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.6, -0.47), pya.DPoint(3.77, -0.47), pya.DPoint(3.77, -0.3), pya.DPoint(3.6, -0.3), pya.DPoint(3.6, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.94, -0.47), pya.DPoint(4.11, -0.47), pya.DPoint(4.11, -0.3), pya.DPoint(3.94, -0.3), pya.DPoint(3.94, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.28, -0.47), pya.DPoint(4.45, -0.47), pya.DPoint(4.45, -0.3), pya.DPoint(4.28, -0.3), pya.DPoint(4.28, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.62, -0.47), pya.DPoint(4.79, -0.47), pya.DPoint(4.79, -0.3), pya.DPoint(4.62, -0.3), pya.DPoint(4.62, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.96, -0.47), pya.DPoint(5.13, -0.47), pya.DPoint(5.13, -0.3), pya.DPoint(4.96, -0.3), pya.DPoint(4.96, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.3, -0.47), pya.DPoint(5.47, -0.47), pya.DPoint(5.47, -0.3), pya.DPoint(5.3, -0.3), pya.DPoint(5.3, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.64, -0.47), pya.DPoint(5.81, -0.47), pya.DPoint(5.81, -0.3), pya.DPoint(5.64, -0.3), pya.DPoint(5.64, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.98, -0.47), pya.DPoint(6.15, -0.47), pya.DPoint(6.15, -0.3), pya.DPoint(5.98, -0.3), pya.DPoint(5.98, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.32, -0.47), pya.DPoint(6.49, -0.47), pya.DPoint(6.49, -0.3), pya.DPoint(6.32, -0.3), pya.DPoint(6.32, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, -0.47), pya.DPoint(6.83, -0.47), pya.DPoint(6.83, -0.3), pya.DPoint(6.66, -0.3), pya.DPoint(6.66, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7, -0.47), pya.DPoint(7.17, -0.47), pya.DPoint(7.17, -0.3), pya.DPoint(7, -0.3), pya.DPoint(7, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.34, -0.47), pya.DPoint(7.51, -0.47), pya.DPoint(7.51, -0.3), pya.DPoint(7.34, -0.3), pya.DPoint(7.34, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.68, -0.47), pya.DPoint(7.85, -0.47), pya.DPoint(7.85, -0.3), pya.DPoint(7.68, -0.3), pya.DPoint(7.68, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.02, -0.47), pya.DPoint(8.19, -0.47), pya.DPoint(8.19, -0.3), pya.DPoint(8.02, -0.3), pya.DPoint(8.02, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, -0.47), pya.DPoint(8.53, -0.47), pya.DPoint(8.53, -0.3), pya.DPoint(8.36, -0.3), pya.DPoint(8.36, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.7, -0.47), pya.DPoint(8.87, -0.47), pya.DPoint(8.87, -0.3), pya.DPoint(8.7, -0.3), pya.DPoint(8.7, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.04, -0.47), pya.DPoint(9.21, -0.47), pya.DPoint(9.21, -0.3), pya.DPoint(9.04, -0.3), pya.DPoint(9.04, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.38, -0.47), pya.DPoint(9.55, -0.47), pya.DPoint(9.55, -0.3), pya.DPoint(9.38, -0.3), pya.DPoint(9.38, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.72, -0.47), pya.DPoint(9.89, -0.47), pya.DPoint(9.89, -0.3), pya.DPoint(9.72, -0.3), pya.DPoint(9.72, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.06, -0.47), pya.DPoint(10.23, -0.47), pya.DPoint(10.23, -0.3), pya.DPoint(10.06, -0.3), pya.DPoint(10.06, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.4, -0.47), pya.DPoint(10.57, -0.47), pya.DPoint(10.57, -0.3), pya.DPoint(10.4, -0.3), pya.DPoint(10.4, -0.47)]))
cell_nmos_1x80_2x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.74, -0.47), pya.DPoint(10.91, -0.47), pya.DPoint(10.91, -0.3), pya.DPoint(10.74, -0.3), pya.DPoint(10.74, -0.47)]))
cell_nmos_1x80_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, 20.87), pya.DPoint(11.12, 20.87), pya.DPoint(11.12, 21.04), pya.DPoint(-0.35, 21.04), pya.DPoint(-0.35, 20.87)]))
cell_nmos_1x80_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.3), pya.DPoint(-0.18, -0.3), pya.DPoint(-0.18, 20.87), pya.DPoint(-0.35, 20.87), pya.DPoint(-0.35, -0.3)]))
cell_nmos_1x80_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.95, -0.3), pya.DPoint(11.12, -0.3), pya.DPoint(11.12, 20.87), pya.DPoint(10.95, 20.87), pya.DPoint(10.95, -0.3)]))
cell_nmos_1x80_2x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.47), pya.DPoint(11.12, -0.47), pya.DPoint(11.12, -0.3), pya.DPoint(-0.35, -0.3), pya.DPoint(-0.35, -0.47)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.44, 21.09), pya.DPoint(5.25, 21.09), pya.DPoint(5.25, 21.35), pya.DPoint(0.44, 21.35), pya.DPoint(0.44, 21.09)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.44, 20.32), pya.DPoint(1.44, 20.32), pya.DPoint(1.44, 21.09), pya.DPoint(0.44, 21.09), pya.DPoint(0.44, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.71, 20.69), pya.DPoint(3.98, 20.69), pya.DPoint(3.98, 20.95), pya.DPoint(1.71, 20.95), pya.DPoint(1.71, 20.69)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.71, 20.32), pya.DPoint(2.71, 20.32), pya.DPoint(2.71, 20.69), pya.DPoint(1.71, 20.69), pya.DPoint(1.71, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.98, 20.32), pya.DPoint(3.98, 20.32), pya.DPoint(3.98, 20.69), pya.DPoint(2.98, 20.69), pya.DPoint(2.98, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.25, 20.32), pya.DPoint(5.25, 20.32), pya.DPoint(5.25, 21.09), pya.DPoint(4.25, 21.09), pya.DPoint(4.25, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.52, 21.09), pya.DPoint(10.33, 21.09), pya.DPoint(10.33, 21.35), pya.DPoint(5.52, 21.35), pya.DPoint(5.52, 21.09)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.52, 20.32), pya.DPoint(6.52, 20.32), pya.DPoint(6.52, 21.09), pya.DPoint(5.52, 21.09), pya.DPoint(5.52, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.79, 20.69), pya.DPoint(9.06, 20.69), pya.DPoint(9.06, 20.95), pya.DPoint(6.79, 20.95), pya.DPoint(6.79, 20.69)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.79, 20.32), pya.DPoint(7.79, 20.32), pya.DPoint(7.79, 20.69), pya.DPoint(6.79, 20.69), pya.DPoint(6.79, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.06, 20.32), pya.DPoint(9.06, 20.32), pya.DPoint(9.06, 20.69), pya.DPoint(8.06, 20.69), pya.DPoint(8.06, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.33, 20.32), pya.DPoint(10.33, 20.32), pya.DPoint(10.33, 21.09), pya.DPoint(9.33, 21.09), pya.DPoint(9.33, 20.32)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.04, 0.28), pya.DPoint(0.28, 0.28), pya.DPoint(0.28, 20.3), pya.DPoint(-0.04, 20.3), pya.DPoint(-0.04, 0.28)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(10.49, 0.28), pya.DPoint(10.81, 0.28), pya.DPoint(10.81, 20.3), pya.DPoint(10.49, 20.3), pya.DPoint(10.49, 0.28)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.98, -0.51), pya.DPoint(3.98, -0.51), pya.DPoint(3.98, 0.26), pya.DPoint(2.98, 0.26), pya.DPoint(2.98, -0.51)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.25, -0.11), pya.DPoint(5.25, -0.11), pya.DPoint(5.25, 0.26), pya.DPoint(4.25, 0.26), pya.DPoint(4.25, -0.11)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.52, -0.11), pya.DPoint(6.52, -0.11), pya.DPoint(6.52, 0.26), pya.DPoint(5.52, 0.26), pya.DPoint(5.52, -0.11)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.25, -0.37), pya.DPoint(6.52, -0.37), pya.DPoint(6.52, -0.11), pya.DPoint(4.25, -0.11), pya.DPoint(4.25, -0.37)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.79, -0.51), pya.DPoint(7.79, -0.51), pya.DPoint(7.79, 0.26), pya.DPoint(6.79, 0.26), pya.DPoint(6.79, -0.51)]))
cell_nmos_1x80_2x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.98, -0.77), pya.DPoint(7.79, -0.77), pya.DPoint(7.79, -0.51), pya.DPoint(2.98, -0.51), pya.DPoint(2.98, -0.77)]))

# === pmos_7x ===
cell_pmos_7x.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.62, -0.97), pya.DPoint(4.62, -0.97), pya.DPoint(4.62, 0.97), pya.DPoint(-4.62, 0.97), pya.DPoint(-4.62, -0.97)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, -0.79), pya.DPoint(-3.31, -0.79), pya.DPoint(-3.31, 0.79), pya.DPoint(-4.31, 0.79), pya.DPoint(-4.31, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -0.79), pya.DPoint(-2.04, -0.79), pya.DPoint(-2.04, 0.79), pya.DPoint(-3.04, 0.79), pya.DPoint(-3.04, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -0.79), pya.DPoint(-0.77, -0.79), pya.DPoint(-0.77, 0.79), pya.DPoint(-1.77, 0.79), pya.DPoint(-1.77, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.79), pya.DPoint(0.5, -0.79), pya.DPoint(0.5, 0.79), pya.DPoint(-0.5, 0.79), pya.DPoint(-0.5, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -0.79), pya.DPoint(1.77, -0.79), pya.DPoint(1.77, 0.79), pya.DPoint(0.77, 0.79), pya.DPoint(0.77, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -0.79), pya.DPoint(3.04, -0.79), pya.DPoint(3.04, 0.79), pya.DPoint(2.04, 0.79), pya.DPoint(2.04, -0.79)]))
cell_pmos_7x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, -0.79), pya.DPoint(4.31, -0.79), pya.DPoint(4.31, 0.79), pya.DPoint(3.31, 0.79), pya.DPoint(3.31, -0.79)]))
cell_pmos_7x.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.435, -0.915), pya.DPoint(4.435, -0.915), pya.DPoint(4.435, 0.915), pya.DPoint(-4.435, 0.915), pya.DPoint(-4.435, -0.915)]))
cell_pmos_7x.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.8, -0.5), pya.DPoint(4.8, -0.5), pya.DPoint(4.8, 0.5), pya.DPoint(-4.8, 0.5), pya.DPoint(-4.8, -0.5)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.235, 0.56), pya.DPoint(-4.065, 0.56), pya.DPoint(-4.065, 0.73), pya.DPoint(-4.235, 0.73), pya.DPoint(-4.235, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.895, 0.56), pya.DPoint(-3.725, 0.56), pya.DPoint(-3.725, 0.73), pya.DPoint(-3.895, 0.73), pya.DPoint(-3.895, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.555, 0.56), pya.DPoint(-3.385, 0.56), pya.DPoint(-3.385, 0.73), pya.DPoint(-3.555, 0.73), pya.DPoint(-3.555, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, 0.56), pya.DPoint(-2.795, 0.56), pya.DPoint(-2.795, 0.73), pya.DPoint(-2.965, 0.73), pya.DPoint(-2.965, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, 0.56), pya.DPoint(-2.455, 0.56), pya.DPoint(-2.455, 0.73), pya.DPoint(-2.625, 0.73), pya.DPoint(-2.625, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, 0.56), pya.DPoint(-2.115, 0.56), pya.DPoint(-2.115, 0.73), pya.DPoint(-2.285, 0.73), pya.DPoint(-2.285, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, 0.56), pya.DPoint(-1.525, 0.56), pya.DPoint(-1.525, 0.73), pya.DPoint(-1.695, 0.73), pya.DPoint(-1.695, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, 0.56), pya.DPoint(-1.185, 0.56), pya.DPoint(-1.185, 0.73), pya.DPoint(-1.355, 0.73), pya.DPoint(-1.355, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, 0.56), pya.DPoint(-0.845, 0.56), pya.DPoint(-0.845, 0.73), pya.DPoint(-1.015, 0.73), pya.DPoint(-1.015, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, 0.56), pya.DPoint(-0.255, 0.56), pya.DPoint(-0.255, 0.73), pya.DPoint(-0.425, 0.73), pya.DPoint(-0.425, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 0.56), pya.DPoint(0.085, 0.56), pya.DPoint(0.085, 0.73), pya.DPoint(-0.085, 0.73), pya.DPoint(-0.085, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, 0.56), pya.DPoint(0.425, 0.56), pya.DPoint(0.425, 0.73), pya.DPoint(0.255, 0.73), pya.DPoint(0.255, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, 0.56), pya.DPoint(1.015, 0.56), pya.DPoint(1.015, 0.73), pya.DPoint(0.845, 0.73), pya.DPoint(0.845, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, 0.56), pya.DPoint(1.355, 0.56), pya.DPoint(1.355, 0.73), pya.DPoint(1.185, 0.73), pya.DPoint(1.185, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, 0.56), pya.DPoint(1.695, 0.56), pya.DPoint(1.695, 0.73), pya.DPoint(1.525, 0.73), pya.DPoint(1.525, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, 0.56), pya.DPoint(2.285, 0.56), pya.DPoint(2.285, 0.73), pya.DPoint(2.115, 0.73), pya.DPoint(2.115, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, 0.56), pya.DPoint(2.625, 0.56), pya.DPoint(2.625, 0.73), pya.DPoint(2.455, 0.73), pya.DPoint(2.455, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, 0.56), pya.DPoint(2.965, 0.56), pya.DPoint(2.965, 0.73), pya.DPoint(2.795, 0.73), pya.DPoint(2.795, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.385, 0.56), pya.DPoint(3.555, 0.56), pya.DPoint(3.555, 0.73), pya.DPoint(3.385, 0.73), pya.DPoint(3.385, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.725, 0.56), pya.DPoint(3.895, 0.56), pya.DPoint(3.895, 0.73), pya.DPoint(3.725, 0.73), pya.DPoint(3.725, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.065, 0.56), pya.DPoint(4.235, 0.56), pya.DPoint(4.235, 0.73), pya.DPoint(4.065, 0.73), pya.DPoint(4.065, 0.56)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, 0.255), pya.DPoint(-4.55, 0.255), pya.DPoint(-4.55, 0.425), pya.DPoint(-4.72, 0.425), pya.DPoint(-4.72, 0.255)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, 0.255), pya.DPoint(4.72, 0.255), pya.DPoint(4.72, 0.425), pya.DPoint(4.55, 0.425), pya.DPoint(4.55, 0.255)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, -0.085), pya.DPoint(-4.55, -0.085), pya.DPoint(-4.55, 0.085), pya.DPoint(-4.72, 0.085), pya.DPoint(-4.72, -0.085)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, -0.085), pya.DPoint(4.72, -0.085), pya.DPoint(4.72, 0.085), pya.DPoint(4.55, 0.085), pya.DPoint(4.55, -0.085)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, -0.425), pya.DPoint(-4.55, -0.425), pya.DPoint(-4.55, -0.255), pya.DPoint(-4.72, -0.255), pya.DPoint(-4.72, -0.425)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, -0.425), pya.DPoint(4.72, -0.425), pya.DPoint(4.72, -0.255), pya.DPoint(4.55, -0.255), pya.DPoint(4.55, -0.425)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.235, -0.73), pya.DPoint(-4.065, -0.73), pya.DPoint(-4.065, -0.56), pya.DPoint(-4.235, -0.56), pya.DPoint(-4.235, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.895, -0.73), pya.DPoint(-3.725, -0.73), pya.DPoint(-3.725, -0.56), pya.DPoint(-3.895, -0.56), pya.DPoint(-3.895, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.555, -0.73), pya.DPoint(-3.385, -0.73), pya.DPoint(-3.385, -0.56), pya.DPoint(-3.555, -0.56), pya.DPoint(-3.555, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, -0.73), pya.DPoint(-2.795, -0.73), pya.DPoint(-2.795, -0.56), pya.DPoint(-2.965, -0.56), pya.DPoint(-2.965, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, -0.73), pya.DPoint(-2.455, -0.73), pya.DPoint(-2.455, -0.56), pya.DPoint(-2.625, -0.56), pya.DPoint(-2.625, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, -0.73), pya.DPoint(-2.115, -0.73), pya.DPoint(-2.115, -0.56), pya.DPoint(-2.285, -0.56), pya.DPoint(-2.285, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, -0.73), pya.DPoint(-1.525, -0.73), pya.DPoint(-1.525, -0.56), pya.DPoint(-1.695, -0.56), pya.DPoint(-1.695, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, -0.73), pya.DPoint(-1.185, -0.73), pya.DPoint(-1.185, -0.56), pya.DPoint(-1.355, -0.56), pya.DPoint(-1.355, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, -0.73), pya.DPoint(-0.845, -0.73), pya.DPoint(-0.845, -0.56), pya.DPoint(-1.015, -0.56), pya.DPoint(-1.015, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, -0.73), pya.DPoint(-0.255, -0.73), pya.DPoint(-0.255, -0.56), pya.DPoint(-0.425, -0.56), pya.DPoint(-0.425, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, -0.73), pya.DPoint(0.085, -0.73), pya.DPoint(0.085, -0.56), pya.DPoint(-0.085, -0.56), pya.DPoint(-0.085, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, -0.73), pya.DPoint(0.425, -0.73), pya.DPoint(0.425, -0.56), pya.DPoint(0.255, -0.56), pya.DPoint(0.255, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, -0.73), pya.DPoint(1.015, -0.73), pya.DPoint(1.015, -0.56), pya.DPoint(0.845, -0.56), pya.DPoint(0.845, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, -0.73), pya.DPoint(1.355, -0.73), pya.DPoint(1.355, -0.56), pya.DPoint(1.185, -0.56), pya.DPoint(1.185, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, -0.73), pya.DPoint(1.695, -0.73), pya.DPoint(1.695, -0.56), pya.DPoint(1.525, -0.56), pya.DPoint(1.525, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, -0.73), pya.DPoint(2.285, -0.73), pya.DPoint(2.285, -0.56), pya.DPoint(2.115, -0.56), pya.DPoint(2.115, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, -0.73), pya.DPoint(2.625, -0.73), pya.DPoint(2.625, -0.56), pya.DPoint(2.455, -0.56), pya.DPoint(2.455, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, -0.73), pya.DPoint(2.965, -0.73), pya.DPoint(2.965, -0.56), pya.DPoint(2.795, -0.56), pya.DPoint(2.795, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.385, -0.73), pya.DPoint(3.555, -0.73), pya.DPoint(3.555, -0.56), pya.DPoint(3.385, -0.56), pya.DPoint(3.385, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.725, -0.73), pya.DPoint(3.895, -0.73), pya.DPoint(3.895, -0.56), pya.DPoint(3.725, -0.56), pya.DPoint(3.725, -0.73)]))
cell_pmos_7x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.065, -0.73), pya.DPoint(4.235, -0.73), pya.DPoint(4.235, -0.56), pya.DPoint(4.065, -0.56), pya.DPoint(4.065, -0.73)]))
cell_pmos_7x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.82, -0.525), pya.DPoint(-4.45, -0.525), pya.DPoint(-4.45, 0.525), pya.DPoint(-4.82, 0.525), pya.DPoint(-4.82, -0.525)]))
cell_pmos_7x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(4.45, -0.525), pya.DPoint(4.82, -0.525), pya.DPoint(4.82, 0.525), pya.DPoint(4.45, 0.525), pya.DPoint(4.45, -0.525)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.33, 0.56), pya.DPoint(-3.29, 0.56), pya.DPoint(-3.29, 0.73), pya.DPoint(-4.33, 0.73), pya.DPoint(-4.33, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, 0.56), pya.DPoint(-2.02, 0.56), pya.DPoint(-2.02, 0.73), pya.DPoint(-3.06, 0.73), pya.DPoint(-3.06, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, 0.56), pya.DPoint(-0.75, 0.56), pya.DPoint(-0.75, 0.73), pya.DPoint(-1.79, 0.73), pya.DPoint(-1.79, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, 0.56), pya.DPoint(0.52, 0.56), pya.DPoint(0.52, 0.73), pya.DPoint(-0.52, 0.73), pya.DPoint(-0.52, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, 0.56), pya.DPoint(1.79, 0.56), pya.DPoint(1.79, 0.73), pya.DPoint(0.75, 0.73), pya.DPoint(0.75, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, 0.56), pya.DPoint(3.06, 0.56), pya.DPoint(3.06, 0.73), pya.DPoint(2.02, 0.73), pya.DPoint(2.02, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.29, 0.56), pya.DPoint(4.33, 0.56), pya.DPoint(4.33, 0.73), pya.DPoint(3.29, 0.73), pya.DPoint(3.29, 0.56)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, -0.53), pya.DPoint(-4.55, -0.53), pya.DPoint(-4.55, 0.53), pya.DPoint(-4.72, 0.53), pya.DPoint(-4.72, -0.53)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, -0.53), pya.DPoint(4.72, -0.53), pya.DPoint(4.72, 0.53), pya.DPoint(4.55, 0.53), pya.DPoint(4.55, -0.53)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.33, -0.73), pya.DPoint(-3.29, -0.73), pya.DPoint(-3.29, -0.56), pya.DPoint(-4.33, -0.56), pya.DPoint(-4.33, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, -0.73), pya.DPoint(-2.02, -0.73), pya.DPoint(-2.02, -0.56), pya.DPoint(-3.06, -0.56), pya.DPoint(-3.06, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, -0.73), pya.DPoint(-0.75, -0.73), pya.DPoint(-0.75, -0.56), pya.DPoint(-1.79, -0.56), pya.DPoint(-1.79, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, -0.73), pya.DPoint(0.52, -0.73), pya.DPoint(0.52, -0.56), pya.DPoint(-0.52, -0.56), pya.DPoint(-0.52, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, -0.73), pya.DPoint(1.79, -0.73), pya.DPoint(1.79, -0.56), pya.DPoint(0.75, -0.56), pya.DPoint(0.75, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, -0.73), pya.DPoint(3.06, -0.73), pya.DPoint(3.06, -0.56), pya.DPoint(2.02, -0.56), pya.DPoint(2.02, -0.73)]))
cell_pmos_7x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.29, -0.73), pya.DPoint(4.33, -0.73), pya.DPoint(4.33, -0.56), pya.DPoint(3.29, -0.56), pya.DPoint(3.29, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.075, 0.56), pya.DPoint(-3.905, 0.56), pya.DPoint(-3.905, 0.73), pya.DPoint(-4.075, 0.73), pya.DPoint(-4.075, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.715, 0.56), pya.DPoint(-3.545, 0.56), pya.DPoint(-3.545, 0.73), pya.DPoint(-3.715, 0.73), pya.DPoint(-3.715, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, 0.56), pya.DPoint(-2.635, 0.56), pya.DPoint(-2.635, 0.73), pya.DPoint(-2.805, 0.73), pya.DPoint(-2.805, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, 0.56), pya.DPoint(-2.275, 0.56), pya.DPoint(-2.275, 0.73), pya.DPoint(-2.445, 0.73), pya.DPoint(-2.445, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, 0.56), pya.DPoint(-1.365, 0.56), pya.DPoint(-1.365, 0.73), pya.DPoint(-1.535, 0.73), pya.DPoint(-1.535, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, 0.56), pya.DPoint(-1.005, 0.56), pya.DPoint(-1.005, 0.73), pya.DPoint(-1.175, 0.73), pya.DPoint(-1.175, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, 0.56), pya.DPoint(-0.095, 0.56), pya.DPoint(-0.095, 0.73), pya.DPoint(-0.265, 0.73), pya.DPoint(-0.265, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, 0.56), pya.DPoint(0.265, 0.56), pya.DPoint(0.265, 0.73), pya.DPoint(0.095, 0.73), pya.DPoint(0.095, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, 0.56), pya.DPoint(1.175, 0.56), pya.DPoint(1.175, 0.73), pya.DPoint(1.005, 0.73), pya.DPoint(1.005, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, 0.56), pya.DPoint(1.535, 0.56), pya.DPoint(1.535, 0.73), pya.DPoint(1.365, 0.73), pya.DPoint(1.365, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, 0.56), pya.DPoint(2.445, 0.56), pya.DPoint(2.445, 0.73), pya.DPoint(2.275, 0.73), pya.DPoint(2.275, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, 0.56), pya.DPoint(2.805, 0.56), pya.DPoint(2.805, 0.73), pya.DPoint(2.635, 0.73), pya.DPoint(2.635, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.545, 0.56), pya.DPoint(3.715, 0.56), pya.DPoint(3.715, 0.73), pya.DPoint(3.545, 0.73), pya.DPoint(3.545, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.905, 0.56), pya.DPoint(4.075, 0.56), pya.DPoint(4.075, 0.73), pya.DPoint(3.905, 0.73), pya.DPoint(3.905, 0.56)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, 0.275), pya.DPoint(-4.55, 0.275), pya.DPoint(-4.55, 0.445), pya.DPoint(-4.72, 0.445), pya.DPoint(-4.72, 0.275)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, 0.275), pya.DPoint(4.72, 0.275), pya.DPoint(4.72, 0.445), pya.DPoint(4.55, 0.445), pya.DPoint(4.55, 0.275)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, -0.085), pya.DPoint(-4.55, -0.085), pya.DPoint(-4.55, 0.085), pya.DPoint(-4.72, 0.085), pya.DPoint(-4.72, -0.085)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, -0.085), pya.DPoint(4.72, -0.085), pya.DPoint(4.72, 0.085), pya.DPoint(4.55, 0.085), pya.DPoint(4.55, -0.085)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.72, -0.445), pya.DPoint(-4.55, -0.445), pya.DPoint(-4.55, -0.275), pya.DPoint(-4.72, -0.275), pya.DPoint(-4.72, -0.445)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.55, -0.445), pya.DPoint(4.72, -0.445), pya.DPoint(4.72, -0.275), pya.DPoint(4.55, -0.275), pya.DPoint(4.55, -0.445)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.075, -0.73), pya.DPoint(-3.905, -0.73), pya.DPoint(-3.905, -0.56), pya.DPoint(-4.075, -0.56), pya.DPoint(-4.075, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.715, -0.73), pya.DPoint(-3.545, -0.73), pya.DPoint(-3.545, -0.56), pya.DPoint(-3.715, -0.56), pya.DPoint(-3.715, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, -0.73), pya.DPoint(-2.635, -0.73), pya.DPoint(-2.635, -0.56), pya.DPoint(-2.805, -0.56), pya.DPoint(-2.805, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, -0.73), pya.DPoint(-2.275, -0.73), pya.DPoint(-2.275, -0.56), pya.DPoint(-2.445, -0.56), pya.DPoint(-2.445, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, -0.73), pya.DPoint(-1.365, -0.73), pya.DPoint(-1.365, -0.56), pya.DPoint(-1.535, -0.56), pya.DPoint(-1.535, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, -0.73), pya.DPoint(-1.005, -0.73), pya.DPoint(-1.005, -0.56), pya.DPoint(-1.175, -0.56), pya.DPoint(-1.175, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, -0.73), pya.DPoint(-0.095, -0.73), pya.DPoint(-0.095, -0.56), pya.DPoint(-0.265, -0.56), pya.DPoint(-0.265, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, -0.73), pya.DPoint(0.265, -0.73), pya.DPoint(0.265, -0.56), pya.DPoint(0.095, -0.56), pya.DPoint(0.095, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, -0.73), pya.DPoint(1.175, -0.73), pya.DPoint(1.175, -0.56), pya.DPoint(1.005, -0.56), pya.DPoint(1.005, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, -0.73), pya.DPoint(1.535, -0.73), pya.DPoint(1.535, -0.56), pya.DPoint(1.365, -0.56), pya.DPoint(1.365, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, -0.73), pya.DPoint(2.445, -0.73), pya.DPoint(2.445, -0.56), pya.DPoint(2.275, -0.56), pya.DPoint(2.275, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, -0.73), pya.DPoint(2.805, -0.73), pya.DPoint(2.805, -0.56), pya.DPoint(2.635, -0.56), pya.DPoint(2.635, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.545, -0.73), pya.DPoint(3.715, -0.73), pya.DPoint(3.715, -0.56), pya.DPoint(3.545, -0.56), pya.DPoint(3.545, -0.73)]))
cell_pmos_7x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.905, -0.73), pya.DPoint(4.075, -0.73), pya.DPoint(4.075, -0.56), pya.DPoint(3.905, -0.56), pya.DPoint(3.905, -0.73)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, 0.53), pya.DPoint(-3.31, 0.53), pya.DPoint(-3.31, 0.76), pya.DPoint(-4.31, 0.76), pya.DPoint(-4.31, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, 0.53), pya.DPoint(-2.04, 0.53), pya.DPoint(-2.04, 0.76), pya.DPoint(-3.04, 0.76), pya.DPoint(-3.04, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 0.53), pya.DPoint(-0.77, 0.53), pya.DPoint(-0.77, 0.76), pya.DPoint(-1.77, 0.76), pya.DPoint(-1.77, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, 0.53), pya.DPoint(0.5, 0.53), pya.DPoint(0.5, 0.76), pya.DPoint(-0.5, 0.76), pya.DPoint(-0.5, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, 0.53), pya.DPoint(1.77, 0.53), pya.DPoint(1.77, 0.76), pya.DPoint(0.77, 0.76), pya.DPoint(0.77, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, 0.53), pya.DPoint(3.04, 0.53), pya.DPoint(3.04, 0.76), pya.DPoint(2.04, 0.76), pya.DPoint(2.04, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, 0.53), pya.DPoint(4.31, 0.53), pya.DPoint(4.31, 0.76), pya.DPoint(3.31, 0.76), pya.DPoint(3.31, 0.53)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.75, -0.51), pya.DPoint(-4.52, -0.51), pya.DPoint(-4.52, 0.51), pya.DPoint(-4.75, 0.51), pya.DPoint(-4.75, -0.51)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.52, -0.51), pya.DPoint(4.75, -0.51), pya.DPoint(4.75, 0.51), pya.DPoint(4.52, 0.51), pya.DPoint(4.52, -0.51)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-4.31, -0.76), pya.DPoint(-3.31, -0.76), pya.DPoint(-3.31, -0.53), pya.DPoint(-4.31, -0.53), pya.DPoint(-4.31, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -0.76), pya.DPoint(-2.04, -0.76), pya.DPoint(-2.04, -0.53), pya.DPoint(-3.04, -0.53), pya.DPoint(-3.04, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -0.76), pya.DPoint(-0.77, -0.76), pya.DPoint(-0.77, -0.53), pya.DPoint(-1.77, -0.53), pya.DPoint(-1.77, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.76), pya.DPoint(0.5, -0.76), pya.DPoint(0.5, -0.53), pya.DPoint(-0.5, -0.53), pya.DPoint(-0.5, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -0.76), pya.DPoint(1.77, -0.76), pya.DPoint(1.77, -0.53), pya.DPoint(0.77, -0.53), pya.DPoint(0.77, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -0.76), pya.DPoint(3.04, -0.76), pya.DPoint(3.04, -0.53), pya.DPoint(2.04, -0.53), pya.DPoint(2.04, -0.76)]))
cell_pmos_7x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.31, -0.76), pya.DPoint(4.31, -0.76), pya.DPoint(4.31, -0.53), pya.DPoint(3.31, -0.53), pya.DPoint(3.31, -0.76)]))

# === nmos_5x ===
cell_nmos_5x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -0.79), pya.DPoint(-2.04, -0.79), pya.DPoint(-2.04, 0.79), pya.DPoint(-3.04, 0.79), pya.DPoint(-3.04, -0.79)]))
cell_nmos_5x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -0.79), pya.DPoint(-0.77, -0.79), pya.DPoint(-0.77, 0.79), pya.DPoint(-1.77, 0.79), pya.DPoint(-1.77, -0.79)]))
cell_nmos_5x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.79), pya.DPoint(0.5, -0.79), pya.DPoint(0.5, 0.79), pya.DPoint(-0.5, 0.79), pya.DPoint(-0.5, -0.79)]))
cell_nmos_5x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -0.79), pya.DPoint(1.77, -0.79), pya.DPoint(1.77, 0.79), pya.DPoint(0.77, 0.79), pya.DPoint(0.77, -0.79)]))
cell_nmos_5x.shapes(L_diff_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -0.79), pya.DPoint(3.04, -0.79), pya.DPoint(3.04, 0.79), pya.DPoint(2.04, 0.79), pya.DPoint(2.04, -0.79)]))
cell_nmos_5x.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.165, -0.915), pya.DPoint(3.165, -0.915), pya.DPoint(3.165, 0.915), pya.DPoint(-3.165, 0.915), pya.DPoint(-3.165, -0.915)]))
cell_nmos_5x.shapes(L_poly_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.48, -0.5), pya.DPoint(3.48, -0.5), pya.DPoint(3.48, 0.5), pya.DPoint(-3.48, 0.5), pya.DPoint(-3.48, -0.5)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, 0.56), pya.DPoint(-2.795, 0.56), pya.DPoint(-2.795, 0.73), pya.DPoint(-2.965, 0.73), pya.DPoint(-2.965, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, 0.56), pya.DPoint(-2.455, 0.56), pya.DPoint(-2.455, 0.73), pya.DPoint(-2.625, 0.73), pya.DPoint(-2.625, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, 0.56), pya.DPoint(-2.115, 0.56), pya.DPoint(-2.115, 0.73), pya.DPoint(-2.285, 0.73), pya.DPoint(-2.285, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, 0.56), pya.DPoint(-1.525, 0.56), pya.DPoint(-1.525, 0.73), pya.DPoint(-1.695, 0.73), pya.DPoint(-1.695, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, 0.56), pya.DPoint(-1.185, 0.56), pya.DPoint(-1.185, 0.73), pya.DPoint(-1.355, 0.73), pya.DPoint(-1.355, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, 0.56), pya.DPoint(-0.845, 0.56), pya.DPoint(-0.845, 0.73), pya.DPoint(-1.015, 0.73), pya.DPoint(-1.015, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, 0.56), pya.DPoint(-0.255, 0.56), pya.DPoint(-0.255, 0.73), pya.DPoint(-0.425, 0.73), pya.DPoint(-0.425, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, 0.56), pya.DPoint(0.085, 0.56), pya.DPoint(0.085, 0.73), pya.DPoint(-0.085, 0.73), pya.DPoint(-0.085, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, 0.56), pya.DPoint(0.425, 0.56), pya.DPoint(0.425, 0.73), pya.DPoint(0.255, 0.73), pya.DPoint(0.255, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, 0.56), pya.DPoint(1.015, 0.56), pya.DPoint(1.015, 0.73), pya.DPoint(0.845, 0.73), pya.DPoint(0.845, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, 0.56), pya.DPoint(1.355, 0.56), pya.DPoint(1.355, 0.73), pya.DPoint(1.185, 0.73), pya.DPoint(1.185, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, 0.56), pya.DPoint(1.695, 0.56), pya.DPoint(1.695, 0.73), pya.DPoint(1.525, 0.73), pya.DPoint(1.525, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, 0.56), pya.DPoint(2.285, 0.56), pya.DPoint(2.285, 0.73), pya.DPoint(2.115, 0.73), pya.DPoint(2.115, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, 0.56), pya.DPoint(2.625, 0.56), pya.DPoint(2.625, 0.73), pya.DPoint(2.455, 0.73), pya.DPoint(2.455, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, 0.56), pya.DPoint(2.965, 0.56), pya.DPoint(2.965, 0.73), pya.DPoint(2.795, 0.73), pya.DPoint(2.795, 0.56)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, 0.255), pya.DPoint(-3.23, 0.255), pya.DPoint(-3.23, 0.425), pya.DPoint(-3.4, 0.425), pya.DPoint(-3.4, 0.255)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, 0.255), pya.DPoint(3.4, 0.255), pya.DPoint(3.4, 0.425), pya.DPoint(3.23, 0.425), pya.DPoint(3.23, 0.255)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, -0.085), pya.DPoint(-3.23, -0.085), pya.DPoint(-3.23, 0.085), pya.DPoint(-3.4, 0.085), pya.DPoint(-3.4, -0.085)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, -0.085), pya.DPoint(3.4, -0.085), pya.DPoint(3.4, 0.085), pya.DPoint(3.23, 0.085), pya.DPoint(3.23, -0.085)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, -0.425), pya.DPoint(-3.23, -0.425), pya.DPoint(-3.23, -0.255), pya.DPoint(-3.4, -0.255), pya.DPoint(-3.4, -0.425)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, -0.425), pya.DPoint(3.4, -0.425), pya.DPoint(3.4, -0.255), pya.DPoint(3.23, -0.255), pya.DPoint(3.23, -0.425)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.965, -0.73), pya.DPoint(-2.795, -0.73), pya.DPoint(-2.795, -0.56), pya.DPoint(-2.965, -0.56), pya.DPoint(-2.965, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.625, -0.73), pya.DPoint(-2.455, -0.73), pya.DPoint(-2.455, -0.56), pya.DPoint(-2.625, -0.56), pya.DPoint(-2.625, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.285, -0.73), pya.DPoint(-2.115, -0.73), pya.DPoint(-2.115, -0.56), pya.DPoint(-2.285, -0.56), pya.DPoint(-2.285, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.695, -0.73), pya.DPoint(-1.525, -0.73), pya.DPoint(-1.525, -0.56), pya.DPoint(-1.695, -0.56), pya.DPoint(-1.695, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, -0.73), pya.DPoint(-1.185, -0.73), pya.DPoint(-1.185, -0.56), pya.DPoint(-1.355, -0.56), pya.DPoint(-1.355, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.015, -0.73), pya.DPoint(-0.845, -0.73), pya.DPoint(-0.845, -0.56), pya.DPoint(-1.015, -0.56), pya.DPoint(-1.015, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.425, -0.73), pya.DPoint(-0.255, -0.73), pya.DPoint(-0.255, -0.56), pya.DPoint(-0.425, -0.56), pya.DPoint(-0.425, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.085, -0.73), pya.DPoint(0.085, -0.73), pya.DPoint(0.085, -0.56), pya.DPoint(-0.085, -0.56), pya.DPoint(-0.085, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.255, -0.73), pya.DPoint(0.425, -0.73), pya.DPoint(0.425, -0.56), pya.DPoint(0.255, -0.56), pya.DPoint(0.255, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.845, -0.73), pya.DPoint(1.015, -0.73), pya.DPoint(1.015, -0.56), pya.DPoint(0.845, -0.56), pya.DPoint(0.845, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, -0.73), pya.DPoint(1.355, -0.73), pya.DPoint(1.355, -0.56), pya.DPoint(1.185, -0.56), pya.DPoint(1.185, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.525, -0.73), pya.DPoint(1.695, -0.73), pya.DPoint(1.695, -0.56), pya.DPoint(1.525, -0.56), pya.DPoint(1.525, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.115, -0.73), pya.DPoint(2.285, -0.73), pya.DPoint(2.285, -0.56), pya.DPoint(2.115, -0.56), pya.DPoint(2.115, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.455, -0.73), pya.DPoint(2.625, -0.73), pya.DPoint(2.625, -0.56), pya.DPoint(2.455, -0.56), pya.DPoint(2.455, -0.73)]))
cell_nmos_5x.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.795, -0.73), pya.DPoint(2.965, -0.73), pya.DPoint(2.965, -0.56), pya.DPoint(2.795, -0.56), pya.DPoint(2.795, -0.73)]))
cell_nmos_5x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.5, -0.525), pya.DPoint(-3.13, -0.525), pya.DPoint(-3.13, 0.525), pya.DPoint(-3.5, 0.525), pya.DPoint(-3.5, -0.525)]))
cell_nmos_5x.shapes(L_npc_drawing).insert(
    pya.DPolygon([pya.DPoint(3.13, -0.525), pya.DPoint(3.5, -0.525), pya.DPoint(3.5, 0.525), pya.DPoint(3.13, 0.525), pya.DPoint(3.13, -0.525)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, 0.56), pya.DPoint(-2.02, 0.56), pya.DPoint(-2.02, 0.73), pya.DPoint(-3.06, 0.73), pya.DPoint(-3.06, 0.56)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, 0.56), pya.DPoint(-0.75, 0.56), pya.DPoint(-0.75, 0.73), pya.DPoint(-1.79, 0.73), pya.DPoint(-1.79, 0.56)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, 0.56), pya.DPoint(0.52, 0.56), pya.DPoint(0.52, 0.73), pya.DPoint(-0.52, 0.73), pya.DPoint(-0.52, 0.56)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, 0.56), pya.DPoint(1.79, 0.56), pya.DPoint(1.79, 0.73), pya.DPoint(0.75, 0.73), pya.DPoint(0.75, 0.56)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, 0.56), pya.DPoint(3.06, 0.56), pya.DPoint(3.06, 0.73), pya.DPoint(2.02, 0.73), pya.DPoint(2.02, 0.56)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, -0.53), pya.DPoint(-3.23, -0.53), pya.DPoint(-3.23, 0.53), pya.DPoint(-3.4, 0.53), pya.DPoint(-3.4, -0.53)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, -0.53), pya.DPoint(3.4, -0.53), pya.DPoint(3.4, 0.53), pya.DPoint(3.23, 0.53), pya.DPoint(3.23, -0.53)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.06, -0.73), pya.DPoint(-2.02, -0.73), pya.DPoint(-2.02, -0.56), pya.DPoint(-3.06, -0.56), pya.DPoint(-3.06, -0.73)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.79, -0.73), pya.DPoint(-0.75, -0.73), pya.DPoint(-0.75, -0.56), pya.DPoint(-1.79, -0.56), pya.DPoint(-1.79, -0.73)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.52, -0.73), pya.DPoint(0.52, -0.73), pya.DPoint(0.52, -0.56), pya.DPoint(-0.52, -0.56), pya.DPoint(-0.52, -0.73)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.75, -0.73), pya.DPoint(1.79, -0.73), pya.DPoint(1.79, -0.56), pya.DPoint(0.75, -0.56), pya.DPoint(0.75, -0.73)]))
cell_nmos_5x.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.02, -0.73), pya.DPoint(3.06, -0.73), pya.DPoint(3.06, -0.56), pya.DPoint(2.02, -0.56), pya.DPoint(2.02, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, 0.56), pya.DPoint(-2.635, 0.56), pya.DPoint(-2.635, 0.73), pya.DPoint(-2.805, 0.73), pya.DPoint(-2.805, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, 0.56), pya.DPoint(-2.275, 0.56), pya.DPoint(-2.275, 0.73), pya.DPoint(-2.445, 0.73), pya.DPoint(-2.445, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, 0.56), pya.DPoint(-1.365, 0.56), pya.DPoint(-1.365, 0.73), pya.DPoint(-1.535, 0.73), pya.DPoint(-1.535, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, 0.56), pya.DPoint(-1.005, 0.56), pya.DPoint(-1.005, 0.73), pya.DPoint(-1.175, 0.73), pya.DPoint(-1.175, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, 0.56), pya.DPoint(-0.095, 0.56), pya.DPoint(-0.095, 0.73), pya.DPoint(-0.265, 0.73), pya.DPoint(-0.265, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, 0.56), pya.DPoint(0.265, 0.56), pya.DPoint(0.265, 0.73), pya.DPoint(0.095, 0.73), pya.DPoint(0.095, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, 0.56), pya.DPoint(1.175, 0.56), pya.DPoint(1.175, 0.73), pya.DPoint(1.005, 0.73), pya.DPoint(1.005, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, 0.56), pya.DPoint(1.535, 0.56), pya.DPoint(1.535, 0.73), pya.DPoint(1.365, 0.73), pya.DPoint(1.365, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, 0.56), pya.DPoint(2.445, 0.56), pya.DPoint(2.445, 0.73), pya.DPoint(2.275, 0.73), pya.DPoint(2.275, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, 0.56), pya.DPoint(2.805, 0.56), pya.DPoint(2.805, 0.73), pya.DPoint(2.635, 0.73), pya.DPoint(2.635, 0.56)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, 0.275), pya.DPoint(-3.23, 0.275), pya.DPoint(-3.23, 0.445), pya.DPoint(-3.4, 0.445), pya.DPoint(-3.4, 0.275)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, 0.275), pya.DPoint(3.4, 0.275), pya.DPoint(3.4, 0.445), pya.DPoint(3.23, 0.445), pya.DPoint(3.23, 0.275)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, -0.085), pya.DPoint(-3.23, -0.085), pya.DPoint(-3.23, 0.085), pya.DPoint(-3.4, 0.085), pya.DPoint(-3.4, -0.085)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, -0.085), pya.DPoint(3.4, -0.085), pya.DPoint(3.4, 0.085), pya.DPoint(3.23, 0.085), pya.DPoint(3.23, -0.085)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.4, -0.445), pya.DPoint(-3.23, -0.445), pya.DPoint(-3.23, -0.275), pya.DPoint(-3.4, -0.275), pya.DPoint(-3.4, -0.445)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.23, -0.445), pya.DPoint(3.4, -0.445), pya.DPoint(3.4, -0.275), pya.DPoint(3.23, -0.275), pya.DPoint(3.23, -0.445)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.805, -0.73), pya.DPoint(-2.635, -0.73), pya.DPoint(-2.635, -0.56), pya.DPoint(-2.805, -0.56), pya.DPoint(-2.805, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-2.445, -0.73), pya.DPoint(-2.275, -0.73), pya.DPoint(-2.275, -0.56), pya.DPoint(-2.445, -0.56), pya.DPoint(-2.445, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.535, -0.73), pya.DPoint(-1.365, -0.73), pya.DPoint(-1.365, -0.56), pya.DPoint(-1.535, -0.56), pya.DPoint(-1.535, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.175, -0.73), pya.DPoint(-1.005, -0.73), pya.DPoint(-1.005, -0.56), pya.DPoint(-1.175, -0.56), pya.DPoint(-1.175, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.265, -0.73), pya.DPoint(-0.095, -0.73), pya.DPoint(-0.095, -0.56), pya.DPoint(-0.265, -0.56), pya.DPoint(-0.265, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.095, -0.73), pya.DPoint(0.265, -0.73), pya.DPoint(0.265, -0.56), pya.DPoint(0.095, -0.56), pya.DPoint(0.095, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.005, -0.73), pya.DPoint(1.175, -0.73), pya.DPoint(1.175, -0.56), pya.DPoint(1.005, -0.56), pya.DPoint(1.005, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.365, -0.73), pya.DPoint(1.535, -0.73), pya.DPoint(1.535, -0.56), pya.DPoint(1.365, -0.56), pya.DPoint(1.365, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.275, -0.73), pya.DPoint(2.445, -0.73), pya.DPoint(2.445, -0.56), pya.DPoint(2.275, -0.56), pya.DPoint(2.275, -0.73)]))
cell_nmos_5x.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.635, -0.73), pya.DPoint(2.805, -0.73), pya.DPoint(2.805, -0.56), pya.DPoint(2.635, -0.56), pya.DPoint(2.635, -0.73)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, 0.53), pya.DPoint(-2.04, 0.53), pya.DPoint(-2.04, 0.76), pya.DPoint(-3.04, 0.76), pya.DPoint(-3.04, 0.53)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 0.53), pya.DPoint(-0.77, 0.53), pya.DPoint(-0.77, 0.76), pya.DPoint(-1.77, 0.76), pya.DPoint(-1.77, 0.53)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, 0.53), pya.DPoint(0.5, 0.53), pya.DPoint(0.5, 0.76), pya.DPoint(-0.5, 0.76), pya.DPoint(-0.5, 0.53)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, 0.53), pya.DPoint(1.77, 0.53), pya.DPoint(1.77, 0.76), pya.DPoint(0.77, 0.76), pya.DPoint(0.77, 0.53)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, 0.53), pya.DPoint(3.04, 0.53), pya.DPoint(3.04, 0.76), pya.DPoint(2.04, 0.76), pya.DPoint(2.04, 0.53)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.43, -0.51), pya.DPoint(-3.2, -0.51), pya.DPoint(-3.2, 0.51), pya.DPoint(-3.43, 0.51), pya.DPoint(-3.43, -0.51)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.2, -0.51), pya.DPoint(3.43, -0.51), pya.DPoint(3.43, 0.51), pya.DPoint(3.2, 0.51), pya.DPoint(3.2, -0.51)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-3.04, -0.76), pya.DPoint(-2.04, -0.76), pya.DPoint(-2.04, -0.53), pya.DPoint(-3.04, -0.53), pya.DPoint(-3.04, -0.76)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -0.76), pya.DPoint(-0.77, -0.76), pya.DPoint(-0.77, -0.53), pya.DPoint(-1.77, -0.53), pya.DPoint(-1.77, -0.76)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.5, -0.76), pya.DPoint(0.5, -0.76), pya.DPoint(0.5, -0.53), pya.DPoint(-0.5, -0.53), pya.DPoint(-0.5, -0.76)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.77, -0.76), pya.DPoint(1.77, -0.76), pya.DPoint(1.77, -0.53), pya.DPoint(0.77, -0.53), pya.DPoint(0.77, -0.76)]))
cell_nmos_5x.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.04, -0.76), pya.DPoint(3.04, -0.76), pya.DPoint(3.04, -0.53), pya.DPoint(2.04, -0.53), pya.DPoint(2.04, -0.76)]))

# === OgueyAebischer_p7_n5 ===
cell_OgueyAebischer_p7_n5.insert(pya.DCellInstArray(
    cell_pmos_7x.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.62, 2.97))))
cell_OgueyAebischer_p7_n5.insert(pya.DCellInstArray(
    cell_nmos_5x.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(4.62, 0.14))))
cell_OgueyAebischer_p7_n5.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 2), pya.DPoint(9.46, 2), pya.DPoint(9.46, 4.46), pya.DPoint(-0.22, 4.46), pya.DPoint(-0.22, 2)]))
cell_OgueyAebischer_p7_n5.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(0.18, 4.03), pya.DPoint(9.06, 4.03), pya.DPoint(9.06, 4.28), pya.DPoint(0.18, 4.28), pya.DPoint(0.18, 4.03)]))
cell_OgueyAebischer_p7_n5.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(0.69, -0.92), pya.DPoint(0.9, -0.92), pya.DPoint(0.9, 1.69), pya.DPoint(0.69, 1.69), pya.DPoint(0.69, -0.92)]))
cell_OgueyAebischer_p7_n5.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(8.34, -0.92), pya.DPoint(8.55, -0.92), pya.DPoint(8.55, 1.69), pya.DPoint(8.34, 1.69), pya.DPoint(8.34, -0.92)]))
cell_OgueyAebischer_p7_n5.shapes(L_tap_drawing).insert(
    pya.DPolygon([pya.DPoint(0.69, -1.13), pya.DPoint(8.55, -1.13), pya.DPoint(8.55, -0.92), pya.DPoint(0.69, -0.92), pya.DPoint(0.69, -1.13)]))
cell_OgueyAebischer_p7_n5.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(0.565, -0.795), pya.DPoint(1.025, -0.795), pya.DPoint(1.025, 2.055), pya.DPoint(0.565, 2.055), pya.DPoint(0.565, -0.795)]))
cell_OgueyAebischer_p7_n5.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(8.215, -0.795), pya.DPoint(8.675, -0.795), pya.DPoint(8.675, 2.055), pya.DPoint(8.215, 2.055), pya.DPoint(8.215, -0.795)]))
cell_OgueyAebischer_p7_n5.shapes(L_psdm_drawing).insert(
    pya.DPolygon([pya.DPoint(0.565, -1.255), pya.DPoint(8.675, -1.255), pya.DPoint(8.675, -0.795), pya.DPoint(0.565, -0.795), pya.DPoint(0.565, -1.255)]))
cell_OgueyAebischer_p7_n5.shapes(L_nsdm_drawing).insert(
    pya.DPolygon([pya.DPoint(0.055, 3.905), pya.DPoint(9.185, 3.905), pya.DPoint(9.185, 4.405), pya.DPoint(0.055, 4.405), pya.DPoint(0.055, 3.905)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.455, 4.07), pya.DPoint(0.625, 4.07), pya.DPoint(0.625, 4.24), pya.DPoint(0.455, 4.24), pya.DPoint(0.455, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.795, 4.07), pya.DPoint(0.965, 4.07), pya.DPoint(0.965, 4.24), pya.DPoint(0.795, 4.24), pya.DPoint(0.795, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.135, 4.07), pya.DPoint(1.305, 4.07), pya.DPoint(1.305, 4.24), pya.DPoint(1.135, 4.24), pya.DPoint(1.135, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.475, 4.07), pya.DPoint(1.645, 4.07), pya.DPoint(1.645, 4.24), pya.DPoint(1.475, 4.24), pya.DPoint(1.475, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.815, 4.07), pya.DPoint(1.985, 4.07), pya.DPoint(1.985, 4.24), pya.DPoint(1.815, 4.24), pya.DPoint(1.815, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.155, 4.07), pya.DPoint(2.325, 4.07), pya.DPoint(2.325, 4.24), pya.DPoint(2.155, 4.24), pya.DPoint(2.155, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.495, 4.07), pya.DPoint(2.665, 4.07), pya.DPoint(2.665, 4.24), pya.DPoint(2.495, 4.24), pya.DPoint(2.495, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.835, 4.07), pya.DPoint(3.005, 4.07), pya.DPoint(3.005, 4.24), pya.DPoint(2.835, 4.24), pya.DPoint(2.835, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.175, 4.07), pya.DPoint(3.345, 4.07), pya.DPoint(3.345, 4.24), pya.DPoint(3.175, 4.24), pya.DPoint(3.175, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.515, 4.07), pya.DPoint(3.685, 4.07), pya.DPoint(3.685, 4.24), pya.DPoint(3.515, 4.24), pya.DPoint(3.515, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.855, 4.07), pya.DPoint(4.025, 4.07), pya.DPoint(4.025, 4.24), pya.DPoint(3.855, 4.24), pya.DPoint(3.855, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.195, 4.07), pya.DPoint(4.365, 4.07), pya.DPoint(4.365, 4.24), pya.DPoint(4.195, 4.24), pya.DPoint(4.195, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.535, 4.07), pya.DPoint(4.705, 4.07), pya.DPoint(4.705, 4.24), pya.DPoint(4.535, 4.24), pya.DPoint(4.535, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.875, 4.07), pya.DPoint(5.045, 4.07), pya.DPoint(5.045, 4.24), pya.DPoint(4.875, 4.24), pya.DPoint(4.875, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.215, 4.07), pya.DPoint(5.385, 4.07), pya.DPoint(5.385, 4.24), pya.DPoint(5.215, 4.24), pya.DPoint(5.215, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.555, 4.07), pya.DPoint(5.725, 4.07), pya.DPoint(5.725, 4.24), pya.DPoint(5.555, 4.24), pya.DPoint(5.555, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.895, 4.07), pya.DPoint(6.065, 4.07), pya.DPoint(6.065, 4.24), pya.DPoint(5.895, 4.24), pya.DPoint(5.895, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.235, 4.07), pya.DPoint(6.405, 4.07), pya.DPoint(6.405, 4.24), pya.DPoint(6.235, 4.24), pya.DPoint(6.235, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.575, 4.07), pya.DPoint(6.745, 4.07), pya.DPoint(6.745, 4.24), pya.DPoint(6.575, 4.24), pya.DPoint(6.575, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.915, 4.07), pya.DPoint(7.085, 4.07), pya.DPoint(7.085, 4.24), pya.DPoint(6.915, 4.24), pya.DPoint(6.915, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.255, 4.07), pya.DPoint(7.425, 4.07), pya.DPoint(7.425, 4.24), pya.DPoint(7.255, 4.24), pya.DPoint(7.255, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.595, 4.07), pya.DPoint(7.765, 4.07), pya.DPoint(7.765, 4.24), pya.DPoint(7.595, 4.24), pya.DPoint(7.595, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.935, 4.07), pya.DPoint(8.105, 4.07), pya.DPoint(8.105, 4.24), pya.DPoint(7.935, 4.24), pya.DPoint(7.935, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.275, 4.07), pya.DPoint(8.445, 4.07), pya.DPoint(8.445, 4.24), pya.DPoint(8.275, 4.24), pya.DPoint(8.275, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.615, 4.07), pya.DPoint(8.785, 4.07), pya.DPoint(8.785, 4.24), pya.DPoint(8.615, 4.24), pya.DPoint(8.615, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, 1.3), pya.DPoint(0.88, 1.3), pya.DPoint(0.88, 1.47), pya.DPoint(0.71, 1.47), pya.DPoint(0.71, 1.3)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, 1.3), pya.DPoint(8.53, 1.3), pya.DPoint(8.53, 1.47), pya.DPoint(8.36, 1.47), pya.DPoint(8.36, 1.3)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, 0.96), pya.DPoint(0.88, 0.96), pya.DPoint(0.88, 1.13), pya.DPoint(0.71, 1.13), pya.DPoint(0.71, 0.96)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, 0.96), pya.DPoint(8.53, 0.96), pya.DPoint(8.53, 1.13), pya.DPoint(8.36, 1.13), pya.DPoint(8.36, 0.96)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, 0.62), pya.DPoint(0.88, 0.62), pya.DPoint(0.88, 0.79), pya.DPoint(0.71, 0.79), pya.DPoint(0.71, 0.62)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, 0.62), pya.DPoint(8.53, 0.62), pya.DPoint(8.53, 0.79), pya.DPoint(8.36, 0.79), pya.DPoint(8.36, 0.62)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, 0.28), pya.DPoint(0.88, 0.28), pya.DPoint(0.88, 0.45), pya.DPoint(0.71, 0.45), pya.DPoint(0.71, 0.28)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, 0.28), pya.DPoint(8.53, 0.28), pya.DPoint(8.53, 0.45), pya.DPoint(8.36, 0.45), pya.DPoint(8.36, 0.28)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, -0.06), pya.DPoint(0.88, -0.06), pya.DPoint(0.88, 0.11), pya.DPoint(0.71, 0.11), pya.DPoint(0.71, -0.06)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, -0.06), pya.DPoint(8.53, -0.06), pya.DPoint(8.53, 0.11), pya.DPoint(8.36, 0.11), pya.DPoint(8.36, -0.06)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, -0.4), pya.DPoint(0.88, -0.4), pya.DPoint(0.88, -0.23), pya.DPoint(0.71, -0.23), pya.DPoint(0.71, -0.4)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, -0.4), pya.DPoint(8.53, -0.4), pya.DPoint(8.53, -0.23), pya.DPoint(8.36, -0.23), pya.DPoint(8.36, -0.4)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, -0.74), pya.DPoint(0.88, -0.74), pya.DPoint(0.88, -0.57), pya.DPoint(0.71, -0.57), pya.DPoint(0.71, -0.74)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, -0.74), pya.DPoint(8.53, -0.74), pya.DPoint(8.53, -0.57), pya.DPoint(8.36, -0.57), pya.DPoint(8.36, -0.74)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.135, -1.11), pya.DPoint(1.305, -1.11), pya.DPoint(1.305, -0.94), pya.DPoint(1.135, -0.94), pya.DPoint(1.135, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.475, -1.11), pya.DPoint(1.645, -1.11), pya.DPoint(1.645, -0.94), pya.DPoint(1.475, -0.94), pya.DPoint(1.475, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.815, -1.11), pya.DPoint(1.985, -1.11), pya.DPoint(1.985, -0.94), pya.DPoint(1.815, -0.94), pya.DPoint(1.815, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.155, -1.11), pya.DPoint(2.325, -1.11), pya.DPoint(2.325, -0.94), pya.DPoint(2.155, -0.94), pya.DPoint(2.155, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.495, -1.11), pya.DPoint(2.665, -1.11), pya.DPoint(2.665, -0.94), pya.DPoint(2.495, -0.94), pya.DPoint(2.495, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.835, -1.11), pya.DPoint(3.005, -1.11), pya.DPoint(3.005, -0.94), pya.DPoint(2.835, -0.94), pya.DPoint(2.835, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.175, -1.11), pya.DPoint(3.345, -1.11), pya.DPoint(3.345, -0.94), pya.DPoint(3.175, -0.94), pya.DPoint(3.175, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.515, -1.11), pya.DPoint(3.685, -1.11), pya.DPoint(3.685, -0.94), pya.DPoint(3.515, -0.94), pya.DPoint(3.515, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.855, -1.11), pya.DPoint(4.025, -1.11), pya.DPoint(4.025, -0.94), pya.DPoint(3.855, -0.94), pya.DPoint(3.855, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.195, -1.11), pya.DPoint(4.365, -1.11), pya.DPoint(4.365, -0.94), pya.DPoint(4.195, -0.94), pya.DPoint(4.195, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.535, -1.11), pya.DPoint(4.705, -1.11), pya.DPoint(4.705, -0.94), pya.DPoint(4.535, -0.94), pya.DPoint(4.535, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.875, -1.11), pya.DPoint(5.045, -1.11), pya.DPoint(5.045, -0.94), pya.DPoint(4.875, -0.94), pya.DPoint(4.875, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.215, -1.11), pya.DPoint(5.385, -1.11), pya.DPoint(5.385, -0.94), pya.DPoint(5.215, -0.94), pya.DPoint(5.215, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.555, -1.11), pya.DPoint(5.725, -1.11), pya.DPoint(5.725, -0.94), pya.DPoint(5.555, -0.94), pya.DPoint(5.555, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.895, -1.11), pya.DPoint(6.065, -1.11), pya.DPoint(6.065, -0.94), pya.DPoint(5.895, -0.94), pya.DPoint(5.895, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.235, -1.11), pya.DPoint(6.405, -1.11), pya.DPoint(6.405, -0.94), pya.DPoint(6.235, -0.94), pya.DPoint(6.235, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.575, -1.11), pya.DPoint(6.745, -1.11), pya.DPoint(6.745, -0.94), pya.DPoint(6.575, -0.94), pya.DPoint(6.575, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.915, -1.11), pya.DPoint(7.085, -1.11), pya.DPoint(7.085, -0.94), pya.DPoint(6.915, -0.94), pya.DPoint(6.915, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.255, -1.11), pya.DPoint(7.425, -1.11), pya.DPoint(7.425, -0.94), pya.DPoint(7.255, -0.94), pya.DPoint(7.255, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.595, -1.11), pya.DPoint(7.765, -1.11), pya.DPoint(7.765, -0.94), pya.DPoint(7.595, -0.94), pya.DPoint(7.595, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_licon1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.935, -1.11), pya.DPoint(8.105, -1.11), pya.DPoint(8.105, -0.94), pya.DPoint(7.935, -0.94), pya.DPoint(7.935, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.29, 4.07), pya.DPoint(8.95, 4.07), pya.DPoint(8.95, 4.24), pya.DPoint(0.29, 4.24), pya.DPoint(0.29, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.29, 3.53), pya.DPoint(8.95, 3.53), pya.DPoint(8.95, 3.7), pya.DPoint(0.29, 3.7), pya.DPoint(0.29, 3.53)]))
cell_OgueyAebischer_p7_n5.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, -0.94), pya.DPoint(0.88, -0.94), pya.DPoint(0.88, 1.67), pya.DPoint(0.71, 1.67), pya.DPoint(0.71, -0.94)]))
cell_OgueyAebischer_p7_n5.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.36, -0.94), pya.DPoint(8.53, -0.94), pya.DPoint(8.53, 1.67), pya.DPoint(8.36, 1.67), pya.DPoint(8.36, -0.94)]))
cell_OgueyAebischer_p7_n5.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.71, -1.11), pya.DPoint(8.53, -1.11), pya.DPoint(8.53, -0.94), pya.DPoint(0.71, -0.94), pya.DPoint(0.71, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.545, 4.07), pya.DPoint(0.715, 4.07), pya.DPoint(0.715, 4.24), pya.DPoint(0.545, 4.24), pya.DPoint(0.545, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(0.905, 4.07), pya.DPoint(1.075, 4.07), pya.DPoint(1.075, 4.24), pya.DPoint(0.905, 4.24), pya.DPoint(0.905, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(1.815, 4.07), pya.DPoint(1.985, 4.07), pya.DPoint(1.985, 4.24), pya.DPoint(1.815, 4.24), pya.DPoint(1.815, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(2.175, 4.07), pya.DPoint(2.345, 4.07), pya.DPoint(2.345, 4.24), pya.DPoint(2.175, 4.24), pya.DPoint(2.175, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.085, 4.07), pya.DPoint(3.255, 4.07), pya.DPoint(3.255, 4.24), pya.DPoint(3.085, 4.24), pya.DPoint(3.085, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(3.445, 4.07), pya.DPoint(3.615, 4.07), pya.DPoint(3.615, 4.24), pya.DPoint(3.445, 4.24), pya.DPoint(3.445, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.355, 4.07), pya.DPoint(4.525, 4.07), pya.DPoint(4.525, 4.24), pya.DPoint(4.355, 4.24), pya.DPoint(4.355, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.715, 4.07), pya.DPoint(4.885, 4.07), pya.DPoint(4.885, 4.24), pya.DPoint(4.715, 4.24), pya.DPoint(4.715, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.625, 4.07), pya.DPoint(5.795, 4.07), pya.DPoint(5.795, 4.24), pya.DPoint(5.625, 4.24), pya.DPoint(5.625, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(5.985, 4.07), pya.DPoint(6.155, 4.07), pya.DPoint(6.155, 4.24), pya.DPoint(5.985, 4.24), pya.DPoint(5.985, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(6.895, 4.07), pya.DPoint(7.065, 4.07), pya.DPoint(7.065, 4.24), pya.DPoint(6.895, 4.24), pya.DPoint(6.895, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(7.255, 4.07), pya.DPoint(7.425, 4.07), pya.DPoint(7.425, 4.24), pya.DPoint(7.255, 4.24), pya.DPoint(7.255, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(8.165, 4.07), pya.DPoint(8.335, 4.07), pya.DPoint(8.335, 4.24), pya.DPoint(8.165, 4.24), pya.DPoint(8.165, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(8.525, 4.07), pya.DPoint(8.695, 4.07), pya.DPoint(8.695, 4.24), pya.DPoint(8.525, 4.24), pya.DPoint(8.525, 4.07)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.355, -1.11), pya.DPoint(4.525, -1.11), pya.DPoint(4.525, -0.94), pya.DPoint(4.355, -0.94), pya.DPoint(4.355, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(4.715, -1.11), pya.DPoint(4.885, -1.11), pya.DPoint(4.885, -0.94), pya.DPoint(4.715, -0.94), pya.DPoint(4.715, -1.11)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.31, 3.73), pya.DPoint(1.31, 3.73), pya.DPoint(1.31, 4.28), pya.DPoint(0.31, 4.28), pya.DPoint(0.31, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.58, 3.73), pya.DPoint(2.58, 3.73), pya.DPoint(2.58, 4.28), pya.DPoint(1.58, 4.28), pya.DPoint(1.58, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.85, 3.73), pya.DPoint(3.85, 3.73), pya.DPoint(3.85, 4.28), pya.DPoint(2.85, 4.28), pya.DPoint(2.85, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.12, 3.73), pya.DPoint(5.12, 3.73), pya.DPoint(5.12, 4.28), pya.DPoint(4.12, 4.28), pya.DPoint(4.12, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.39, 3.73), pya.DPoint(6.39, 3.73), pya.DPoint(6.39, 4.28), pya.DPoint(5.39, 4.28), pya.DPoint(5.39, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, 3.73), pya.DPoint(7.66, 3.73), pya.DPoint(7.66, 4.28), pya.DPoint(6.66, 4.28), pya.DPoint(6.66, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.93, 3.73), pya.DPoint(8.93, 3.73), pya.DPoint(8.93, 4.28), pya.DPoint(7.93, 4.28), pya.DPoint(7.93, 3.73)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.31, 3.5), pya.DPoint(8.93, 3.5), pya.DPoint(8.93, 3.73), pya.DPoint(0.31, 3.73), pya.DPoint(0.31, 3.5)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 1.81), pya.DPoint(0.1, 1.81), pya.DPoint(0.1, 3.48), pya.DPoint(-0.22, 3.48), pya.DPoint(-0.22, 1.81)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.31, 1.01), pya.DPoint(0.63, 1.01), pya.DPoint(0.63, 2.44), pya.DPoint(0.31, 2.44), pya.DPoint(0.31, 1.01)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.1, -0.37), pya.DPoint(1.42, -0.37), pya.DPoint(1.42, 1.67), pya.DPoint(1.1, 1.67), pya.DPoint(1.1, -0.37)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(1.58, 1.41), pya.DPoint(1.9, 1.41), pya.DPoint(1.9, 2.44), pya.DPoint(1.58, 2.44), pya.DPoint(1.58, 1.41)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.26, 0.67), pya.DPoint(2.58, 0.67), pya.DPoint(2.58, 2.07), pya.DPoint(2.26, 2.07), pya.DPoint(2.26, 0.67)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.85, 1.41), pya.DPoint(3.17, 1.41), pya.DPoint(3.17, 2.44), pya.DPoint(2.85, 2.44), pya.DPoint(2.85, 1.41)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.53, 0.67), pya.DPoint(3.85, 0.67), pya.DPoint(3.85, 2.07), pya.DPoint(3.53, 2.07), pya.DPoint(3.53, 0.67)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.12, 1.81), pya.DPoint(4.44, 1.81), pya.DPoint(4.44, 2.44), pya.DPoint(4.12, 2.44), pya.DPoint(4.12, 1.81)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.8, 0.67), pya.DPoint(5.12, 0.67), pya.DPoint(5.12, 1.67), pya.DPoint(4.8, 1.67), pya.DPoint(4.8, 0.67)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.39, 1.41), pya.DPoint(5.71, 1.41), pya.DPoint(5.71, 2.44), pya.DPoint(5.39, 2.44), pya.DPoint(5.39, 1.41)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.07, 0.67), pya.DPoint(6.39, 0.67), pya.DPoint(6.39, 2.07), pya.DPoint(6.07, 2.07), pya.DPoint(6.07, 0.67)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, 1.41), pya.DPoint(6.98, 1.41), pya.DPoint(6.98, 2.44), pya.DPoint(6.66, 2.44), pya.DPoint(6.66, 1.41)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.34, 0.67), pya.DPoint(7.66, 0.67), pya.DPoint(7.66, 2.07), pya.DPoint(7.34, 2.07), pya.DPoint(7.34, 0.67)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.82, -0.37), pya.DPoint(8.14, -0.37), pya.DPoint(8.14, 1.67), pya.DPoint(7.82, 1.67), pya.DPoint(7.82, -0.37)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(8.61, 1.01), pya.DPoint(8.93, 1.01), pya.DPoint(8.93, 2.44), pya.DPoint(8.61, 2.44), pya.DPoint(8.61, 1.01)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.14, 1.81), pya.DPoint(9.46, 1.81), pya.DPoint(9.46, 3.48), pya.DPoint(9.14, 3.48), pya.DPoint(9.14, 1.81)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(2.26, -1.02), pya.DPoint(2.58, -1.02), pya.DPoint(2.58, -0.39), pya.DPoint(2.26, -0.39), pya.DPoint(2.26, -1.02)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(3.53, -1.02), pya.DPoint(3.85, -1.02), pya.DPoint(3.85, -0.39), pya.DPoint(3.53, -0.39), pya.DPoint(3.53, -1.02)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(4.12, -1.42), pya.DPoint(5.12, -1.42), pya.DPoint(5.12, -0.39), pya.DPoint(4.12, -0.39), pya.DPoint(4.12, -1.42)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(5.39, -1.02), pya.DPoint(5.71, -1.02), pya.DPoint(5.71, -0.39), pya.DPoint(5.39, -0.39), pya.DPoint(5.39, -1.02)]))
cell_OgueyAebischer_p7_n5.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, -1.02), pya.DPoint(6.98, -1.02), pya.DPoint(6.98, -0.39), pya.DPoint(6.66, -0.39), pya.DPoint(6.66, -1.02)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.415, 3.925), pya.DPoint(0.565, 3.925), pya.DPoint(0.565, 4.075), pya.DPoint(0.415, 4.075), pya.DPoint(0.415, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, 3.925), pya.DPoint(0.885, 3.925), pya.DPoint(0.885, 4.075), pya.DPoint(0.735, 4.075), pya.DPoint(0.735, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.055, 3.925), pya.DPoint(1.205, 3.925), pya.DPoint(1.205, 4.075), pya.DPoint(1.055, 4.075), pya.DPoint(1.055, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.685, 3.925), pya.DPoint(1.835, 3.925), pya.DPoint(1.835, 4.075), pya.DPoint(1.685, 4.075), pya.DPoint(1.685, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.005, 3.925), pya.DPoint(2.155, 3.925), pya.DPoint(2.155, 4.075), pya.DPoint(2.005, 4.075), pya.DPoint(2.005, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.325, 3.925), pya.DPoint(2.475, 3.925), pya.DPoint(2.475, 4.075), pya.DPoint(2.325, 4.075), pya.DPoint(2.325, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.955, 3.925), pya.DPoint(3.105, 3.925), pya.DPoint(3.105, 4.075), pya.DPoint(2.955, 4.075), pya.DPoint(2.955, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(3.275, 3.925), pya.DPoint(3.425, 3.925), pya.DPoint(3.425, 4.075), pya.DPoint(3.275, 4.075), pya.DPoint(3.275, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(3.595, 3.925), pya.DPoint(3.745, 3.925), pya.DPoint(3.745, 4.075), pya.DPoint(3.595, 4.075), pya.DPoint(3.595, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.225, 3.925), pya.DPoint(4.375, 3.925), pya.DPoint(4.375, 4.075), pya.DPoint(4.225, 4.075), pya.DPoint(4.225, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.545, 3.925), pya.DPoint(4.695, 3.925), pya.DPoint(4.695, 4.075), pya.DPoint(4.545, 4.075), pya.DPoint(4.545, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.865, 3.925), pya.DPoint(5.015, 3.925), pya.DPoint(5.015, 4.075), pya.DPoint(4.865, 4.075), pya.DPoint(4.865, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(5.495, 3.925), pya.DPoint(5.645, 3.925), pya.DPoint(5.645, 4.075), pya.DPoint(5.495, 4.075), pya.DPoint(5.495, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(5.815, 3.925), pya.DPoint(5.965, 3.925), pya.DPoint(5.965, 4.075), pya.DPoint(5.815, 4.075), pya.DPoint(5.815, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.135, 3.925), pya.DPoint(6.285, 3.925), pya.DPoint(6.285, 4.075), pya.DPoint(6.135, 4.075), pya.DPoint(6.135, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.765, 3.925), pya.DPoint(6.915, 3.925), pya.DPoint(6.915, 4.075), pya.DPoint(6.765, 4.075), pya.DPoint(6.765, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.085, 3.925), pya.DPoint(7.235, 3.925), pya.DPoint(7.235, 4.075), pya.DPoint(7.085, 4.075), pya.DPoint(7.085, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.405, 3.925), pya.DPoint(7.555, 3.925), pya.DPoint(7.555, 4.075), pya.DPoint(7.405, 4.075), pya.DPoint(7.405, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.035, 3.925), pya.DPoint(8.185, 3.925), pya.DPoint(8.185, 4.075), pya.DPoint(8.035, 4.075), pya.DPoint(8.035, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.355, 3.925), pya.DPoint(8.505, 3.925), pya.DPoint(8.505, 4.075), pya.DPoint(8.355, 4.075), pya.DPoint(8.355, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.675, 3.925), pya.DPoint(8.825, 3.925), pya.DPoint(8.825, 4.075), pya.DPoint(8.675, 4.075), pya.DPoint(8.675, 3.925)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.135, 1.865), pya.DPoint(0.015, 1.865), pya.DPoint(0.015, 2.015), pya.DPoint(-0.135, 2.015), pya.DPoint(-0.135, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.345, 1.865), pya.DPoint(2.495, 1.865), pya.DPoint(2.495, 2.015), pya.DPoint(2.345, 2.015), pya.DPoint(2.345, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(3.615, 1.865), pya.DPoint(3.765, 1.865), pya.DPoint(3.765, 2.015), pya.DPoint(3.615, 2.015), pya.DPoint(3.615, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.205, 1.865), pya.DPoint(4.355, 1.865), pya.DPoint(4.355, 2.015), pya.DPoint(4.205, 2.015), pya.DPoint(4.205, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.155, 1.865), pya.DPoint(6.305, 1.865), pya.DPoint(6.305, 2.015), pya.DPoint(6.155, 2.015), pya.DPoint(6.155, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.425, 1.865), pya.DPoint(7.575, 1.865), pya.DPoint(7.575, 2.015), pya.DPoint(7.425, 2.015), pya.DPoint(7.425, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(9.225, 1.865), pya.DPoint(9.375, 1.865), pya.DPoint(9.375, 2.015), pya.DPoint(9.225, 2.015), pya.DPoint(9.225, 1.865)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.185, 1.465), pya.DPoint(1.335, 1.465), pya.DPoint(1.335, 1.615), pya.DPoint(1.185, 1.615), pya.DPoint(1.185, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.665, 1.465), pya.DPoint(1.815, 1.465), pya.DPoint(1.815, 1.615), pya.DPoint(1.665, 1.615), pya.DPoint(1.665, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.935, 1.465), pya.DPoint(3.085, 1.465), pya.DPoint(3.085, 1.615), pya.DPoint(2.935, 1.615), pya.DPoint(2.935, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.885, 1.465), pya.DPoint(5.035, 1.465), pya.DPoint(5.035, 1.615), pya.DPoint(4.885, 1.615), pya.DPoint(4.885, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(5.475, 1.465), pya.DPoint(5.625, 1.465), pya.DPoint(5.625, 1.615), pya.DPoint(5.475, 1.615), pya.DPoint(5.475, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.745, 1.465), pya.DPoint(6.895, 1.465), pya.DPoint(6.895, 1.615), pya.DPoint(6.745, 1.615), pya.DPoint(6.745, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.905, 1.465), pya.DPoint(8.055, 1.465), pya.DPoint(8.055, 1.615), pya.DPoint(7.905, 1.615), pya.DPoint(7.905, 1.465)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.395, 1.065), pya.DPoint(0.545, 1.065), pya.DPoint(0.545, 1.215), pya.DPoint(0.395, 1.215), pya.DPoint(0.395, 1.065)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.695, 1.065), pya.DPoint(8.845, 1.065), pya.DPoint(8.845, 1.215), pya.DPoint(8.695, 1.215), pya.DPoint(8.695, 1.065)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(2.345, -0.965), pya.DPoint(2.495, -0.965), pya.DPoint(2.495, -0.815), pya.DPoint(2.345, -0.815), pya.DPoint(2.345, -0.965)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(3.615, -0.965), pya.DPoint(3.765, -0.965), pya.DPoint(3.765, -0.815), pya.DPoint(3.615, -0.815), pya.DPoint(3.615, -0.965)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(5.475, -0.965), pya.DPoint(5.625, -0.965), pya.DPoint(5.625, -0.815), pya.DPoint(5.475, -0.815), pya.DPoint(5.475, -0.965)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.745, -0.965), pya.DPoint(6.895, -0.965), pya.DPoint(6.895, -0.815), pya.DPoint(6.745, -0.815), pya.DPoint(6.745, -0.965)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.225, -1.365), pya.DPoint(4.375, -1.365), pya.DPoint(4.375, -1.215), pya.DPoint(4.225, -1.215), pya.DPoint(4.225, -1.365)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.545, -1.365), pya.DPoint(4.695, -1.365), pya.DPoint(4.695, -1.215), pya.DPoint(4.545, -1.215), pya.DPoint(4.545, -1.365)]))
cell_OgueyAebischer_p7_n5.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(4.865, -1.365), pya.DPoint(5.015, -1.365), pya.DPoint(5.015, -1.215), pya.DPoint(4.865, -1.215), pya.DPoint(4.865, -1.365)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 3.87), pya.DPoint(9.46, 3.87), pya.DPoint(9.46, 4.13), pya.DPoint(-0.22, 4.13), pya.DPoint(-0.22, 3.87)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 1.81), pya.DPoint(9.46, 1.81), pya.DPoint(9.46, 2.07), pya.DPoint(-0.22, 2.07), pya.DPoint(-0.22, 1.81)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 1.41), pya.DPoint(9.46, 1.41), pya.DPoint(9.46, 1.67), pya.DPoint(-0.22, 1.67), pya.DPoint(-0.22, 1.41)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, 1.01), pya.DPoint(9.46, 1.01), pya.DPoint(9.46, 1.27), pya.DPoint(-0.22, 1.27), pya.DPoint(-0.22, 1.01)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, -1.02), pya.DPoint(9.46, -1.02), pya.DPoint(9.46, -0.76), pya.DPoint(-0.22, -0.76), pya.DPoint(-0.22, -1.02)]))
cell_OgueyAebischer_p7_n5.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.22, -1.42), pya.DPoint(9.46, -1.42), pya.DPoint(9.46, -1.16), pya.DPoint(-0.22, -1.16), pya.DPoint(-0.22, -1.42)]))

# === OgueyAebischerBias ===
cell_OgueyAebischerBias.insert(pya.DCellInstArray(
    cell_nmos_1x80_2x.cell_index(),
    pya.DCplxTrans(1, 0, True,
                  pya.DVector(-1.4, -2.33))))
cell_OgueyAebischerBias.insert(pya.DCellInstArray(
    cell_OgueyAebischer_p7_n5.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_OgueyAebischerBias.shapes(L_nwell_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 2), pya.DPoint(9.74, 2), pya.DPoint(9.74, 4.46), pya.DPoint(-1.77, 4.46), pya.DPoint(-1.77, 2)]))
cell_OgueyAebischerBias.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.72, -2.03), pya.DPoint(7.6, -2.03), pya.DPoint(7.6, -1.86), pya.DPoint(6.72, -1.86), pya.DPoint(6.72, -2.03)]))
cell_OgueyAebischerBias.shapes(L_li1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.99, -2.03), pya.DPoint(8.87, -2.03), pya.DPoint(8.87, -1.86), pya.DPoint(7.99, -1.86), pya.DPoint(7.99, -2.03)]))
cell_OgueyAebischerBias.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(6.895, -2.03), pya.DPoint(7.065, -2.03), pya.DPoint(7.065, -1.86), pya.DPoint(6.895, -1.86), pya.DPoint(6.895, -2.03)]))
cell_OgueyAebischerBias.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(7.255, -2.03), pya.DPoint(7.425, -2.03), pya.DPoint(7.425, -1.86), pya.DPoint(7.255, -1.86), pya.DPoint(7.255, -2.03)]))
cell_OgueyAebischerBias.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(8.165, -2.03), pya.DPoint(8.335, -2.03), pya.DPoint(8.335, -1.86), pya.DPoint(8.165, -1.86), pya.DPoint(8.165, -2.03)]))
cell_OgueyAebischerBias.shapes(L_mcon_drawing).insert(
    pya.DPolygon([pya.DPoint(8.525, -2.03), pya.DPoint(8.695, -2.03), pya.DPoint(8.695, -1.86), pya.DPoint(8.525, -1.86), pya.DPoint(8.525, -2.03)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.44, -1.96), pya.DPoint(-1.12, -1.96), pya.DPoint(-1.12, 1.27), pya.DPoint(-1.44, 1.27), pya.DPoint(-1.44, -1.96)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.96, -1.96), pya.DPoint(0.04, -1.96), pya.DPoint(0.04, 1.27), pya.DPoint(-0.96, 1.27), pya.DPoint(-0.96, -1.96)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.44, -2.19), pya.DPoint(0.04, -2.19), pya.DPoint(0.04, -1.96), pya.DPoint(-1.44, -1.96), pya.DPoint(-1.44, -2.19)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.44, -22.63), pya.DPoint(-1.12, -22.63), pya.DPoint(-1.12, -2.19), pya.DPoint(-1.44, -2.19), pya.DPoint(-1.44, -22.63)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.96, -2.59), pya.DPoint(0.04, -2.59), pya.DPoint(0.04, -2.19), pya.DPoint(-0.96, -2.19), pya.DPoint(-0.96, -2.59)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(0.31, -2.59), pya.DPoint(1.31, -2.59), pya.DPoint(1.31, -0.76), pya.DPoint(0.31, -0.76), pya.DPoint(0.31, -2.59)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(6.66, -2.59), pya.DPoint(7.66, -2.59), pya.DPoint(7.66, -1.16), pya.DPoint(6.66, -1.16), pya.DPoint(6.66, -2.59)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(7.93, -2.59), pya.DPoint(8.93, -2.59), pya.DPoint(8.93, -1.16), pya.DPoint(7.93, -1.16), pya.DPoint(7.93, -2.59)]))
cell_OgueyAebischerBias.shapes(L_met1_drawing).insert(
    pya.DPolygon([pya.DPoint(9.09, -22.63), pya.DPoint(9.41, -22.63), pya.DPoint(9.41, 1.27), pya.DPoint(9.09, 1.27), pya.DPoint(9.09, -22.63)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.355, 1.065), pya.DPoint(-1.205, 1.065), pya.DPoint(-1.205, 1.215), pya.DPoint(-1.355, 1.215), pya.DPoint(-1.355, 1.065)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.855, 1.065), pya.DPoint(-0.705, 1.065), pya.DPoint(-0.705, 1.215), pya.DPoint(-0.855, 1.215), pya.DPoint(-0.855, 1.065)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.535, 1.065), pya.DPoint(-0.385, 1.065), pya.DPoint(-0.385, 1.215), pya.DPoint(-0.535, 1.215), pya.DPoint(-0.535, 1.065)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(-0.215, 1.065), pya.DPoint(-0.065, 1.065), pya.DPoint(-0.065, 1.215), pya.DPoint(-0.215, 1.215), pya.DPoint(-0.215, 1.065)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(9.175, 1.065), pya.DPoint(9.325, 1.065), pya.DPoint(9.325, 1.215), pya.DPoint(9.175, 1.215), pya.DPoint(9.175, 1.065)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.415, -0.965), pya.DPoint(0.565, -0.965), pya.DPoint(0.565, -0.815), pya.DPoint(0.415, -0.815), pya.DPoint(0.415, -0.965)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(0.735, -0.965), pya.DPoint(0.885, -0.965), pya.DPoint(0.885, -0.815), pya.DPoint(0.735, -0.815), pya.DPoint(0.735, -0.965)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(1.055, -0.965), pya.DPoint(1.205, -0.965), pya.DPoint(1.205, -0.815), pya.DPoint(1.055, -0.815), pya.DPoint(1.055, -0.965)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(6.765, -1.365), pya.DPoint(6.915, -1.365), pya.DPoint(6.915, -1.215), pya.DPoint(6.765, -1.215), pya.DPoint(6.765, -1.365)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.085, -1.365), pya.DPoint(7.235, -1.365), pya.DPoint(7.235, -1.215), pya.DPoint(7.085, -1.215), pya.DPoint(7.085, -1.365)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(7.405, -1.365), pya.DPoint(7.555, -1.365), pya.DPoint(7.555, -1.215), pya.DPoint(7.405, -1.215), pya.DPoint(7.405, -1.365)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.035, -1.365), pya.DPoint(8.185, -1.365), pya.DPoint(8.185, -1.215), pya.DPoint(8.035, -1.215), pya.DPoint(8.035, -1.365)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.355, -1.365), pya.DPoint(8.505, -1.365), pya.DPoint(8.505, -1.215), pya.DPoint(8.355, -1.215), pya.DPoint(8.355, -1.365)]))
cell_OgueyAebischerBias.shapes(L_via_drawing).insert(
    pya.DPolygon([pya.DPoint(8.675, -1.365), pya.DPoint(8.825, -1.365), pya.DPoint(8.825, -1.215), pya.DPoint(8.675, -1.215), pya.DPoint(8.675, -1.365)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 3.87), pya.DPoint(9.74, 3.87), pya.DPoint(9.74, 4.13), pya.DPoint(-1.77, 4.13), pya.DPoint(-1.77, 3.87)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 1.81), pya.DPoint(9.74, 1.81), pya.DPoint(9.74, 2.07), pya.DPoint(-1.77, 2.07), pya.DPoint(-1.77, 1.81)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.76, 1.41), pya.DPoint(9.74, 1.41), pya.DPoint(9.74, 1.67), pya.DPoint(-1.76, 1.67), pya.DPoint(-1.76, 1.41)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, 1.01), pya.DPoint(9.74, 1.01), pya.DPoint(9.74, 1.27), pya.DPoint(-1.77, 1.27), pya.DPoint(-1.77, 1.01)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -1.02), pya.DPoint(9.74, -1.02), pya.DPoint(9.74, -0.76), pya.DPoint(-1.77, -0.76), pya.DPoint(-1.77, -1.02)]))
cell_OgueyAebischerBias.shapes(L_met2_drawing).insert(
    pya.DPolygon([pya.DPoint(-1.77, -1.42), pya.DPoint(9.74, -1.42), pya.DPoint(9.74, -1.16), pya.DPoint(-1.77, -1.16), pya.DPoint(-1.77, -1.42)]))
_txt = pya.Text("vss",
               pya.Trans(0, False, pya.Vector(-1640, -1290)))
_txt.halign = 1
_txt.valign = 1
cell_OgueyAebischerBias.shapes(L_met2_pin).insert(_txt)
cell_OgueyAebischerBias.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-1.77, -1.42), pya.DPoint(-1.51, -1.42), pya.DPoint(-1.51, -1.16), pya.DPoint(-1.77, -1.16), pya.DPoint(-1.77, -1.42)]))
_txt = pya.Text("vdd",
               pya.Trans(0, False, pya.Vector(-1640, 4000)))
_txt.halign = 1
_txt.valign = 1
cell_OgueyAebischerBias.shapes(L_met2_pin).insert(_txt)
cell_OgueyAebischerBias.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-1.77, 3.87), pya.DPoint(-1.51, 3.87), pya.DPoint(-1.51, 4.13), pya.DPoint(-1.77, 4.13), pya.DPoint(-1.77, 3.87)]))
_txt = pya.Text("vbp",
               pya.Trans(0, False, pya.Vector(-1640, 1940)))
_txt.halign = 1
_txt.valign = 1
cell_OgueyAebischerBias.shapes(L_met2_pin).insert(_txt)
cell_OgueyAebischerBias.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-1.77, 1.81), pya.DPoint(-1.51, 1.81), pya.DPoint(-1.51, 2.07), pya.DPoint(-1.77, 2.07), pya.DPoint(-1.77, 1.81)]))
_txt = pya.Text("vbn",
               pya.Trans(0, False, pya.Vector(-1630, 1540)))
_txt.halign = 1
_txt.valign = 1
cell_OgueyAebischerBias.shapes(L_met2_pin).insert(_txt)
cell_OgueyAebischerBias.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-1.76, 1.41), pya.DPoint(-1.5, 1.41), pya.DPoint(-1.5, 1.67), pya.DPoint(-1.76, 1.67), pya.DPoint(-1.76, 1.41)]))
_txt = pya.Text("vbr",
               pya.Trans(0, False, pya.Vector(-1640, 1140)))
_txt.halign = 1
_txt.valign = 1
cell_OgueyAebischerBias.shapes(L_met2_pin).insert(_txt)
cell_OgueyAebischerBias.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-1.77, 1.01), pya.DPoint(-1.51, 1.01), pya.DPoint(-1.51, 1.27), pya.DPoint(-1.77, 1.27), pya.DPoint(-1.77, 1.01)]))

# === reference ===
cell_reference.insert(pya.DCellInstArray(
    cell_ToBiasStartup.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(-4.06, 0))))
cell_reference.insert(pya.DCellInstArray(
    cell_OgueyAebischerBias.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
_txt = pya.Text("vss",
               pya.Trans(0, False, pya.Vector(-6275, -1290)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, -1.42), pya.DPoint(-6.14, -1.42), pya.DPoint(-6.14, -1.16), pya.DPoint(-6.41, -1.16), pya.DPoint(-6.41, -1.42)]))
_txt = pya.Text("vdd",
               pya.Trans(0, False, pya.Vector(-6275, 4000)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, 3.87), pya.DPoint(-6.14, 3.87), pya.DPoint(-6.14, 4.13), pya.DPoint(-6.41, 4.13), pya.DPoint(-6.41, 3.87)]))
_txt = pya.Text("vbp",
               pya.Trans(0, False, pya.Vector(-6275, 1940)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, 1.81), pya.DPoint(-6.14, 1.81), pya.DPoint(-6.14, 2.07), pya.DPoint(-6.41, 2.07), pya.DPoint(-6.41, 1.81)]))
_txt = pya.Text("vbn",
               pya.Trans(0, False, pya.Vector(-6275, 1540)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, 1.41), pya.DPoint(-6.14, 1.41), pya.DPoint(-6.14, 1.67), pya.DPoint(-6.41, 1.67), pya.DPoint(-6.41, 1.41)]))
_txt = pya.Text("vbr",
               pya.Trans(0, False, pya.Vector(-6275, 1140)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, 1.01), pya.DPoint(-6.14, 1.01), pya.DPoint(-6.14, 1.27), pya.DPoint(-6.41, 1.27), pya.DPoint(-6.41, 1.01)]))
_txt = pya.Text("disable",
               pya.Trans(0, False, pya.Vector(-6275, 740)))
_txt.halign = 1
_txt.valign = 1
cell_reference.shapes(L_met2_pin).insert(_txt)
cell_reference.shapes(L_met2_label).insert(
    pya.DPolygon([pya.DPoint(-6.41, 0.61), pya.DPoint(-6.14, 0.61), pya.DPoint(-6.14, 0.87), pya.DPoint(-6.41, 0.87), pya.DPoint(-6.41, 0.61)]))

# === tatzelreference_tile ===
cell_tatzelreference_tile.insert(pya.DCellInstArray(
    cell_reference.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(45.33, 32.22))))
cell_tatzelreference_tile.shapes(L_235_4).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
cell_tatzelreference_tile.shapes(L_81_53).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 2), pya.DPoint(39.57, 2), pya.DPoint(39.57, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 2), pya.DPoint(58.89, 2), pya.DPoint(58.89, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 2), pya.DPoint(78.21, 2), pya.DPoint(78.21, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 2), pya.DPoint(97.53, 2), pya.DPoint(97.53, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 2), pya.DPoint(116.85, 2), pya.DPoint(116.85, 0)]))
cell_tatzelreference_tile.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 2), pya.DPoint(136.17, 2), pya.DPoint(136.17, 0)]))

# === tt_um_tatzelreference ===
cell_tt_um_tatzelreference.insert(pya.DCellInstArray(
    cell_tatzelreference_tile.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_tt_um_tatzelreference.shapes(L_235_4).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(145.36, 0), pya.DPoint(145.36, 225.76), pya.DPoint(0, 225.76), pya.DPoint(0, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(15.03, 224.76), pya.DPoint(15.33, 224.76), pya.DPoint(15.33, 225.76), pya.DPoint(15.03, 225.76), pya.DPoint(15.03, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(17.79, 224.76), pya.DPoint(18.09, 224.76), pya.DPoint(18.09, 225.76), pya.DPoint(17.79, 225.76), pya.DPoint(17.79, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(20.55, 224.76), pya.DPoint(20.85, 224.76), pya.DPoint(20.85, 225.76), pya.DPoint(20.55, 225.76), pya.DPoint(20.55, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(23.31, 224.76), pya.DPoint(23.61, 224.76), pya.DPoint(23.61, 225.76), pya.DPoint(23.31, 225.76), pya.DPoint(23.31, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(26.07, 224.76), pya.DPoint(26.37, 224.76), pya.DPoint(26.37, 225.76), pya.DPoint(26.07, 225.76), pya.DPoint(26.07, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(28.83, 224.76), pya.DPoint(29.13, 224.76), pya.DPoint(29.13, 225.76), pya.DPoint(28.83, 225.76), pya.DPoint(28.83, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(31.59, 224.76), pya.DPoint(31.89, 224.76), pya.DPoint(31.89, 225.76), pya.DPoint(31.59, 225.76), pya.DPoint(31.59, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(34.35, 224.76), pya.DPoint(34.65, 224.76), pya.DPoint(34.65, 225.76), pya.DPoint(34.35, 225.76), pya.DPoint(34.35, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(37.11, 224.76), pya.DPoint(37.41, 224.76), pya.DPoint(37.41, 225.76), pya.DPoint(37.11, 225.76), pya.DPoint(37.11, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(39.87, 224.76), pya.DPoint(40.17, 224.76), pya.DPoint(40.17, 225.76), pya.DPoint(39.87, 225.76), pya.DPoint(39.87, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(42.63, 224.76), pya.DPoint(42.93, 224.76), pya.DPoint(42.93, 225.76), pya.DPoint(42.63, 225.76), pya.DPoint(42.63, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(45.39, 224.76), pya.DPoint(45.69, 224.76), pya.DPoint(45.69, 225.76), pya.DPoint(45.39, 225.76), pya.DPoint(45.39, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(48.15, 224.76), pya.DPoint(48.45, 224.76), pya.DPoint(48.45, 225.76), pya.DPoint(48.15, 225.76), pya.DPoint(48.15, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(50.91, 224.76), pya.DPoint(51.21, 224.76), pya.DPoint(51.21, 225.76), pya.DPoint(50.91, 225.76), pya.DPoint(50.91, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(53.67, 224.76), pya.DPoint(53.97, 224.76), pya.DPoint(53.97, 225.76), pya.DPoint(53.67, 225.76), pya.DPoint(53.67, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(56.43, 224.76), pya.DPoint(56.73, 224.76), pya.DPoint(56.73, 225.76), pya.DPoint(56.43, 225.76), pya.DPoint(56.43, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(59.19, 224.76), pya.DPoint(59.49, 224.76), pya.DPoint(59.49, 225.76), pya.DPoint(59.19, 225.76), pya.DPoint(59.19, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(61.95, 224.76), pya.DPoint(62.25, 224.76), pya.DPoint(62.25, 225.76), pya.DPoint(61.95, 225.76), pya.DPoint(61.95, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(64.71, 224.76), pya.DPoint(65.01, 224.76), pya.DPoint(65.01, 225.76), pya.DPoint(64.71, 225.76), pya.DPoint(64.71, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(67.47, 224.76), pya.DPoint(67.77, 224.76), pya.DPoint(67.77, 225.76), pya.DPoint(67.47, 225.76), pya.DPoint(67.47, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(70.23, 224.76), pya.DPoint(70.53, 224.76), pya.DPoint(70.53, 225.76), pya.DPoint(70.23, 225.76), pya.DPoint(70.23, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(72.99, 224.76), pya.DPoint(73.29, 224.76), pya.DPoint(73.29, 225.76), pya.DPoint(72.99, 225.76), pya.DPoint(72.99, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(75.75, 224.76), pya.DPoint(76.05, 224.76), pya.DPoint(76.05, 225.76), pya.DPoint(75.75, 225.76), pya.DPoint(75.75, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(78.51, 224.76), pya.DPoint(78.81, 224.76), pya.DPoint(78.81, 225.76), pya.DPoint(78.51, 225.76), pya.DPoint(78.51, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(81.27, 224.76), pya.DPoint(81.57, 224.76), pya.DPoint(81.57, 225.76), pya.DPoint(81.27, 225.76), pya.DPoint(81.27, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(84.03, 224.76), pya.DPoint(84.33, 224.76), pya.DPoint(84.33, 225.76), pya.DPoint(84.03, 225.76), pya.DPoint(84.03, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(86.79, 224.76), pya.DPoint(87.09, 224.76), pya.DPoint(87.09, 225.76), pya.DPoint(86.79, 225.76), pya.DPoint(86.79, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(89.55, 224.76), pya.DPoint(89.85, 224.76), pya.DPoint(89.85, 225.76), pya.DPoint(89.55, 225.76), pya.DPoint(89.55, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(92.31, 224.76), pya.DPoint(92.61, 224.76), pya.DPoint(92.61, 225.76), pya.DPoint(92.31, 225.76), pya.DPoint(92.31, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(95.07, 224.76), pya.DPoint(95.37, 224.76), pya.DPoint(95.37, 225.76), pya.DPoint(95.07, 225.76), pya.DPoint(95.07, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(97.83, 224.76), pya.DPoint(98.13, 224.76), pya.DPoint(98.13, 225.76), pya.DPoint(97.83, 225.76), pya.DPoint(97.83, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(100.59, 224.76), pya.DPoint(100.89, 224.76), pya.DPoint(100.89, 225.76), pya.DPoint(100.59, 225.76), pya.DPoint(100.59, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(103.35, 224.76), pya.DPoint(103.65, 224.76), pya.DPoint(103.65, 225.76), pya.DPoint(103.35, 225.76), pya.DPoint(103.35, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(106.11, 224.76), pya.DPoint(106.41, 224.76), pya.DPoint(106.41, 225.76), pya.DPoint(106.11, 225.76), pya.DPoint(106.11, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(108.87, 224.76), pya.DPoint(109.17, 224.76), pya.DPoint(109.17, 225.76), pya.DPoint(108.87, 225.76), pya.DPoint(108.87, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(111.63, 224.76), pya.DPoint(111.93, 224.76), pya.DPoint(111.93, 225.76), pya.DPoint(111.63, 225.76), pya.DPoint(111.63, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(114.39, 224.76), pya.DPoint(114.69, 224.76), pya.DPoint(114.69, 225.76), pya.DPoint(114.39, 225.76), pya.DPoint(114.39, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(117.15, 224.76), pya.DPoint(117.45, 224.76), pya.DPoint(117.45, 225.76), pya.DPoint(117.15, 225.76), pya.DPoint(117.15, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(119.91, 224.76), pya.DPoint(120.21, 224.76), pya.DPoint(120.21, 225.76), pya.DPoint(119.91, 225.76), pya.DPoint(119.91, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(122.67, 224.76), pya.DPoint(122.97, 224.76), pya.DPoint(122.97, 225.76), pya.DPoint(122.67, 225.76), pya.DPoint(122.67, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(125.43, 224.76), pya.DPoint(125.73, 224.76), pya.DPoint(125.73, 225.76), pya.DPoint(125.43, 225.76), pya.DPoint(125.43, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(128.19, 224.76), pya.DPoint(128.49, 224.76), pya.DPoint(128.49, 225.76), pya.DPoint(128.19, 225.76), pya.DPoint(128.19, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(130.95, 224.76), pya.DPoint(131.25, 224.76), pya.DPoint(131.25, 225.76), pya.DPoint(130.95, 225.76), pya.DPoint(130.95, 224.76)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(1, 5), pya.DPoint(3, 5), pya.DPoint(3, 220.76), pya.DPoint(1, 220.76), pya.DPoint(1, 5)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(4, 5), pya.DPoint(6, 5), pya.DPoint(6, 220.76), pya.DPoint(4, 220.76), pya.DPoint(4, 5)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(7, 5), pya.DPoint(9, 5), pya.DPoint(9, 220.76), pya.DPoint(7, 220.76), pya.DPoint(7, 5)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(0.93, 0), pya.DPoint(1.83, 0), pya.DPoint(1.83, 1), pya.DPoint(0.93, 1), pya.DPoint(0.93, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(20.25, 0), pya.DPoint(21.15, 0), pya.DPoint(21.15, 1), pya.DPoint(20.25, 1), pya.DPoint(20.25, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 1), pya.DPoint(39.57, 1), pya.DPoint(39.57, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 1), pya.DPoint(58.89, 1), pya.DPoint(58.89, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 1), pya.DPoint(78.21, 1), pya.DPoint(78.21, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 1), pya.DPoint(97.53, 1), pya.DPoint(97.53, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 1), pya.DPoint(116.85, 1), pya.DPoint(116.85, 0)]))
cell_tt_um_tatzelreference.shapes(L_met4_drawing).insert(
    pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 1), pya.DPoint(136.17, 1), pya.DPoint(136.17, 0)]))
_txt = pya.Text("clk",
               pya.Trans(1, False, pya.Vector(128340, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(128.19, 224.76), pya.DPoint(128.49, 224.76), pya.DPoint(128.49, 225.76), pya.DPoint(128.19, 225.76), pya.DPoint(128.19, 224.76)]))
_txt = pya.Text("ena",
               pya.Trans(1, False, pya.Vector(131100, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(130.95, 224.76), pya.DPoint(131.25, 224.76), pya.DPoint(131.25, 225.76), pya.DPoint(130.95, 225.76), pya.DPoint(130.95, 224.76)]))
_txt = pya.Text("rst_n",
               pya.Trans(1, False, pya.Vector(125580, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(125.43, 224.76), pya.DPoint(125.73, 224.76), pya.DPoint(125.73, 225.76), pya.DPoint(125.43, 225.76), pya.DPoint(125.43, 224.76)]))
_txt = pya.Text("ua[0]",
               pya.Trans(0, False, pya.Vector(136620, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(136.17, 0), pya.DPoint(137.07, 0), pya.DPoint(137.07, 1), pya.DPoint(136.17, 1), pya.DPoint(136.17, 0)]))
_txt = pya.Text("ua[1]",
               pya.Trans(0, False, pya.Vector(117300, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(116.85, 0), pya.DPoint(117.75, 0), pya.DPoint(117.75, 1), pya.DPoint(116.85, 1), pya.DPoint(116.85, 0)]))
_txt = pya.Text("ua[2]",
               pya.Trans(0, False, pya.Vector(97980, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(97.53, 0), pya.DPoint(98.43, 0), pya.DPoint(98.43, 1), pya.DPoint(97.53, 1), pya.DPoint(97.53, 0)]))
_txt = pya.Text("ua[3]",
               pya.Trans(0, False, pya.Vector(78660, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(78.21, 0), pya.DPoint(79.11, 0), pya.DPoint(79.11, 1), pya.DPoint(78.21, 1), pya.DPoint(78.21, 0)]))
_txt = pya.Text("ua[4]",
               pya.Trans(0, False, pya.Vector(59340, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(58.89, 0), pya.DPoint(59.79, 0), pya.DPoint(59.79, 1), pya.DPoint(58.89, 1), pya.DPoint(58.89, 0)]))
_txt = pya.Text("ua[5]",
               pya.Trans(0, False, pya.Vector(40020, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(39.57, 0), pya.DPoint(40.47, 0), pya.DPoint(40.47, 1), pya.DPoint(39.57, 1), pya.DPoint(39.57, 0)]))
_txt = pya.Text("ua[6]",
               pya.Trans(0, False, pya.Vector(20700, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(20.25, 0), pya.DPoint(21.15, 0), pya.DPoint(21.15, 1), pya.DPoint(20.25, 1), pya.DPoint(20.25, 0)]))
_txt = pya.Text("ua[7]",
               pya.Trans(0, False, pya.Vector(1380, 500)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(0.93, 0), pya.DPoint(1.83, 0), pya.DPoint(1.83, 1), pya.DPoint(0.93, 1), pya.DPoint(0.93, 0)]))
_txt = pya.Text("ui_in[0]",
               pya.Trans(1, False, pya.Vector(122820, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(122.67, 224.76), pya.DPoint(122.97, 224.76), pya.DPoint(122.97, 225.76), pya.DPoint(122.67, 225.76), pya.DPoint(122.67, 224.76)]))
_txt = pya.Text("ui_in[1]",
               pya.Trans(1, False, pya.Vector(120060, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(119.91, 224.76), pya.DPoint(120.21, 224.76), pya.DPoint(120.21, 225.76), pya.DPoint(119.91, 225.76), pya.DPoint(119.91, 224.76)]))
_txt = pya.Text("ui_in[2]",
               pya.Trans(1, False, pya.Vector(117300, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(117.15, 224.76), pya.DPoint(117.45, 224.76), pya.DPoint(117.45, 225.76), pya.DPoint(117.15, 225.76), pya.DPoint(117.15, 224.76)]))
_txt = pya.Text("ui_in[3]",
               pya.Trans(1, False, pya.Vector(114540, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(114.39, 224.76), pya.DPoint(114.69, 224.76), pya.DPoint(114.69, 225.76), pya.DPoint(114.39, 225.76), pya.DPoint(114.39, 224.76)]))
_txt = pya.Text("ui_in[4]",
               pya.Trans(1, False, pya.Vector(111780, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(111.63, 224.76), pya.DPoint(111.93, 224.76), pya.DPoint(111.93, 225.76), pya.DPoint(111.63, 225.76), pya.DPoint(111.63, 224.76)]))
_txt = pya.Text("ui_in[5]",
               pya.Trans(1, False, pya.Vector(109020, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(108.87, 224.76), pya.DPoint(109.17, 224.76), pya.DPoint(109.17, 225.76), pya.DPoint(108.87, 225.76), pya.DPoint(108.87, 224.76)]))
_txt = pya.Text("ui_in[6]",
               pya.Trans(1, False, pya.Vector(106260, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(106.11, 224.76), pya.DPoint(106.41, 224.76), pya.DPoint(106.41, 225.76), pya.DPoint(106.11, 225.76), pya.DPoint(106.11, 224.76)]))
_txt = pya.Text("ui_in[7]",
               pya.Trans(1, False, pya.Vector(103500, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(103.35, 224.76), pya.DPoint(103.65, 224.76), pya.DPoint(103.65, 225.76), pya.DPoint(103.35, 225.76), pya.DPoint(103.35, 224.76)]))
_txt = pya.Text("uio_in[0]",
               pya.Trans(1, False, pya.Vector(100740, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(100.59, 224.76), pya.DPoint(100.89, 224.76), pya.DPoint(100.89, 225.76), pya.DPoint(100.59, 225.76), pya.DPoint(100.59, 224.76)]))
_txt = pya.Text("uio_in[1]",
               pya.Trans(1, False, pya.Vector(97980, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(97.83, 224.76), pya.DPoint(98.13, 224.76), pya.DPoint(98.13, 225.76), pya.DPoint(97.83, 225.76), pya.DPoint(97.83, 224.76)]))
_txt = pya.Text("uio_in[2]",
               pya.Trans(1, False, pya.Vector(95220, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(95.07, 224.76), pya.DPoint(95.37, 224.76), pya.DPoint(95.37, 225.76), pya.DPoint(95.07, 225.76), pya.DPoint(95.07, 224.76)]))
_txt = pya.Text("uio_in[3]",
               pya.Trans(1, False, pya.Vector(92460, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(92.31, 224.76), pya.DPoint(92.61, 224.76), pya.DPoint(92.61, 225.76), pya.DPoint(92.31, 225.76), pya.DPoint(92.31, 224.76)]))
_txt = pya.Text("uio_in[4]",
               pya.Trans(1, False, pya.Vector(89700, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(89.55, 224.76), pya.DPoint(89.85, 224.76), pya.DPoint(89.85, 225.76), pya.DPoint(89.55, 225.76), pya.DPoint(89.55, 224.76)]))
_txt = pya.Text("uio_in[5]",
               pya.Trans(1, False, pya.Vector(86940, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(86.79, 224.76), pya.DPoint(87.09, 224.76), pya.DPoint(87.09, 225.76), pya.DPoint(86.79, 225.76), pya.DPoint(86.79, 224.76)]))
_txt = pya.Text("uio_in[6]",
               pya.Trans(1, False, pya.Vector(84180, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(84.03, 224.76), pya.DPoint(84.33, 224.76), pya.DPoint(84.33, 225.76), pya.DPoint(84.03, 225.76), pya.DPoint(84.03, 224.76)]))
_txt = pya.Text("uio_in[7]",
               pya.Trans(1, False, pya.Vector(81420, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(81.27, 224.76), pya.DPoint(81.57, 224.76), pya.DPoint(81.57, 225.76), pya.DPoint(81.27, 225.76), pya.DPoint(81.27, 224.76)]))
_txt = pya.Text("uio_oe[0]",
               pya.Trans(1, False, pya.Vector(34500, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(34.35, 224.76), pya.DPoint(34.65, 224.76), pya.DPoint(34.65, 225.76), pya.DPoint(34.35, 225.76), pya.DPoint(34.35, 224.76)]))
_txt = pya.Text("uio_oe[1]",
               pya.Trans(1, False, pya.Vector(31740, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(31.59, 224.76), pya.DPoint(31.89, 224.76), pya.DPoint(31.89, 225.76), pya.DPoint(31.59, 225.76), pya.DPoint(31.59, 224.76)]))
_txt = pya.Text("uio_oe[2]",
               pya.Trans(1, False, pya.Vector(28980, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(28.83, 224.76), pya.DPoint(29.13, 224.76), pya.DPoint(29.13, 225.76), pya.DPoint(28.83, 225.76), pya.DPoint(28.83, 224.76)]))
_txt = pya.Text("uio_oe[3]",
               pya.Trans(1, False, pya.Vector(26220, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(26.07, 224.76), pya.DPoint(26.37, 224.76), pya.DPoint(26.37, 225.76), pya.DPoint(26.07, 225.76), pya.DPoint(26.07, 224.76)]))
_txt = pya.Text("uio_oe[4]",
               pya.Trans(1, False, pya.Vector(23460, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(23.31, 224.76), pya.DPoint(23.61, 224.76), pya.DPoint(23.61, 225.76), pya.DPoint(23.31, 225.76), pya.DPoint(23.31, 224.76)]))
_txt = pya.Text("uio_oe[5]",
               pya.Trans(1, False, pya.Vector(20700, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(20.55, 224.76), pya.DPoint(20.85, 224.76), pya.DPoint(20.85, 225.76), pya.DPoint(20.55, 225.76), pya.DPoint(20.55, 224.76)]))
_txt = pya.Text("uio_oe[6]",
               pya.Trans(1, False, pya.Vector(17940, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(17.79, 224.76), pya.DPoint(18.09, 224.76), pya.DPoint(18.09, 225.76), pya.DPoint(17.79, 225.76), pya.DPoint(17.79, 224.76)]))
_txt = pya.Text("uio_oe[7]",
               pya.Trans(1, False, pya.Vector(15180, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(15.03, 224.76), pya.DPoint(15.33, 224.76), pya.DPoint(15.33, 225.76), pya.DPoint(15.03, 225.76), pya.DPoint(15.03, 224.76)]))
_txt = pya.Text("uio_out[0]",
               pya.Trans(1, False, pya.Vector(56580, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(56.43, 224.76), pya.DPoint(56.73, 224.76), pya.DPoint(56.73, 225.76), pya.DPoint(56.43, 225.76), pya.DPoint(56.43, 224.76)]))
_txt = pya.Text("uio_out[1]",
               pya.Trans(1, False, pya.Vector(53820, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(53.67, 224.76), pya.DPoint(53.97, 224.76), pya.DPoint(53.97, 225.76), pya.DPoint(53.67, 225.76), pya.DPoint(53.67, 224.76)]))
_txt = pya.Text("uio_out[2]",
               pya.Trans(1, False, pya.Vector(51060, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(50.91, 224.76), pya.DPoint(51.21, 224.76), pya.DPoint(51.21, 225.76), pya.DPoint(50.91, 225.76), pya.DPoint(50.91, 224.76)]))
_txt = pya.Text("uio_out[3]",
               pya.Trans(1, False, pya.Vector(48300, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(48.15, 224.76), pya.DPoint(48.45, 224.76), pya.DPoint(48.45, 225.76), pya.DPoint(48.15, 225.76), pya.DPoint(48.15, 224.76)]))
_txt = pya.Text("uio_out[4]",
               pya.Trans(1, False, pya.Vector(45540, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(45.39, 224.76), pya.DPoint(45.69, 224.76), pya.DPoint(45.69, 225.76), pya.DPoint(45.39, 225.76), pya.DPoint(45.39, 224.76)]))
_txt = pya.Text("uio_out[5]",
               pya.Trans(1, False, pya.Vector(42780, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(42.63, 224.76), pya.DPoint(42.93, 224.76), pya.DPoint(42.93, 225.76), pya.DPoint(42.63, 225.76), pya.DPoint(42.63, 224.76)]))
_txt = pya.Text("uio_out[6]",
               pya.Trans(1, False, pya.Vector(40020, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(39.87, 224.76), pya.DPoint(40.17, 224.76), pya.DPoint(40.17, 225.76), pya.DPoint(39.87, 225.76), pya.DPoint(39.87, 224.76)]))
_txt = pya.Text("uio_out[7]",
               pya.Trans(1, False, pya.Vector(37260, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(37.11, 224.76), pya.DPoint(37.41, 224.76), pya.DPoint(37.41, 225.76), pya.DPoint(37.11, 225.76), pya.DPoint(37.11, 224.76)]))
_txt = pya.Text("uo_out[0]",
               pya.Trans(1, False, pya.Vector(78660, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(78.51, 224.76), pya.DPoint(78.81, 224.76), pya.DPoint(78.81, 225.76), pya.DPoint(78.51, 225.76), pya.DPoint(78.51, 224.76)]))
_txt = pya.Text("uo_out[1]",
               pya.Trans(1, False, pya.Vector(75900, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(75.75, 224.76), pya.DPoint(76.05, 224.76), pya.DPoint(76.05, 225.76), pya.DPoint(75.75, 225.76), pya.DPoint(75.75, 224.76)]))
_txt = pya.Text("uo_out[2]",
               pya.Trans(1, False, pya.Vector(73140, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(72.99, 224.76), pya.DPoint(73.29, 224.76), pya.DPoint(73.29, 225.76), pya.DPoint(72.99, 225.76), pya.DPoint(72.99, 224.76)]))
_txt = pya.Text("uo_out[3]",
               pya.Trans(1, False, pya.Vector(70380, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(70.23, 224.76), pya.DPoint(70.53, 224.76), pya.DPoint(70.53, 225.76), pya.DPoint(70.23, 225.76), pya.DPoint(70.23, 224.76)]))
_txt = pya.Text("uo_out[4]",
               pya.Trans(1, False, pya.Vector(67620, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(67.47, 224.76), pya.DPoint(67.77, 224.76), pya.DPoint(67.77, 225.76), pya.DPoint(67.47, 225.76), pya.DPoint(67.47, 224.76)]))
_txt = pya.Text("uo_out[5]",
               pya.Trans(1, False, pya.Vector(64860, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(64.71, 224.76), pya.DPoint(65.01, 224.76), pya.DPoint(65.01, 225.76), pya.DPoint(64.71, 225.76), pya.DPoint(64.71, 224.76)]))
_txt = pya.Text("uo_out[6]",
               pya.Trans(1, False, pya.Vector(62100, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(61.95, 224.76), pya.DPoint(62.25, 224.76), pya.DPoint(62.25, 225.76), pya.DPoint(61.95, 225.76), pya.DPoint(61.95, 224.76)]))
_txt = pya.Text("uo_out[7]",
               pya.Trans(1, False, pya.Vector(59340, 225260)))
_txt.halign = 1
_txt.valign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(59.19, 224.76), pya.DPoint(59.49, 224.76), pya.DPoint(59.49, 225.76), pya.DPoint(59.19, 225.76), pya.DPoint(59.19, 224.76)]))
_txt = pya.Text("VDPWR",
               pya.Trans(0, False, pya.Vector(2000, 112880)))
_txt.halign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(1, 5), pya.DPoint(3, 5), pya.DPoint(3, 220.76), pya.DPoint(1, 220.76), pya.DPoint(1, 5)]))
_txt = pya.Text("VGND",
               pya.Trans(0, False, pya.Vector(5000, 112880)))
_txt.halign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(4, 5), pya.DPoint(6, 5), pya.DPoint(6, 220.76), pya.DPoint(4, 220.76), pya.DPoint(4, 5)]))
_txt = pya.Text("VAPWR",
               pya.Trans(0, False, pya.Vector(8000, 112880)))
_txt.halign = 1
cell_tt_um_tatzelreference.shapes(L_met4_pin).insert(_txt)
cell_tt_um_tatzelreference.shapes(L_met4_label).insert(
    pya.DPolygon([pya.DPoint(7, 5), pya.DPoint(9, 5), pya.DPoint(9, 220.76), pya.DPoint(7, 220.76), pya.DPoint(7, 5)]))

# Save
layout.write("output.gds")
