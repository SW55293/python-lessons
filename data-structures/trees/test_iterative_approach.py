class TreeNode:
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None
'''
a) stacks are last-in-first-out.

b) queues are first-in-first-out.
'''
class Iterative:
# --------- In-Order --------- left -> root -> right
    def inorder_traversal_2(self, root):
        stack = []
        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.val, end=" ")
                current = current.right


    def inorder_traversal(self, root):
        if not root:
            return []
        
        stack, output = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            
            # print(current.val)
            output.append(current.val)
            current = current.right

        return output

# --------- Pre-Order --------- root -> left -> right
    def preorder_traversal(self, root):
        stack = []
        current = root

        while stack or current:
            if current:
                print(current.val, end=" ")
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    def preorderTraversal(root):
        if root is None:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)  # Right child is pushed first so that left is processed first
                stack.append(node.left)
        return output
    
 # --------- Post-Order --------- left -> right -> root  
    def postorder_traversal(self, root):
        stack = []
        current = root
        last_visited = None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack[-1]
                if current.right is None or current.right == last_visited:
                    print(current.val, end=" ")
                    last_visited = current
                    stack.pop()
                else:
                    current = current.right

    def postorderTraversal(root):
        if not root:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            output.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return [node.val for node in reversed(output)]  # Reverse the result



root = TreeNode(20)
root.left = TreeNode(15)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.right = TreeNode(30)
root.right.left = TreeNode(25)
root.right.right = TreeNode(40)

iterative = Iterative()
start = iterative.inorder_traversal_2(root)
print(start)