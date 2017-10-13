
def random_transducer_placment(ntrans,half_grid_size, min_allowable_dist):
    
    # Function to take in a number of transducers and space them randomly in a grid 
    # centered on (0,0) taking in a half grid size in [m] and a min allowable disatance
    # between transducers and randomly placing them on a grid. 
    # Outputting an array of transducer co-ordinates

    
    import random;    import numpy as np;    import math    
    
    rt = np.zeros((ntrans,1,3))     # Defininf the output matrix of transducer positions
    keep_x =  np.zeros ((ntrans))
    keep_z =  np.zeros ((ntrans))
    distances = np.ones ((ntrans))
    
    keep_x[0] = (random.random() * 2 * half_grid_size) - half_grid_size
    keep_z[0] = (random.random() * 2 * half_grid_size) - half_grid_size
    
    counter = 2
    end_counter = 1 # counter to terminate the function if stuck in infinate loop
    while counter < ntrans and end_counter < 200:
        
        trial_x = (random.random() * 2 * half_grid_size) - half_grid_size
        trial_z = (random.random() * 2 * half_grid_size) - half_grid_size
        
        for transducers in range (0, counter):
            
            distances[transducers] = math.sqrt((trial_x - keep_x[transducers])**2 + (trial_z - keep_z[transducers])**2)
        min_distance = np.amin(distances)
            
        if min_distance >= min_allowable_dist:
            keep_x[counter] = trial_x
            keep_z[counter] = trial_z
            counter = counter + 1
        else:
            end_counter = end_counter + 1
            
        if end_counter >199 :
            print('#################################################################')
            print(' Could not fit that many transducers in with that minimum spacing')
            print('#################################################################')  
    
    for transducer in range (0,ntrans): # Writing the coordinates to output rt
    
        rt[transducer,0,0] = keep_x[transducer]
        rt[transducer,0,2] = keep_z[transducer]
    
    return(rt)