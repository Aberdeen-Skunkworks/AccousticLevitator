import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pos = np.zeros(3); vel = np.zeros(3); mass = np.zeros(1); time = np.zeros(1); force = np.zeros(3);

inital_pos = [0,0,0]
inital_vel = [3,15,16]
gravity    = [0, -9.81, 0] # m/s^2


dt = 0.0001        # Time step seconds
end_time = 3  # End time seconds

number_of_time_steps = int( end_time / dt )

mass[0] = 1
pos[0] = inital_pos[0]; pos[1] = inital_pos[1]; pos[2] = inital_pos[2]
vel[0] = inital_vel[0]; vel[1] = inital_vel[1]; vel[2] = inital_vel[2]
force[0] = gravity[0]*mass[0]; force[1] = gravity[1]*mass[0]; force[2] = gravity[2]*mass[0]
pos_over_time = np.zeros((number_of_time_steps,3))
x = np.zeros(number_of_time_steps); y = np.zeros(number_of_time_steps); z = np.zeros(number_of_time_steps)


for time_step in range(0, number_of_time_steps):
    pos_over_time[time_step][0] = pos[0]; pos_over_time[time_step][1] = pos[1]; pos_over_time[time_step][2] = pos[2] 
    pos = np.add(pos,(np.multiply(dt, vel)))
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

yy, xx = np.meshgrid(np.linspace(-50, 50, num=21), np.linspace(-50, 50, num=21))
zz = xx*0

ax = plt.subplot(projection='3d')
ax.plot_surface(xx, yy, zz)

ax.plot(x, y, z, label='Trajectory')
ax.legend()

plt.show()