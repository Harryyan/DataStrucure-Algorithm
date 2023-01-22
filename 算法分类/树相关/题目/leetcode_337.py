from Node import TreeNode
import collections

# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
# 这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
# 一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。



# 动态规划解决方案
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         # DP二叉树
#         def robTree(cur: TreeNode):
#             if not cur: return [0, 0]
#             left = robTree(cur.left)
#             right = robTree(cur.right)
#             val1 = cur.val + left[0] + right[0]
#             val2 = max(left[0], left[1]) + max(right[0], right[1])
#             return [val2, val1]
#         res = robTree(root)
#         return max(res[0], res[1])

class Solution:
    
    visited = collections.defaultdict(int)
    
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        
        if self.visited[root]: return self.visited[root]
        
        val1 = root.val
        
        if root.left: val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right: val1 += self.rob(root.right.left) + self.rob(root.right.right)
        
        val2 = self.rob(root.left) + self.rob(root.right)
        res = max(val1, val2)
        
        self.visited[root] = res
        
        return res