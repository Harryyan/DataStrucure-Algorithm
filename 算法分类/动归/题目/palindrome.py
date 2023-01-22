# 给你一个字符串 s，找到 s 中最长的回文子串。
# abacd: reutrn aba
 
# 暴力解法 - 最坏情况时间复杂度退化严重 aaaaaaaaaaaaaaaaaaaaaaaaa
class Solution_Loop:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        
        for i in range(0, n):
            for j in range(0, i):
                dp[i] = max(self.palindrome(j,i,s), dp[i])
        
        endIndex = dp.index(max(dp))
        startIndex = endIndex - max(dp) + 1
             
        return s[startIndex:endIndex+1]
    
    
    def palindrome(self, i, j, s: str) -> int:
        x = j - i + 1
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return 0 
              
        return x
 
# dp(i, j) = max(dp(i+1,j-1), dp(i+1,j), dp(i, j-1))   
class Solution_DP:
    def longestPalindrome(self, s: str) -> str:
        if not s: return 0
        
        n = len(s)
        
        if n == 1: return s
        
        start = 0
        maxLeng = 1
        
        dp = [[0 for _ in range(0, n)] for _ in range(0,n)]
        
        for i in range(0, n):
            dp[i][i] = 1
        
        for i in range(1, n):
            for j in range(0, i+1):
                if s[i] == s[j]:
                    if i-j < 2:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j+1][i-1]
                else:
                    dp[j][i] = False
                    
                if dp[j][i] and i-j + 1 > maxLeng:
                    maxLeng = i - j + 1
                    start = j
        return s[start:start+maxLeng]
    
    
s = Solution_DP()
sample = "babad"

print(s.longestPalindrome(sample))   