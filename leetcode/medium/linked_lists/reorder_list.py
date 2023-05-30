def reorderList(head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        '''
        The function works by first using two pointers, slow and fast, to find the middle of the linked list. 
        The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time. When the fast pointer 
        reaches the end of the linked list, the slow pointer will be pointing to the middle node.
        '''
        # finds the middle and the last node
        slow = head 
        fast = head.next
        #while fast and fast.next != None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Separates the 2 halfs 
        start_of_second = slow.next
        slow.next = None
        prev = None
        while start_of_second:
            temp = start_of_second.next
            start_of_second.next = prev
            prev = start_of_second
            start_of_second = temp

        # Reverses the next pointers of the 2 halfs and shifts the nodes around 
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
    












def reorder_List(head):
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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    

'''