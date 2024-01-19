class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList(Node):
    def __init__(self, head):
        self.head = head

    def printLinkedList(self): 
            temp = self.head 
            while (temp): 
                print (temp.data, " -> ", end = '') 
                temp = temp.next_node
            print("")

    def addNode(self, new_node):
        curr = self.head

        while curr and curr.next: 
              curr = curr.next
        curr.next = new_node
        
    



     