# Graph can be represnted in 3 ways

# Edge List
graph = [[0,2], [2,3], [2,1], [1,3]]
# It shows simply connection to the nodes
# that 0 is connected to 2, 2 is connected to 3.


# Adjacency/ Adjacent List

# Using list
graph = [[2], [2,3], [0,1,3], [1,2]]
# Here index denotes the nodes
# Node 0 has connection with node 2
# Node 2 has connection with nodes 0,1,3

# Using maps
graph = {
    0: [2],
    1: [2,3],
    2: [0,1,3],
    3: [1,2] 
}


# Adjacent Matrix

# Using lists
graph = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0],
]
# It represents the same connections but with different way.
# If the graph is weighted, then we can use the weights instead of 1.

# Using maps
graph = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0]
}
