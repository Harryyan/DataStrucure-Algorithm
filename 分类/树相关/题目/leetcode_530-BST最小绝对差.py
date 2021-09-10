from Node import TreeNode

# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值


class Solution:
    result = float('inf')
    preNode = None
    
    def getMinimumDifference(self, root: TreeNode) -> int:

        def inOrder(node: TreeNode):
            if not node: return
            
            inOrder(node.left)
            
            if self.preNode:
                self.result = min(self.result, abs(self.preNode.val-node.val))

            self.preNode = node
            
            inOrder(node.right)
            
        inOrder(root)
        
        return self.result