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
    L.L_nwell_drawing = layout.layer(pya.LayerInfo(31, 0, "NWell.drawing"))
    L.L_diff_drawing = layout.layer(pya.LayerInfo(1, 0, "Activ.drawing"))
    L.L_tap_drawing = layout.layer(pya.LayerInfo(6, 0, "Cont.drawing"))
    L.L_poly_drawing = layout.layer(pya.LayerInfo(5, 0, "GatPoly.drawing"))
    L.L_licon1_drawing = layout.layer(pya.LayerInfo(6, 0, "Cont.drawing"))
    L.L_li1_drawing = layout.layer(pya.LayerInfo(8, 0, "Metal1.drawing"))
    L.L_mcon_drawing = layout.layer(pya.LayerInfo(19, 0, "Via1.drawing"))
    L.L_met1_drawing = layout.layer(pya.LayerInfo(10, 0, "Metal2.drawing"))
    L.L_via_drawing = layout.layer(pya.LayerInfo(29, 0, "Via2.drawing"))
    L.L_met2_pin = layout.layer(pya.LayerInfo(30, 2, "Metal3.pin"))
    L.L_met2_label = layout.layer(pya.LayerInfo(30, 25, "Metal3.text"))
    L.L_met2_drawing = layout.layer(pya.LayerInfo(30, 0, "Metal3.drawing"))
    L.L_met4_pin = layout.layer(pya.LayerInfo(50, 2, "Metal4.pin"))
    L.L_met4_label = layout.layer(pya.LayerInfo(50, 25, "Metal4.text"))
    L.L_met4_drawing = layout.layer(pya.LayerInfo(50, 0, "Metal4.drawing"))
    L.L_81_53 = layout.layer(81, 53)
    L.L_nsdm_drawing = layout.layer(pya.LayerInfo(7, 0, "nSD.drawing"))
    L.L_psdm_drawing = layout.layer(pya.LayerInfo(14, 0, "pSD.drawing"))
    L.L_npc_drawing = layout.layer(pya.LayerInfo(95, 20, "npc.drawing"))
    L.L_235_4 = layout.layer(pya.LayerInfo(189, 4, "prBoundary.boundary"))
    return L
