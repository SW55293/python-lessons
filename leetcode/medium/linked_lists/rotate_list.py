from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        for x in range(k):
            temp = head

            while temp.next.next:
                temp = temp.next

            last = temp.next
            temp.next = None
            last.next = head
            head = last
        return head    





        