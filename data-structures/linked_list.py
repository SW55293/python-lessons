# This class and function initialize the node object
# which consist of data and next pointer
# the data points/contains the value inside the node
# and the next pointer points to the next node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
# we always want to Start the next pointer pointed at null/none

# The linked list class and function initializes the linked
# list object. here we set head and head contains everything thats in the Node class    
class Linked_list:
    def __init__(self):
        self.head = Node() 
