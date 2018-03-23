    
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


def find_edges_mcb():    ### Creates duplicates in coeners and edges
    dimensions = [3,3]
    d = len(dimensions)
    #Loop over the dimensions whose faces you are collecting
    edges=[]
    for d1 in range(d):
       #Calculate a list of the dimensions you will iterate over
       facedims=[(d1+a) % d for a in range(1,d)]
    
       #Loop over all face cells
       #This is the coordinate of the face cell you are working on
       print("dim = ",d1)
       face_coord = [0]*d
       while True:
           print(face_coord)
           edge_cell = [0]*d
           for di in range(d-1):
               edge_cell[facedims[di]] = face_coord[di]
           edge_cell[d1] = 0
           edges.append(edge_cell)
           edge_cell[d1] = dimensions[d1]-1
           edges.append(edge_cell)
    
           #This is just rollover math for integers
           face_coord[0] = face_coord[0] + 1
           for di in range(0,d-1):
               if face_coord[di] >= dimensions[facedims[di]]:
                   face_coord[di] = 0
                   face_coord[di+1] += 1
           if face_coord[d-1] > 0:
               break


def set_all_parents_false(index):
    regions_list[index][2] = False
    if regions_list[index][0] != None:
        set_all_parents_false(regions_list[index][0])
    

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
    
tests() ## Run all tests  


# -------------------------------- Input data --------------------------------

test_1d_array_1 = [1,2,3,4,5,4,3,4,5,6,5,4,3,2,1,2,3,2,1,0]
test_1d_array_2 = [10.1,9,10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,3,2,1,2,3,4,5,6,7,8,9,10,9,10.1]
test_1d_array_3 = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0] ## Single Hill
test_1d_array_4 = [10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10] ## Single vally

test_2d_array_1 = [5.1,5.2,5.3,5.4,5.5,5.6,3.1,3.2,3.3,5.7,5.8,3.4,4.5,3.5,5.9,5.11,3.6,3.7,3.8,5.12,5.13,5.14,5.15,5.16,5.17]## 5 by 5


flat_array = test_big.flatten()      ## Input array
dim = [61,61]         ## Shape of input array [length, length, length].. so on

# ----------------------------------------------------------------------------


regions = [-1] * len(flat_array)
regions_list = []
length = len(flat_array)
sorted_indices = []
sorted_indices = list(range(len(flat_array)))
sorted_indices.sort(key=lambda idx : flat_array[idx])
region = 0 # Starts at zero

for pixle in range(length):
    neighbours = nbhood(sorted_indices[pixle],dim)
    assigned_neighbour = []
    
    for num_nb in range(len(neighbours)):
        if regions[neighbours[num_nb]] != -1:
            assigned_neighbour.append(regions[neighbours[num_nb]])
    unique_assigned_neighbour = list(set(assigned_neighbour))
            
    if len(unique_assigned_neighbour) == 0: # Check if there is zero assigned neighbours
        regions[sorted_indices[pixle]] = region
        regions_list.append([None, [],True])
        region += 1
        
    elif len(unique_assigned_neighbour) == 1: # Checks if there is only 1 assigned neighbour
        set_to_this_region = find_highest_parent(unique_assigned_neighbour[0])
        regions[sorted_indices[pixle]] = set_to_this_region
    
    else: # multiple assigned neighbours
        adj_regions = []
        for num_nb in range(len(neighbours)):
            if regions[neighbours[num_nb]] != -1:
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
        


edges = find_edges(dim)
inside_regions_list = []
edge_regions = []
highest_intetnal_parents = []

for i in range(len(edges)):
    edge_regions.append(regions[edges[i]])

for i in range(len(edge_regions)):
    set_all_parents_false(edge_regions[i])
    
for i in range(region):
    if regions_list[i][2] == True and regions_list[regions_list[i][0]][2] == False:
        highest_intetnal_parents.append(i)





# ------------- Exporting Tree To Dot File - Use Graphviz To View -------------
# - number - = Inside     number  = Outside

from anytree import Node

def find_children_add_to_dict(index):
    children = regions_list[index][1]
    for i in range(len(children)):
        if regions_list[children[i]][2] == True:
            nodes[children[i]] = Node("- "+str(children[i])+" -", parent = nodes[index])
            find_children_add_to_dict(children[i])
        elif regions_list[children[i]][2] == False:
            nodes[children[i]] = Node(str(children[i]), parent = nodes[index])
            find_children_add_to_dict(children[i])
    
nodes = dict()
root_node  = find_highest_parent(0)
nodes[root_node] = Node("Region "+str(root_node)+" = Root", parent = None,)
find_children_add_to_dict(root_node)

from anytree.exporter import DotExporter
DotExporter(nodes[root_node]).to_dotfile("tree.dot")
















