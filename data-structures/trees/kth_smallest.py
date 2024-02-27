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

# We want to place values in an array and sort them, from there we want to
# return the index kth value. The indices start from 1 and not 0
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
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
# k = 3
# result = Solution().kthSmallest(root, k)
# print(result)  # Output: 4
# result = inOrderTraversalIterative(root)
# print(result)
root.print_tree_ascii(root)