from itertools import combinations,combinations_with_replacement
from typing import List


# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 排序 - 未来好剔除重复项
        nums.sort()
        
        res = [[]]
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: 
                temp = [ n + [nums[i]] for n in temp]
            else:
                temp = [ n + [nums[i]] for n in res]    
              
            res += temp 
        return res
    
    
    
s = Solution()
nums = [1,2,2]
r = s.subsetsWithDup(nums)
print(r)