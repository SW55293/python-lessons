class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'
    
    def print_tree_ascii(self, root, level=0):
        if root:
            self.print_tree_ascii(root.right, level + 1)
            print(" " * 4 * level + "--> " + str(root.val))
            self.print_tree_ascii(root.left, level + 1)

# We want to find the kth smallest value. So we place values in a stack and decrememnt 
# the k's value as we go down the tree on the left side.
# The root has an index of 1 and the indices continue in order from left to right.
# You will process None leaf nodes, they will trigger the pop's
# Ex: arr=10,2,35,11 k=3, we return index 3 which is value 35

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []
        curr = root

        while curr or stack:
            # Traverse left subtree until reaching a leaf node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit the leaf node (kth smallest element if count matches k)
            curr = stack.pop()
            k = k - 1
            if k == 0:
                return curr.val

            # Traverse right subtree
            curr = curr.right

        return None
#------------------------------------------------------- 
def inOrderTraversalIterative(root):
    stack = []
    current = root

    while current or stack:
        print(f'current = {str(current)}')
        # Reach the left most Node of the current Node
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        print(current.val)  # Visit the node

        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right



# Example usage
root = TreeNode(10, TreeNode(2,TreeNode(1), TreeNode(3)), TreeNode(35, TreeNode(11), TreeNode(40)))
k = 4
result = Solution().kthSmallest(root, k)
print(result) 
# result = inOrderTraversalIterative(root)
# print(result)
root.print_tree_ascii(root)

# commented code 
def kthSmallest(self, root: TreeNode, k: int) -> int:
    # Initialize an empty stack for simulating tree traversal 
    stack = []  
    # Start with the root node
    curr = root

    while curr or stack:  # Continue until we've exhausted all nodes 
        # Traverse left subtree until reaching a leaf node
        while curr: 
            stack.append(curr)   # Keep track of nodes as we go down
            curr = curr.left

        # Visit the leaf node (kth smallest element if count matches k)
        curr = stack.pop()   # Backtrack to the most recent node
        k = k - 1            # Decrement count ('k' elements visited so far)
        if k == 0:           # Did we find the 'k'th smallest?
            return curr.val  # Return the value

        # Traverse right subtree
        curr = curr.right    # Explore the right children of the current node

    return None  # If the tree didn't have 'k' elements
