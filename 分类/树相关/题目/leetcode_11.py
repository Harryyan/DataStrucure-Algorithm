from Node import TreeNode

class Solution:
    sum = 0
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.cal(root)
        return self.sum
        
        
    def cal(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return root.val
        
        ls = self.cal(root.left)
        rs = self.cal(root.right)
        
        self.sum += ls
        
        return 0