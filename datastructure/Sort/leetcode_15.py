from typing import List

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 
# a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) < 3: return []
        
        
        
        
        return [[0]]