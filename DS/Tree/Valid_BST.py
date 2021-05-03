from Node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _values = []
    _result = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.depth_iteration_middle(root)

        return self._result

    def depth_iteration_middle(self, node):
        if node is None or self._result == False:
            return

        left = self.depth_iteration_middle(node.left)

        if self._values and self._values[-1] > node.val:
            self._result = False
        else:
            self._values.append(node.val)

        right = self.depth_iteration_middle(node.right)