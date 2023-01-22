from typing import List, DefaultDict
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume the input array always has a valid answer.

# 桶排序
# 分别插入奇数位和偶数位
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        dict = DefaultDict(int)

        for i in range(5001):
            dict[i] = 0

        for num in nums:
            dict[num] += 1

        small = 0
        big = 0
        m = len(nums)

        if m % 2 != 0:
            small = m-1
            big = m-2
        else:
            small = m-2
            big = m-1

        j = 5000

        for i in range(1, big+1, 2):
            while dict[j] == 0: j -= 1
            nums[i] = j
            dict[j] -= 1

        for i in range(0, small+1, 2):
            while dict[j] == 0: j -= 1
            nums[i] = j
            dict[j] -= 1

nums = [5,5,5,4,4,4]
s = Solution()

s.wiggleSort(nums)

print(nums)