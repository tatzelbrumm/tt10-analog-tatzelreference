# Save the layout and export GDS/LEF
# ----------------------------------
set TOP_LEVEL_CELL     tt_um_tatzelreference
save ${TOP_LEVEL_CELL}.mag
file mkdir gds
gds write gds/${TOP_LEVEL_CELL}.gds
file mkdir lef
lef write lef/${TOP_LEVEL_CELL}.lef -hide -pinonly
