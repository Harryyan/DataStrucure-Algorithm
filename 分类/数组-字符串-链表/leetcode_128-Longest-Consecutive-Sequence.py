from typing import List

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    # tc: O(n)
    # sc: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for i in nums:
            # 只找每个片段开头
            if i-1 not in nums:
                j = i+1
                # 计算每个片段长度
                while j in nums:
                    j += 1

                res = max(res,j-i)

        return res


s = Solution()
nums = [100,4,200,1,3,2]

r = s.longestConsecutive(nums)

print(r)