#!/usr/bin/python3
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
    x[transducer]= rt[transducer,0]
    y[transducer]= rt[transducer,2] 
#plt.plot(x, y,'ro'); plt.show() # Show Plot of the positions
# -------------------------------------------------------------------------- #p


choose = input("Please choose haptic as (h) or pattern as (p) or moving as (m): ")


## --------------------------- Haptic feedback --------------------------- ##
    
if choose == ("h"):
    print ("Haptic mode selected")
    phase_index = np.zeros((ntrans),dtype=int)
    phi_focus = phase_algorithms.phase_find(rt,0,0,0.12)
    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi_focus[transducer]/((2*math.pi)/1250))
        
    from connect import Controller 
    with Controller() as ctl:        
        for i in range(ctl.outputs):
            ctl.setOffset(i,phase_index[i])
        ctl.setOutputDACFreq(200)
        ctl.loadOffsets()
## -------------------------- Focused traps ------------------------------- ##  

elif choose == ("p"):
    print ("Pattern mode selected")
    
    on_or_off = np.zeros(1250)
    transducer_test = np.zeros(88)
    phi_focus = phase_algorithms.phase_find(rt,0,0,0.018)
    phi = phase_algorithms.add_twin_signature(rt, phi_focus, 0)
    phase_index = np.zeros((ntrans),dtype=int)

    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi[transducer]/((2*math.pi)/1250))
        
    from connect import Controller 
    with Controller() as ctl:
        ctl.setOutputDACPower(256)
        ctl.setOutputDACDivisor(100)
        for i in range(ctl.outputs):
            ctl.setOffset(i,phase_index[i])
        ctl.loadOffsets()

# -------------------------------------------------------------------------- #



## -------------------------- Moving traps ------------------------------- ##

elif choose == ("m"):
    print ("Move mode selected")
    
    circle_co_ords = algorithms.circle_co_ords(50, 0.005)
    #line_coordinates = np.linspace(0,2,100)
    
    
    phi_focus = np.zeros([ntrans,len(circle_co_ords[0])])
    phi =  np.zeros([ntrans,len(circle_co_ords[0])])
    phase_index = np.zeros(([ntrans,len(circle_co_ords[0])]),dtype=int)
    

    for point in range (0,len(circle_co_ords[0])):
        
        phi_focus_all = phase_algorithms.phase_find(rt,circle_co_ords[0][point],0.015,circle_co_ords[1][point]) # phi is the initial phase of each transducer to focus on a point
        for transducer in range(0,ntrans):
            phi_focus[transducer][point] = phi_focus_all[transducer]
    
        phi_all = phase_algorithms.add_twin_signature(rt,phi_focus_all)
        for transducer in range(0,ntrans):
            phi[transducer][point] = phi_all[transducer]
        
        for transducer in range(0,ntrans):
            phase_index[transducer][point] = int(2500-phi_focus[transducer][point]/((2*math.pi)/1250))    
        
    
    from connect import Controller  
    with Controller() as ctl:
        ctl.setOutputDACPower(256)
        ctl.setOutputDACDivisor(100)

        print("You have 25 seconds to trap the particle until fuzzing stops")
        a = 1
        print(circle_co_ords[0][0],circle_co_ords[1][0])
        while a==1: 
            for fuzz in range(6000):
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i][0])
                ctl.loadOffsets()
            a = 0
    
        print("Moving")
        while True: 
            for point in range (0,len(circle_co_ords[0])):
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i][point])
                ctl.loadOffsets()
                
# -------------------------------------------------------------------------- #

elif choose == ("two"):
    print ("Move mode selected")
    
    sideways_1 = np.copy(rt)
    sideways_2 = np.copy(rt)
    
    sideways_1[:,0] = np.add(rt[:,2], -0.0925)
    sideways_1[:,2] = np.add(rt[:,0], 0.05)
    
    sideways_2[:,0] = np.add(rt[:,2], 0.0925)
    sideways_2[:,2] = np.add(rt[:,0], 0.05)

    
    phi_focus = phase_algorithms.phase_find(sideways_1,0,0,0.05) # phi is the initial phase of each transducer to focus on a point
    phi = phase_algorithms.add_twin_signature(sideways_1,phi_focus)
    phase_index = np.zeros((ntrans),dtype=int)
    #phi_focus = algorithms.read_from_excel_phases() # Takes phases from an excel spreadsheet of phases from 0 to 2pi, any over 2pi just loops
    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi[transducer]/((2*math.pi)/1250))

    
    from connect import Controller 
    with Controller() as ctl:
        ctl.setOutputDACPower(256)
        ctl.setOutputDACDivisor(100)
        print("got here")
        for i in range(ctl.outputs):
            ctl.setOffset(i,phase_index[i])
        ctl.loadOffsets()
        print("loaded offsets")


elif choose == ("w"):
    from connect import Controller  
    phase_index = np.zeros((ntrans),dtype=int)
    phi_focus = phase_algorithms.phase_find(rt,0,0,0.2)
    for transducer in range(0,ntrans):
        phase_index[transducer] = int(2500-phi_focus[transducer]/((2*math.pi)/1250))
    
    with Controller() as ctl:
        updateRate = ctl.benchmarkPower()
        print("Update freq = ", updateRate)
        ctl.setOutputDACDivisor(50)
        ctl.setOutputDACPower(255)

        for i in range(ctl.outputs):
            ctl.setOffset(i,phase_index[i])

        targetfreq = 1000
        rollover = updateRate / targetfreq / 2
        counter = 0
        import wave
        wav = wave.open("test.wav", 'r')
        
        while True:
            if (counter > 2* rollover):
                counter = counter % (2 * rollover)

            if (counter < rollover):
                ctl.setOutputDACPower(0)
            elif (counter < 2 * rollover):
                ctl.setOutputDACPower(255)
            counter = counter + 1

elif choose == ("t"):
    
    import wave, struct, numpy as np
    
    wav = wave.open("test.wav", 'r')
    length = wav.getnframes()
    data_whole = np.zeros(length)
   
    for i in range(0,length):
        waveData = wav.readframes(1)
        data = struct.unpack("<h", waveData)
        data_whole[i] = int(data[0])
        #print(int(data[0]))

    def scale_range (array, low, high):
        #array.astype("float")
        array += -(np.min(array))
        array /= np.max(array) / (high - low)
        array += low
        return array
    
    data_whole_scaled = scale_range (np.copy(data_whole), 0, 255)
    data_whole_scaled_int = np.round(np.copy(data_whole_scaled), 0)

else:
    print("Come on, pick one of the correct letters!")
