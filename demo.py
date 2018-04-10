#!/usr/bin/python3
##############################################################################
#----------------------------------DEMO--------------------------------------#
##############################################################################


## ----------------- Writing transducer locations to rt ------------------ ##

import numpy as np; import transducer_placment; import matplotlib.pyplot as plt; import phase_algorithms; import math; import algorithms; import time; from PyQt5 import QtWidgets; import sys
trans_to_delete = []  # List of unwanted transducers leave blank to keep all
rt = transducer_placment.big_daddy()
rt = transducer_placment.delete_transducers(rt,trans_to_delete)
ntrans = len(rt); 
#x = np.zeros(ntrans); y = np.zeros(ntrans)
#for transducer in range (0,ntrans): # Writing the coordinates to output rt
#    x[transducer]= rt[transducer,0]
#    y[transducer]= rt[transducer,1] 
#plt.plot(x, y,'ro'); plt.show() # Show Plot of the positions
# -------------------------------------------------------------------------- #p

print(" ")
print("Control modes:")
print("(h) = Haptic")
print("(p) = Pattern")
print("(m) = Moving - Circles abvoe array (NOT WORKING)")
print("(two) = Two boards, Needs work for both boards at once")
print("(w) = Frequency mode not really required anymore")
print("(t) = Start on sound mode (NOT WORKING)")
print("(GUI) = Graphical user interface mode")

choose = input("Please choose a mode from above: ")


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

# -------------------------------------------------------------------------- #

elif choose == ("w"):
    # Frequency mode not really required anymore
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
            
# -------------------------------------------------------------------------- #

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
    
# -------------------------------------------------------------------------- #

