# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# leetcode 343

class Solution:

    # 时间复杂度: O(n²)
    # 空间复杂度: O(n)
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