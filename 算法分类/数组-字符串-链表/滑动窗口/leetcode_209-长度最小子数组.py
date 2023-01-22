from typing import List

# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        
        ret, left, total = len(nums), 0, 0
        
        for i, j in enumerate(nums):
            total += j
            while left <= i and total >= target:
                ret = min(i - left + 1, ret)
                total -= nums[left]
                left += 1
        
        return ret
    
nums =  [2,3,1,2,4,3]
target = 7
s = Solution()

r = s.minSubArrayLen(target, nums)

print(r)