from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree_ascii(self, root, level=0):
        if root:
            self.print_tree_ascii(root.right, level + 1)
            print(" " * 4 * level + "--> " + str(root.val))
            self.print_tree_ascii(root.left, level + 1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        left_side = self.maxDepth(root.left) + 1
        right_side = self.maxDepth(root.right) + 1


        return max(left_side,right_side)

    
root = TreeNode(20)

root.left = TreeNode(10)
# root.left.left = TreeNode(8)
# root.left.right = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.left.left = TreeNode(6)

root.right = TreeNode(30)
# root.right.left = TreeNode(31)
# root.right.right = TreeNode(40)

solution = Solution()
start = solution.maxDepth(root)
print(start)
# root.PrintTree()
root.print_tree_ascii(root)