from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            cloned = Node(node.val)
            visited[node] = cloned

            for n in node.neighbors:
                cloned.neighbors.append(dfs(n))
        
            return cloned
        
        return dfs(node)
        


# Creating a sample graph to test the cloneGraph function
# The graph is:
# 1 -- 2
# |    |
# 4 -- 3

entry_node = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

entry_node.neighbors = [node_2, node_4]
node_2.neighbors = [entry_node, node_3]
node_3.neighbors = [node_2, node_4]
node_4.neighbors = [entry_node, node_3]

solution = Solution()
cloned_graph = solution.cloneGraph(entry_node)

