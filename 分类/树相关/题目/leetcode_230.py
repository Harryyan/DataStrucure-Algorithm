from Node import TreeNode

# 给定一个二叉搜索树的根节点 root ，
# 和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

class Solution:
    values = []
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        
        self.inorder_traversal(root)
        
        return self.values[k-1]
    
    def inorder_traversal(self, node):
        if node is None:
            return

        left = self.inorder_traversal(node.left)
        self.values.append(node.val)
        right = self.inorder_traversal(node.right)