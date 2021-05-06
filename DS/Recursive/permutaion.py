from typing import List

# 给定一个没有重复数字的序列，返回其所有可能的全排列。


class Solution:

    _result = []

    def _permute(self, n, k, nums):
        if k == 1:
            self._result.append(nums)

        i = 0
        while i < k:
            nums[i], nums[k - 1] = nums[k - 1], nums[i]
            self._permute(n, k - 1, nums)
            nums[i], nums[k - 1] = nums[k - 1], nums[i]

            i += 1

    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        n = k

        return result
