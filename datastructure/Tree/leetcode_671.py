from Node import TreeNode
from queue import Queue

# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
# 如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        test = root.val
        
        sec_min = -1
        res = sec_min
        
        queue = Queue()
        queue.put(root)
        
        while not queue.empty():
            node = queue.get()
            
            left = node.left
            right = node.right

            if left : queue.put(left)
            if right : queue.put(right)
            
            if left and left.val != test: res = left.val
            if right and right.val != test: res = right.val
            
            if res != -1:
                if sec_min == -1:
                    sec_min = res
                else:
                    sec_min = min(res, sec_min)
                    
        return sec_min