# -*- coding: utf-8 -*-

# -------------------------Import Libaries------------------------------------

import constants; import numpy as np; import calc_pressure_field; import time; import algorithms
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import scipy.ndimage

# -------------------------Variables to set------------------------------------



##opposite arrays
    
rt = transducer_placment.big_daddy()

ntrans = len (rt)   # Total number of transducers in grid
nt_1 = transducer_placment.direction_vectors(ntrans,[1,0,0]) # nt is the direction vector of each transducer
nt_2 = transducer_placment.direction_vectors(ntrans,[-1,0,0])

sideways_1 = np.copy(rt)
sideways_2 = np.copy(rt)

sideways_1[:,0] = np.add(rt[:,2], -0.05)
sideways_1[:,2] = np.add(rt[:,0], 0.05)

sideways_2[:,0] = np.add(rt[:,2], 0.05)
sideways_2[:,2] = np.add(rt[:,0], 0.05)

rt_both_arrays = np.append(sideways_1, sideways_2, axis=0)
nt_both_arrays = np.append(nt_1, nt_2, axis=0)

#transducer_placment.plot_as_vectors(rt_both_arrays,nt_both_arrays)  # Use to plot the array layout in 3D

rt = rt_both_arrays

nt = nt_both_arrays



#rt = transducer_placment.big_daddy()   # spcing , x nummber, y number of transducers
ntrans = len (rt)   # Total number of transducers in grid

#nt = transducer_placment.direction_vectors(ntrans,[0,0,1]) # nt is the direction vector of each transducer

focus_point = [ 0 , 0 , 0.05 ]

phi_focus = phase_algorithms.phase_find(rt, focus_point[0], focus_point[1], focus_point[2]) # phi is the initial phase of each transducer to focus on a point
phi_signature = phase_algorithms.add_twin_signature(rt, np.copy(phi_focus), 90) # Positions, phases, angle of plane betweem 0 and 180 degrees
#phi_noise = phase_algorithms.phase_random_noise(2, np.copy(phi_signature)) # number is randomness multiplier (0-1)*multiplier scaled between 0 and 2pi

phi = phi_signature

#phi = phase_algorithms.phase_discretize(np.copy(phi))




# ----------------------Setting up output arrays-------------------------------

pcombined = np.zeros ((constants.npoints,constants.npoints,constants.npoints),dtype=complex)

px = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=complex)
py = np.copy(px); pz = np.copy(px)

ux = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)
uy = np.copy(ux); uz = np.copy(ux)

pabs = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float) 
pxabs = np.copy(pabs); pyabs = np.copy(pabs); pzabs = np.copy(pabs)

u = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)

height = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)

# ----------------------------------------------------------------------------

t0 = time.time()

#p_old = calc_pressure_field.calc_pressure_field(rt, nt, ntrans, phi) # calculate pressure field

t1 = time.time()
p = calc_pressure_field.calc_pressure_field_numpy(rt, nt, ntrans, phi)
t2 = time.time()
print(" ")
print("Numpy pressure calculation took ",round(t2-t1,2), " seconds" )
print(" ")


# -----------------Loop to sum pressure of all transducers---------------------

height = np.multiply(constants.deltaxyz, np.indices([constants.npoints, constants.npoints, constants.npoints])[2]) # 55 times faster
pcombined = np.sum(np.copy(p), axis = 0) 

# -----------------Calculating derrivitive of the pressure field---------------

diff_p = np.gradient(pcombined,constants.deltaxyz)
px = np.copy(diff_p[0]); py = np.copy(diff_p[1]); pz = np.copy(diff_p[2])

# ----------------- Calculating the Gork’ov potential-------------------------

# Calculating absuloute values for the pressure field and its derrivitives
       
pabs   = np.absolute(pcombined)  
pxabs  = np.absolute(px)  
pyabs  = np.absolute(py)  
pzabs  = np.absolute(pz)  

# Calculating Gork’ov potential u (Including gravity)

u = ( np.subtract( np.subtract( np.multiply(np.multiply(2, constants.k1), np.power(pabs, 2) ), 
np.multiply( np.multiply(2, constants.k2), np.add(np.add(np.power(pxabs, 2), np.power(pyabs, 2)), np.power(pzabs, 2) ) ) ),  
np.multiply(constants.p_mass, np.multiply(constants.gravity, np.copy(height)))) ) # Gravity term

# -----------------Calculating derrivitive of Gork’ov potential ---------------

diff_u = np.gradient(u,constants.deltaxyz)
ux = np.copy(diff_u[0]); uy = np.copy(diff_u[1]); uz = np.copy(diff_u[2])

# -----------------Calculating force on particle ---------------

fx = np.copy(-ux); fy = np.copy(-uy); fz = np.copy(-uz)


laplace_u = scipy.ndimage.filters.laplace(u)



# -------------------Creating output images and vtk file----------------------

vti_writer (constants.npoints, pabs, fx, fy, fz, u, laplace_u)


print("For use in paraview: ")
print("Trap point at index ", np.divide(focus_point, constants.deltaxyz), " Away from [0,0,0]")
print("Particle radius in indexes = ", np.divide(np.divide(constants.particle_diamiter,2), constants.deltaxyz))
print(" ")
print("Calculations compleated successfuly")







"""


# ------------Main file but using the analyitical pressure equations-----------

import constants; import numpy as np; from calc_pressure_field import calc_pressure_field
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import algorithms;


#rt = transducer_placment.big_daddy()
rt = transducer_placment.array_grid(0.01, 6, 6) 
ntrans = len (rt)
nt = transducer_placment.direction_vectors(ntrans)
phi_focus = phase_algorithms.phase_find(rt,0, 0.02, 0) # phi is the initial phase of each transducer to focus on a point
phi = phase_algorithms.add_twin_signature(rt, np.copy(phi_focus))


################# Wont work now without adding p_abs to the acoustic_potential function in algorithms(invalid index to scalar variable.)
u = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)
p_abs = np.zeros ((constants.npoints,constants.npoints,constants.npoints), dtype=float)

x = constants.x; y = constants.y; z = constants.z
gsize = constants.gsize
for xloop in range (0,constants.npoints):
    for yloop in range (0,constants.npoints):
        for zloop in range (0,constants.npoints):
            
            r = [ x  , y , z ]          # Point in space for each itteriation
            u_and_p = algorithms.acoustic_potential(r, rt, phi, nt)
            u[xloop,yloop,zloop] = u_and_p[0] - (constants.p_mass*constants.gravity*(yloop*constants.deltaxyz)) # including potential energy (mass*g*height)
            p_abs[xloop,yloop,zloop] = u_and_p[1]            
                        
            z = z + constants.deltaxyz    # Adding delta to x,y and z
        y = y + constants.deltaxyz
        z = -gsize               # Resetting the value of z to start value for next loop
    x = x + constants.deltaxyz
    y = 0                       # Resetting the value of y to start value for next loop
    z = -gsize                   # Resetting the value of z to start value for next loop
x = -gsize # Initial values of x,y and z in (m) Grid volume
y = 0.00
z = -gsize


diff_u = np.gradient(u,constants.deltaxyz)
ux = np.copy(diff_u[0]); uy = np.copy(diff_u[1]); uz = np.copy(diff_u[2])

# -----------------Calculating force on particle ---------------

fx = np.copy(-ux); fy = np.copy(-uy); fz = np.copy(-uz)

vti_writer (constants.npoints,p_abs,fx,fy,fz,u)

print("Calculations compleated successfuly")


"""












