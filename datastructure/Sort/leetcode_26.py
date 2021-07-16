from typing import List

class Solution:
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
        
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()

r = s.removeDuplicates(nums)

print(r)