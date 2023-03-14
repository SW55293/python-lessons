# Pattern          = Two Pointer
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = Singly Linked List
Return type = Singly Linked List
"""

def reverseList(head):
    # Initialize prev pointer to NULL
    prev = None
    # Initialize the curr pointer to the head
    curr = head
    # Run a loop till curr points to NULL
    while curr:
        # Initialize next pointer as the next pointer of curr
        temp_next = curr.next
        # Assign curr.next to what prev current value is
        curr.next = prev
        # Assign curr to prev, next to curr
        prev = curr
        curr = temp_next
    return prev       # Return the prev pointer to get the reverse linked list



   
    
'''
We are keeping 3 pointer basically
with one of them only being visible 
inside of the while loop.

We keep track of the prev pointer previous value/number before moving it forward
We keep track of curr next 
'''