
# Function to take in a phase and output the closest value with phase resolution taken into account

def phase_discretize(phase):
    
    import numpy as np; import math; import constants
    
    cutoffs = np.linspace(0,(2*math.pi),constants.phaseresolution) # Calculates phase cutoffs from 0 to 2pi taking into account the resolution (infinite resolution would be continious)

    def find_nearest(cutoffs, phase):  # Finds the value of cutoff that is closest to the "real phase"
        idx = (np.abs(cutoffs-phase)).argmin()
        return cutoffs[idx]
    
    phase_with_resoluton = find_nearest(cutoffs,phase)
    
    return phase_with_resoluton
