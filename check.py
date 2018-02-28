##############################################################################
#----------------------------------DEMO--------------------------------------#
##############################################################################


## ----------------- Writing transducer locations to rt ------------------ ##

import numpy as np; import transducer_placment; import matplotlib.pyplot as plt; import phase_algorithms; import math; import algorithms; import time
trans_to_delete = []  # List of unwanted transducers leave blank to keep all
rt = transducer_placment.big_daddy()
rt = transducer_placment.delete_transducers(rt,trans_to_delete)
ntrans = len(rt); x = np.zeros(ntrans); y = np.zeros(ntrans)
for transducer in range (0,ntrans): # Writing the coordinates to output rt
    x[transducer]= rt[transducer,0,0]
    y[transducer]= rt[transducer,0,2] 
#plt.plot(x, y,'ro'); plt.show() # Show Plot of the positions
# -------------------------------------------------------------------------- #p


print ("Pattern mode selected")
phi_focus = phase_algorithms.phase_find(rt,0,0.018,0) # phi is the initial phase of each transducer to focus on a point
phi = phase_algorithms.add_twin_signature(rt,phi_focus)
phase_index = np.zeros((ntrans),dtype=int)
#phi_focus = algorithms.read_from_excel_phases() # Takes phases from an excel spreadsheet of phases from 0 to 2pi, any over 2pi just loops
for transducer in range(0,ntrans):
    phase_index[transducer] = int(2500-phi[transducer]/((2*math.pi)/1250))    


from connect import Controller 
with Controller() as ctl:
    print("You have 35 seconds to trap the particle until fuzzing stops")
    a = 1
    for i in range(ctl.outputs):
        ctl.setOffset(i,phase_index[i])
    ctl.loadOffsets()
    ctl.setOffset(0,0)
