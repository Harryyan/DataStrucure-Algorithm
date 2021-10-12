from Node import TreeNode

# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true

# 两数之和变体问题
# 中序遍历之后
# 双指针求两数之和
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        def mid_order(root):
            if root:
                mid_order(root.left)
                nums.append(root.val)
                mid_order(root.right)
        mid_order(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
                
        return False