from typing import List
# BFS (Topological)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge case where the nodes are already reduced to the smallest possible set
        if n <= 2:
            return [i for i in range(n)] #returns the values from 0 to n

       
        neighbors = [set() for _ in range(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        # Find initial leaf nodes
        leaves = [i for i in range(n) if len(neighbors[i]) == 1]

        # Repeatedly remove leaves layer by layer
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                temp = neighbors[leaf].pop()  # The only neighbor of the leaf
                neighbors[temp].remove(leaf) #remove the leaf that was popped from the dict/list of nodes

                if len(neighbors[temp]) == 1:
                    new_leaves.append(temp)
            leaves = new_leaves

        return leaves  # The remaining nodes are the roots of MHTs
   
n = 4
edges = [[1,0],[1,2],[1,3]]
sol = Solution()

answer = sol.findMinHeightTrees(n, edges)
print(answer)

'''
Example output for neighbors and for loop code

>>> n = 4
>>> edges = [[1,0],[1,2],[1,3]]
>>> neighbors = [set() for _ in range(n)]
>>> for u, v in edges:
...     neighbors[u].add(v)
...     neighbors[v].add(u)
... 
>>> print(neighbors)
[{1}, {0, 2, 3}, {1}, {1}]
>>> 

'''
#graph = {x:[] for x in range(n)}
#for u, v in edges:
#    neighbors[u].append(v)
#    neighbors[v].append(u)
# represent the nodes and edges in a graph using a hashmap
# [0 -> 1, 2]
# [1 -> 0]
# ...etc
# this creates a dictionary with nodes on one column from 0 to n
# and a list of all the other nodes they are connected to



