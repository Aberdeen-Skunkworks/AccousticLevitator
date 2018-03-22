

def nbhood_bad(i_d, length):
    """ 1 dimentional neighbourhood pixle finder: Takes in id location and 
        length of array and outputs list of neighbours"""
    
    list_of_nbhood_pixles = []
    x = int(i_d % length)
    if i_d < 0 or i_d >= length:
        print("Out of range!")
    else:
        if i_d < length-1:
            list_of_nbhood_pixles.append(int(x + 1))
            
        if i_d > 0:
             list_of_nbhood_pixles.append(int(x - 1))

    
    return list_of_nbhood_pixles


def test_nbhood():
    
    test_array = [2,5,2,7,5,2,3,1]
    
    id_1 = 5
    length_1 = len(test_array)
    
    test1 = nbhood_bad(id_1, length_1)
    
    if test1 == [6,4]:
        print("Test Passed")
    else:
        print("Test Failed")
        
    
    id_2 = 7
    length_2 = len(test_array)
    
    test2 = nbhood_bad(id_2, length_2)

    if test2 == [6]:
        print("Test Passed")
    else:
        print("Test Failed")
        

    id_3 = 0
    length_3 = len(test_array)
    
    test3 = nbhood_bad(id_3, length_3)

    if test3 == [1]:
        print("Test Passed")
    else:
        print("Test Failed")
    
    
    id_4 = -5
    length_4 = len(test_array)
    
    test4 = nbhood_bad(id_4, length_4)

    if test4 == []:
        print("Test Passed (Error expected = Out of range!)")
    else:
        print("Test Failed")
        

def _2d_nbhood(i_d, length):
    """ 2 dimentional neighbourhood pixle finder: Takes in id location and 
        length of array and outputs list of neighbours"""
    
    list_of_nbhood_pixles = []
    x = int(i_d % length)
    y = int((i_d / length) %length)
    
    
    if i_d < 0 or i_d >= length**2:
        print("Out of range!")
    else:
        # Four Neighbours
        if x > 0 and x < length-1 and y > 0 and y < length-1:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
            
        # Three Neighbours
        elif x == 0 and y > 0 and y < length-1:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
            
        elif x == length-1 and y > 0 and y < length-1:
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
          
        elif y == 0 and x > 0 and x < length-1:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            
        elif y == length-1 and x > 0 and x < length-1:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
        
        # Two Neighbours
        elif x == 0 and y == 0:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            
        elif x == 0 and y == length-1:
            list_of_nbhood_pixles.append(int( x + 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
            
        elif x == length-1 and y == 0:
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y + 1) ))
            
        elif x == length-1 and y == length-1:
            list_of_nbhood_pixles.append(int( x - 1 + length * y ))
            list_of_nbhood_pixles.append(int( x + length * (y - 1) ))
            
    
    return list_of_nbhood_pixles     
        
       



 

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
        
    








"""
from anytree import Node, RenderTree
number = 1

region = Node(["reg" + str(number)] )
print(region)

number = 2
region_2 = Node(["reg" + str(number)] , parent = region )
print(region)


from anytree.exporter import DotExporter
DotExporter(region).to_dotfile("region.dot")
"""




