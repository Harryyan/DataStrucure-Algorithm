from typing import List
# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        dic = {0 : 0}
        res = 0
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in dic:
                res = max(res, i + 1 - dic[pre_sum - k])
            if pre_sum not in dic:
                dic[pre_sum] = i + 1
        return res

nums = [1,-1,5,-2,3]
k = 3

s = Solution()
r = s.maxSubArrayLen(nums,k)

print(r)