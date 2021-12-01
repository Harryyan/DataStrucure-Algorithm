from typing import List

# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# You may assume the input array always has a valid answer.


class Solution:
    # tc: O(n)
    # sc: O(1)
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n - 1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

nums = [3,5,2,1,6,4]
s = Solution()

r = s.wiggleSort(nums)
print(nums)