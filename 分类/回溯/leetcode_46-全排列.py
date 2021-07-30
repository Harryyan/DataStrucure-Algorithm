from typing import List
from itertools import permutations
import collections

# 给定一个没有重复数字的序列，返回其所有可能的全排列。


class Solution:

    _result = []

    def _permute(self, k, nums):
        if k == 1:
            print(nums)
            self._result.append(nums[:])

        i = 0
        while i < k:
            nums[i], nums[k - 1] = nums[k - 1], nums[i]

            self._permute(k - 1, nums)

            nums[i], nums[k - 1] = nums[k - 1], nums[i]

            i += 1

    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        n = k

        self._permute(k, nums)

        return self._result

    def system_permutation(self, nums):
        return permutations(nums)

    def pprint(self):
        print(self._result)
        
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        check = [0 for i in range(len(nums))]
        self.backtrack([], nums, check)
        
        return self.res
    
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            print(sol, end='\t')
            print(i)
            check[i] = 0


test = Solution2()
data = [1,2,3]
r = test.permute(data)


