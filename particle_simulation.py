import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


inital_pos = [0,0,0]        # m
inital_vel = [0,15,15]      # m/s
gravity    = [0, -9.81, 0]  # m/s^2
mass       = 1              # kg

dt = 0.0001   # Time step s
end_time = 3  # End time s



number_of_time_steps = int( end_time / dt )

mass = np.copy(mass)
pos = np.copy(inital_pos)
vel = np.copy(inital_vel)
force = np.multiply( np.copy(gravity), mass)
time = np.zeros(1)


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