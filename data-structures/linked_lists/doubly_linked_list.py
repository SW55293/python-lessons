# This Node class will be different for a singly or circular linked list
# this only appliese to a doubly linked list
class Node:
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

'''
In the Node class we have the data node that tells us what values are in the node
The next gives us the info of what it is pointing to
The previous lets us know what is before our node
'''

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
'''
The doubly linked list class add more functionality 
'''