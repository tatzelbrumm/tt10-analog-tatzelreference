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
    L.L_81_53 = layout.layer(81, 53)  # TODO remap for IHP
    L.L_235_4 = layout.layer(235, 4)  # TODO remap for IHP
    return L