elif choose == ("GUI"):
    print ("GUI mode selected")
    
    # Initial position in m (x , y , z) (z = up)
    global x,y,z
    x = 0    
    y = 0
    z = 0.02
    rt = transducer_placment.big_daddy()
    ntrans = len(rt);
    phase_index = np.zeros((ntrans),dtype=int)
    
    class Window_update_trap(QtWidgets.QWidget):
    
        def __init__(self):
            
            super().__init__()
            
            #from connect import Controller
            #self.ctl = Controller()
            #self.ctl.__enter__()
            self.init_ui()
        
        def init_ui(self):
            
            
            self.forward = QtWidgets.QPushButton('Forward')
            self.backward = QtWidgets.QPushButton('Backwards')
            self.right = QtWidgets.QPushButton('Right')
            self.left = QtWidgets.QPushButton('Left')
            self.up = QtWidgets.QPushButton('Up')
            self.down = QtWidgets.QPushButton('Down')
            self.fuzz = QtWidgets.QPushButton('FUZZ')
            self.reset = QtWidgets.QPushButton('Reset to [0, 0, 0.02]')
            self.turn_off = QtWidgets.QPushButton('OFF')
            self.turn_on = QtWidgets.QPushButton('ON')   
            self.capture = QtWidgets.QPushButton('Capture')   
        
            
            self.label1 = QtWidgets.QLabel('Movement Controls')
            self.label2 = QtWidgets.QLabel('Extra Controls')
    
    
            h_box_label = QtWidgets.QHBoxLayout()
            h_box_label.addStretch()
            h_box_label.addWidget(self.label1)
            h_box_label.addStretch() 
            
            h_box_labe2 = QtWidgets.QHBoxLayout()
            h_box_labe2.addStretch()
            h_box_labe2.addWidget(self.label2)
            h_box_labe2.addStretch() 
            
            h_box = QtWidgets.QHBoxLayout()
            h_box.addWidget(self.down)
            h_box.addWidget(self.forward)
            h_box.addWidget(self.up) 
        
            h_box2 = QtWidgets.QHBoxLayout()
            h_box2.addWidget(self.left)
            h_box2.addWidget(self.backward)
            h_box2.addWidget(self.right) 
            
            h_box3 = QtWidgets.QHBoxLayout()
            h_box3.addWidget(self.fuzz)
            h_box3.addWidget(self.capture)
            h_box3.addWidget(self.reset)
            
            h_box4 = QtWidgets.QHBoxLayout()
            h_box4.addWidget(self.turn_on)
            h_box4.addWidget(self.turn_off)

        
            v_box = QtWidgets.QVBoxLayout()
            v_box.addLayout(h_box_label)
            v_box.addLayout(h_box)
            v_box.addLayout(h_box2)
            v_box.addLayout(h_box_labe2)
            v_box.addLayout(h_box3)
            v_box.addLayout(h_box4)
            
            self.setLayout(v_box)
            self.setWindowTitle('Particle Mover!')
            
            self.forward.clicked.connect(self.forward_click)
            self.backward.clicked.connect(self.backward_click)
            self.left.clicked.connect(self.left_click)
            self.right.clicked.connect(self.right_click)
            self.up.clicked.connect(self.up_click)
            self.down.clicked.connect(self.down_click)
            self.fuzz.clicked.connect(self.fuzz_click)
            self.reset.clicked.connect(self.reset_click)
            self.turn_off.clicked.connect(self.turn_off_board_click)
            self.turn_on.clicked.connect(self.turn_on_board_click)
            self.capture.clicked.connect(self.capture_click)
            
            self.show()
    
        def calculate_and_move_trap(self):
            import math; import phase_algorithms; import numpy as np; import transducer_placment
            global phase_index
            
            phi_focus = phase_algorithms.phase_find(rt,x,y,z)
            phi = phase_algorithms.add_twin_signature(rt,phi_focus, 90)
            for transducer in range(0,ntrans):
                phase_index[transducer] = int(2500-phi[transducer]/((2*math.pi)/1250)) 
            print(" ")
            print("Moved!")
            print("Phase index is ", phase_index)
            print("New Position: ","x = " "%.3f" % x, "y = " "%.3f" % y, "z = " "%.3f" % z) #tester
            
            from connect import Controller
            with Controller() as ctl:
                ctl.setOutputDACPower(256)
                ctl.setOutputDACDivisor(100)
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i])
                ctl.loadOffsets()

        def calculate_and_move_trap_no_print(self):
            
            from connect import Controller
            with Controller() as ctl:
                ctl.setOutputDACPower(256)
                ctl.setOutputDACDivisor(100)
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i])
                ctl.setOutputDACFreq(200)
                ctl.loadOffsets()
        
        def turn_off_board_click(self):
            from connect import Controller
            with Controller() as ctl:
                for i in range(ctl.outputs):
                    ctl.disableOutput(i)
                ctl.loadOffsets()

        def turn_on_board_click(self):
            from connect import Controller
            with Controller() as ctl:
                ctl.setOutputDACPower(256)
                ctl.setOutputDACDivisor(100)
                for i in range(ctl.outputs):
                    ctl.setOffset(i,phase_index[i])
                ctl.loadOffsets()
                
        def capture_click(self):
            
            for up in range(50):
                global z
                print("Rising trap 2 cm")
                z += 0.0004
                self.calculate_and_move_trap()
                time.sleep(0.05)
                print("Raised to final height")
    
        def forward_click(self):
            global x               
            x += 0.001
            self.calculate_and_move_trap()
            print('x changed to = ', "%.3f" % x)
        
        def backward_click(self):
            global x 
            x -= 0.001
            self.calculate_and_move_trap()
            print('x changed to = ', "%.3f" % x)
            
        def left_click(self):
            global y 
            y += 0.001
            self.calculate_and_move_trap()
            print('y changed to = ', "%.3f" % y)
            
        def right_click(self):
            global y 
            y -= 0.001
            self.calculate_and_move_trap()
            print('y changed to = ', "%.3f" % y)
            
        def up_click(self):
            global z 
            z += 0.001
            self.calculate_and_move_trap()
            print('z changed to = ', "%.3f" % z)
            
        def down_click(self):
            global z 
            z -= 0.001
            self.calculate_and_move_trap()
            print('z changed to = ', "%.3f" % z)
            
        def fuzz_click(self):
            print(' ')
            print('Fuzzing for 10 seconds')
            self.calculate_and_move_trap_no_print()
            time.sleep(10)
            print(' ')
            self.calculate_and_move_trap()
            print('Finished Fuzzing')
            
        def reset_click(self):
            global x,y,z
            x = 0; y = 0; z = 0.02;
            print(' ')
            print('Reset to [0, 0, 0.02]')
    
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    a_window = Window_update_trap()
    sys.exit(app.exec_())
    
# -------------------------------------------------------------------------- #

else:
    print("Come on, pick one of the correct letters!")
