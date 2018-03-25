import constants; import numpy as np; import calc_pressure_field; import time; import algorithms; import math
import transducer_placment; from vti_writer import vti_writer; import phase_algorithms; import scipy.ndimage
import numpy.ma as ma

# Flooding filling regions by slowly rising up in values form a start point until the value does down
# somewhere then the region is full and that value is the stregnth of the trap.


# ---- For Niall's reference 
## Adding new value to list = np.append(neighbours, new_list, axis=0)
## Deleting min from list = np.delete(neighbours,np.argmin(neighbours[:,0]),0)

"""
heights = np.zeros((41,2))
for height_rise in range(41):
    heights[height_rise][0] = (height_rise*2)/1000
     ## to go in the focus point for z : (height_rise*2)/1000
"""
    
# ----------------------Setup for potential calculation------------------------

#rt = transducer_placment.array_grid(0.01,10,10) # spcing , x nummber, y number of transducers
rt = transducer_placment.big_daddy()
#rt = transducer_placment.random(88,0.05,0.01)
ntrans = len (rt)   # Total number of transducers in grid

nt = transducer_placment.direction_vectors(ntrans,[0,0,1]) # nt is the direction vector of each transducer

focus_point = [ 0 , 0, 0]

phi_focus = phase_algorithms.phase_find(rt, focus_point[0], focus_point[1], focus_point[2]) # phi is the initial phase of each transducer to focus on a point
phi_signature = phase_algorithms.add_twin_signature(rt, np.copy(phi_focus), 90)
#phi_signature = phase_algorithms.add_vortex_signature(rt, np.copy(phi_focus))
#phi_signature = phase_algorithms.add_bottle_signature(rt, np.copy(phi_focus),0.03)
#phi_noise = phase_algorithms.phase_random_noise(2, np.copy(phi_signature)) # number is randomness multiplier (0-1)*multiplier scaled between 0 and 2pi

phi = phi_signature

potential_calculated = algorithms.force_calc(focus_point, rt, nt, phi, vti = False) ## Outputs = pabs, fx, fy, fz, u_with_gravity, u_with_gravity_nano, laplace_u

u_with_gravity_nano = potential_calculated[5]

    
potential_array = u_with_gravity_nano
potential_array = np.pad(potential_array, (1), 'constant', constant_values=(0)) # Padding the edge with 0
length = len(potential_array)
regions = np.full((length, length, length), 0, dtype=int)
been = np.full((length, length, length), False, dtype=bool)
region = 0 # First region index - 1

been[0,:,:] = True
been[length-1,:,:] = True
been[:,0,:] = True
been[:,length-1,:] = True
been[:,:,0] = True
been[:,:,length-1] = True



def flood_region(neighbours, x, y, z, current_minimum, region):
    
    run = True
    while run == True:
        if x > 0 and x < length and y > 0 and y < length and z > 0 and z < length:
            neighbours = np.delete(neighbours,np.argmin(neighbours[:,0]),0)
            if been[x+1,y,z] == True: # x+1
                pass
            else:
                
                been[x+1,y,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x+1,y,z]
                new_list[0][1] = x+1; new_list[0][2] = y; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x-1,y,z] == True: # x-1
                pass
            else:
                
                been[x-1,y,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x-1,y,z]
                new_list[0][1] = x-1; new_list[0][2] = y; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y+1,z] == True: # y+1
                pass
            else:
                
                been[x,y+1,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y+1,z]
                new_list[0][1] = x; new_list[0][2] = y+1; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y-1,z] == True: # y-1
                pass
            else:
                
                been[x,y-1,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y-1,z]
                new_list[0][1] = x; new_list[0][2] = y-1; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y,z+1] == True: # z+1
                pass
            else:
                
                been[x,y,z+1] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y,z+1]
                new_list[0][1] = x; new_list[0][2] = y; new_list[0][3] = z+1;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y,z-1] == True: # z-1
                pass
            else:
                
                been[x,y,z-1] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y,z-1]
                new_list[0][1] = x; new_list[0][2] = y; new_list[0][3] = z-1;
                neighbours = np.append(neighbours, new_list, axis=0)
            
            if len(neighbours) == 0:
                #print("Skipped as there are no neighbours for this region")
                run = False
                end_point = [x,y,z]
                been[x,y,z] = True
                return current_minimum, end_point, []
            else:
                new_minimum_id = np.argmin(neighbours[:,0])
                new_minimum    = neighbours[new_minimum_id][0]
                if new_minimum >= current_minimum:
                    x = int(neighbours[new_minimum_id][1])
                    y = int(neighbours[new_minimum_id][2])
                    z = int(neighbours[new_minimum_id][3])
                    regions[x,y,z] = region
                    edge_mask[x,y,z] = True
                    been[x,y,z] = True
                    current_minimum = new_minimum
    
                else:
                    #print("Stopped since the boundary has been found")
                    #print("Edge Value = ", current_minimum)
                    end_point = [neighbours[new_minimum_id][1], neighbours[new_minimum_id][2], neighbours[new_minimum_id][2]]
                    run = False
                    for number in range(len(neighbours)):
                    1       been[int(neighbours[number][1]),int(neighbours[number][2]),int(neighbours[number][3])] = False
                    return current_minimum, end_point, neighbours
        
        else:
            #print("Reached the edge of the box")
            run = False
            return current_minimum, 0, neighbours
        
        
       
