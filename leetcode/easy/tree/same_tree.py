# Pattern          = Recursion
# Time Complexity  = O(p+q)
# Space Complexity = O(n)
"""
Input 1 = Binary Tree (TreeNode)
Input 2 = Binary Tree (TreeNode)
Return type = Boolean
"""

def isSameTree(p, q):

    #Using recursion
    #base case 1: both are null
    if p == None and q == None:
       return True 
    #base case 2: one or the other is null or if the values are not same then return false
    if p == None or q == None or p.val != q.val:
        return False
    
    # Recursive part checking the rest of the tree with the base cases given.. And go to left and right subtree.
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

def isSameTree(p, q):

    if p is None and q is None:
       return True 

    if p is None or q is None: 
        return False
    
    if p.val != q.val:
        return False
    
    # Recursive part checking the rest of the tree with the base cases given.. And go to left and right subtree.
    return (
        isSameTree(p.left, q.left) 
        and 
        isSameTree(p.right, q.right))