from typing import List

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0 

        while right < n: 
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right += 1

        return nums

nums = [9,1,0,3,12]
s = Solution()

r = s.moveZeroes(nums)
print(r)