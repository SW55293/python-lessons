def lowestCommonAncestor(root, p, q):
       """
       :type root: TreeNode
       :type p: TreeNode
       :type q: TreeNode
       :rtype: TreeNode
       """
       # Find the first common ancestor
       cur = root
       while cur:
           if p.val > cur.val and q.val > cur.val:     #right subtree case
               cur = cur.right
           elif p.val < cur.val and q.val < cur.val:   #left subtree case
               cur = cur.left
           else:
               return cur
            


# the root will always be the absolute lowest common ancestor of every node
# we want the most recent for the 2 nodes p & q (sub-trees) 

#edge cases & all cases
#1: p & q are in the same subtree (left or right) - answer will be in that subtree
#2: p & q are in separate subtrees (one left and one right) - then root is lowest ancestor
#3: p or q are the root node - then root is lowest ancestor