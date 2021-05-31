

# 给你一个字符串 s，找到 s 中最长的回文子串。
# abacd: reutrn aba
 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        
        for i in range(0, n):
            for j in range(0, i):
                dp[i] = max(self.palindrome(j,i,s), dp[i])
        
        print(dp)
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
    
    
s = Solution()
sample = "ac"

print(s.longestPalindrome(sample))    