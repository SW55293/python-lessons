from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:
            return []
        
        queue = [root]
        
        while queue:
            q_len = len(queue)
            # keeps track of the values in the current level
            sublist = []
            
            for _ in range(q_len):
                node = queue.pop(0)  # Remove the first element from the queue
                sublist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print(sublist)
        


root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
solution = Solution()
solution.levelOrder(root)
