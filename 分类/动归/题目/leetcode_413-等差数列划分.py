from typing import List


# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 子数组 是数组中的一个连续序列。


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        
        dp = [0] * len(nums)
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i - 2]:
                dp[i] = 1
                
                if dp[i-1] > 0:
                    dp[i] += dp[i-1]

        return sum(dp)
    
    
nums = [1,2,3,5,6,7]
s = Solution()

r = s.numberOfArithmeticSlices(nums)

print(r)