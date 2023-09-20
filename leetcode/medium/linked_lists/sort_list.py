from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
       arr = []

       while head:
           arr.append(head.val)
           head = head.next
       arr.sort()
       if not arr: 
           return None
       
       root = ListNode(arr[0])
       curr = root
       
       for val in arr[1:]:
           curr.next = ListNode(val)
           curr = curr.next
       return root

