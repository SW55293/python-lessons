# Pattern          = Recursion
# Time Complexity  = O(n * n)
# Space Complexity = O(n)
"""
Input1      = root TreeNode
Input2      = subRoot TreeNode
Return type = Boolean
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    
    def isSubtree(self, root, subRoot):

    #we use a separate function to do the comparing
        def compareTree(r,s):
            print('comparing', r, s) 
            if not r and not s:  
                print('not r & s', r,s)          #if both nodes are null/empty then they are the same
                return True
            if r and s and r.val==s.val:  #if the nodes are not empty then check there values
                return compareTree(r.left,s.left) and compareTree(r.right,s.right) 
            return False                  #return false if none of the above is true          

        if not subRoot: 
            print('not', subRoot)                #if subroot is null return true
            return True
        if not root:
            print('not', root)                     #if root is null return false
            return False
        if compareTree(root,subRoot):
            print('comapreTree', root, subRoot)    #take both nodes and compare them using other function
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

broot = [3,4,5,1,2]
sroot = [4,1,2]
compare1 = Solution(broot, sroot)


'''
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

compare func 
('r val = ', TreeNode{val: 3, left: TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}, right: TreeNode{val: 5, left: None, right: None}})
('s val = ', TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}})
compare func
('r val = ', TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}})
('s val = ', TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}})
compare func
('r val = ', TreeNode{val: 1, left: None, right: None})
('s val = ', TreeNode{val: 1, left: None, right: None})
compare func
('r val = ', None)
('s val = ', None)
compare func
('r val = ', None)
('s val = ', None)
compare func
('r val = ', TreeNode{val: 2, left: None, right: None})
('s val = ', TreeNode{val: 2, left: None, right: None})
compare func
('r val = ', None)
('s val = ', None)
compare func
('r val = ', None)
('s val = ', None)
('comapreTree input = ', TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}, TreeNode{val: 4, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}})


'''