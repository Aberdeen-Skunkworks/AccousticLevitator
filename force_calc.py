# -------------------------Import Libaries------------------------------------

import constants; import numpy as np; import calc_pressure_field; import time; import algorithms; import math
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import scipy.ndimage

# -------------------------Variables to set------------------------------------



##opposite arrays
    
rt = transducer_placment.big_daddy()

ntrans = len (rt)   # Total number of transducers in grid
nt_1 = transducer_placment.direction_vectors(ntrans,[1,0,0]) # nt is the direction vector of each transducer
nt_2 = transducer_placment.direction_vectors(ntrans,[-1,0,0])

sideways_1 = np.copy(rt)
sideways_2 = np.copy(rt)

sideways_1[:,0] = np.add(rt[:,2], -0.0516)
sideways_1[:,2] = np.add(rt[:,0], 0.05)

sideways_2[:,0] = np.add(rt[:,2], 0.0516)
sideways_2[:,2] = np.add(rt[:,0], 0.05)

rt_both_arrays = np.append(sideways_1, sideways_2, axis=0)
nt_both_arrays = np.append(nt_1, nt_2, axis=0)

#transducer_placment.plot_as_vectors(rt_both_arrays,nt_both_arrays)  # Use to plot the array layout in 3D

rt = rt_both_arrays

nt = nt_both_arrays



#rt = transducer_placment.array_grid(0.01,8,8) # spcing , x nummber, y number of transducers
#rt = transducer_placment.big_daddy()
#rt = transducer_placment.random(88,0.05,0.01)
ntrans = len (rt)   # Total number of transducers in grid

#nt = transducer_placment.direction_vectors(ntrans,[0,0,1]) # nt is the direction vector of each transducer

focus_point = [ 0 , 0, 0.05]

calculation_centre_point = [ 0 , 0, 0.05]


phi_focus = phase_algorithms.phase_find(rt, focus_point[0], focus_point[1], focus_point[2]) # phi is the initial phase of each transducer to focus on a point
phi_signature = phase_algorithms.add_twin_signature(rt, np.copy(phi_focus), 90)
#phi_signature = phase_algorithms.add_vortex_signature(rt, np.copy(phi_focus))
#phi_signature = phase_algorithms.add_bottle_signature(rt, np.copy(phi_focus),0.02)
#phi_noise = phase_algorithms.phase_random_noise(2, np.copy(phi_signature)) # number is randomness multiplier (0-1)*multiplier scaled between 0 and 2pi

phi = phi_signature


potential_calculated = algorithms.force_calc(calculation_centre_point, rt, nt, phi, vti = True)



pabs = potential_calculated[0]
fx = potential_calculated[1]
fy = potential_calculated[2] 
fz = potential_calculated[3] 
u_with_gravity = potential_calculated[4]
u_with_gravity_nano = potential_calculated[5] 
laplace_u = potential_calculated[6]


print("For use in paraview: ")
print("Trap point at index ", np.divide(focus_point, constants.deltaxyz), " Away from [0,0,0]")
print("Particle radius in indexes = ", np.divide(np.divide(constants.particle_diamiter,2), constants.deltaxyz))
print(" ")
print("Calculations compleated successfuly")




# For plotting graphs of forces and potential

x_distances = np.linspace(-constants.gsize + focus_point[0],   constants.gsize + focus_point[0], constants.npoints)
y_distances = np.linspace(-constants.gsize + focus_point[1],   constants.gsize + focus_point[1], constants.npoints)
z_distances = np.linspace(-constants.gsize + focus_point[2],   constants.gsize + focus_point[2], constants.npoints)

focus_as_index = int(((constants.npoints-1)/ 2))

x_forces = fx[ :               , focus_as_index  , focus_as_index]
y_forces = fy[ focus_as_index  , :               , focus_as_index]
z_forces = fz[ focus_as_index  , focus_as_index  , :             ]

x_pressure = pabs[ :               , focus_as_index , focus_as_index]
y_pressure = pabs[ focus_as_index  , :              , focus_as_index]
z_pressure = pabs[ focus_as_index  , focus_as_index , :             ]

x_potential = u_with_gravity[ :               , focus_as_index , focus_as_index]
y_potential = u_with_gravity[ focus_as_index  , :              , focus_as_index]
z_potential = u_with_gravity[ focus_as_index  , focus_as_index , :             ]


import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import axes3d
"""

ax = plt.axes()
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

fig = plt.figure()
"""

ax4 = plt.axes()
ax4.plot(x_distances, x_potential, 'ro')
ax4.set_xlabel('Distance from origin /m')
ax4.set_ylabel('Potential Energy /J')
ax4.set_title('X - Potential energy around trap point: ' + str(focus_point))

fig = plt.figure()

ax5 = plt.axes()
ax5.plot(y_distances, y_potential, 'ro')
ax5.set_xlabel('Distance from origin /m')
ax5.set_ylabel('Potential Energy /J')
ax5.set_title('Y - Potential energy around trap point: ' + str(focus_point))

fig = plt.figure()

ax6 = plt.axes()
ax6.plot(z_distances, z_potential, 'ro')
ax6.set_xlabel('Distance from origin /m')
ax6.set_ylabel('Potential Energy /J')
ax6.set_title('Z - Potential energy around trap point: ' + str(focus_point))


fig = plt.figure()

ax7 = fig.add_subplot(111, projection='3d')
x = np.tile(x_distances,(len(x_distances),1))
y = np.transpose(np.tile(y_distances,(len(y_distances),1)))
u_plane = u_with_gravity[ :               , : , focus_as_index]
ax7.plot_wireframe(x,y,u_plane, rstride = 1, cstride = 1)

