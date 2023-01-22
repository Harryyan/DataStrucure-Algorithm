from typing import List

# 峰值元素是指其值大于左右相邻值的元素。

# 给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞ 。


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        
        while(l<r):
            mid=(l+r) >> 1
            
            if(nums[mid]>nums[mid+1]):
                r=mid
            else:
                l=mid+1
                
        return l

nums = [1,2]
s = Solution()

r = s.findPeakElement(nums)

print(r)