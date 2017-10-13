
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

