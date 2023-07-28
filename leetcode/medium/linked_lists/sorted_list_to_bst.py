
# we want to first find the middle node
# then use recursion to call the nodes on the left and right
# side of the middle node which we will make the root. 
# when we're calling those node we check if they are bigger or smaller
# than root and the previous node, so that assign it to the right side


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        #base case
        if not head:        #no nodes
            return None
        if not head.next:   #one node
            return TreeNode(head.val)

        # this finds the middle node and last node
        slow = head 
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #temp pointer to root of bst
        temp = slow.next
        #disconnect the root
        slow.next = None

        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root







   
        


    