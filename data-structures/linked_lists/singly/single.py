class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def printLinkedList(self): 
            temp = self.head 
            while (temp): 
                print (temp.data, " -> ", end = '') 
                temp = temp.next_node
            print("")

    def addNodeAtHead(self, new_node):
        new_node.next = self.head
        self.head = new_node
    
    def addNodeAtTail(self, new_node):
         #just for example, you should already have the tail node known
         #or call another function to get that tail node
         tail = LinkedList()
         new_node.next = None
         tail.next = new_node
         tail = new_node

         
        

    



     