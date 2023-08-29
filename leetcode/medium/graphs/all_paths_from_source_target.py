from typing import List

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    paths = [[0]]
    routes = []

    while paths:
        path = paths.pop(0)
        edges = graph[path[-1]]
        if not edges: 
            continue
        for edge in edges:
            if edge == target:
                routes.append(path+[edge])
            else:
                paths = [path+[edge]] + paths
    return routes 
        
'''
# Set the target node to the last node in the graph.
target = len(graph) - 1

# Initialize a list of paths, starting with just the path containing the starting node (node 0).
paths = [[0]]

# Initialize an empty list to store paths that reach the target node.
routes = []

# While there are paths to explore:
while paths:
    # Get the first path from the list of paths.
    path = paths.pop(0)
    
    # Get the edges (neighbors) of the last node in the current path.
    edges = graph[path[-1]]
    
    # If there are no edges, skip to the next iteration.
    if not edges:
        continue
    
    # For each edge from the last node:
    for edge in edges:
        # If the edge leads to the target node:
        if edge == target:
            # Append the path that reaches the target to the routes list.
            routes.append(path + [edge])
        else:
            # Otherwise, create a new path by extending the current path with the edge,
            # and add it to the beginning of the list of paths to explore.
            paths = [path + [edge]] + paths

# Return the list of paths that reach the target node.
return routes

'''


'''
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [4, 5],
    4: [5],
    5: []
}
In this example, the graph has nodes from 0 to 5. We want to find all 
paths from node 0 to node 5. Let's go step by step through the code execution:

target is set to 5 (last node).
paths is initialized with [[0]].
routes is an empty list.
The while loop starts.
First path [0] is popped from paths.
Edges of node 0 are [1, 2].
The first edge is 1.
Since 1 is not the target, a new path [0, 1] is added to paths.
The second edge is 2.
Since 2 is not the target, a new path [0, 2] is added to paths.
Next iteration of the loop:
paths becomes [[0, 1], [0, 2]].
Now, the path [0, 1] is popped from paths.
Edges of node 1 are [3, 4].
The first edge is 3.
Since 3 is not the target, a new path [0, 1, 3] is added to paths.
The second edge is 4.
Since 4 is not the target, a new path [0, 1, 4] is added to paths.
Next iteration of the loop:
paths becomes [[0, 2], [0, 1, 3], [0, 1, 4]].
The remaining paths are explored similarly until all possibilities are exhausted.
Finally, the paths that lead to the target node 5 ([0, 1, 3, 5] and [0, 2, 4, 5]) are added to the routes list.
The while loop finishes.
The routes list is returned, containing [[0, 1, 3, 5], [0, 2, 4, 5]].
The code essentially performs a breadth-first search (BFS) through the graph, maintaining a 
list of paths to explore. It continues to extend and explore new paths until reaching the target node, 
and then it collects the successful paths.


'''