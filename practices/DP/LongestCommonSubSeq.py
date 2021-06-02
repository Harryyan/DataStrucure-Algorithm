


# 给定两个字符串 text1 和 text2，
# 返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        if n == 0 or m == 0:
            return 0
        
        dp = [0 for _ in range(m + 1)]
        
        for i in range(1, n + 1):
            left_up = 0 # 对角线
            dp[0] = 0
            
            for j in range(1, m + 1):
                left = dp[j-1]
                up = dp[j]
                
                if text1[i-1] == text2[j-1]:
                    dp[j] = left_up + 1
                else:
                    dp[j] = max([left, up])
                
                left_up = up 
        
        return dp[-1]
    
    
    
s = Solution()
a = "aaa"
b = "new zelaand"

result = s.longestCommonSubsequence(a,b)
print(result)