from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b

s = Solution()
nums = [4,4,0,1,0,2]
val = 2

r = s.removeElement(nums, val)
print(r)
print(nums[:r])