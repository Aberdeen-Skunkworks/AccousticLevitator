#import algorithms
#import constants
#
#import numpy
#import numpy as np
#
#Vector = numpy.array
#
#trap_point = Vector([0.0,0.0,0.2])
#x_temp = np.linspace(-constants.gsize + trap_point[0],   constants.gsize + trap_point[0], constants.npoints)
#y_temp = np.linspace(-constants.gsize + trap_point[1],   constants.gsize + trap_point[1], constants.npoints)
#z_temp = np.linspace(-constants.gsize + trap_point[2],   constants.gsize + trap_point[2], constants.npoints )
##z_temp = np.linspace(               0.005, 2*constants.gsize, constants.npoints)
#x_y_z_mesh = np.meshgrid(x_temp, y_temp, z_temp)
#
#x_co_ords = x_y_z_mesh[0]
#y_co_ords = x_y_z_mesh[1]
#z_co_ords = x_y_z_mesh[2]
#
#
#print(x_co_ords[34,34,44], y_co_ords[34,34,44], z_co_ords[34,34,34])
#absp, fx,fy,fz,u_incl_grav, u_incl_grav_nano, laplaceu = algorithms.force_calc(focus_point=trap_point, rt=Vector([[0,0,0]]), nt=Vector([[0,0,1]]), phi=[0.5], vti = False)
#print("abs_p=",absp[34,34,34])
#print("u=",u_incl_grav[34,34,34])


from UltrasonicLevitator import *

import matplotlib.pyplot as plt

sys = ParticleSystem()
sys.appendTransducer(Vector([0,0,0]), Vector([0,1,0]))

import numpy as np

res = 0.001
xs = np.arange(-0.1,0.1,res)
ys = np.arange(0.005,0.2,res)
z = np.zeros((len(xs), len(ys)))

def calcFields(shift:float =0):
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            z[i,j] = sys.pressure(Vector([x,y,0]), shift).real

calcFields(0)

fig = plt.figure()
ax = plt.gca()
im = plt.imshow(numpy.flip(z.T, 0), extent=(min(xs), max(xs), min(ys), max(ys)), animated=True,  cmap="jet")
plt.ylim(min(ys)-0.02, max(ys))
import matplotlib.patches as patches
rect = patches.Rectangle((-0.005, -0.005), 0.01, 0.01, fill=True, facecolor="black")
ax.add_patch(rect)

def animate(ishift):
    calcFields(-2 * math.pi *  ishift / 30)
    im.set_array(numpy.flip(z.T, 0))
    return im,

import matplotlib.animation as animation
anim = animation.FuncAnimation(fig, animate, frames=30, interval=20, blit=True)
#anim.save('single_transducer.gif', fps=30, dpi=80, writer='imagemagick')
"""
sys.clear()
for x in np.arange(-0.03, 0.035, 0.01):    
    sys.appendTransducer(Vector([x,0,0]), Vector([0,1,0]))
    rect = patches.Rectangle((x-0.005, -0.005), 0.01, 0.01, fill=True, facecolor="black", edgecolor="white")
    ax.add_patch(rect)

anim = animation.FuncAnimation(fig, animate, frames=30, interval=20, blit=True)
anim.save('multi_transducer.gif', fps=30, dpi=80, writer='imagemagick')

sys.focus(Vector([0, 0.05, 0]))
anim = animation.FuncAnimation(fig, animate, frames=30, interval=20, blit=True)
anim.save('multi_transducer_focussed.gif', fps=30, dpi=80, writer='imagemagick')
"""