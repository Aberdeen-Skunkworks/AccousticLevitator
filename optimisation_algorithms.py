

def find_best(phase_offset):

    # -------------------------Import Libaries------------------------------------
    
    import constants; import numpy as np; from calc_pressure_field import calc_pressure_field; 
    
    # -------------------------Variables to set------------------------------------
    
    phi = np.add(phi_focus, phase_offset)
    #phi = phase_algorithms.add_vortex_signature(rt,phi_focus)
    
    # ----------------------Setting up output arrays-------------------------------
    
    p = np.zeros ((constants.npoints,constants.npoints,constants.npoints,ntrans), dtype=complex)
    pcombined = np.zeros ((constants.npoints,constants.npoints,constants.npoints),dtype=complex)
    realcombined = np.zeros ((constants.npoints,constants.npoints,constants.npoints),dtype=float)
    px = py = pz = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=complex)
    ux = uy = uz = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)
    pabs = pxabs = pyabs = pzabs   = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float) 
    u = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)
    
    # ----------------------------------------------------------------------------
    
    p = calc_pressure_field(rt, nt, ntrans, phi) # calculate pressure field
    
    # -----------------Loop to sum pressure of all transducers---------------------
    
    for xloop in range (0,constants.npoints): #Combining the tranducer fields
            for yloop in range (0,constants.npoints):
                for zloop in range (0,constants.npoints):
                    for transducers in range (0,ntrans):
                        pcombined[xloop,yloop,zloop] = pcombined[xloop,yloop,zloop] + p[xloop,yloop,zloop, transducers]
                        realcombined[xloop,yloop,zloop] = np.absolute(pcombined[xloop,yloop,zloop]) 
                        
                        
    # -----------------Calculating derrivitive of the pressure field---------------
    
    
    diff_p = np.gradient(pcombined,constants.deltaxyz)
    px = diff_p[0]; py = diff_p[1]; pz = diff_p[2]
    
    
    # ----------------- Calculating the Gork’ov potential-------------------------
    
    # Calculating absuloute values for the pressure field and its derrivitives
    
    for xloop in range (0,(constants.npoints)):
        for yloop in range (0,(constants.npoints)):
            for zloop in range (0,(constants.npoints)): 
                pabs[xloop,yloop,zloop]   = np.absolute(pcombined[xloop,yloop,zloop])  
                pxabs[xloop,yloop,zloop]  = np.absolute(px[xloop,yloop,zloop])  
                pyabs[xloop,yloop,zloop]  = np.absolute(py[xloop,yloop,zloop])  
                pzabs[xloop,yloop,zloop]  = np.absolute(pz[xloop,yloop,zloop])  
    
    # Calculating Gork’ov potential u
    for xloop in range (0,constants.npoints):
        for yloop in range (0,constants.npoints):
            for zloop in range (0,constants.npoints):
                u[xloop,yloop,zloop] = (2*constants.k1*pabs[xloop,yloop,zloop]**2) - (2*constants.k2*(pxabs[xloop,yloop,zloop]**2 + pyabs[xloop,yloop,zloop]**2 + pzabs[xloop,yloop,zloop]**2))
                u[xloop,yloop,zloop] = u[xloop,yloop,zloop] - (constants.p_mass*constants.gravity*(yloop*constants.deltaxyz)) # including potential energy (mass*g*height) it is taken away even though gravity is negitive so that when the negitive gradient is takn then the force will be downwards
    
    # -----------------Calculating derrivitive of Gork’ov potential ---------------
    
    
    diff_u = np.gradient(u,constants.deltaxyz)
    ux = -diff_u[0]; uy = -diff_u[1]; uz = -diff_u[2]
    
    
    # -------------- Calculating second derrivitive of the gorkov potential -------
    
    
    u_xx_xy_xz = np.gradient(ux, constants.deltaxyz)
    u_yx_yy_yz = np.gradient(uy, constants.deltaxyz)
    u_zx_zy_zz = np.gradient(uz, constants.deltaxyz)
    
    uxx = u_xx_xy_xz[0]
    uyy = u_yx_yy_yz[1]
    uzz = u_zx_zy_zz[2]
    
    # ---------------------------- Objective function ----------------------------
    
    objective = realcombined[2,2,2] - 0.005*uxx[2,2,2] - 0.005*uyy[2,2,2] - 0.001*uzz[2,2,2]    # function to minimise (missing weights?)
    
    if done == 1:
        print(realcombined[2,2,2])
        print(uxx[2,2,2])
        print(uyy[2,2,2])
        print(uzz[2,2,2])
    
    return objective
    



import scipy; import constants; import numpy as np; import math
import transducer_placment; import phase_algorithms; 


phase_offset = np.random.uniform(0, (2*math.pi), (16))

rt = transducer_placment.hex_grid(0.01,4,4) # See transducer_placment for variable inputs
    
ntrans = len (rt)   # Total number of transducers in grid
    
nt = transducer_placment.direction_vectors(ntrans) # nt is the direction vector of each transducer
    
phi_focus = phase_algorithms.phase_find(rt,constants.x, constants.y, constants.z) # phi is the initial phase of each transducer to focus on a point





# For finding the minimum of the objective function
done = 0
find_min = scipy.optimize.minimize(find_best, phase_offset, method='Powell', options = {'disp':True})
phase_offset = find_min.get("x")
done = 1
find_best(phase_offset)

test = find_best





# For finding the value of the objective function with twin and vortex signatures
"""
test = find_best(phase_offset)
print(test)
"""




# For finding average value of objective function for that transducer arrangment
"""
test = np.zeros((500))
for x in range (0, 500):
    phase_offset = np.random.uniform(0, (2*math.pi), (4))
    test[x] = find_best(phase_offset)
print(np.average(test))
"""













