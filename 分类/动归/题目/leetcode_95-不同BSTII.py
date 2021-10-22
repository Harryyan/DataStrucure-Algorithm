from typing import List

# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
# leetcode-95

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen(num):
            if not num: yield None
            
            for i, n in enumerate(num):
                for l in gen(num[:i]):
                    for r in gen(num[i + 1:]):
                        yield TreeNode(n, l, r)
        
        return bool(n) * [*gen([*range(1, 1 + n)])]