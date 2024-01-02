from doubly_linked_list import *

def add_to_head(self, new_value):
  new_head = Node(new_value)
  current_head = self.head_node

  if current_head != None:
    current_head.set_prev_node(new_head)
    new_head.set_next_node(current_head)
  self.head_node = new_head
  
  if self.tail_node == None:
    self.tail_node = new_head



def add_to_tail(self, new_value):
   new_tail = Node(new_value)
   current_tail = self.tail

   if current_tail != None:
     current_tail.set_next_node(new_tail)
     new_tail.set_prev_node(current_tail)

   self.tail = new_tail

   if self.head == None:
     self.head = new_tail