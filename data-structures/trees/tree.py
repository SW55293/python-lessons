# binary tree node class

class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

    

   def insert(self, root, val):
      #this places any node into an empyt null/none spot
      if root is None:
         root = Node(val)
         return root
      
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
root.insert(6) #root.left
root.insert(14) #root.right
root.insert(3) #root.left

root.PrintTree()