
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        
        slow = head
        fast = head.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        return False

# Time:  O(n) : depends on the size of the linked list which is n
# Space: O(1) : No extra data structures are added, we do all the lookups using whats already there