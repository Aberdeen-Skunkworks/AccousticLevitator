
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


def pressure (r, rt, phi, nt):
    import numpy as np; import math; import cmath; import constants
    rs = np.subtract(r,rt)
    k = (2*math.pi)/(float(constants.lamda))   
    mag_rs = np.linalg.norm(rs)
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponential =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    frac =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )

    pressure = (exponential*frac)
    return pressure



def differentiate_pressure(r,rt,nt,phi):
    # Differentiation of pressure with respect to (x,y,z) done analytically
    import math; import cmath; import numpy as np; import constants

    rs = np.subtract(r,rt)
    mag_rs = np.linalg.norm(rs)
    rs_hat = rs / mag_rs
    k = (2*math.pi)/(float(constants.lamda))  
    
    theta = math.acos((np.dot(rs,nt)) / (mag_rs))
    exponent_term =  cmath.exp( 1j * (phi + k * mag_rs) ) / mag_rs
    fraction_term =  (constants.p0*constants.A)*( (math.sin(k*constants.a*math.sin(theta))) /  (k*constants.a*math.sin(theta)) )
    
    d_exponential_term_dr = ((rs_hat * 1j * k * cmath.exp(1j*(phi + k * mag_rs)) ) / (mag_rs))  -  ((cmath.exp(1j*(phi + k * mag_rs)) * rs_hat) / (mag_rs**2) )
    
    numerator = constants.p0 * constants.A * math.sin(k*constants.a*math.sin(theta))
    denominator =  k*constants.a*math.sin(theta)
    d_denominator_dr = k*constants.a*(( ((-np.dot(rs,nt))/(mag_rs) ) / ((1 - (np.dot(rs,nt))/(mag_rs) )**0.5) ) * ( (np.dot(nt,mag_rs) - (rs_hat*np.dot(nt,rs)) ) / (mag_rs**2) ) )
    d_numerator_dr = constants.p0 * constants.A * math.cos(k*constants.a*math.sin(theta))*d_denominator_dr
    d_fraction_dr = ((d_numerator_dr*denominator) - (numerator*d_denominator_dr))/(denominator**2)
    
    d_p_dr = (d_fraction_dr * exponent_term) + (fraction_term * d_exponential_term_dr)
    
    return (d_p_dr)

        
        
#def circle_co_ords(splits)

import math; import matplotlib.pyplot as plt; import numpy as np

splits = 25
x = np.zeros (splits)
y = np.zeros (splits)
coordinates = np.zeros((splits),(splits))
for point in range(0,splits):
    angle = ((2*math.pi) / splits+1) * (point+1)
    x[point] = 0.01 * math.cos(point)
    y[point] = 0.01 * math.sin(point)
    coordinates

coordinates = [x,y]
plt.plot(x, y, 'ro')
    

    