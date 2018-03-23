    
import numpy as np

def coord_to_idx(coord, dim):
    idx = coord[-1]
    for i in range(1,len(dim)):
        idx = idx * dim[-i-1] + coord[-i-1]
    return idx


def idx_to_coord(idx, dim):
    coord = []
    for i in range(len(dim)):
        coord.append(idx % dim[i])
        idx = int (idx / dim[i])
    return coord


def nbhood(idx, dim):
    centre = idx_to_coord(idx, dim)
    nbs = []
    for i in range(len(dim)):
        if centre[i] > 0:
            nbcoord = list(centre)
            nbcoord[i] = centre[i]-1
            nbs.append(coord_to_idx(nbcoord, dim))
        if centre[i] < (dim[i]-1):
            nbcoord = list(centre)
            nbcoord[i] = centre[i]+1
            nbs.append(coord_to_idx(nbcoord, dim))
    return nbs

        
def find_highest_parent(idx):
    while regions_list[idx][0] != None:
        idx = regions_list[idx][0]
    return idx


def find_edges(dim): # As array [dimention,dimention...] (Finds index of edges of any dimentional array) 
    if len(dim) > 1:
        dim = tuple(dim)
    edges = []
    smaller_array = np.full((np.subtract(dim,2)), False, dtype=bool)
    same_sized_with_edges = np.pad(smaller_array, (1), 'constant', constant_values=(True))
    flat_version = same_sized_with_edges.flatten()
    for i in range(len(flat_version)):
        if flat_version[i] == True:
            edges.append(i)
    return edges


def tests():
    test_1d_array = [1,2,3,4,5,4,3,4,5,6,5,4,3,2,1,2,3,2,1,0]
    #test_1d_array = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0] ## Single Hill
    #test_1d_array = [10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10] ## Single vally
    
    
    coords = coord_to_idx((0,0),[2,2])
    if coords != 0:
        raise Exception("Failed coord_to_idx test 1")
    if isinstance(coords, int) != True:
        raise Exception("Failed coord_to_idx test 2")
    coords2 = coord_to_idx((1,1),[2,2])
    if coords2 != 3:
        raise Exception("Failed coord_to_idx test 3")    
    if isinstance(coords2, int) != True:
        raise Exception("Failed coord_to_idx test 4")


    index = idx_to_coord(0, [2,2])
    if index != [0,0]:
        raise Exception("Failed idx_to_coord test 1")
    if len(index) != 2:
        raise Exception("Failed idx_to_coord test 2")
    index2 = idx_to_coord(3, [2,2])
    if index2 != [1,1]:
        raise Exception("Failed idx_to_coord test 3")
    if len(index2) != 2:
        raise Exception("Failed idx_to_coord test 4")
        
        
    nhood = nbhood(0, [5])
    if len(nhood) != 1:
        raise Exception("Failed nbhood test 1")
    if nhood != [1]:
        raise Exception("Failed nbhood test 2")
    nhood2 = nbhood(1, [5])
    if len(nhood2) != 2:
        raise Exception("Failed nbhood test 3")
    if nhood2 != [0,2]:
        raise Exception("Failed nbhood test 4")
    nhood3 = nbhood(4, [5])
    if len(nhood3) != 1:
        raise Exception("Failed nbhood test 5")
    if nhood3 != [3]:
        raise Exception("Failed nbhood test 6")        

    edges = find_edges((3,3))
    if 4 in edges:
        raise Exception("Failed find_edges test 1")
    if len(edges) != 8:
        raise Exception("Failed find_edges test 2")
    print("All Tests Passed!")
    
    

tests()



test_1d_array = [1,2,3,4,5,4,3,4,5,6,5,4,3,2,1,2,3,2,1,0]
#test_1d_array = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0] ## Single Hill
#test_1d_array = [10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10] ## Single vally


regions = [-1] * len(test_1d_array)
regions_list = []

dim = (len(test_1d_array))
sorted_indices = []

sorted_indices = list(range(len(test_1d_array)))
sorted_indices.sort(key=lambda idx : test_1d_array[idx])

region = 0 # Starts at zero

for pixle in range(dim):
    neighbours = nbhood(sorted_indices[pixle],[dim])
    assigned = [False] * len(neighbours)

    for num_nb in range(len(neighbours)):
        if regions[neighbours[num_nb]] != -1:
            assigned[num_nb] = True
    
    if not any(assigned): # Check if there is zero assigned neighbours
        regions[sorted_indices[pixle]] = region
        regions_list.append([None, [],True])
        region += 1
        
    elif sum(map(bool, assigned)) == 1: # Checks if there is only 1 assigned neighbour
        for num_nb in range(len(neighbours)):
            if regions[neighbours[num_nb]] != -1:
                set_to_this_region = find_highest_parent(regions[neighbours[num_nb]])
                regions[sorted_indices[pixle]] = set_to_this_region
    
    else: # multiple assigned neighbours
        adj_regions = []
        for num_nb in range(len(neighbours)):
            adj_regions.append(regions[neighbours[num_nb]])
        region_parents = list(map(find_highest_parent, adj_regions))
        unique_region_parents = list(set(region_parents))
        if len(unique_region_parents) == 1:
            regions[sorted_indices[pixle]] = unique_region_parents[0]
        else:
            regions_list.append([None, unique_region_parents,True])
            regions[sorted_indices[pixle]] = region
            for len_region_parents in range(len(unique_region_parents)):
                regions_list[unique_region_parents[len_region_parents]][0] = region
            region += 1
        


edges = find_edges([dim])
inside_regions_list = []
edge_regions = []

for i in range(len(edges)):
    edge_regions.append(regions[edges[i]])






