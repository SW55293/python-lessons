from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False

        if subRoot is None:
            return True

        def compare(r, s):
            if r is None and s is None:
                return True
            
            if r is None or s is None:
                return False

            if r.val != s.val:
                return False

            # check left and right children
            return compare(r.left, s.left) and compare(r.right, s.right)      

        if compare(root, subRoot):
            return True    

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
root = TreeNode(3)

root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

solution = Solution()
start = solution.isSubtree(root, subRoot)
print(start)
