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









