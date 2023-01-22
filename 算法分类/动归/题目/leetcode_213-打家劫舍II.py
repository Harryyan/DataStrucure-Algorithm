from typing import List

# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp0 = [0,nums[0]]
        dp1 = [0,nums[-1]]
        
        for i in range(1, len(nums)-1):
            temp = dp0[0]
            dp0[0] = max(temp,dp0[1])
            dp0[1] = temp+nums[i]
        
        for i in range(0, len(nums)-2):
            temp = dp1[0]
            dp1[0] = max(temp,dp1[1])
            dp1[1] = temp+nums[i]

        return max(max(dp1[0], dp1[1]),max(dp0[0], dp0[1]))
    
    
s = Solution()
sample = [1,2,100]
r = s.rob(sample)

print(r)