
def phase_discretize(phase): ### Not needed anymore
    
    # Function to take in a phase and output the closest value with phase resolution taken into account
    
    import numpy as np; import math; import constants
    
    phase_with_resoluton = np.zeros(len(phase))
    cutoffs = np.linspace((2*math.pi)/constants.phaseresolution,(2*math.pi),constants.phaseresolution) # Calculates phase cutoffs from 0 to 2pi taking into account the resolution (infinite resolution would be continious)

    def find_nearest(cutoffs, phase):  # Finds the value of cutoff that is closest to the "real phase"
        idx = (np.abs(cutoffs-phase)).argmin()
        return cutoffs[idx]
    for transducer in range(len(phase)):
        if phase[transducer] > (math.pi*2):
            number_over_2pi = phase[transducer] / (math.pi*2)
            fraction_of_2pi =  number_over_2pi%1 # Mod 1 gives the decimal remainder
            phase[transducer] = fraction_of_2pi * (math.pi*2)
        phase_with_resoluton[transducer] = find_nearest(cutoffs,phase[transducer])
    
    return phase_with_resoluton


def phase_random_noise(multiplier, phase):
    """"Function to take in a intager which defines how spread the randomness should be and a 
    list of phases. then outputs the phases with added noise to their signals"""
    
    import random; import math
    
    for transducer in range(len(phase)):
        
        phase[transducer] = phase[transducer] + random.random()*multiplier
        if phase[transducer] > (math.pi*2):
            number_over_2pi = phase[transducer] / (math.pi*2)
            fraction_of_2pi =  number_over_2pi%1 # Mod 1 gives the decimal remainder
            phase[transducer] = fraction_of_2pi * (math.pi*2)
        
    return phase
    

def phase_find(rt, x, y, z):
    
    # This function takes in a array of transducers and a position in space and
    # outputs the phases of all the transducers so that the magnitude of
    # the complex pressure at that point is maximum (ie a focus point).

    # -------------------------Import Libaries------------------------------------
    
    import numpy as np; import math; import constants;
    
    r = (x,y,z)                                 # r is the position of desired minimum
    ntrans = len (rt)                           # Number of transducers to find phase for
    phi = np.zeros((ntrans))                    # Phase of all the transducers
    lamda = constants.lamda                     # Wavelegnth of sound from constants file
    
    # -----------------Loop to calculate pressure field----------------------------
    for transducer in range (0,ntrans):
                    
        d = [0,0,0]                 # defining the seperation vector of transducer form point in space
        
        for i in range (3):
            d[i] = r[i] - rt[transducer,i]   # Calculating the seperation vector of transducer form point in space
        
        dmag = np.linalg.norm(d)     # Distance between transducer and point in space
        
        phi[transducer] = (( 1 - ((dmag/lamda) % 1)) * 2 * math.pi )

    return phi



def add_twin_signature(rt, phase): # Array needs to be centerd around the origin for this to work

    import algorithms; import math; import numpy as np
    
    transducer_angles = algorithms.get_angle(rt)
    ntrans = len(rt)
    phi_2 = np.zeros((ntrans))
    """
    for transducer in range(0, ntrans):
        if (3/2)*math.pi <= transducer_angles[transducer]: # all possitive z value transducers have pi added to their phase signature to create twin trap
            phi_2[transducer] = phase[transducer] + math.pi
        elif transducer_angles[transducer] <= math.pi/2:
            phi_2[transducer] = phase[transducer] + math.pi
        else:
            phi_2[transducer] = phase[transducer]
       
      """  
        
    for transducer in range(0, ntrans):
        if transducer_angles[transducer] <= math.pi:
            phi_2[transducer] = phase[transducer] + math.pi
        else:
            phi_2[transducer] = phase[transducer]
    return phi_2



def add_vortex_signature(rt, phi): # Array needs to be centerd around the origin for this to work

    import algorithms;
    
    transducer_angles = algorithms.get_angle(rt)
    ntrans = len(rt)
    
    for transducer in range(0, ntrans):
        phi[transducer] = phi[transducer] + transducer_angles[transducer]
            
    
    return phi


def phase_contributions(point, complex_pressure):
    
    import numpy as np; import math; import constants
    
    x = int(point[0] / constants.deltaxyz)
    y = int(point[1] / constants.deltaxyz)
    z = int(point[2] / constants.deltaxyz)
      
    number_of_transducers = np.ma.size(complex_pressure,0)
    
    phase_at_point_per_transducer = np.zeros(number_of_transducers)
    
    for transducer in range (number_of_transducers):
        
        phase_at_point_per_transducer[transducer] = math.atan((complex_pressure[transducer][x][y][z].imag) / (complex_pressure[transducer][x][y][z].real))
        
    
    
    
    return phase_at_point_per_transducer

"""

import numpy as np; import matplotlib.pyplot as plt

r = [0.008,0.006,0.008]
test = phase_contributions(r, p)

print(np.min(test))
print(np.max(test))


ones = np.ones(len(test))
plt.figure()
plt.plot(test, ones, 'ro')
plt.show()

"""










