
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

