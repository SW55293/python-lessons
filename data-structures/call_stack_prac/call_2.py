
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        #find middle, we want fast to end up at the last nodes None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        
        root = TreeNode(temp.val)
        # print("Call Stack:")
        # traceback.print_stack()
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root

# Example usage:
linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
# linked.insert(3)
# linked.insert(4)
# linked.insert(5)
# linked.insert(10)
# linked.insert(5)
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
root = solution.sortedListToBST(linked)