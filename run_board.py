
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


choose = input("Please choose haptic as (h) or pattern as (p) or moving as (m): ")


## --------------------------- Haptic feedback --------------------------- ##
    
if choose == ("h"):
    print ("Haptic mode selected")
    phase_index = np.zeros((ntrans),dtype=int)
    phi_focus = phase_algorithms.phase_find(rt,0,0.1,0)
    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi_focus[transducer]/((2*math.pi)/1250))
        
    from connect import Controller 
    with Controller() as ctl:
        
        while True:          # Turns the pattern off and on as fast as possible
            
            for i in range(ctl.outputs):
                ctl.setOffset(i,phase_index[i])
            ctl.loadOffsets()
    
            for i in range(ctl.outputs):
                ctl.disableOutput(i)
# -------------------------------------------------------------------------- #
    


## -------------------------- Focused traps ------------------------------- ##  

elif choose == ("p"):
    print ("Pattern mode selected")
    phi_focus = phase_algorithms.phase_find(rt,0,0.018,0) # phi is the initial phase of each transducer to focus on a point
    phi = phase_algorithms.add_twin_signature(rt,phi_focus)
    phase_index = np.zeros((ntrans),dtype=int)
    #phi_focus = algorithms.read_from_excel_phases() # Takes phases from an excel spreadsheet of phases from 0 to 2pi, any over 2pi just loops
    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi[transducer]/((2*math.pi)/1250))    
    
    
    from connect import Controller 
    with Controller() as ctl:
        
        while True: 
        
            for i in range(ctl.outputs):
                ctl.setOffset(i,phase_index[i])
            ctl.loadOffsets()
        
    
# -------------------------------------------------------------------------- #



## -------------------------- Moving traps ------------------------------- ##

elif choose == ("m"):
    print ("Move mode selected")
    
    circle_co_ords = algorithms.circle_co_ords(400, 0.01)
    
    phi_focus = np.zeros([ntrans,len(circle_co_ords[0])])
    phi =  np.zeros([ntrans,len(circle_co_ords[0])])
    phase_index = np.zeros(([ntrans,len(circle_co_ords[0])]),dtype=int)
    

    for point in range (0,len(circle_co_ords[0])):
        
        phi_focus_all = phase_algorithms.phase_find(rt,0,0.018,0) # phi is the initial phase of each transducer to focus on a point
        for transducer in range(0,ntrans):
            phi_focus[transducer][point] = phi_focus_all[transducer]
    
        phi_all = phase_algorithms.add_twin_signature(rt,phi_focus_all)
        for transducer in range(0,ntrans):
            phi[transducer][point] = phi_all[transducer]
        
        for transducer in range(0,ntrans):
            phase_index[transducer][point] = int(2500-phi_focus[transducer][point]/((2*math.pi)/1250))    
        
    
    from connect import Controller 
    with Controller() as ctl:
        for i in range(ctl.outputs):
            ctl.setOffset(i,phase_index[i][0])
        ctl.loadOffsets()
        try:
            input("Press enter once the particle is trapped")
        except SyntaxError:
            pass
        print("Moving")
        while True: 
            for point in range (0,len(circle_co_ords[0])):
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i][point])
                ctl.loadOffsets()
# -------------------------------------------------------------------------- #

else:
    print("Come on, pick one of the correct letters!")
    
    
    
    
    
    
    
    
    
    
    
    
    