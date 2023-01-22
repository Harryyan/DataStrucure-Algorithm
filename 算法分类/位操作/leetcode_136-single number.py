from typing import List

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    # tc: O(n)
    # sc: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            result ^= nums[i]

        return result

nums = [1,1,2,2,3,4,4]
s = Solution()

r = s.singleNumber(nums)
print(r)