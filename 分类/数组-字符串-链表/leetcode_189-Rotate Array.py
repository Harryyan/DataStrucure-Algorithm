from typing import List
# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    # tc: O(n)
    # sc: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))

        # move too much
        # for i in range(k, 0, -1):
        #     temp = nums.pop()
        #     nums.insert(0, temp)
