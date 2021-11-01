from typing import List

# 给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
# leetcode - 540

class Solution:
    # 时间复杂度: O(logn)
    # 空间复杂度: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if m % 2 == 1:
                m -= 1
            
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m

        return nums[l]

s = Solution()
nums = [3,3,7,7,10,11,11]
r = s.singleNonDuplicate(nums)

print(r)