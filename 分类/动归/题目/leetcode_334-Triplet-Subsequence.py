from typing import List

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k 
# and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# leetcode - 334

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        set_num = set(nums)
        n = len(set_num)
        if n < 3: return False

        n = len(nums)

        dp = [1] * n
        count = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:  
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                        
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                        
            if dp[i] == 3:
                return True

        return False

nums = [1,2,1,2,1,2]
s = Solution()

r = s.increasingTriplet(nums)

print(r)