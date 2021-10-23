from typing import List

# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同二叉搜索树 。可以按 任意顺序 返回答案。
# leetcode-95

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 官方解释如下:
    # 时间复杂度:  
    # 取决于 可行二叉搜索树的个数: 而对于n个点生成的二叉搜索树数量等价于数学上第n个卡特兰数
    # O(nGn) Gn代表卡特兰数

    # 空间复杂度:O(nGn) Gn代表卡特兰数
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None,]
            
            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            
            return allTrees
        
        return generateTrees(1, n) if n else []