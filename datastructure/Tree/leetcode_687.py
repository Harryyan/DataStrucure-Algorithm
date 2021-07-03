from Node import TreeNode


class Solution:
    sum = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.cal(root)
        
        return self.sum

    def cal(self, node):
        if not node:
            return 0

        left = self.cal(node.left)
        right = self.cal(node.right)

        left_sum = 0
        right_sum = 0

        if node.left and node.val == node.left.val:
            left_sum = left + 1
            
        if node.right and node.val == node.right.val:
            right_sum = right + 1

        self.sum = max(self.sum, left_sum+right_sum)

        return max(left_sum, right_sum)



















