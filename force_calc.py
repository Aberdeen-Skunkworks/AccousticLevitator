
# -------------------------Import Libaries------------------------------------

import constants; import numpy as np; import calc_pressure_field; import time; import algorithms
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import scipy.ndimage

# -------------------------Variables to set------------------------------------


"""
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
"""


rt = transducer_placment.array_grid(0.01,10,10) # spcing , x nummber, y number of transducers
ntrans = len (rt)   # Total number of transducers in grid

nt = transducer_placment.direction_vectors(ntrans,[0,0,1]) # nt is the direction vector of each transducer

focus_point = [ 0 , 0 , 0.02]

phi_focus = phase_algorithms.phase_find(rt, focus_point[0], focus_point[1], focus_point[2]) # phi is the initial phase of each transducer to focus on a point
phi_signature = phase_algorithms.add_twin_signature(rt, np.copy(phi_focus), 90)
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
p = calc_pressure_field.calc_pressure_field_numpy_around_trap(rt, nt, ntrans, phi, focus_point)
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




focus_as_index = np.divide(focus_point , constants.deltaxyz)

focus_as_index_x = int(focus_as_index[0])
focus_as_index_y = int(focus_as_index[1])
focus_as_index_z = int(focus_as_index[2])

x_forces = fx[ :               , 0, 0]
y_forces = fy[ 0, :               , 0]
z_forces = fz[ 0, 0, :               ]

x_potential = u[ :               , 0, 0]
y_potential = u[ 0, :               , 0]
z_potential = u[ 0, 0, :               ]

x_distances = np.linspace(-constants.gsize + focus_point[0],   constants.gsize + focus_point[0], constants.npoints)
y_distances = np.linspace(-constants.gsize + focus_point[1],   constants.gsize + focus_point[1], constants.npoints)
z_distances = np.linspace(-constants.gsize + focus_point[2],   constants.gsize + focus_point[2], constants.npoints)


import matplotlib.pyplot as plt;


ax = plt.axes()
"""
ax.plot(x_distances, x_forces, 'ro')
ax.set_xlabel('Distance from origin /m')
ax.set_ylabel('Force /N')
ax.set_title('X forces for trap point of: ' + str(focus_point))

fig = plt.figure()

ax2 = plt.axes()
ax2.plot(y_distances, y_forces, 'ro')
ax2.set_xlabel('Distance from origin /m')
ax2.set_ylabel('Force /N')
ax2.set_title('Y forces for trap point of: ' + str(focus_point))

fig = plt.figure()

ax3 = plt.axes()
ax3.plot(z_distances, z_forces, 'ro')
ax3.set_xlabel('Distance from origin /m')
ax3.set_ylabel('Force /N')
ax3.set_title('Z forces for trap point of: ' + str(focus_point))
"""

#fig = plt.figure()

ax.plot(x_distances, x_potential, 'ro')
ax.set_xlabel('Distance from origin /m')
ax.set_ylabel('Potential Energy /J')
ax.set_title('X - Potential energy around trap point: ' + str(focus_point))

fig = plt.figure()

ax2 = plt.axes()
ax2.plot(y_distances, y_potential, 'ro')
ax2.set_xlabel('Distance from origin /m')
ax2.set_ylabel('Potential Energy /J')
ax2.set_title('Y - Potential energy around trap point: ' + str(focus_point))

fig = plt.figure()

ax3 = plt.axes()
ax3.plot(z_distances, z_potential, 'ro')
ax3.set_xlabel('Distance from origin /m')
ax3.set_ylabel('Potential Energy /J')
ax3.set_title('Z - Potential energy around trap point: ' + str(focus_point))