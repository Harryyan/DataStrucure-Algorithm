# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, 
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# leetcode - 279

class Solution:
    # overtime O(n^2)
    def numSquares(self, n: int) -> int:
        INF = 10 ** 5
        dp = [INF] * n

        for i in range(n):
            if (i+1) ** 2 <= n:
                dp[(i+1) ** 2 - 1] = 1

        for i in range(1, n):
            if dp[i] == 1:
                continue
            else:
                for j in range(i):
                    dp[i] = min(dp[i], dp[j]+dp[i-1-j])

        return dp[-1]

class Solution_Opt:
    # tc: O(n * 0.5 * n)
    # sc: O(n)
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            # reduce iterations
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]

n = 1
s = Solution()

r = s.numSquares(n)
print(r)