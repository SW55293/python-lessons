# Binary Search Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, val):
        # This places any node into an empty null/none spot
        if root is None:
            return Node(val)  # Return the new node directly

        # If the value is less
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root  # Return the updated root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)
            # When you specify end=" ", you're telling print() to not add a newline character, 
            # but instead to add a space character () at the end of the output.
            # often used in situations like printing elements of a list or tree structure 
            # where you want to display them on a single line, separated by spaces.

    def search(self, value, node):
        if node is None or node.val == value:
            return node
        
        elif value < node.val:
            self.search(value, node.left)
        else:
            value > node.val
            self.search(value, node.right)




#   Print The Tree 
    def print_tree_ascii(self, root, level=0):
        if root:
            self.print_tree_ascii(root.right, level + 1)
            print(" " * 4 * level + "--> " + str(root.val))
            self.print_tree_ascii(root.left, level + 1)



 
# Root is not part of the node class, you have to define it outside of the class
root = Node(12)

# Use the insert method to add nodes
root.insert(root, 6)  # root.left
root.insert(root, 14)  # root.right
root.insert(root, 3)  # root.left.left
root.insert(root,18)

root.inorder_traversal(root)
print()
print("---------------------")
root.print_tree_ascii(root)








'''
# binary tree node class

class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

    

   def insert(self, root, val):
      #this places any node into an empyt null/none spot
      if root is None:
         return Node(val)
      
      
      # If the value is less
      if val < root.val:
            root.left = self.insert(root.left, val)
      else:
            root.right = self.insert(root.right, val)
      return root
           

    # Print the tree
   def PrintTree(self):
      # if self.left is True, if theres a left subtree then print
      print(self.val)
      if self.left:
         self.left.PrintTree()

      if self.right:
         self.right.PrintTree()
    


#root is not part of the node class, you have to define it outside of the class
root = Node(12)

# Use the insert method to add nodes
root.insert(root, 6) #root.left
root.insert(root, 14) #root.right
root.insert(root, 3) #root.left

root.PrintTree()
'''