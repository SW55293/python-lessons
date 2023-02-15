# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform preorder traversal on a given binary tree
def preorder(root):
 
    if root is None:
        return
 
    print(root.data)
    preorder(root.left)
    preorder(root.right)
 
 
# Utility function to swap left subtree with right subtree
def swap(root):
 
    if root is None:
        return
 
    temp = root.left
    print('temp = ', temp)
    root.left = root.right
    print('root.left = ', root.left)
    root.right = temp
    print('root.right = ', root.right)

 
 
# Function to invert a given binary tree using preorder traversal
def invertBinaryTree(root):
 
    # base case: if the tree is empty
    if root is None:
        return
 
    # swap left subtree with right subtree
    swap(root)
 
    # invert left subtree
    invertBinaryTree(root.left)
 
    # invert right subtree
    invertBinaryTree(root.right)
 
 
if __name__ == '__main__':
 
    ''' 
Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
'''
 
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
 
    invertBinaryTree(root)
    preorder(root)
 