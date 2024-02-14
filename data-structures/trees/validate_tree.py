from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val} '
    

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, node, left_val, right_val):
        print(f'Node = {str(node)}')
        if node is None:
            return True
        
        print(left_val, node.val, right_val)
        print()

        if not (node.val > left_val and node.val < right_val):
            return False

        # if not left_val < node.val < right_val:
        #     return False
        
        return self.checkBST(node.left, left_val, node.val) and self.checkBST(node.right, node.val, right_val)
'''
Print statement output
-inf 20 inf
-inf 10 20
-inf 9 10
10 11 20
20 30 inf
20 22 30
30 40 inf
'''    

# Test case 1: A valid BST
root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(9)
root.left.right = TreeNode(11)
root.right = TreeNode(30)
root.right.left = TreeNode(22)
root.right.right = TreeNode(40)


# Test case 2: An invalid BST (right child of the left subtree has a value greater than the root)
# root2 = TreeNode(5)
# root2.left = TreeNode(1)
# root2.right = TreeNode(4)
# root2.right.left = TreeNode(3)
# root2.right.right = TreeNode(6)

# # Test case 3: An empty tree
# root3 = None

# Instantiate Solution and run tests
solution = Solution()
solution.isValidBST(root)

# print("Test case 1 - Expected: True, Actual:", solution.isValidBST(root1))
# print("Test case 2 - Expected: False, Actual:", solution.isValidBST(root2))
# print("Test case 3 - Expected: True, Actual:", solution.isValidBST(root3))

