
# Pressure field calculation function


def calc_pressure_field(rt, nt, ntrans, phi):
    
    import numpy as np; import math; import cmath; import constants
    
    gsize = constants.gsize; deltaxyz = constants.deltaxyz; x = constants.x; y = constants.y; z = constants.z
    npoints = constants.npoints; p0 = constants.p0; A = constants.A; a = constants.a; lamda = constants.lamda
    
    p = np.zeros ((ntrans, npoints,npoints,npoints), dtype=complex)
    
    k = (2*math.pi)/(float(lamda))                         # Wavenumber
    
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
                        p[transducer, xloop, yloop, zloop] = 0 
                    else:
                        
                        dot = d[0]*nt[transducer,0,0] + d[1]*nt[transducer,0,1] + d[2]*nt[transducer,0,2] # Dot product of the direction of the transducer and the separation vector
                        theta = math.acos(dot/dmag)
    
                        exp = cmath.exp(1j*(float(phi[transducer])+k*dmag))    # Exponential term
                            
                        if theta < 1*(10**-13):
                            Df = 1 + 0j # setting the Df value to 1 directly above the transducers
                        else:
                            Df = (cmath.sin(k*a*cmath.sin(theta)))/(k*a*cmath.sin(theta))   # Directivity function of a circular piston source
                            
                        p[transducer, xloop, yloop, zloop] = p0*A*((Df)/(dmag))*exp    
                                            
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


def calc_pressure_field_numpy(rt, nt, ntrans, phi):
    
    import numpy as np; import math; import constants; 
    
    p = np.zeros ((ntrans, constants.npoints, constants.npoints, constants.npoints), dtype=complex)
    k = (2*math.pi)/(float(constants.lamda)) # Wavenumber
    
    x_temp = np.linspace(-constants.gsize,   constants.gsize, constants.npoints)
    y_temp = np.linspace(               0, 2*constants.gsize, constants.npoints)
    z_temp = np.linspace(-constants.gsize,   constants.gsize, constants.npoints)
    
    x_y_z_mesh = np.meshgrid(y_temp, z_temp, x_temp)
    
    x_co_ords = x_y_z_mesh[2]
    y_co_ords = x_y_z_mesh[0]
    z_co_ords = x_y_z_mesh[1]
    
    
    for transducer in range (0,ntrans):
        print("Calculated up to transducer ", transducer, " out of ", ntrans)
        d_x = np.subtract(x_co_ords, rt[transducer,0,0])
        d_y = np.subtract(y_co_ords, rt[transducer,0,1])
        d_z = np.subtract(z_co_ords, rt[transducer,0,2])
        
        d = np.array([d_x, d_y, d_z])
        
        dmag = np.linalg.norm(d, axis = 0)
        
        dot = np.add( np.add(np.multiply(d_x, nt[transducer,0,0]) ,  np.multiply(d_y, nt[transducer,0,1])) ,  np.multiply(d_z, nt[transducer,0,2]))
        
        theta = np.arccos( np.divide(dot, dmag) )
        
        exp = np.exp(np.multiply(1j, np.add(phi[transducer], np.multiply(k, dmag))))
        
        df_numerator   = np.sin(np.multiply(k, np.multiply(constants.a, np.sin(theta))))
        df_denominator = np.multiply(k, np.multiply(constants.a, np.sin(theta)))
        df = np.divide(df_numerator, df_denominator)
        
        p[transducer] = np.multiply(np.multiply(np.multiply(constants.p0, constants.A), exp), np.divide(df, dmag) )
        
    return p
    
    
    