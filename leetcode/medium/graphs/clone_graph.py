class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    #base case
    if not node:
            return node
    
    visited = {} # dictionary to store the cloned nodes. Will contain original(key) node and cloned(value) node
    def dfs(node):
        if node in visited:
            return visited[node]     # if node was already visited, return the corresponding cloned node
        
        cloned_node = Node(node.val) # create a new clone of the node that hasnt been visited
        visited[node] = cloned_node  # add the original node and its clone to the dictionary

        for n in node.neighbors:    # visit all neighbors of the original node
            cloned_node.neighbors.append(dfs(n)) # if the neighbors have not been visited then create the cloned node and append to the neighbors
    
    # list of the cloned node we are currently visiting. Otherwise, append the 
    # corresponding cloned node to the neighbors list.
        
        return cloned_node
    
    return dfs(node) # start DFS from the first node and return its clone









'''Explanation for dumb bitches
This code is a Python implementation of a depth-first search algorithm for cloning an undirected 
graph represented as a Node class. The Node class is assumed to have a value (stored in the val attribute)
and a list of neighbors (stored in the neighbors attribute), which contains other nodes that are directly
connected to the node.

The cloneGraph function takes a single argument node, which is the starting node of the graph to be cloned.
If the node argument is None, then the function simply returns None.

The function then initializes an empty dictionary called visited, which will be used to keep track of the 
nodes that have been visited during the depth-first search.

The dfs function is a recursive helper function that takes a single argument node, which is a node in the 
original graph. The function first checks if node has already been visited by looking up the node in the 
visited dictionary. If the node has already been visited, the function simply returns the cloned version 
of the node that was stored in the dictionary.

If the node has not been visited yet, the function creates a new cloned node with the same value as the 
original node, and adds it to the visited dictionary. The function then loops over the neighbors list of 
the original node and recursively calls dfs on each neighbor, appending the cloned version of the neighbor
to the neighbors list of the cloned node.

Finally, the cloneGraph function calls dfs with the node argument and returns the cloned node.



'''