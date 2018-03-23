    
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


class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
       
        
def find_highest_parent(idx):
    while regions_list[idx][0] != None:
        idx = regions_list[idx][0]
    return idx






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
        regions_list.append([None, []])
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
            regions_list.append([None, unique_region_parents])
            regions[sorted_indices[pixle]] = region
            for len_region_parents in range(len(unique_region_parents)):
                regions_list[unique_region_parents[len_region_parents]][0] = region
            region += 1
        


