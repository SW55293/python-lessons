
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    
    if not head:
        # Quick response for empty linked list
        return None
    
    # ------------------------------------------
    # Locate the mid point of linked list
    # First half is the linked list before mid point
    # Second half is the linked list after mid point
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        
    mid = slow
    
    # ------------------------------------------
    # Reverse second half
    
    prev, cur = None, mid
    
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    
    head_of_second_rev = prev
    
    # ------------------------------------------
    # Update link between first half and reversed second half
    
    first, second = head, head_of_second_rev
    
    while second.next:
        
        next_hop = first.next
        first.next = second
        first = next_hop
        
        next_hop = second.next
        second.next = first
        second = next_hop


'''
head=ListNode()
class Solution:
  def reorderList(self, head: ListNode) -> None:
    def findMid(head: ListNode):
      prev = None
      slow = head
      fast = head

      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None

      return slow

    def reverse(head: ListNode) -> ListNode:
      prev = None
      curr = head

      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

      return prev

    def merge(l1: ListNode, l2: ListNode) -> None:
      while l2:
        next = l1.next
        l1.next = l2
        l1 = l2
        l2 = next

    if not head or not head.next:
      return

    mid = findMid(head)
    reversed = reverse(mid)
    merge(head, reversed)

'''