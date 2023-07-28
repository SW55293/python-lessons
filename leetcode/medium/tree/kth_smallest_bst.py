# My try

def kthSmallest(root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # return the k smallest number in the tree
        # add values to a list, then return the kth index value
        result = []

        def in_order(node, arr):
            if node is None:
                return
            in_order(node.left, arr)
            arr.append(node.val)
            in_order(node.right, arr)

        in_order(root, result)
        # result.sort()

        new_k = k-1

        return result[new_k]

# copied try
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val
            root = root.right