"""
while not np.all(been):
    potential_array = ma.masked_array(potential_array, been)
    global_min_index = np.unravel_index(np.argmin(potential_array, axis=None), potential_array.shape)
    start_point = [global_min_index[0],global_min_index[1],global_min_index[2]]
    x = start_point[0]
    y = start_point[1]
    z = start_point[2]
    current_minimum = potential_array[x,y,z]
    neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
    neighbours[0][0] = current_minimum; 
    neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
    region = int(region + 1)
    #print("Filling region: ", region)
    regions[x,y,z] = region
    been[x,y,z] = True
    flood_region(neighbours, x, y, z, current_minimum, region)
"""
"""
sorted_size_of_regions = np.zeros((np.max(regions),2)) # Format = [number of gridpoints, region]
for number_of_region in range(np.max(regions)):
    number_of_gridpoints = list(regions.flatten()).count(number_of_region)
    sorted_size_of_regions[number_of_region][0] = number_of_gridpoints; 
    sorted_size_of_regions[number_of_region][1] = number_of_region; 
    
sorted_size_of_regions = np.sort(sorted_size_of_regions, axis=0)
"""





edge_potential_array = np.copy(potential_array)

edge_mask = np.copy(been)
for x in range(2,length-2):
    for y in range(2,length-2):
        for z in range(2,length-2):
            edge_mask[x,y,z] = True
edge_potential_array = ma.masked_array(edge_potential_array, edge_mask)


neighbours_list = np.zeros((0,4)) # Format: neighbours[Value, X, Y, Z]


# Finds all edge regions
run_number = 1
while not np.all(edge_mask):
    print("Filling Outer edge: ",int(run_number))
    run_number += 1
    edge_potential_array = ma.masked_array(edge_potential_array, edge_mask)
    global_min_index = np.unravel_index(np.argmin(edge_potential_array, axis=None), edge_potential_array.shape)
    x = global_min_index[0]
    y = global_min_index[1]
    z = global_min_index[2]
    current_minimum = edge_potential_array[x,y,z]
    neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
    neighbours[0][0] = current_minimum
    neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
    region = int(1)
    #print("Filling region: ", region)
    regions[x,y,z] = region
    edge_mask[x,y,z] = True
    been[x,y,z] = True

    output = flood_region(neighbours, x, y, z, current_minimum, region)[2]
    if len(output)>=1:
            neighbours_list = np.append(neighbours_list,output, axis=0)


while not np.all(been):  
    potential_array = ma.masked_array(potential_array, been)
    global_min_index = np.unravel_index(np.argmin(potential_array, axis=None), potential_array.shape)
    x = global_min_index[0]
    y = global_min_index[1]
    z = global_min_index[2]
    current_minimum = potential_array[x,y,z]
    neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
    neighbours[0][0] = current_minimum
    neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
    region = int(region+1)
    print("Filling region: ", region)
    regions[x,y,z] = region

    output = flood_region(neighbours, x, y, z, current_minimum, region)[2]
    been[x,y,z] = True
    #if len(output)>=1:
            #neighbours_list = np.append(neighbours_list,output, axis=0)




unique, counts = np.unique(regions, return_counts=True)
dict_sorted = dict(zip(unique, counts))

import operator

sorted_regions = sorted(dict_sorted.items(), key=operator.itemgetter(1))

pop_off = True
regions_that_are_big_enough = np.zeros(0)
while pop_off == True:
    next_region = sorted_regions.pop()
    if next_region[1] > 40:
        regions_that_are_big_enough = np.append(regions_that_are_big_enough, next_region[0])
    else:
        pop_off = False

