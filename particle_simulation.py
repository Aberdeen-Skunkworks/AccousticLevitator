import matplotlib as mpl; import numpy as np; import matplotlib.pyplot as plt; from mpl_toolkits.mplot3d import Axes3D;
import math; import algorithms; import transducer_placment; import phase_algorithms; import constants;
 
 
inital_pos = [0.01,0.0185,0.01]             # m
inital_vel = [0,0,0]                        # m/s
gravity    = [0, -9.81, 0]                  # m/s^2
diamiter   = constants.particle_diamiter    # m    
density    = constants.rhos                 # kg/m^3
dt         = 0.0001                          # Time step s
end_time   = 0.1                            # End time s

vol_sph =   constants.v                     # m^3
mass    = vol_sph * density                 # kg


rt = transducer_placment.big_daddy()
ntrans = len (rt)
nt = transducer_placment.direction_vectors(ntrans)
phi_focus = phase_algorithms.phase_find(rt,0,0.018,0) # phi is the initial phase of each transducer to focus on a point
phi = phase_algorithms.add_twin_signature(rt,phi_focus)


number_of_time_steps = int( end_time / dt )

mass = np.copy(mass)
pos = np.copy(inital_pos)
vel = np.copy(inital_vel)
force_g = np.multiply( np.copy(gravity), mass)
total_energy = np.zeros(number_of_time_steps)

time = np.zeros(1)

force_over_time = np.zeros((number_of_time_steps,3))
pos_over_time = np.zeros((number_of_time_steps,3))
x = np.zeros(number_of_time_steps); y = np.zeros(number_of_time_steps); z = np.zeros(number_of_time_steps)

"""
###### Forward Euler Algorithm
for time_step in range(0, number_of_time_steps):
    pos_over_time[time_step][0] = pos[0]; pos_over_time[time_step][1] = pos[1]; pos_over_time[time_step][2] = pos[2] 
    pos = np.add(pos,(np.multiply(dt, vel)))
    force = np.add( force_g, np.multiply(-1, algorithms.differentiate_acoustic_potential(dt,pos,rt,phi,nt)))
    vel = np.add(vel, (np.multiply(dt, np.divide(force, mass) ) ) )  
    time = np.add(time, dt)
    total_energy[time_step] = algorithms.acoustic_potential(pos, rt, phi, nt) + (0.5 * mass * np.linalg.norm(vel)**2) + (mass * 9.81 * pos[1])
    #if pos[1]<0:
    #    break
"""

##### Verlet Algorithm
for time_step in range(0, number_of_time_steps):
    pos_over_time[time_step][0] = pos[0]; pos_over_time[time_step][1] = pos[1]; pos_over_time[time_step][2] = pos[2] 
    
    force = np.add( force_g, np.multiply(-1, algorithms.differentiate_acoustic_potential(dt,pos,rt,phi,nt)))
    acceleration = np.divide(force,mass)
    
    pos = np.add( pos, np.multiply(dt, vel), (acceleration*( (dt**2) / 2 ) ) )
    
    force_next = np.add( force_g, np.multiply(-1, algorithms.differentiate_acoustic_potential(dt,pos,rt,phi,nt)))
    acceleration_next = np.divide(force,mass)
    
    vel = np.add(vel, np.multiply( ( dt / 2 ) , np.add( acceleration, acceleration_next ) )   )
    
    time = np.add(time, dt)
    #total_energy[time_step] = algorithms.acoustic_potential(pos, rt, phi, nt) + (0.5 * mass * np.linalg.norm(vel)**2) + (mass * 9.81 * pos[1])
    if pos[1]<0:
        break

"""
##### Leapfrog Verlet Algorithm (In progress)
for time_step in range(0, number_of_time_steps):
    pos_over_time[time_step][0] = pos[0]; pos_over_time[time_step][1] = pos[1]; pos_over_time[time_step][2] = pos[2] 
    
    
    
    pos = np.add( pos, np.multiply(dt, vel))
    
    force = np.add( force_g, np.multiply(-1, algorithms.differentiate_acoustic_potential(dt,pos,rt,phi,nt)))
    acceleration = np.divide(force,mass)
    
    vel = np.add(vel, np.multiply( ( dt / 2 ) , np.add( acceleration, acceleration_next ) )   )
    
    time = np.add(time, dt)
    #total_energy[time_step] = algorithms.acoustic_potential(pos, rt, phi, nt) + (0.5 * mass * np.linalg.norm(vel)**2) + (mass * 9.81 * pos[1])
    if pos[1]<0:
        break
"""
fig = plt.figure()
ax = fig.gca(projection='3d')

for time_step in range(0, number_of_time_steps):
    x[time_step] = pos_over_time[time_step][0]
    z[time_step] = pos_over_time[time_step][1]
    y[time_step] = pos_over_time[time_step][2]

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.set_zlabel('zlabel')

yy, xx = np.meshgrid(np.linspace(-0.05, 0.05, num=21), np.linspace(-0.05, 0.05, num=21))
zz = xx*0

ax = plt.subplot(projection='3d')
#x.plot_surface(xx, yy, zz)

ax.plot(x, y, z, label='Trajectory')
ax.legend()

plt.show()

# Energy Plot
#plt.plot(np.linspace(0,1000,1000), total_energy, 'ro')
#plt.show()