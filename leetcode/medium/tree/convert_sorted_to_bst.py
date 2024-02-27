from typing import Optional, ListNode

class TreeNode:
     def __init__(self, val=0) -> None:
          self.val = val
          self.left = None
          self.right = None
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # If the condition if not head: is true (meaning head is empty) return None,
        # if no head return None
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # or combine both if's
        # if not head or not head.next:
            # return TreeNode(head.val) if head else None
        
        #find middle, we want fast to end up at the last nodes None
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root
    
'''
We want the middle value in the list to become the root node. 
Then all values from head to temp will be on the left subtree
and all values from temp.next till the end of the list will
be on the right subtree.
'''