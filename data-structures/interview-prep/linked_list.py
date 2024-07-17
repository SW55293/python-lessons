class LinkedList:
    def __init__(self, val=0, next =None) -> None:
        self.val = val
        self.next = next

class testing_linked:
    def singly(self, nums):
        if not nums:
            return None
        
        head = LinkedList(nums[0])
        current = head

        for num in nums[1:]:
            current.next = LinkedList(num)
            current = current.next

        return head
    
def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    return head
    
    
linked_list = testing_linked()
test = linked_list.singly([1,2,4,3])
print_list(test)
        

