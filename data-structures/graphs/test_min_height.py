from typing import List
# BFS (Topological)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge case where the nodes are already reduced to the smallest possible set
        if n <= 2:
            return [i for i in range(n)] #returns the values from 0 to n

        # represent the nodes and edges in a graph using a hashmap
        # [0 -> 1, 2]
        # [1 -> 0]
        # ...etc
        # this creates a dictionary with nodes on one column from 0 to n
        # and a list of all the other nodes they are connected to
        graph = {num_nodes: [] for num_nodes in range(n)}

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # populate the first leaf layer
        leaves = []
        for node in graph:
            # leaves will only have one connection
            if len(graph[node]) == 1:
                leaves.append(node)

        # outer while loop runs until only two nodes left as leaves are removed
        while n > 2:
            n -= len(leaves)
            # store next layer of leaves which will be constructed in inner while loop
            next_leaves_layer = []
            while leaves:
                leaf = leaves.pop()
                # 1. remove leaf-neighbour edges
                neighbour = graph[leaf].pop()
                neighbour_connections = graph[neighbour]
                neighbour_connections.remove(leaf)
                # 2. create new leaf layer from neighbour
                if len(neighbour_connections) == 1:
                    next_leaves_layer.append(neighbour)
            # reassign next layer to 'leaves'
            leaves = next_leaves_layer
        
        return leaves