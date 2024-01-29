# binary tree node class

class Node:
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

    

   def insert(self, val):
      # If the value is less
      if val < self.val:
        if not self.left: # If there isnt a parent node, then create node of that val
            self.left = Node(val)
        else:
            self.left.insert(val) # If the parent is present then insert

      else:
        if not self.right:
            self.right = Node(val)
        else:
            self.right.insert(val)
           

# Print the tree
   def printTree(self):
      if self.left:
         self.left.printTree()

      print(self.val)

      if self.right:
         self.right.printTree()

#root is not part of the node class, you have to define it outside of the class
root = Node(12)

# Use the insert method to add nodes
root.insert(6) #root.left
root.insert(14) #root.right
root.insert(3) #root.left

root.printTree()