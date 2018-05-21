# Accoustic Levitator

A device for trapping and manipulating particles in three dimensions as well as the software to simulate these traps.

This Project is split into two distinct sections (1) The control software for the physical array, (2) The acoustic simulation to model the fields produced by this array.

The goal is to have a system that can self-calibrate where the control software can detect and automatically figure out where multiple acoustic arrays are in relation to each other, (Using the -> Aberdeen-Skunkworks/AccousticTracker project) It can then take this positional information and form acoustic traps at desired locations.

The files in the /eagle folder are PCB design files that use the Autodesk PCB design software Eagle which can be found here: https://www.autodesk.com/products/eagle/overview

The files in the /FPGA folder are the setup files that are running on the Field-Programable Gate Arrays that create the ultrasonic signals that are sent to the transducers.

# (1) Control software


# (2) Acoustic simulation
