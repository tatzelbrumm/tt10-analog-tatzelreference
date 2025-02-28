v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 670 -500 740 -500 { lab=node}
N 740 -500 740 -430 { lab=node}
N 520 -540 520 -500 { lab=vdd}
N 740 -400 760 -400 { lab=vdd}
N 760 -540 760 -400 { lab=vdd}
N 640 -540 760 -540 { lab=vdd}
N 520 -460 520 -400 { lab=vbp}
N 640 -400 700 -400 { lab=vbp}
N 740 -500 800 -500 { lab=node}
N 860 -500 910 -500 { lab=iout}
N 460 -500 490 -500 { lab=#net1}
N 740 -370 740 -340 { lab=#net2}
N 740 -280 740 -230 { lab=isink}
N 350 -400 520 -400 { lab=vbp}
N 350 -500 400 -500 { lab=iin}
N 350 -540 520 -540 { lab=vdd}
N 640 -540 640 -500 { lab=vdd}
N 640 -460 640 -400 { lab=vbp}
N 520 -540 640 -540 {
lab=vdd}
N 520 -400 640 -400 {
lab=vbp}
N 550 -500 610 -500 {
lab=ds}
C {devices/title.sym} 160 -40 0 0 {name=l1 author="Christoph Maier"}
C {sky130_fd_pr/pfet_01v8.sym} 520 -480 3 0 {name=M12
L=15.5
W=1
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {devices/iopin.sym} 360 -500 0 1 {name=p1 lab=iin}
C {devices/iopin.sym} 360 -540 0 1 {name=p0 lab=vdd}
C {devices/iopin.sym} 360 -400 0 1 {name=p2 lab=vbp}
C {devices/ammeter.sym} 430 -500 3 0 {name=Viin}
C {devices/ammeter.sym} 830 -500 3 0 {name=Viout}
C {sky130_fd_pr/pfet_01v8.sym} 720 -400 0 0 {name=M1
L=2
W=1
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {devices/iopin.sym} 900 -500 0 0 {name=p3 lab=iout}
C {devices/iopin.sym} 740 -240 1 0 {name=p4 lab=isink}
C {devices/ammeter.sym} 740 -310 0 0 {name=Visink}
C {devices/lab_wire.sym} 740 -500 0 0 {name=l2 lab=node}
C {sky130_fd_pr/pfet_01v8.sym} 640 -480 3 0 {name=M2
L=15.5
W=1
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {devices/lab_wire.sym} 590 -500 0 0 {name=l3 lab=ds}
