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

t = Transducer(Vector([0,0,0]), Vector([0,1,0]), 0)

import numpy as np

res = 0.001
xs = np.arange(-0.1,0.1,res)
ys = np.arange(0,0.2,res)
z = np.zeros((len(xs), len(ys)))

for i,x in enumerate(xs):
    for j,y in enumerate(ys):
        z[i,j] = t.pressure(Vector([x,y,0])).real

fig = plt.figure()
im = plt.imshow(numpy.flip(z.T, 0), extent=(min(xs), max(xs), min(ys), max(ys)), animated=True)
        
def animate(ishift):
    shift = -2 * math.pi *  ishift / 10
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            z[i,j] = t.pressure(Vector([x,y,0]), shift).real
    im.set_array(numpy.flip(z.T, 0))
    return im,

import matplotlib.animation as animation
anim = animation.FuncAnimation(fig, animate, frames=10, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
