import numpy as np
import matplotlib.pyplot as plt
import constants
import math



k = (2*math.pi)/(float(constants.lamda))
a = 0.0043


theta = np.arange(0.001, 2*math.pi, 0.01)
pressure = np.zeros((len(theta)))
decebel = np.zeros((len(theta)))

for i in range(len(theta)):
    pressure[i] = math.sin(k * a * math.sin(theta[i])) / (k * a * math.sin(theta[i]))
    if pressure[i] < 0:
        pressure[i] = 0.0001
    decebel[i] = 20*math.log10(pressure[i]/0.00002)


ax = plt.subplot(111, projection='polar')
ax.plot(theta, decebel)
ax.set_rmax(np.max(decebel))
ax.set_rticks([60,70,80])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()










