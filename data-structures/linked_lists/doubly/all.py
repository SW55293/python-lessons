class Node:
  """
  Node class for a doubly linked list.
  """
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  """
  Doubly linked list implementation.
  """
  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head is None

  def append(self, value):
    """
    Adds a new node to the end of the list.
    """
    new_node = Node(value)
    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def prepend(self, value):
    """
    Adds a new node to the beginning of the list.
    """
    new_node = Node(value)
    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def insert_after(self, node, value):
    """
    Inserts a new node after a given node.
    """
    new_node = Node(value)
    if node is None:
      raise ValueError("Node cannot be None")
    if node.next is None:
      self.tail = new_node
    else:
      new_node.next = node.next
      node.next.prev = new_node
    new_node.prev = node
    node.next = new_node

  def insert_before(self, node, value):
    """
    Inserts a new node before a given node.
    """
    new_node = Node(value)
    if node is None:
      raise ValueError("Node cannot be None")
    if node is self.head:
      self.head = new_node
    else:
      new_node.next = node
      node.prev.next = new_node
    new_node.prev = node.prev
    node.prev = new_node

  def remove(self, node):
    """
    Removes a node from the list.
    """
    if node is None:
      raise ValueError("Node cannot be None")
    if node is self.head:
      self.head = node.next
    elif node is self.tail:
      self.tail = node.prev
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
    node.next = None
    node.prev = None

  def search(self, value):
    """
    Searches for a node with a specific value.
    """
    current = self.head
    while current is not None:
      if current.value == value:
        return current
      current = current.next
    return None

  def __str__(self):
    """
    Returns a string representation of the list.
    """
    output = ""
    current = self.head
    while current is not None:
      output += f"{current.value} -> "
      current = current.next
    output += "None"
    return output

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(9)
dll.insert_after(dll.head.next, 1.5)
dll.insert_before(dll.tail, 3.5)
# dll.remove(dll.tail.prev)
node = dll.search(100)
print(dll)

if node:
    print(node.value)
else:
  print(f"Node with that value was not found")