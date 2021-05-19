import collections
from typing import List

# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1
        result = 0
        sum = 0

        for i in range(0, len(nums)):
            sum += nums[i]
            
            x = sum - target
            result += pre_sum[x]
            pre_sum[sum] += 1
            
        return result
    
