from itertools import permutations
from typing import List

class Solution:
    # Approach one  将nums拆解，递归求解， 相当于每次将nums[0] 添加到其他所有的已有子集中。  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        
        res = self.subsets(nums[1:])
        
        print(res + [[nums[0]] + s for s in res])
        return res + [[nums[0]] + s for s in res]
    
        # res = [[]]
        # for i in nums:
        #     res += [ n + [i] for n in res]
        #     return res
    
    
nums = [1,2,3]

s = Solution()
s.subsets(nums)