

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    #if we hit an end leaf with no children return o since
    #we're at the end of that branch and the count has already happened
    if root is None:
        return 0
        
    left = maxDepth(root.left) + 1
    right = maxDepth(root.right) + 1
    return max(left,right)
            
        


'''
* faster runtime
* bit more memory used

if root is None:
    return 0

left = self.maxDepth(root.left) + 1
right = self.maxDepth(root.right) + 1

return max(left,right)
------
* slower runtime
* less memory used

if root is None:
    return 0
left = self.maxDepth(root.left)
right = self.maxDepth(root.right)
        

return max(left, right) + 1

'''

        

