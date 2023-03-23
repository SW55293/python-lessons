
def isSubtree(root, subRoot):
    
                # Traversing throught whole tree (root) if root matches the subroot go in same function and check if both are same then return True or if Tree value touches to Null return False
            if root == None:  # If root Touches to Null value directly return False
                return False
            if same(root , subRoot)== True:  # if same function returns True return True itself
                return True 
                 # go inside the tree and call recursively root.left and root.right and we are taking 'or' of them because even if one value comes out to be true then we will return True itself
            return (isSubtree(root.left , subRoot) or isSubtree(root.right , subRoot))
    
def same(root , subroot):
            # if both root and subroot become Null at same time then we return True and whole answer would be true 
            if root == None and subroot == None:
                return True
            # if root value does'nt match with subroot value then we return False or even if root value becomes null and subroot is not null and viceversa is true then it will still return False
            if root== None or subroot == None or root.val != subroot.val :
                return False
            # Now we call the function recursively to give root and subroot childrens to see if it matches or not
            return (same(root.left, subroot.left) and same(root.right , subroot.right))
        
    # Same function to calculate the root and Subroot