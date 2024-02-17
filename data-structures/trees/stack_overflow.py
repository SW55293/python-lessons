from typing import Optional



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val} '
    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Define the helper function for inorder traversal
        def inorder(node):
            if node is None:
                return []
            # print(f'node.val = {str(node)}')
            # Traverse left, visit the node, and then right
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Perform the inorder traversal to get a sorted list of values
        result = inorder(root)
        print(result)
        # Return the kth smallest element
        return result[k-1]  # k-1 because list indices start at 0
    
# Create the binary tree
root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(9)
root.left.right = TreeNode(11)
root.right = TreeNode(30)
root.right.left = TreeNode(22)
root.right.right = TreeNode(40)

# Instantiate Solution and call kthSmallest
solution = Solution()
print(solution.kthSmallest(root, 3))  # Example: Find the 3rd smallest element

