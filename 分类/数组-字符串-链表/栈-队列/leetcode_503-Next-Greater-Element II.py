from typing import List

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next 
# in the array, which means you could search circularly to find its next greater number. 
# If it doesn't exist, return -1 for this number.

class Solution():
    # 核心在循环，取余数；double长度
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res