

# Code testing and visulisation


''' Test hex_grid '''
from transducer_placment import hex_grid 
import numpy as np
import matplotlib.pyplot as plt
import math


rt = hex_grid(0.011,5,5)
trans_to_delete = [0,1,4,5,18,16,24]                   # List of unwanted transducers 

trans_to_delete = sorted(trans_to_delete)
ntrans = len (rt)
n_trans_to_delete = len(trans_to_delete)

fig, ax = plt.subplots()
plt.plot(rt[:,0,0], rt[:,0,2], 'ro')                    # Plots small dots

for loop in range (0, (n_trans_to_delete)):             # Deletes unwanted transducers
    rt = np.delete(rt, trans_to_delete[loop], 0)
    trans_to_delete = np.subtract(trans_to_delete, 1)
    
for trans in range (0, (ntrans - n_trans_to_delete)):   # Plots circles
    circle = plt.Circle((rt[trans,0,0], rt[trans,0,2]), 0.005, color='r')
    ax.add_artist(circle)

plt.xlim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075))
plt.ylim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075))

