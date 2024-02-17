class Node:
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root
    
    def find_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current
    
    def find_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    def in_order(self, root):
        if root is None:
            return 
        
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def pre_order(self, root):
        if root is None:
            return 
        
        print(root.val)
        self.in_order(root.left)
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return 
        
        self.in_order(root.left)
        self.in_order(root.right)
        print(root.val)



