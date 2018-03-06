# Flood fill start

import numpy as np
size = 21

test = np.zeros((size,size), dtype = float)
test_with_walls = np.pad(test, (1), 'constant', constant_values=(1))
test_with_walls[:, int(size/2)] =  1.0
test_with_walls[int(size/2), :] =  1.0

def floodfill(matrix, x, y):
    #"hidden" stop clause - not reinvoking for "c" or "b", only for "a".
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
            

floodfill(test_with_walls, 1, 5 )