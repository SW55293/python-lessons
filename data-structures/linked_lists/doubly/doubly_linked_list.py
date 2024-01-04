# This Node class will be different for a singly or circular linked list
# this only appliese to a doubly linked list
class Node:
    def __init__(self, value, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous

'''
In the Node class we have the data node that tells us what values are in the node
The next gives us the info of what it is pointing to
The previous lets us know what is before our node
'''

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
'''
The doubly linked list class add more functionality 
'''


# Getters and Setters

def set_next_node(self, next):
    self.next = next
    
def get_next_node(self):
  return self.next

def set_prev_node(self, previous):
  self.previos = previous
  
def get_prev_node(self):
  return self.previous

def get_value(self):
  return self.value

'''


**Overall Purpose:**


**Breakdown of Methods:**

1. **`set_next_node(self, next)`:**
   - Assigns the `next` node to the current node's `next` reference.
   - Establishes the forward link in the list.

2. **`get_next_node(self)`:**
   - Returns the current node's `next` node, allowing access to the subsequent node in the list.

3. **`set_prev_node(self, previous)`:**
   - Assigns the `previous` node to the current node's `previous` reference.
   - Establishes the backward link in the list.

4. **`get_prev_node(self)`:**
   - Returns the current node's `previous` node, allowing access to the preceding node in the list.

5. **`get_value(self)`:**
   - Returns the value stored within the current node.

**Key Points:**

- **Doubly linked lists** offer flexibility in traversal compared to singly linked lists, which only allow forward movement.
- These methods are essential for creating, manipulating, and traversing nodes within a doubly linked list.

**Additional Insights:**

- **Node Class:** These methods are typically part of a `Node` class, which defines the structure and behavior of individual nodes.
- **Common Operations:** Doubly linked lists support operations like insertion, deletion, search, and traversal in both directions.
- **Applications:** They are used in various scenarios, including implementing queues, stacks, undo/redo functionality, and managing browser history.

**If you have any further questions or specific areas you'd like me to elaborate on, please don't hesitate to ask!**

'''