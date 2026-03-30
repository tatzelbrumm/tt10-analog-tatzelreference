# Layer Maps for gds2klayout

## Files

| File             | PDK            | Entries | Source |
|------------------|----------------|---------|--------|
| `sg13_layers.map`| IHP SG13G2     | 376     | `sg13g2.lyp` (hand-extracted) |
| `sky130A.map`    | Sky130A / B    | 69      | `sky130A.lyt` + `sky130gds.tech` |

sky130A and sky130B use **identical** GDS layer numbers. Use `sky130A.map` for both.

---

## Usage

```bash
python gds2klayout.py design.gds design_named.py --layer-map sky130A.map
python gds2klayout.py design.gds design_named.py --layer-map sg13_layers.map
```

---

## Generating a fresh map from your installed PDK

The authoritative source for layer numbers is always the `.lyp` file inside your
PDK installation. Use `lyp2map.py` to convert it directly — no manual transcription,
no guessing:

```bash
# IHP SG13G2 (if installed via open_pdks or the IHP GitHub repo)
python lyp2map.py $PDK_ROOT/ihp-sg13g2/libs.tech/klayout/tech/sg13g2.lyp sg13_layers.map

# Sky130A
python lyp2map.py $PDK_ROOT/sky130A/libs.tech/klayout/tech/sky130A.lyp sky130A.map

# Sky130B
python lyp2map.py $PDK_ROOT/sky130B/libs.tech/klayout/tech/sky130B.lyp sky130B.map

# GF180MCU (GlobalFoundries 180nm)
python lyp2map.py $PDK_ROOT/gf180mcuA/libs.tech/klayout/tech/gf180mcuA.lyp gf180mcu.map
```

### Where `$PDK_ROOT` lives

| Installation method | Typical path |
|---------------------|--------------|
| `volare` / efabless | `~/.volare/<pdk>/` |
| `open_pdks` manual  | `/usr/share/pdk/` or wherever you ran `make install` |
| Nix / IIC-OSIC-TOOLS | `/foss/pdk/<pdk>/` |
| IHP repo clone      | `<repo>/ihp-sg13g2/libs.tech/klayout/tech/` |

If you have KLayout installed with the technology loaded, the `.lyp` is also at:
```
~/.klayout/tech/<tech-name>/<tech-name>.lyp
```

### If the `.lyp` doesn't exist yet

Some PDK installations put the layer properties inside a `.lyt` technology file
rather than a standalone `.lyp`. In KLayout: open the GDS, select the technology,
then **File → Save Layer Properties** to export a `.lyp` you can feed to `lyp2map.py`.

---

## What `lyp2map.py` does and doesn't do

**Does:**
- Parse the XML with a conformant parser (no regex on raw XML)
- Skip wildcard sources (`*/*`), named-only sources, and entries with no numeric layer/datatype
- Sanitize names (collapse spaces/special chars to underscores)
- Warn on duplicates (first entry wins, matching KLayout's own precedence)
- Reject layer/datatype values > 4095 (GDS 12-bit limit)

**Doesn't:**
- Preserve display colors, fill patterns, or visibility settings (not needed for `.map`)
- Handle OASIS named layers (no GDS integer identity)
- Handle grouped/nested layer properties that don't have their own `<source>`

---

## A note on sky130 layer numbering

Sky130 uses a non-intuitive numbering scheme. The BEOL stack is:

```
licon1  66/44   (poly/diff contact -> LI1)
li1     67/20   (local interconnect)
mcon    67/44   (LI1 -> Met1 contact)
met1    68/20
via     68/44   (Met1 -> Met2)
met2    69/20
via2    69/44
met3    70/20
via3    70/44
met4    71/20
via4    71/44
met5    72/20   ← NOT 77, despite met5 being the 5th metal
pad     76/20
```

The numbers jump around because sky130 evolved from an older numbering scheme
and some layers were renumbered when the process was extended.
