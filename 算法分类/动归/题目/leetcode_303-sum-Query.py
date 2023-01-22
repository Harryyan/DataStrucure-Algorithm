from typing import List

# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between
# indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    # tc: O(n)
    # sc: O(n)
    def __init__(self, nums: List[int]):
        if not nums: return 

        n=len(nums)
        self.dp=[0]*(n+1)
        self.dp[1]=nums[0]

        for i in range(2,n+1):
            self.dp[i] = nums[i-1] + self.dp[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1]-self.dp[left]


nums = [-2, 0, 3, -5, 2, -1]
s = NumArray(nums)

r = s.sumRange(2,5)
print(r)