# In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.
# You are given an integer n. There is originally an array consisting of n integers from 1 to n in ascending order, 
# return the number of derangements it can generate. Since the answer may be huge, return it modulo 109 + 7.

# leetcode 634
# 斐波那契数列变种

class Solution:
    # tc: O(n)
    # sc: O(n)
    def findDerangement(self, n: int) -> int:
        if n < 2: return 0

        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = (i - 1) * (dp[i-1] + dp[i-2])
            dp[i] = dp[i] % (10**9 + 7)

        return dp[-1]

class Solution_Opt:
    # tc: O(n)
    # sc: O(1)
    def findDerangement(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1
        mod, a, b = 10 ** 9 + 7, 1, 0
        for i in range(3, n+1):
            # update f(n-1) and f(n-2)
            a, b = (i-1) * (a + b) % mod, a
        return a


s = Solution_Opt()
r = s.findDerangement(3)

print(r)