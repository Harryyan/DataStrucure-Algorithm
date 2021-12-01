from typing import List

# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two 
# non-equal elements are trivially wiggle sequences.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive,
#  and the second is not because its last difference is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements 
# in their original order.

# Given an integer array nums, return the length of the longest wiggle subsequence of nums.


class Solution:
    # tc: O(n)
    # sc: O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1

        return max(up, down)

# 贪心
class Solution:
    # tc: O(n)
    # sc: O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res, trend = 1, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and trend <= 0:
                res += 1
                trend = 1
            elif nums[i] < nums[i-1] and trend >= 0:
                res += 1
                trend = -1
        return res


nums = [1,17,5,10,13,15,10,5,16,8]
s = Solution()

r = s.wiggleMaxLength(nums)

print(r)