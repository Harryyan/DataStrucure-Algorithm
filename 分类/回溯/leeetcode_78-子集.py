from typing import List

class Solution:
    # Approach one  将nums拆解，递归求解， 相当于每次将nums[0] 添加到其他所有的已有子集中。  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # if not nums: return [[]]
        
        # #递归
        # res = self.subsets(nums[1:])
        
        # return res + [[nums[0]] + s for s in res]
    
        # 迭代
        res = [[]]
        for i in nums:
            res += [ n + [i] for n in res]
        print(res)
        return res
    
            
        
        # 库函数
        # res = []
        # for i in range(len(nums)+1):
        #     for tmp in itertools.combinations(nums, i):
        #         res.append(tmp)
        # return res   
    
nums = [1,2,2]

s = Solution()
s.subsets(nums)
