# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#class Solution(object):
def invertTree(self, root):
        """
        :type root: TreeNode
        :return type: TreeNode
        """
        #base case when you get to a node with no left or right
        #children
        if root is None:
            return root 

        temp_left = root.left
        root.left = root.right
        root.right = temp_left

        self.invertTree(root.left)
        self.invertTree(root.right)

tree = [4,2,7,1,3,6,9]
print(invertTree(tree))