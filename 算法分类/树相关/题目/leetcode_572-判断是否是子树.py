from Node import TreeNode

# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
# s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (
            s.val == t.val
            and self.isSameTree(s.left, t.left)
            and self.isSameTree(s.right, t.right)
        )


test = Solution()