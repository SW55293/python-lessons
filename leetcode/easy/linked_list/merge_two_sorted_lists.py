# Pattern          = Two Pointer
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = Singly Linked List
Return type = Singly Linked List
"""

#Iterative Case (faster than recursively)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        # Create an empty ListNode
        dummy_list = ListNode()
        new_head = dummy_list
     
        while list1 and list2:   
            if list1.val < list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next

        # covering the cases when list1 or list2 end up empty before the other
        if list1:
            new_head.next = list1
        if list2:
            new_head.next = list2
        

        return dummy_list.next
        #need to return dummy_list.next because if you return
        #the whole thing you get a zero as the first node