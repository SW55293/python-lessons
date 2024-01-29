# Pattern          = Recursion
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input 1     = Tree Node
Return Type = Tree Node
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root):
        """
        :type root: TreeNode
        :return type: TreeNode
        """
        #base case when you get to a node with no left or right
        #children
        if root is None:
            return None
        
        temp_left = root.left
        root.left = root.right
        root.right = temp_left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# The return value of root is not just 1 variable/value like an int ora string
# the return value is a whole function which contains val, left, and right. Each one of those 
# could equal anything from a string to an int or float

'''
Input
root = [4,2,7,1,3,6,9]
Output = [4,7,2,6,9,1,3]
Expected = [4,7,2,9,6,3,1]

---------------------------

root = TreeNode{val: 1, left: None, right: None}
root = TreeNode{val: 3, left: None, right: None}
root = TreeNode{val: 1, left: None, right: None}
TreeNode{val: 1, left: None, right: None}
root = TreeNode{val: 3, left: None, right: None}
TreeNode{val: 3, left: None, right: None}
root = TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
temp = TreeNode{val: 1, left: None, right: None}
root.left = TreeNode{val: 3, left: None, right: None}
root.right = TreeNode{val: 1, left: None, right: None}
root = TreeNode{val: 6, left: None, right: None}
root = TreeNode{val: 9, left: None, right: None}
root = TreeNode{val: 6, left: None, right: None}
TreeNode{val: 6, left: None, right: None}
root = TreeNode{val: 9, left: None, right: None}
TreeNode{val: 9, left: None, right: None}
root = TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}
temp = TreeNode{val: 6, left: None, right: None}
root.left = TreeNode{val: 9, left: None, right: None}
root.right = TreeNode{val: 6, left: None, right: None}
root = TreeNode{val: 3, left: None, right: None}
root = TreeNode{val: 1, left: None, right: None}
root = TreeNode{val: 3, left: None, right: None}
TreeNode{val: 3, left: None, right: None}
root = TreeNode{val: 1, left: None, right: None}
TreeNode{val: 1, left: None, right: None}
root = TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}
temp = TreeNode{val: 3, left: None, right: None}
root.left = TreeNode{val: 1, left: None, right: None}
root.right = TreeNode{val: 3, left: None, right: None} TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
root = TreeNode{val: 9, left: None, right: None}
root = TreeNode{val: 6, left: None, right: None}
root = TreeNode{val: 9, left: None, right: None}
TreeNode{val: 9, left: None, right: None}
root = TreeNode{val: 6, left: None, right: None}
TreeNode{val: 6, left: None, right: None}
root = TreeNode{val: 7, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 6, left: None, right: None}}
temp = TreeNode{val: 9, left: None, right: None}
root.left = TreeNode{val: 6, left: None, right: None}
root.right = TreeNode{val: 9, left: None, right: None}
TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}
root = TreeNode{val: 4, left: TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}}
temp = TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
root.left = TreeNode{val: 7, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 9, left: None, right: None}}
root.right = TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}

'''