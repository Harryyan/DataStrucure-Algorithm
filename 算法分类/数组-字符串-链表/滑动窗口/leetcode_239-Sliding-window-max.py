from typing import List
from collections import deque 

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to 
# the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# leetcode - 239

class Solution:
    # tc: o(n)
    # dc: O(k)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ret = deque(), []

        for i, j in enumerate(nums):
            while q and nums[q[-1]] < j:
                q.pop()

            if q and q[0] <= i - k:
                q.popleft()

            q.append(i)

            if i >= k - 1:
                ret.append(nums[q[0]])

        return ret

nums = [1,3,-1,-3,5,3,6,7]
k = 3

s = Solution()

r = s.maxSlidingWindow(nums, k)
print(r)