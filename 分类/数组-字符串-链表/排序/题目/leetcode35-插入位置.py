from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]: return len(nums)
        if target < nums[0]: return 0
        
        start, end = 0, len(nums)-1
        mid = start + ((end - start) >> 1)
        result = False
        
        while start <= end:
            if nums[mid] == target:
                result = True
                break
            
            if nums[mid] < target:
                start = mid + 1
                
            if nums[mid] > target:
                end = mid - 1
                
            mid = start + ((end - start) >> 1)
            
        return mid if result else mid + 1
    
    
nums = [1,3,5,6]
target = 0

s = Solution()
r = s.searchInsert(nums, target)


print(r)
