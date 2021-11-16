from typing import List

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

class Solution:
    def isOverlapped(self, interval: List[int], newInterval: List[int]) -> bool:
        return not (interval[1] < newInterval[0] or interval[0] > newInterval[1])

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x: x[0])

        dp = [1] * n
        
        for i in range(1, n):
            for j in range(0, i):
                if not self.isOverlapped(pairs[i], pairs[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    dp[i] = max(dp[i], dp[j])
        return dp[-1]


pairs = [[1,2],[7,8],[4,5]]
s =Solution()

r = s.findLongestChain(pairs)
print(r)