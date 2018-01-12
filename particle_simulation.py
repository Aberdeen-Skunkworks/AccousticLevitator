import matplotlib as mpl; import numpy as np; import matplotlib.pyplot as plt; from mpl_toolkits.mplot3d import Axes3D;
import math; import algorithms; import transducer_placment; import phase_algorithms
 
 
inital_pos = [0,0.021,-0]        # m
inital_vel = [0,0,0]        # m/s
gravity    = [0, -9.81, 0]  # m/s^2
diamiter   = 0.005          # m    
density    = 29             # kg/m^3
dt         = 0.0001         # Time step s
end_time   = 0.2             # End time s

vol_sph = (1/6) * math.pi * diamiter**3      # m^3
mass    = vol_sph * density               # kg


rt = transducer_placment.array_grid(0.01,6,6)
ntrans = len (rt)
nt = transducer_placment.direction_vectors(ntrans)
phi_focus = phase_algorithms.phase_find(rt,0,0.02,0) # phi is the initial phase of each transducer to focus on a point
phi = phase_algorithms.add_twin_signature(rt,phi_focus)


number_of_time_steps = int( end_time / dt )

mass = np.copy(mass)
pos = np.copy(inital_pos)
vel = np.copy(inital_vel)
force_g = np.multiply( np.copy(gravity), mass)

time = np.zeros(1)

pos_over_time = np.zeros((number_of_time_steps,3))
x = np.zeros(number_of_time_steps); y = np.zeros(number_of_time_steps); z = np.zeros(number_of_time_steps)


for time_step in range(0, number_of_time_steps):
    pos_over_time[time_step][0] = pos[0]; pos_over_time[time_step][1] = pos[1]; pos_over_time[time_step][2] = pos[2] 
    pos = np.add(pos,(np.multiply(dt, vel)))
    #print(pos)
    force = np.add( force_g, np.multiply(-1, algorithms.differentiate_acoustic_potential(dt,pos,rt,phi,nt)))
    #print(force)
    vel = np.add(vel, (np.multiply(dt, np.divide(force, mass) ) ) )  
    time = np.add(time, dt)


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
#ax.plot_surface(xx, yy, zz)

ax.plot(x, y, z, label='Trajectory')
ax.legend()

plt.show()