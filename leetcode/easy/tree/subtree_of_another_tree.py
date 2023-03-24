# Pattern          = Recursion
# Time Complexity  = O(n * n)
# Space Complexity = O(n)
"""
Input1      = root TreeNode
Input2      = subRoot TreeNode
Return type = Boolean
"""
def isSubtree(root, subRoot):

    #we use a separate function to do the comparing
    def compareTree(r,s):
        if not r and not s:           #if both nodes are null/empty then they are the same
            return True
        if r and s and r.val==s.val:  #if the nodes are not empty then check there values
            return compareTree(r.left,s.left) and compareTree(r.right,s.right) 
        return False                  #return false if none of the above is true          
    
    if not subRoot:                 #if subroot is null return true
        return True
    if not root:                    #if root is null return false
        return False
    if compareTree(root,subRoot):   #take both nodes and compare them using other function
        return True
        
    return isSubtree(root.left,subRoot) or isSubtree(root.right,subRoot)