from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        last = head

        for x in range(1, k):
            first = first.next
        
        #This part creates a section of node that are k
        #spaces apart, so when temp reached the last node in the list
        #we know that last the variable is k spaces from the last node in the list
        temp = first
        while temp.next:
            last = last.next
            temp = temp.next

        f = first.val
        first.val = last.val
        last.val = f


        return head
'''
saving first's val to a variable (is faster)
f = first.val
first.val = last.val
last.val = f
'''
 
# This is slower, first.val, last.val = last.val, first.val

        



        