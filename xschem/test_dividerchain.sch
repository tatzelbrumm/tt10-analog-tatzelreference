v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 840 -400 840 -360 { lab=vdd}
N 660 -400 840 -400 { lab=vdd}
N 660 -400 660 -200 { lab=vdd}
N 660 -140 660 -100 { lab=0}
N 740 -140 740 -100 { lab=0}
N 740 -260 740 -200 { lab=#net1}
N 760 -260 760 -100 { lab=0}
N 780 -260 780 -100 { lab=0}
N 800 -260 800 -100 { lab=0}
N 820 -260 820 -100 { lab=0}
N 840 -260 840 -100 { lab=0}
N 860 -260 860 -100 { lab=0}
N 880 -260 880 -100 { lab=0}
N 900 -260 900 -100 { lab=0}
N 920 -260 920 -100 { lab=0}
N 940 -260 940 -100 { lab=0}
N 660 -100 940 -100 { lab=0}
C {devices/title.sym} 160 -40 0 0 {name=l1 author="Christoph Maier"}
C {dividerchain.sym} 840 -320 0 0 {name=xdut}
C {devices/vsource.sym} 660 -170 0 1 {name=Vdd value=1.2}
C {devices/isource.sym} 740 -170 0 1 {name=Iref value=100n}
C {devices/lab_pin.sym} 660 -100 0 0 {name=l2 lab=0}
C {devices/lab_pin.sym} 660 -400 0 0 {name=lvdd lab=vdd}
C {devices/code.sym} 10 -210 0 0 {name=TT_MODELS
spice_ignore=false
only_toplevel=true
format="tcleval( @value )"
value=".lib $::SKYWATER_MODELS/sky130.lib.spice tt

.param mc_mm_switch=0
.param mc_pr_switch=1

"}
C {devices/code_shown.sym} 0 -730 0 0 {name=ngspice 
only_toplevel=true 
value=" 
.options gmin=1e-15 abstol=1f
.option savecurrents
.control
save all
op
remzerovec
write test_dividerchain.op.raw
dc Iref 10u 100u 1u
remzerovec
write test_dividerchain.raw
plot v.xdut.viin#branch/v.xdut.vi0#branch
plot v.xdut.vi0#branch/v.xdut.vi1#branch
plot v.xdut.vi1#branch/v.xdut.vi2#branch
plot v.xdut.vi2#branch/v.xdut.vi3#branch
plot v.xdut.vi3#branch/v.xdut.vi4#branch
plot v.xdut.vi4#branch/v.xdut.vi5#branch
plot v.xdut.vi5#branch/v.xdut.vi6#branch
plot v.xdut.vi6#branch/v.xdut.vi7#branch
plot v.xdut.vi7#branch/v.xdut.vi8#branch
plot v.xdut.vi8#branch/v.xdut.vi9#branch
.endc
"}
