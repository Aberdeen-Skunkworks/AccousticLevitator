def phifind(rt,x,y,z):
    

    # This function takes in a array of transducers and a position in space and
    # outputs the phases of all the transducers so that the magnitude of
    # the complex pressure is zero at that point.

    import scipy.optimize; import numpy as np
    
    r = (x,y,z) # r is the position of desired minimum
    
    ntrans = len (rt)
    initial_guess = np.zeros((ntrans))    
    initial_guess.fill((2))
    

    def find(phi):
        # -------------------------Import Libaries------------------------------------
        
        import cmath; import math; import numpy as np; from direction_vectors import direction_vectors; import constants
        
        # -------------------------Variables to set------------------------------------
        
        ntrans = len (rt)   # Total number of transducers in grid
        
        # nt is the direction vector of each transducer-------------------------------
        nt = direction_vectors(ntrans) 
        
        p0 = constants.p0; A = constants.A; a = constants.a; lamda = constants.lamda
        
        # ----------------------Setting up output arrays-------------------------------
        
        p = np.zeros ((ntrans), dtype=complex)
        pcombined = np.zeros ((),dtype=complex)
        
        # -----------------Loop to calculate pressure field----------------------------
        for transducer in range (0,ntrans):
                        
            d = [0,0,0]                 # defining the seperation vector of transducer form point in space
            
            for i in range (3):
                d[i] = r[i] - rt[transducer,0,i]   # Calculating the seperation vector of transducer form point in space
            
            dmag = np.linalg.norm(d)     # Distance between transducer and point in space
            
            if dmag < (1*10**(-13)): # Calculating complex acoustic pressure at point r[x,y,z] 
                p[transducer] = 0 
            else:
                
                dot = d[0]*nt[transducer,0,0] + d[1]*nt[transducer,0,1] + d[2]*nt[transducer,0,2] # Dot product of the direction of the transducr and the position in space
                theta = math.acos(dot/dmag)
            
                k = (2*math.pi)/(float(lamda))                         # Wavenumber
                exp = cmath.exp(1j*(float(phi[transducer])+k*dmag))    # Exponential term
                    
                if theta < 1*(10**-13):
                    Df = 1 + 0j # setting the Df value to 1 directly above the transducers
                else:
                    Df = (cmath.sin(k*a*cmath.sin(theta)))/(k*a*cmath.sin(theta))   # Directivity function of a circular piston source
                    
                p[transducer] = p0*A*((Df)/(dmag))*exp    
                                            
        
        # -----------------Loop to sum pressure of all transducers---------------------
        
        
        for transducers in range (0,ntrans):
            pcombined = pcombined + p[transducers]
            realcombined = np.absolute(pcombined) 
            
        return realcombined
    
    calc_phi = scipy.optimize.minimize(find, initial_guess , method='Nelder-Mead', tol=1e-6)
    
    check_success = calc_phi.get('success',)
    
    if check_success:
        print('Phase calculation successful')
        return(calc_phi)    
    else:
        print("Optimize Failed message = " + calc_phi.get('message',) )





############TEST###################
        
#from array_grid import array_grid

#rt = array_grid(0.01,3,3)

#test = phifind(rt,0,0.03,0)





