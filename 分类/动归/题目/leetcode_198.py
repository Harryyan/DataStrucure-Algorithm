
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp = [0,nums[0]]
        
        for i in range(0, len(nums)-2):
            temp = dp[0]
            dp[0] = max(temp,dp[1])
            dp[1] = temp+nums[i]
        
        return max(dp[0], dp[1])
    
    
s = Solution()
sample = [2,3,2]
r = s.rob(sample)

print(r)