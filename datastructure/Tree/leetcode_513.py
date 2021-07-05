from Node import TreeNode
from typing import List


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right: return root.val
        
        queue = [root]
        
        while queue:
            size = len(queue)
            values = []
            
            for i in range(0, size):
                n = queue.pop(0)
                
                values.append(n.val)
                
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
        
        return values[0]
    
    
class Solution_Opt:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right: return root.val
        
        queue = [root]
        
        while queue:
            n = queue.pop(0)

            # 先加右侧节点进队列，有助于让最左侧节点最后出队
            if n.right: queue.append(n.right)
            if n.left: queue.append(n.left)

        return n.val