class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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
            #everything on the right of the right_subtree is the right side of the tree
            #while everything to the left is the left side of the tree
            right_subtree = inorder.index(preorder[0])

            root.left = self.buildTree(preorder[1 : right_subtree + 1], inorder[:right_subtree])
            root.right = self.buildTree(preorder[right_subtree + 1 :], inorder[right_subtree + 1 :])
            return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
start =sol.buildTree(preorder, inorder)
print(start)