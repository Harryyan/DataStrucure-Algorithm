from typing import List
import bisect

# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

class Solution:
    # tc: O(n^2)
    # sc: O(n)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x: x[0])

        dp = [1] * n
        
        for i in range(1, n):
            for j in range(0, i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    dp[i] = max(dp[i], dp[j])
        return dp[-1]

class Solution_Bisect:
    # tc: O(nlogn)
    # sc: O(n)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        tail = [pairs[0][1]]

        for i in range(1, n):
            # 二分
            idx = bisect.bisect_left(tail, pairs[i][0])

            if idx == len(tail):
                tail.append(pairs[i][1])

            if pairs[i][1] < tail[idx]:
                # 这里其实也是贪心
                tail[idx] = pairs[i][1]

        return len(tail)

class Solution_Greedy:
    # tc: O(nlogn) - sorting
    # sc: O(n)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        pairs.sort(key=lambda x: x[1])
        count = 1
        cur = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > cur:
                count += 1
                cur = pairs[i][1]

        return count


pairs = [[1,8],[6,10],[9,12], [13,15]]
s =Solution_Greedy()

r = s.findLongestChain(pairs)
print(r)