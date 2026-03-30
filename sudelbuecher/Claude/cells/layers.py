# layers.py  -  edit THIS file to remap sky130 layers to IHP sg13g2
# Format: L_<name> = layout.layer(layer, datatype)
#
# sky130 -> IHP sg13g2 quick reference:
#   nwell.drawing  (64/20)  -> NWell.drawing      (31/0)
#   diff.drawing   (65/20)  -> Activ.drawing       (1/0)
#   tap.drawing    (65/44)  -> Activ.drawing       (1/0)
#   poly.drawing   (66/20)  -> GatPoly.drawing     (5/0)
#   licon1.drawing (66/44)  -> Cont.drawing        (6/0)
#   li1.drawing    (67/20)  -> Metal1.drawing      (8/0)  [no li1 in IHP]
#   mcon.drawing   (67/44)  -> Via1.drawing       (19/0)
#   met1.drawing   (68/20)  -> Metal1.drawing      (8/0)
#   via.drawing    (68/44)  -> Via1.drawing       (19/0)
#   met2.drawing   (69/20)  -> Metal2.drawing     (10/0)
#   met4.drawing   (71/20)  -> Metal4.drawing     (50/0)
#   nsdm.drawing   (93/44)  -> nSD.drawing         (7/0)
#   psdm.drawing   (94/20)  -> pSD.drawing        (14/0)
#
import pya

def register_layers(layout):
    class Layers: pass
    L = Layers()
    L.L_nwell_drawing = layout.layer(pya.LayerInfo(64, 20, "nwell.drawing"))
    L.L_diff_drawing = layout.layer(pya.LayerInfo(65, 20, "diff.drawing"))
    L.L_tap_drawing = layout.layer(pya.LayerInfo(65, 44, "tap.drawing"))
    L.L_poly_drawing = layout.layer(pya.LayerInfo(66, 20, "poly.drawing"))
    L.L_licon1_drawing = layout.layer(pya.LayerInfo(66, 44, "licon1.drawing"))
    L.L_li1_drawing = layout.layer(pya.LayerInfo(67, 20, "li1.drawing"))
    L.L_mcon_drawing = layout.layer(pya.LayerInfo(67, 44, "mcon.drawing"))
    L.L_met1_drawing = layout.layer(pya.LayerInfo(68, 20, "met1.drawing"))
    L.L_via_drawing = layout.layer(pya.LayerInfo(68, 44, "via.drawing"))
    L.L_met2_pin = layout.layer(pya.LayerInfo(69, 5, "met2.pin"))
    L.L_met2_label = layout.layer(pya.LayerInfo(69, 16, "met2.label"))
    L.L_met2_drawing = layout.layer(pya.LayerInfo(69, 20, "met2.drawing"))
    L.L_met4_pin = layout.layer(pya.LayerInfo(71, 5, "met4.pin"))
    L.L_met4_label = layout.layer(pya.LayerInfo(71, 16, "met4.label"))
    L.L_met4_drawing = layout.layer(pya.LayerInfo(71, 20, "met4.drawing"))
    L.L_81_53 = layout.layer(81, 53)
    L.L_nsdm_drawing = layout.layer(pya.LayerInfo(93, 44, "nsdm.drawing"))
    L.L_psdm_drawing = layout.layer(pya.LayerInfo(94, 20, "psdm.drawing"))
    L.L_npc_drawing = layout.layer(pya.LayerInfo(95, 20, "npc.drawing"))
    L.L_235_4 = layout.layer(235, 4)
    return L
