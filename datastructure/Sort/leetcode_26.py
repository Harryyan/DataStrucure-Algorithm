from typing import List

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        
        pre = nums[0]
        
        i = 1
        while i < len(nums):
            if pre == nums[i]:
                nums.pop(i)
                continue  
                     
            pre = nums[i]
            i += 1 
            
        return len(nums)


# 双指针 -- 快，慢指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


      
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()

r = s.removeDuplicates(nums)

print(r)