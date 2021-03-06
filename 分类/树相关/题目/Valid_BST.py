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


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        x = 0

        def find_max(node, x) -> int:
            if not node:
                return x

            x += 1

            l_m = find_max(node.left, x)
            l_r = find_max(node.right, x)

            return max(l_m, l_r)

        return find_max(root, x)


node_9 = TreeNode(9, None, None)
node_10 = TreeNode(10, None, None)
node_5 = TreeNode(5, None, None)
node_7 = TreeNode(7, None, None)
node_6 = TreeNode(6, None, node_7)
node_11 = TreeNode(11, node_5, node_6)
node_30 = TreeNode(30, None, node_11)
node_20 = TreeNode(20, node_10, node_30)
node_3 = TreeNode(3, node_9, node_20)

test = Solution2()
result = test.maxDepth(node_3)

print(result)