#给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

from functools import cmp_to_key
from typing import DefaultDict, List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        compare = lambda x, y: 1 if x + y <= y + x else -1
        nums_str = sorted(nums_str, key=cmp_to_key(compare))
        res = "".join(nums_str)
        
        if res[0] == "0":
            res = "0"
        return res
        
            
s = Solution()
sample = [3,30,34,5,9]
result = s.largestNumber(sample)

print(result)