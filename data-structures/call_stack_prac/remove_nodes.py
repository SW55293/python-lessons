from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        next_node = self.removeNodes(head.next)
        
        if head.val < next_node.val:
            return next_node
        else:
            head.next = next_node
            return head


linked = ListNode(5, ListNode(2, ListNode(90, ListNode(4, ListNode(8, ListNode(6))))))
solution = Solution()
root = solution.removeNodes(linked)

current = root
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")