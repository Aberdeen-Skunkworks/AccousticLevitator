

# Code testing and visulisation


''' Test hex_grid '''
import transducer_placment 
import numpy as np
import matplotlib.pyplot as plt
import math


rt = transducer_placment.hex_grid(0.011,6,7)
trans_to_delete = [0,4,5,11,23,30,35,36,37,41]                   # List of unwanted transducers 

trans_to_delete = sorted(trans_to_delete)
ntrans = len (rt)
n_trans_to_delete = len(trans_to_delete)

for loop in range (0, (n_trans_to_delete)):             # Deletes unwanted transducers
    rt = np.delete(rt, trans_to_delete[loop], 0)
    trans_to_delete = np.subtract(trans_to_delete, 1)
    
fig, ax = plt.subplots() 
plt.plot(rt[:,0,0], rt[:,0,2], 'ro')                    # Plots small dots

for trans in range (0, (ntrans - n_trans_to_delete)):   # Plots circles
    circle = plt.Circle((rt[trans,0,0], rt[trans,0,2]), 0.005, color='r')
    ax.add_artist(circle)

plt.xlim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075)) 
plt.ylim(-(math.sqrt(ntrans)*0.0075),(math.sqrt(ntrans)*0.0075)) 

