# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

# LeetCode- 260

from typing import List
from functools import reduce

class Solution:
    # TC: O(n)
    # SC: O(1)
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(lambda a, b: a ^ b, nums)

        # low bit 算法
        low_bit = x & -x

        num1, num2 = 0, 0

        for num in nums:
            # 分组
            if num & low_bit:
                num1 ^= num
            else:
                num2 ^= num 
        
        #  num1 = reduce(lambda a, b: a ^ b if b & x & -x else a, nums, 0) 
        #  return [num1, x ^ num1]

        return [num1, x ^ num1]

nums = [1,2,1,3,2,5]
s = Solution()

r = s.singleNumber(nums)