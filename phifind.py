def phifind(rt, x, y, z):
    
    # This function takes in a array of transducers and a position in space and
    # outputs the phases of all the transducers so that the magnitude of
    # the complex pressure at that point is maximum (ie a focus point).

    # -------------------------Import Libaries------------------------------------
    
    import numpy as np; import math; import constants
    
    r = (x,y,z)                 # r is the position of desired minimum
    ntrans = len (rt)           # Number of transducers to find phase for
    phi = np.zeros((ntrans))    # Phase of all the transducers
    lamda = constants.lamda     # Wavelegnth of sound from constants file
    
    # -----------------Loop to calculate pressure field----------------------------
    for transducer in range (0,ntrans):
                    
        d = [0,0,0]                 # defining the seperation vector of transducer form point in space
        
        for i in range (3):
            d[i] = r[i] - rt[transducer,0,i]   # Calculating the seperation vector of transducer form point in space
        
        dmag = np.linalg.norm(d)     # Distance between transducer and point in space
        
        phi[transducer] = (( 1 - ((dmag/lamda) % 1)) * 2 * math.pi ) #/ math.pi ??????????????
        ##
        ## FIND OUT IF THE EQUATION NEEDS TO BE DIVIDED BY PI  
        ## in the netbeams code ----> public class SimplePhaseAlgorithms   - focus     

    return phi
