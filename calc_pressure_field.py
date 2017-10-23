
# Pressure field calculation function


def calc_pressure_field(rt, nt, ntrans, phi):
    
    import numpy as np; import math; import cmath; import constants
    
    gsize = constants.gsize; deltaxyz = constants.deltaxyz; x = constants.x; y = constants.y; z = constants.z
    npoints = constants.npoints; p0 = constants.p0; A = constants.A; a = constants.a; lamda = constants.lamda
    
    p = np.zeros ((npoints,npoints,npoints,ntrans), dtype=complex)
    
    
    for transducer in range (0,ntrans):
        for xloop in range (0,npoints):
            for yloop in range (0,npoints):
                for zloop in range (0,npoints):
                    
                    r = [ x  , y , z ]          # Point in space for each itteriation
                    d = [0,0,0]                 # Seperation vector of transducer form point in space
                    
                    for i in range (3):
                        d[i] = r[i] - rt[transducer,0,i]   # Seperation vector of transducer form point in space
                    
                    dmag = np.linalg.norm(d)     # Distance between transducer and point in space
                    
                    if dmag < (1*10**(-13)):     # Calculating complex acoustic pressure at point r[x,y,z] 
                        p[xloop,yloop,zloop,transducer] = 0 
                    else:
                        
                        dot = d[0]*nt[transducer,0,0] + d[1]*nt[transducer,0,1] + d[2]*nt[transducer,0,2] # Dot product of the direction of the transducer and the separation vector
                        theta = math.acos(dot/dmag)
    
                        k = (2*math.pi)/(float(lamda))                         # Wavenumber
                        exp = cmath.exp(1j*(float(phi[transducer])+k*dmag))    # Exponential term
                            
                        if theta < 1*(10**-13):
                            Df = 1 + 0j # setting the Df value to 1 directly above the transducers
                        else:
                            Df = (cmath.sin(k*a*cmath.sin(theta)))/(k*a*cmath.sin(theta))   # Directivity function of a circular piston source
                            
                        p[xloop,yloop,zloop,transducer] = p0*A*((Df)/(dmag))*exp    
                                            
                    z = z + deltaxyz    # Adding delta to x,y and z
                y = y + deltaxyz
                z = -gsize               # Resetting the value of z to start value for next loop
            x = x + deltaxyz
            y = 0                       # Resetting the value of y to start value for next loop
            z = -gsize                   # Resetting the value of z to start value for next loop
        x = -gsize # Initial values of x,y and z in (m) Grid volume
        y = 0.00
        z = -gsize
    
    
    return p