new_regions =  np.full((length, length, length), 0, dtype=int)

for region_itteration in range(len(regions_that_are_big_enough)):
    for x in range(length):
        for y in range(length):
            for z in range(length):
                if regions[x,y,z] == regions_that_are_big_enough[region_itteration]:
                    new_regions[x,y,z] = region_itteration





"""

#### Middle Start Point

start_point = [int(np.argmin(x_potential_middle)+(length-1-20)/2),int(np.argmin(y_potential_middle)+(length-1-20)/2),int(np.argmin(z_potential_middle)+(length-1-20)/2)]
print("Start point = ", start_point)
x = start_point[0]
y = start_point[1]
z = start_point[2]
current_minimum = potential_array[x,y,z]
trap_minimum_potential = np.copy(current_minimum)
neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
neighbours[0][0] = current_minimum; 
neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
## Region?
region = 2
regions[x,y,z] = region
been[x,y,z] = True
output = flood_region(neighbours, x, y, z, current_minimum, region)

edge_potential = output[0]
end_point = output[1]
neighbours = output[2]

distance = np.linalg.norm(np.subtract(start_point, end_point))
distance_meters = constants.deltaxyz * distance
change_in_energy = edge_potential - trap_minimum_potential
force = (change_in_energy/1000000)/distance_meters

print("Potential between trap centre and lowest edge = ", "%.2f" % (edge_potential - trap_minimum_potential), "Micro joules ")
#print("Maximum Potential of the trap = ", "%.2f" % maximum_of_trap, "Micro joules ")
print("Distance between trap centre and lowest edge = ", "%.2f" % (distance_meters*1000), "mm ")
print("Force to leave trap = ","%.5f" % force, "Newtons ")






x = 1
for y in range(1,length):
        for z in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)
            
x = length-2
for y in range(1,length):
        for z in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)   
y = 1
for x in range(1,length):
        for z in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)
            
y = length-2
for x in range(1,length):
        for z in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)            
z = 1
for x in range(1,length):
        for y in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)
            
z = length-2
for x in range(1,length):
        for y in range(1,length):
            regions[x,y,z] = region ## Only for the edge since the edge is "Forbidden"
            neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
            neighbours[0][0] = current_minimum; 
            neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
            current_minimum = potential_array[x,y,z]
            region = 1
            flood_region(neighbours, x, y, z, current_minimum, region)   
            
            
"""

         
"""
# Plotting the different heights stuff
heights[height_rise][1] = force
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import axes3d
ax = plt.axes()
ax.plot(heights[:,0], heights[:,1], 'ro')

"""
"""


#### Edge Start Point
# Index of minimum as a tupple
# np.unravel_index(np.argmin(potential_array, axis=None), potential_array.shape)

global_min_index = np.unravel_index(np.argmin(potential_array, axis=None), potential_array.shape)
start_point = [global_min_index[0],global_min_index[1],global_min_index[2]]
print("Start point = ", start_point)
x = start_point[0]
y = start_point[1]
z = start_point[2]
current_minimum = potential_array[x,y,z]
neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
neighbours[0][0] = current_minimum; 
neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
## Region?
region = 3
regions[x,y,z] = region
been[x,y,z] = True



####masked!!!
mx = ma.masked_array(potential_array, been)

np.unravel_index(np.argmin(mx, axis=None), mx.shape)
Out[121]: (23, 33, 1)

np.unravel_index(np.argmin(potential_array, axis=None), potential_array.shape)
Out[122]: (23, 49, 1)

"""

import vtk; import numpy as  np
# creating vti image file 
filename = "regions.vti"
imageData = vtk.vtkImageData()
imageData.SetDimensions(length, length, length )
imageData.SetOrigin( (-length+1)/2, (-length+1)/2, 0 )
if vtk.VTK_MAJOR_VERSION <= 5:
    imageData.SetNumberOfScalarComponents(1)
    imageData.SetScalarTypeToDouble()
else:
    imageData.AllocateScalars(vtk.VTK_DOUBLE, 1)
dims = imageData.GetDimensions()
# Fill every entry of the image data
for z in range(dims[2]):
    for y in range(dims[1]):
        for x in range(dims[0]):
            imageData.SetScalarComponentFromDouble(x, y, z, 0, new_regions[x,y,z])
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(filename)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()

   
            