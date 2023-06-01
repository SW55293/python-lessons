class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        #start of binary tree
        root = TreeNode(preorder[0])
        #everything on the right of the partition is the right side of tree\
        #while everything to the left is the left side of the tree
        partition = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : partition + 1], inorder[:partition])
        root.right = self.buildTree(preorder[partition + 1 :], inorder[partition + 1 :])
        return root