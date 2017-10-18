
def phase_discretize(phase):
    
    # Function to take in a phase and output the closest value with phase resolution taken into account
    
    import numpy as np; import math; import constants
    
    cutoffs = np.linspace(0,(2*math.pi),constants.phaseresolution) # Calculates phase cutoffs from 0 to 2pi taking into account the resolution (infinite resolution would be continious)

    def find_nearest(cutoffs, phase):  # Finds the value of cutoff that is closest to the "real phase"
        idx = (np.abs(cutoffs-phase)).argmin()
        return cutoffs[idx]
    
    phase_with_resoluton = find_nearest(cutoffs,phase)
    
    return phase_with_resoluton




def phase_find(rt, x, y, z):
    
    # This function takes in a array of transducers and a position in space and
    # outputs the phases of all the transducers so that the magnitude of
    # the complex pressure at that point is maximum (ie a focus point).

    # -------------------------Import Libaries------------------------------------
    
    import numpy as np; import math; import constants;
    
    r = (x,y,z)                                 # r is the position of desired minimum
    ntrans = len (rt)                           # Number of transducers to find phase for
    phi = np.zeros((ntrans))                    # Phase of all the transducers
    phase_with_resoluton = np.zeros((ntrans))   # Phase of all the transducers adjusted so they belong to a step of the phase resolution
    lamda = constants.lamda                     # Wavelegnth of sound from constants file
    
    # -----------------Loop to calculate pressure field----------------------------
    for transducer in range (0,ntrans):
                    
        d = [0,0,0]                 # defining the seperation vector of transducer form point in space
        
        for i in range (3):
            d[i] = r[i] - rt[transducer,0,i]   # Calculating the seperation vector of transducer form point in space
        
        dmag = np.linalg.norm(d)     # Distance between transducer and point in space
        
        phi[transducer] = (( 1 - ((dmag/lamda) % 1)) * 2 * math.pi )
        phase_with_resoluton[transducer] = phase_discretize(phi[transducer])

    return phase_with_resoluton




def add_twin_signature(rt, phi):

    import algorithms; import math
    
    transducer_angles = algorithms.get_angle(rt)
    ntrans = len(rt)
    
    for transducer in range(0, ntrans):
        if 0 < transducer_angles[transducer] < math.pi: # all possitive y value transducers have pi added to their phase signature to create twin trap
            phi[transducer] = phi[transducer] + math.pi
            
    
    return (phi)


def add_vortex_signature(rt, phi):

    import algorithms;
    
    transducer_angles = algorithms.get_angle(rt)
    ntrans = len(rt)
    
    for transducer in range(0, ntrans):
        phi[transducer] = phi[transducer] + transducer_angles[transducer]
            
    
    return (phi)



