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
            #z[i,j] = sys.pressure(Vector([x,y,0]), shift).real
            z[i,j] = sys.Gorkov_potential(Particle(Vector([x,y,0]), 7.176591426e-7, 0.0042))

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

render_animations=False

if render_animations:
    import matplotlib.animation as animation
    anim = animation.FuncAnimation(fig, animate, frames=30, interval=20, blit=True)
    anim.save('single_transducer.gif', fps=30, dpi=80, writer='imagemagick')
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
else:
    animate(0)
    plt.show(block=False)
    wait = input("PRESS ENTER TO CONTINUE.")
    
    sys.clear()
    for x in np.arange(-0.03, 0.035, 0.01):    
        sys.appendTransducer(Vector([x,0,0]), Vector([0,1,0]))
        rect = patches.Rectangle((x-0.005, -0.005), 0.01, 0.01, fill=True, facecolor="black", edgecolor="white")
        ax.add_patch(rect)

    animate(0)
    plt.draw()
    wait = input("PRESS ENTER TO CONTINUE.")

    sys.focus(Vector([0, 0.05, 0]))
    animate(0)
    print("Showing multi-focussed")
    plt.draw()
    wait = input("PRESS ENTER TO CONTINUE.")
