# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        if n == 0 or m == 0:
            return 0
        
        dp = [0 for _ in range(m + 1)]
        
        for i in range(1, n + 1):
            left_up = 0 # 对角线
             
            for j in range(1, m + 1):
                up = dp[j]
                
                if text1[i-1] == text2[j-1]:
                    dp[j] = left_up + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
                
                left_up = up 
        
        return dp[-1]
    
      
    
s = Solution()
a = "aaa"
b = "aaaaa"

result = s.longestCommonSubsequence(a,b)
print(result)