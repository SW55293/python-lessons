from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def PrintTree(self):
      # if self.left is True, if theres a left subtree then print
      print(self.val)
      if self.left:
         self.left.PrintTree()

      if self.right:
         self.right.PrintTree()

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
  
        left_height = self.maxDepth(root.left) + 1
        right_height = self.maxDepth(root.right) + 1
        
        return max(left_height, right_height)

    
root = TreeNode(10)

root.left = TreeNode(9)
root.left.left = TreeNode(8)
root.right = TreeNode(15)

solution = Solution()
start = solution.maxDepth(root)
root.PrintTree()