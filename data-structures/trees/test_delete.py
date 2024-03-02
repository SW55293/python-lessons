from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        # we found our value and has 1 child 
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right,current.val)
        return root
# --------------------

class So:
    def smallestDescendant(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        else:
            # Checks for Lesser value
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            # Checks for Greater value
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            # Checks if we have reached the node we want to delete
            else:
                # First we check if only 1 child node is present
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                # If both the children are present then we find the
                # smallest child in the right child and assign it's
                # value to node and recursively delete that child 
                # until we have reach node with 1 child or leaf node
                    temp = self.smallestDescendant(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
            return root


        