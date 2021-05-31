

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
        
        pass
    
    
s = Solution_Loop()
sample = "ac"

print(s.longestPalindrome(sample))   