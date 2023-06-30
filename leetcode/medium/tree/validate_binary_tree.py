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