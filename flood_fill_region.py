
import numpy as np; import constants; import numpy.ma as ma
# Flooding filling regions by slowly rising up in values form a start point until the value does down
# somewhere then the region is full and that value is the stregnth of the trap.


# ---- For Niall's reference 
## Adding new value to list = np.append(neighbours, new_list, axis=0)
## Deleting min from list = np.delete(neighbours,np.argmin(neighbours[:,0]),0)



potential_array = u_with_gravity_nano
potential_array = np.pad(potential_array, (1), 'constant', constant_values=(np.max(potential_array))) # Padding the edge with max of array
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

focus_as_index = int(((constants.npoints-1)/ 2))
x_potential = potential_array[ :               , focus_as_index , focus_as_index]
x_potential_middle = x_potential[(focus_as_index-10):(focus_as_index+10)]
y_potential = potential_array[ focus_as_index  , :              , focus_as_index]
y_potential_middle = y_potential[(focus_as_index-10):(focus_as_index+10)]
z_potential = potential_array[ focus_as_index  , focus_as_index , :             ]
z_potential_middle = z_potential[(focus_as_index-10):(focus_as_index+10)]


def flood_region(neighbours, x, y, z, current_minimum, region):
    
    run = True
    while run == True:
        if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
            neighbours = np.delete(neighbours,np.argmin(neighbours[:,0]),0)
            if been[x+1,y,z] == True: # x+1
                pass
            else:
                regions[x+1,y,z] = region
                been[x+1,y,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x+1,y,z]
                new_list[0][1] = x+1; new_list[0][2] = y; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x-1,y,z] == True: # x-1
                pass
            else:
                regions[x-1,y,z] = region
                been[x-1,y,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x-1,y,z]
                new_list[0][1] = x-1; new_list[0][2] = y; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y+1,z] == True: # y+1
                pass
            else:
                regions[x,y+1,z] = region
                been[x,y+1,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y+1,z]
                new_list[0][1] = x; new_list[0][2] = y+1; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y-1,z] == True: # y-1
                pass
            else:
                regions[x,y-1,z] = region
                been[x,y-1,z] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y-1,z]
                new_list[0][1] = x; new_list[0][2] = y-1; new_list[0][3] = z;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y,z+1] == True: # z+1
                pass
            else:
                regions[x,y,z+1] = region
                been[x,y,z+1] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y,z+1]
                new_list[0][1] = x; new_list[0][2] = y; new_list[0][3] = z+1;
                neighbours = np.append(neighbours, new_list, axis=0)
                
            if been[x,y,z-1] == True: # z-1
                pass
            else:
                regions[x,y,z-1] = region
                been[x,y,z-1] = True
                new_list = np.zeros((1,4))
                new_list[0][0] = potential_array[x,y,z-1]
                new_list[0][1] = x; new_list[0][2] = y; new_list[0][3] = z-1;
                neighbours = np.append(neighbours, new_list, axis=0)
            
            if len(neighbours) == 0:
                #print("Skipped as there are no neighbours for this region")
                run = False
            else:
                new_minimum_id = np.argmin(neighbours[:,0])
                new_minimum    = neighbours[new_minimum_id][0]
                
                if new_minimum >= current_minimum:
                    x = int(neighbours[new_minimum_id][1])
                    y = int(neighbours[new_minimum_id][2])
                    z = int(neighbours[new_minimum_id][3])
                    regions[x,y,z] = region
                    current_minimum = new_minimum
    
                else:
                    #print("Stopped since the boundary has been found")
                    run = False
        
        else:
            #print("Reached the edge of the box")
            run = False


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
sorted_size_of_regions = np.zeros((np.max(regions),2)) # Format = [number of gridpoints, region]
for number_of_region in range(np.max(regions)):
    number_of_gridpoints = list(regions.flatten()).count(number_of_region)
    sorted_size_of_regions[number_of_region][0] = number_of_gridpoints; 
    sorted_size_of_regions[number_of_region][1] = number_of_region; 
    
sorted_size_of_regions = np.sort(sorted_size_of_regions, axis=0)
"""






#### Middle Start Point
"""
start_point = [int(np.argmin(x_potential_middle)+(length-1-20)/2),int(np.argmin(y_potential_middle)+(length-1-20)/2),int(np.argmin(z_potential_middle)+(length-1-20)/2)]
print("Start point = ", start_point)
x = start_point[0]
y = start_point[1]
z = start_point[2]
current_minimum = potential_array[x,y,z]
neighbours = np.zeros((1,4)) # Format: neighbours[Value, X, Y, Z]
neighbours[0][0] = current_minimum; 
neighbours[0][1] = x; neighbours[0][2] = y; neighbours[0][3] = z;
## Region?
region = 1
regions[x,y,z] = region
been[x,y,z] = True




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
            imageData.SetScalarComponentFromDouble(x, y, z, 0, regions[x,y,z])
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(filename)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()

        
        
        
            