
def get_angle(rt): 
    
# takes in co-odinates of transducers and outputs the angles between 0 and 2 pi 
# angles are anticlockwise from the x axis for each transducer in turn
    
    import numpy as np; import math;
    
    ntrans = len(rt)
    theta = np.zeros ((ntrans),dtype=float)
    xdir = np.array ((1,0,0)) # Vector pointing down the x axis to take angles from
    
    for transducer in range(0, ntrans):
        
        r = [rt[transducer,0,0], rt[transducer,0,1], rt[transducer,0,2]]
        dmag = np.linalg.norm(r)     # Distance between transducer and origin

        if dmag < (1*10**(-13)):
            theta[transducer] = 0 # setting angle to zero if transducer is ontop of the origin
        else:
            dot = r[0]*xdir[0] + r[1]*xdir[1] + r[2]*xdir[2] # Dot product of the direction of the transducr and the position in space
            theta[transducer] = math.acos(dot/dmag)
            
        if rt[transducer,0,2] < 0: # making angle go from 0 to 2 pi anticlockwise angle from the x axis
            theta[transducer] = math.pi*2 - theta[transducer]
            
        #print(theta[transducer]/(math.pi/180)) # To test uncomment to get angle in degrees 
    
    return (theta)

# Test using one point to check if angles are correct from x axis in anti-clockwise direction
#import numpy as np
#rt = np.zeros ((1,1,3))
#rt[0,0,0] = 1           # x coordinate
#rt[0,0,2] = -0.001      # y coordinate
#testangles = get_angle(rt)