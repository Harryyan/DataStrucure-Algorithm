from typing import List
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in 
# the sequence has an edge connecting them. A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 后序遍历 - 自底向上动态规划
# 先序也行
class Solution:
    # tc: O(n)
    # sc: O(1) - 也有说和层数相关 故O(n)更准确
    def _postOrder(self, node):
        if not node: return 0

        left = self._postOrder(node.left)
        right = self._postOrder(node.right)

        if left < 0:
            left = 0

        if right < 0:
            right = 0 
        
        # 状态转移方程
        val = node.val + left + right

        if not self.result or self.result < val:
            self.result = val

        # 贪心 - 选择路径
        node_val = node.val + max(left, right)

        return node_val

    def maxPathSum(self, root: TreeNode) -> int:
        self.result = None
        self._postOrder(root)

        return self.result