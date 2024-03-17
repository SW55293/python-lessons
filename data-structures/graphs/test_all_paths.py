from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        stack = [(0,)]
        last_node = len(graph) - 1

        while stack:
            path = stack.pop()

            if path[-1] == last_node:
                result.append(path)

            for neighbors in graph[path[-1]]:
                stack.append(path + (neighbors,))
                
        return result
    
    # 
        # target = len(graph) - 1
        # paths = [[0]]
        # routes = []
# 
        # while paths:
            # path = paths.pop(0)
            # edges = graph[path[-1]]
# 
            # if not edges: 
                # continue
# 
            # for edge in edges:
                # if edge == target:
                    # routes.append(path+[edge])
                # else:
                    # paths = [path+[edge]] + paths
        # return routes 
def allPathsSourceTarget2(graph: List[List[int]]) -> List[List[int]]:
    result = []  # Storage for all the complete paths we find
    stack = [(0,)]  # Start with a path containing only the source node (0)
    last_node = len(graph) - 1  # The index of the target node

    while stack:  # As long as there are paths to explore
        path = stack.pop()  # Take a path from the stack

        if path[-1] == last_node:  # Did we reach the target?
            result.append(path)  # Yes! Add this path to the results

        for neighbor in graph[path[-1]]:  # Look at the neighbors of the last node in the path
            stack.append(path + (neighbor,))  # Extend the path by adding a neighbor 
                                              # and put it back on the stack

    return result 
'''
result = [] initializes a list to store all valid paths from source to target.
stack = [(0,)] initializes a stack with a tuple containing just the source node. Tuples are used to ensure immutability of paths.
while stack: keeps iterating until there are paths to explore.
path = stack.pop() takes the last path added to the stack to continue exploration.
If path[-1] == last_node, the path reached the target, and it's added to result.
for neighbors in graph[path[-1]]: iterates over all neighbors of the last node in the path, creating new paths by appending each neighbor.
stack.append(path + (neighbors,)) adds these new paths to the stack for further exploration
'''