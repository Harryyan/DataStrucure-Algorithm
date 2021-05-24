from Node import TreeNode
import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.test(root)

    def test(self, root: TreeNode) -> int:
        if not root:
            return float("inf")

        l = self.test(root.left)
        r = self.test(root.right)

        if l == sys.maxint and r == sys.maxint:
            return 1
        else:
            return 1 + min(l, r)


# 优化版本
class Solution2:
    result = 1000000

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0

        self.test(root, count)

        return self.result

    def test(self, root: TreeNode, count: int) -> int:
        count += 1

        if count > self.result:
            return -1

        if not root.left and not root.right:
            self.result = min(self.result, count)
            return 1

        if not root.left and root.right:
            return 1 + self.test(root.right, count)

        if not root.right and root.left:
            return 1 + self.test(root.left, count)

        l = self.test(root.left, count)
        r = self.test(root.right, count)

        return 1 + min(l, r)