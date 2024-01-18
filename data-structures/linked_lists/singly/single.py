class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head) -> None:
        self.head = head