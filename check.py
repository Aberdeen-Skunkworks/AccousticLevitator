#!/usr/bin/python3
##############################################################################
#----------------------------------DEMO--------------------------------------#
##############################################################################


## ----------------- Writing transducer locations to rt ------------------ ##

import numpy as np;
import transducer_placment;
import matplotlib.pyplot as plt;
import phase_algorithms;
import math;
import algorithms;
import time
trans_to_delete = []  # List of unwanted transducers leave blank to keep all
rt = transducer_placment.big_daddy()
rt = transducer_placment.delete_transducers(rt,trans_to_delete)
ntrans = len(rt); x = np.zeros(ntrans); y = np.zeros(ntrans)
for transducer in range (0,ntrans): # Writing the coordinates to output rt
    x[transducer]= rt[transducer,0]
    y[transducer]= rt[transducer,2] 
#plt.plot(x, y,'ro'); plt.show() # Show Plot of the positions
# -------------------------------------------------------------------------- #p

## --------------------------- Haptic feedback --------------------------- ##
    
print ("Haptic mode selected")
phase_index = np.zeros((ntrans),dtype=float)
phi_focus = phase_algorithms.phase_find(rt,0,0,0.12)
for transducer in range(0,ntrans):
    phase_index[transducer] = 1.0

from connect import Controller 
with Controller() as ctl:  
    ctl.setOutputDACPower(256)
    ctl.setOutputDACDivisor(100)
    for i in range(ctl.outputs):
        ctl.setOffset(i,phase_index[i])
    ctl.setOffset(0,0, enable=False)
    ctl.loadOffsets()
