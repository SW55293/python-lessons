from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def remove(self, root, new_val):
        if root is None:
            return root

        if root.val < new_val:
            self.remove(root.left, new_val)
        elif root.val > new_val:
            self.remove(root.right, new_val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
        
        # get inorder successor from right side
            successor = getSuccessor(root.right)
    
    def getSuccessor(right_val):
        current = right_val
        while current:
            current = current.left
        return current.val

        ''' Cases
        - No nodes in tree
        - The value isnt in the tree
        - Node to delete has only 1 child
            - Has only left child
            - Has only right child
        - Node to delete has 2 children
        '''
root = TreeNode(10)

root.left = TreeNode(9)
root.left.left = TreeNode(8)
root.right = TreeNode(15)