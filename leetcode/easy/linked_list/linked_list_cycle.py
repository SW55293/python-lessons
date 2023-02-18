# Pattern          = Two Pointer
# Time Complexity  = 
# Space Complexity = 
"""
Input1 = head: ListNode
return type = bool
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        slow_pointer = head
        fast_pointer = head

        while fast_pointer!=None and fast_pointer.next!=None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer is slow_pointer:
                return True
        return False

'''
Another way (much faster)

def hasCycle(self,head):
    slow = head
    fast = head.next

    while slow is not fast:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
        return True
    return False

'''

# Time:  O(n) : depends on the size of the linked list which is n
# Space: O(1) : No extra data structures are added, we do all the lookups using whats already there
