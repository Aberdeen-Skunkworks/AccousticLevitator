# Flood fill start

import numpy as np
"""
size = 17

test = np.zeros((size,size), dtype = float)
test_with_walls = np.pad(test, (1), 'constant', constant_values=(1))
test_with_walls[:, int(size/2)] =  1.0
test_with_walls[int(size/2), :] =  1.0

test_with_walls_after_fill = np.copy(test_with_walls)

def floodfill(matrix, x, y):
    #"hidden" stop clause - not reinvoking for numbers less than a value.
    if matrix[x][y] < 1:  
        matrix[x][y] = 2 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y)
        if y > 0:
            floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1)
            
floodfill(test_with_walls_after_fill, 1, 5 )
    
"""


############ Algorithm that has much less recursion ############
#def floodfill_3d(potential_array,x,y,z):
    

def floodfill_vertical(matrix, x, y, z):
    if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
        been[x][y][z] = True
        minimum = matrix[x][y]
        up = matrix[x][y+1]
        down = matrix[x][y-1]
        
        def flood_up(matrix, x, y):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix[x][y]
                up = matrix[x][y+1]
                if up >= minimum:
                    been[x][y][z] = True
                    flood_up(matrix, x, y+1)
        
        def flood_down(matrix, x, y):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix[x][y]
                down = matrix[x][y-1]
                if down >= minimum:
                    been[x][y][z] = True
                    flood_down(matrix, x, y-1)
                    
   
        if up >= minimum:
            flood_up(matrix, x, y+1)

        if down >= minimum:
            flood_down(matrix, x, y-1)




def floodfill_horizontal(matrix, x, y, z):
    if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
        been[x][y][z] = True
        minimum = matrix[x][y]
        right = matrix[x+1][y]
        left = matrix[x-1][y]
        
        def flood_right(matrix, x, y):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix[x][y]
                right = matrix[x+1][y]
                if right >= minimum:
                    been[x][y][z] = True
                    flood_right(matrix, x+1, y)
                    
                    
        def flood_left(matrix, x, y):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix[x][y]
                left = matrix[x-1][y]
                if left >= minimum:
                    been[x][y][z] = True
                    flood_left(matrix, x-1, y)
                    
        if right >= minimum:
            flood_right(matrix, x+1, y)     
            
        if left >= minimum:
            flood_left(matrix, x-1, y)
            



def floodfill_through(matrix_3d, x, y, z):
    if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
        been[x][y][z] = True
        minimum = matrix_3d[x][y][z]
        through = matrix_3d[x][y][z+1]
        back = matrix_3d[x][y][z-1]
        
        def flood_through(matrix_3d, x, y, z):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix_3d[x][y][z]
                through = matrix_3d[x][y][z+1]
                if through >= minimum:
                    been[x][y][z] = True
                    flood_through(matrix_3d, x, y, z+1)
                    
        def flood_back(matrix_3d, x, y, z):
            if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
                minimum = matrix_3d[x][y][z]
                back = matrix_3d[x][y][z-1]
                if back >= minimum:
                    been[x][y][z] = True
                    flood_back(matrix_3d, x, y, z-1)
                    
        if through >= minimum:
            flood_through(matrix_3d, x, y, z+1)     
            
        if back >= minimum:
            flood_back(matrix_3d, x, y, z-1)

length = len(potential_array)
been = np.full((length, length, length), False, dtype=bool)

middle = int((length-1)/2)
layer_1 = potential_array[:,:,middle]

floodfill_vertical(layer_1,middle,middle, middle)  
floodfill_horizontal(layer_1,middle,middle, middle)  

for itterations in range(5):
    for z in range(length):
        for row in range(length):
            for column in range(length):
                if been[row,column,z]:
                    layer = potential_array[:,:,z]
                    floodfill_horizontal(layer, row, column, z)
                    floodfill_vertical(layer, row, column, z)
                    floodfill_through(potential_array, row, column, z)




"""

      
def floodfill_3d(matrix, x, y, z):
    #"hidden" stop clause - not reinvoking for numbers less than a value.
    if matrix[x][y][z] < 1:  
        matrix[x][y][z] = 2 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill_3d(matrix,x-1,y, z)
        if x < len(matrix[y]) - 1:
            floodfill_3d(matrix,x+1,y, z)
        if y > 0:
            floodfill_3d(matrix,x,y-1, z)
        if y < len(matrix) - 1:
            floodfill_3d(matrix,x,y+1, z)
        if z > 0:
            floodfill_3d(matrix,x,y, z-1)
        if z < len(matrix) - 1:
            floodfill_3d(matrix,x,y, z+1)




test_3d = np.zeros((size, size, size), dtype = float)
test_3d_with_walls = np.pad(test_3d, (1), 'constant', constant_values=(1))
test_3d_with_walls[:, int(size/2)] =  1.0
test_3d_with_walls[int(size/2), :] =  1.0

test_3d_with_walls_after_fill = np.copy(test_3d_with_walls)

floodfill_3d(test_3d_with_walls_after_fill, 1, 3 ,4)

npoints = size + 2
"""

import vtk; import numpy as  np
# creating vti image file 
filename = "3d_test.vti"
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
            imageData.SetScalarComponentFromDouble(x, y, z, 0, been[x,y,z])
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName(filename)
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInputConnection(imageData.GetProducerPort())
else:
    writer.SetInputData(imageData)
writer.Write()
























