class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # print(root)
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, node, min_val, max_val):

        if node is None:
            return True

        print(node.left)
        if node.val <= min_val or node.val >= max_val:
            return False

        return self.checkBST(node.left, min_val, node.val) and self.checkBST(node.right, node.val, max_val)


# the left side has to be less than the it's root val but greater than negative infinity
# the right side has to be greater than it's root value but less than infinity

def test_isValidBST():
    tree = TreeNode()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(20)
    assert tree.isValidBST()

if __name__ == "__main__":
    test_isValidBST()



# Construct the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


# Good example
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    def checkBST(self, node, left_val, right_val):
        if node is None:
            return True
        
        print(left_val, node.val, right_val)

        if not (node.val > left_val and node.val < right_val):
            return False

        # if not left_val < node.val < right_val:
        #     return False
        
        return self.checkBST(node.left, left_val, node.val) and self.checkBST(node.right, node.val, right_val)
    

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








# Example for
'''

        5
       / \
      3   7
     / \ / \
    2  4 6  8



In our example, when we call checkBST(root, float('-inf'), float('inf')), the following steps will be executed:

Start at thr root, value = 5 -> The current node is not None, so we proceed.

The value of the current node (5) is not less than or equal to negative infinity or greater than or equal to positive infinity, so we proceed.

Recursive call: checkBST(node.left, min_val, node.val)
Check left side -> node val 3
node.left is the node with value 3.
min_val remains negative infinity.
max_val becomes 5 (value of the current node).
We go to the left subtree.
Repeat steps 1-3 for the left subtree.
--------
Recursive call: checkBST(node.left, min_val, node.val)
Check left side -> node val 2
node.left is the node with value 2.
min_val remains negative infinity.
max_val becomes 3 (value of the current node).
We go to the left subtree.
The current node is not None (value is 2), so we proceed.
The value of the current node (2) is not less than or equal to negative infinity or greater than or equal to
3, so we proceed.
Both the left and right subtrees of this node are None, so we return True.
--------

We go back to the previous recursive call (step 5).

The left subtree is a valid BST, so we proceed to the right subtree.
--------

Recursive call: checkBST(node.right, node.val, max_val)
Check lefts right side -> node val 4
node.right is the node with value 4.
min_val becomes 3 (value of the current node).
max_val remains positive infinity.
We go to the right subtree.
The current node is not None (value is 4), so we proceed.
The value of the current node (4) is not less than or equal to 3 or greater than or equal to positive infinity, so we proceed.
Both the left and right subtrees of this node are None, so we return True.
--------
We go back to the previous recursive call (step 11). the recursive call to right side of left side

The right subtree is a valid BST, so we return the logical AND of the results obtained from steps 8 and 16, which is True.

We go back to the initial call to checkBST (step 3).

The left subtree is a valid BST (True), and the right subtree is also a valid BST (True), so we return the logical AND of these results, which is True.
'''