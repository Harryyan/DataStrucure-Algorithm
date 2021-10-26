from typing import List

# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# leetcode - 152

class Solution:
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return nums[0]

        result = nums[0]
        # 初始化 最大 最小 数组
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        # 巧妙解决了附属符号问题，不需要记录sign； 无后效性；
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])  
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])            
            result = max(result, dp_max[i])

        return result

# 利用符号
# 当负数个数为偶数时候，全部相乘一定最大
# 当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
# 当有 0 情况，重置就可以了

class Solution_Cool:
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]

        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            # 防止 0 的出现，出现了就从当前元素重新开始
            reverse_nums[i] *= reverse_nums[i - 1] or 1

        # 合并数组，求最大值
        return max(nums + reverse_nums)

nums = [3,-2,-2,4,-3]
s = Solution_Cool()

r = s.maxProduct(nums)

print(r)