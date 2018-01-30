
def array_grid(tspacing,xtrans,ztrans):
    
    # This function takes a spacing and number of x and z transducers and outputs
    # a grid that is equally spaced and centered on (0,0)
    
    # -------------------------Import Libaries--------------------------------
    import numpy as np
    #----------------------------inputs---------------------------------------
    # "tspacing" is spacing between transducer centers in [m] min value = 0.01 m
    # "xtrans" is the number of transducers in the grid in the x direction 
    # "ztrans" is the number of transducers in the grid in the z direction
    #-------------------------------------------------------------------------
        
    xtrans = int(xtrans)
    ztrans = int(ztrans)
    
    if tspacing < 0.01:
        print ("Min value of spacing between transducer centers  = 0.01 m")
    
    else:
        ntrans = int(xtrans*ztrans) # Total number of transducers in grid
        
        rt = np.zeros((ntrans,1,3)) # Defininf the output matrix of transducer positions
        
        x = np.linspace(-(tspacing*xtrans-tspacing)/2, (tspacing*xtrans-tspacing)/2, xtrans)
        z = np.linspace(-(tspacing*ztrans-tspacing)/2, (tspacing*ztrans-tspacing)/2, ztrans)
        xv, zv = np.meshgrid(x, z) # Creating x and z coordinates zeroeod on the center of the grid 
        
        xv = np.ndarray.flatten(xv) # making the values flat so they can be easily read by the loop
        zv = np.ndarray.flatten(zv)
        
        for transducer in range (0,ntrans): # Writing the coordinates to output rt
            
            rt[transducer,0,0] = xv[transducer]
            rt[transducer,0,2] = zv[transducer]
    
        return rt
    
    
def hex_grid(tspacing,xtrans,ztrans): 
    
    # tspacing is transducer spacing in [m] between their centers
    # xtrans is number of x transducers
    # ztrans is number of z transducers
    
    import math; import numpy as np
    
    columns = xtrans;    rows = ztrans;    space = tspacing
    
    sqrt3half = math.sqrt(3) / 2
    rt = np.zeros((columns*rows,1,3)) # Defininf the output matrix of transducer positions
    
    counter = 0
    for row in range (0, rows):
        for column in range(0, columns):

            if row % 2 == 0: # Calculating even row co-ordinates and adjusting to be centered on (0,0)
                
                rt[counter,0,0]= (column * space) - ((columns-1) * space /2)
                rt[counter,0,2]= (sqrt3half * row * space ) - (((rows-1)*sqrt3half) * space/2)
            
            else: # Calculating odd row co-ordinates and adjusting to be centered on (0,0)
                
                rt[counter,0,0]= ((column + 0.5) * space) - ((columns-1) * space /2)
                rt[counter,0,2]= ((sqrt3half * row) * space) - (((rows-1)*sqrt3half) * space/2)
            
            counter += 1
   
    return rt
    

def random(ntrans,half_grid_size, min_allowable_dist):
    
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
    
    counter = 1
    end_counter = 1 # counter to terminate the function if stuck in infinate loop
    while counter < ntrans and end_counter < 20000:
        
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
            
        if end_counter >19999 :
            print('#################################################################')
            print(' Could not fit that many transducers in with that minimum spacing')
            print('#################################################################')  
    
    for transducer in range (0,ntrans): # Writing the coordinates to output rt
    
        rt[transducer,0,0] = keep_x[transducer]
        rt[transducer,0,2] = keep_z[transducer]
    
    return rt


def direction_vectors(ntrans):
    
    # This function takes a number of transducers and outputs a vertical direction
    # vector for each transducer
    
    # -------------------------Import Libaries--------------------------------
    import numpy as np
    # -------------------- Calculate direction vectors------------------------     
    
    
    nt = np.zeros((ntrans,1,3))     # Defininf the output matrix of transducer directions

    for trans in range(0,ntrans):   # setting all the transducers vertical
        
        nt[trans,0,1] = 1 
        
    return nt


def delete_transducers(rt,trans_to_delete):
    import numpy as np
    trans_to_delete = sorted(trans_to_delete)
    n_trans_to_delete = len(trans_to_delete)
    
    for loop in range (0, (n_trans_to_delete)):             # Deletes unwanted transducers
        rt = np.delete(rt, trans_to_delete[loop], 0)
        trans_to_delete = np.subtract(trans_to_delete, 1)
    return rt    


def big_daddy():
    from algorithms import read_from_excel; from numpy import zeros;
    coordinates = read_from_excel()
    ntrans = len(coordinates[0])
    rt = zeros((ntrans,1,3))
    for transducer in range (0,ntrans): # Writing the coordinates to output rt
    
        rt[transducer,0,0] = coordinates[0][transducer]
        rt[transducer,0,2] = coordinates[1][transducer]
    return rt



