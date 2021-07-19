import queue
from Node import TreeNode
from queue import Queue
from typing import List

# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

# class Solution:
#     def averageOfLevels(self, root: TreeNode) -> List[float]:
#         res = []
#         if root is None: return res
#         que = [root]
#         while que:
#             n = len(que)
#             Sum = 0
#             for _ in range(n):
#                 cur = que.pop(0)
#                 Sum += cur.val
#                 if cur.left: que.append(cur.left)
#                 if cur.right: que.append(cur.right)
#             res.append(Sum / n)
#         return res

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        values = []
        
        q = Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            sum = 0
            
            for i in range(0, size):
                n = q.get()
                
                sum += n.val
                
                if n.left: q.put(n.left)
                if n.right: q.put(n.right)
            
            values.append(sum / size)
        
        return values