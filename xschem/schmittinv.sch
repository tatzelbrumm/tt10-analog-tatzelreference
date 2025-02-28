v {xschem version=3.4.5 file_version=1.2

* Copyright 2020 Stefan Frederik Schippers
* 
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     https://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.

}
G {}
K {}
V {}
S {}
E {}
N 460 -140 480 -140 { lab=vss}
N 480 -140 480 -80 { lab=vss}
N 460 -110 460 -80 { lab=vss}
N 460 -540 480 -540 { lab=vdd}
N 460 -600 480 -600 { lab=vdd}
N 460 -600 460 -570 { lab=vdd}
N 600 -460 620 -460 { lab=vdd}
N 360 -380 400 -380 { lab=in}
N 480 -600 480 -540 { lab=vdd}
N 460 -80 480 -80 { lab=vss}
N 660 -320 680 -320 { lab=out}
N 400 -140 420 -140 { lab=in}
N 400 -540 420 -540 { lab=in}
N 660 -460 680 -460 { lab=out}
N 400 -220 400 -140 { lab=in}
N 400 -460 400 -380 { lab=in}
N 460 -460 480 -460 { lab=vdd}
N 400 -460 420 -460 { lab=in}
N 460 -300 480 -300 { lab=vss}
N 400 -300 420 -300 { lab=in}
N 480 -220 480 -140 { lab=vss}
N 480 -540 480 -460 { lab=vdd}
N 460 -260 460 -250 { lab=dn}
N 460 -500 460 -490 { lab=dp}
N 460 -380 460 -330 { lab=out}
N 460 -380 740 -380 { lab=out}
N 460 -500 620 -500 { lab=dp}
N 620 -500 620 -490 { lab=dp}
N 620 -290 620 -280 { lab=dsn}
N 400 -540 400 -460 { lab=in}
N 400 -380 400 -300 { lab=in}
N 460 -430 460 -380 { lab=out}
N 460 -270 460 -260 { lab=dn}
N 460 -510 460 -500 { lab=dp}
N 480 -600 600 -600 { lab=vdd}
N 600 -600 600 -460 { lab=vdd}
N 480 -80 600 -80 { lab=vss}
N 540 -420 620 -360 { lab=vdd}
N 540 -600 540 -420 { lab=vdd}
N 620 -430 620 -400 { lab=vss}
N 540 -340 620 -400 { lab=vss}
N 680 -460 680 -380 { lab=out}
N 360 -600 460 -600 { lab=vdd}
N 360 -80 460 -80 { lab=vss}
N 480 -300 480 -220 {
lab=vss}
N 400 -300 400 -220 {
lab=in}
N 460 -250 460 -170 {
lab=dn}
N 540 -340 540 -260 {
lab=vss}
N 600 -240 620 -240 { lab=vss}
N 660 -240 680 -240 { lab=out}
N 620 -210 620 -200 { lab=dn}
N 540 -260 540 -80 {
lab=vss}
N 620 -360 620 -350 {
lab=vdd}
N 460 -190 620 -190 {
lab=dn}
N 620 -200 620 -190 {
lab=dn}
N 680 -320 680 -240 {
lab=out}
N 680 -380 680 -320 {
lab=out}
N 600 -300 600 -240 {
lab=vss}
N 600 -240 600 -80 {
lab=vss}
N 620 -280 620 -270 {
lab=dsn}
N 600 -320 620 -320 {}
N 600 -320 600 -300 {}
C {sky130_fd_pr/nfet_01v8.sym} 440 -140 0 0 {name=M1
L=8
W=0.5  
nf=1 mult=1
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet_01v8.sym} 440 -540 0 0 {name=M5
L=2
W=0.5
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet_01v8.sym} 640 -320 0 1 {name=M3
L=12
W=0.5
nf=1 mult=1
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet_01v8.sym} 640 -460 0 1 {name=M6
L=4
W=0.5
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {devices/lab_pin.sym} 620 -280 2 0 {name=l2 lab=dsn
}
C {devices/title.sym} 160 0 0 0 {name=l5 author="Christoph Maier"}
C {sky130_fd_pr/pfet_01v8.sym} 440 -460 0 0 {name=M4
L=2
W=0.5
nf=1 mult=1
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet_01v8.sym} 440 -300 0 0 {name=M2
L=8
W=0.5 
nf=1 mult=1
model=nfet_01v8
spiceprefix=X
}
C {devices/lab_pin.sym} 620 -500 2 0 {name=l1 lab=dp
}
C {devices/iopin.sym} 360 -600 0 1 {name=p1 lab=vdd}
C {devices/iopin.sym} 360 -80 0 1 {name=p2 lab=vss}
C {devices/ipin.sym} 360 -380 0 0 {name=p3 lab=in}
C {devices/opin.sym} 740 -380 0 0 {name=p4 lab=out}
C {sky130_fd_pr/nfet_01v8.sym} 640 -240 0 1 {name=M30
L=12
W=0.5
nf=1 mult=1
model=nfet_01v8
spiceprefix=X
}
C {devices/lab_pin.sym} 620 -200 2 0 {name=l3 lab=dn
}
