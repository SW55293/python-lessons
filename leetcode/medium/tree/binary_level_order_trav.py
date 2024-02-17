from typing import Optional, List

class TreeNode:
     def __init__(self, val=0) -> None:
          self.val = val
          self.left = None
          self.right = None


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        final_list = []
        queue = [root]
        
        while queue:
            q_len = len(queue)
            sublist = []
            
            for _ in range(q_len):
                node = queue.pop(0)  # Remove the first element from the queue
                sublist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            final_list.append(sublist)
        
        return final_list