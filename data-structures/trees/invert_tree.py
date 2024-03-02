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
    
    def print_tree_ascii(self, root, level=0):
        if root:
            self.print_tree_ascii(root.right, level + 1)
            print(" " * 4 * level + "--> " + str(root.val))
            self.print_tree_ascii(root.left, level + 1)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

       

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    
root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(7)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)

solution = Solution()
start = solution.invertTree(root)
# root.PrintTree()
root.print_tree_ascii(root)