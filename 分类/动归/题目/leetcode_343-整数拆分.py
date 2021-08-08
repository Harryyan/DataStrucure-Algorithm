class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] = max(dp[i], max((i-j) * j, dp[i-j] * j))
        
        return dp[-1]
    
    
    
s = Solution()
n = 3

r = s.integerBreak(n)

print(r)