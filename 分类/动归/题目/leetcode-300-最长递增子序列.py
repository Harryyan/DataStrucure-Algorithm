
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        n = len(nums)
        if n == 1: return 1
        
        dp = [1] * n
        
        for i in range(0, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        dp.sort()
        
        return dp[-1]
    
    
s = Solution()
sample = [9,2,3,4,5,6,7,10,4]
print(s.lengthOfLIS(sample))