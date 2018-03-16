import numpy as np

length = len(potential_array)
regions = np.full((length, length, length), 0, dtype=int)



start_point = [int((length-1)/2),int((length-1)/2),int((length-1)/2)]
x = start_point[0]
y = start_point[1]
z = start_point[2]
trap_value = potential_array[x,y,z]


run = True
while run == True:
    if x > 0 and x < length-1 and y > 0 and y < length-1 and z > 0 and z < length-1:
        
        # Check which edge is minimum
        been = np.full((length, length, length), False, dtype=bool)
        edges = np.full((length, length, length), np.max(potential_array)+10, dtype=float)
        been[x,y,z] = True
        been[x-1,y,z] = True; edges[x-1,y,z] = potential_array[x-1,y,z]
        been[x+1,y,z] = True; edges[x+1,y,z] = potential_array[x+1,y,z]
        been[x,y+1,z] = True; edges[x,y+1,z] = potential_array[x,y+1,z]
        been[x,y-1,z] = True; edges[x,y-1,z] = potential_array[x,y-1,z]
        been[x,y,z+1] = True; edges[x,y,z+1] = potential_array[x,y,z+1]
        been[x,y,z-1] = True; edges[x,y,z-1] = potential_array[x,y,z-1]
        
        run = False
            
        
        
        
        
        
        
            