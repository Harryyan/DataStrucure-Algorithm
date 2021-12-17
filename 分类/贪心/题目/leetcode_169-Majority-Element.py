from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0:
                count += 1
                flag = i
            elif i == flag:
                count += 1
            else:
                count -= 1
        return flag