def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head

        for _ in range(n):          # this will only loop from 1 -> n 
            fast = fast.next
        if not fast:                # if fast is null/none (is fast == null?)
            return head.next
        while fast.next:            # while fast.next is not null
            fast = fast.next
            slow = slow.next
             
        slow.next = slow.next.next  # this sets the value before the nth node to the next node
        return head
