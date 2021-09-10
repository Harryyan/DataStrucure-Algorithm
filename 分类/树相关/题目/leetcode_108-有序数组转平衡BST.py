from Node import TreeNode
from typing import List

# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def getNode(nums) -> TreeNode:
            if not nums: return None
            if len(nums) == 1: return TreeNode(nums[0], None, None)
            
            n = len(nums)
            m = n // 2
            
            left = getNode(nums[0:m])
            right = getNode(nums[m+1: n])
            node = TreeNode(nums[m], left, right)
            
            return node
            
        return getNode(nums)