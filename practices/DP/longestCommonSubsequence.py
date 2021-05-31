
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        n = len(nums)
        if n == 1: return nums[0]
        
        dp = [1] * n
        dp[0] = 1
        
        for i in range(0, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp
    
    
s = Solution()
sample = [7,7,7,7,7,7,7]
print(s.lengthOfLIS(sample))