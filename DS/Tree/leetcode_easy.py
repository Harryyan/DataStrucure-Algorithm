from Node import TreeNode

# 110. 给定一个二叉树，判断它是否是高度平衡的二叉树。
class Solution1:
    result = True
    def isBalanced(self, root: TreeNode) -> bool:
        
        def height(node) -> int: 
            if not node or self.result == False:
                return 0

            l_m = height(node.left)
            l_r = height(node.right)
            
            if abs(l_m - l_r) > 1:
                self.result = False

            return 1 + max(l_m, l_r)

        height(root)
        
        return self.result
    
# 543. 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。 
class Solution2:
    result = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def height(node) -> int: 
            if not node:
                return 0

            l_m = height(node.left)
            l_r = height(node.right)

            self.result = max(self.result, l_m + l_r)

            return 1 + max(l_m, l_r)


        height(root)

        return self.result

# 翻转一棵二叉树
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def invert(node) -> TreeNode: 
            if not node:
                return None

            left = invert(node.left)
            right = invert(node.right)
            
            node.left = right
            node.right = left

            return node
        
        return invert(root)
    
# 617. 合并二叉树
class Solution4:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2: return None
        if not root1: return root2
        if not root2: return root1
        
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        
        return root
# 112. 路径总和 
class Solution5:
    result = False
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            self.result = False
        
        test = 0
        self.dfs(root, test, targetSum)
        
        return self.result

    def dfs(self, node, test, targetSum):
        if not node:
            return 0
    
        test += node.val
        left = self.dfs(node.left, test, targetSum)
        right = self.dfs(node.right, test, targetSum)
    
        if not node.left and not node.right:
            if test == targetSum:
                self.result = True
    
        return test  