import collections
from typing import List

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
    
