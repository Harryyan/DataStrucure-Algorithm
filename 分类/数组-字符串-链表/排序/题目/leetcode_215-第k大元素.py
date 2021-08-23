from typing import List

# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        n = len(nums)
        return nums[n-k]
    
    
nums = [3,2,1,5,6,4]
k = 2
 
s = Solution()
r = s.findKthLargest(nums, k)

print(r)