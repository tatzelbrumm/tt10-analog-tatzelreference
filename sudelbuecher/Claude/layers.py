# layers.py  –  edit THIS file to remap sky130 layers to IHP sg13g2
# Format: L_<GDS_layer>_<GDS_datatype> = layout.layer(layer, datatype)
# Replace the (layer, datatype) pairs with IHP equivalents.
#
# sky130 → IHP sg13g2 mapping hints (fill in IHP numbers from sg13g2 PDK docs):
#   64/20  nwell       → IHP NWell          (?/0)
#   65/20  diff/active → IHP Activ           (1/0)
#   65/44  tap         → IHP Activ           (1/0)  [same layer, no tap distinction]
#   66/20  poly        → IHP GatPoly         (5/0)
#   66/44  contact     → IHP Cont            (6/0)
#   67/20  li1         → IHP (no li1 equiv – use Metal1 or merge into contact)
#   67/44  mcon        → IHP Via1            (19/0)
#   68/20  met1        → IHP Metal1          (8/0)
#   68/44  via1        → IHP Via1            (19/0)
#   69/20  met2        → IHP Metal2          (10/0)
#   71/20  met4        → IHP Metal4          (?) – check PDK
#   93/44  nsdm        → IHP nSD             (?) 
#   94/20  psdm        → IHP pSD             (?)
#   81/53  areaid      → IHP prBoundary / TT keepout
#   235/4  prBoundary  → IHP prBoundary
#
# NOTE: sky130 li1 (local interconnect) has no direct IHP equivalent.
# Geometry on li1 must be re-drawn using Metal1 with IHP DRC clearances.

import pya

def register_layers(layout):
    """Call this once with your pya.Layout() instance.
       Returns a namespace object with all layer index variables."""
    class Layers: pass
    L = Layers()
    L.L_64_20 = layout.layer(64, 20)  # sky130 64/20 – TODO remap for IHP
    L.L_65_20 = layout.layer(65, 20)  # sky130 65/20 – TODO remap for IHP
    L.L_65_44 = layout.layer(65, 44)  # sky130 65/44 – TODO remap for IHP
    L.L_66_20 = layout.layer(66, 20)  # sky130 66/20 – TODO remap for IHP
    L.L_66_44 = layout.layer(66, 44)  # sky130 66/44 – TODO remap for IHP
    L.L_67_20 = layout.layer(67, 20)  # sky130 67/20 – TODO remap for IHP
    L.L_67_44 = layout.layer(67, 44)  # sky130 67/44 – TODO remap for IHP
    L.L_68_20 = layout.layer(68, 20)  # sky130 68/20 – TODO remap for IHP
    L.L_68_44 = layout.layer(68, 44)  # sky130 68/44 – TODO remap for IHP
    L.L_69_5 = layout.layer(69, 5)  # sky130 69/5 – TODO remap for IHP
    L.L_69_16 = layout.layer(69, 16)  # sky130 69/16 – TODO remap for IHP
    L.L_69_20 = layout.layer(69, 20)  # sky130 69/20 – TODO remap for IHP
    L.L_71_5 = layout.layer(71, 5)  # sky130 71/5 – TODO remap for IHP
    L.L_71_16 = layout.layer(71, 16)  # sky130 71/16 – TODO remap for IHP
    L.L_71_20 = layout.layer(71, 20)  # sky130 71/20 – TODO remap for IHP
    L.L_81_53 = layout.layer(81, 53)  # sky130 81/53 – TODO remap for IHP
    L.L_93_44 = layout.layer(93, 44)  # sky130 93/44 – TODO remap for IHP
    L.L_94_20 = layout.layer(94, 20)  # sky130 94/20 – TODO remap for IHP
    L.L_95_20 = layout.layer(95, 20)  # sky130 95/20 – TODO remap for IHP
    L.L_235_4 = layout.layer(235, 4)  # sky130 235/4 – TODO remap for IHP
    return L
