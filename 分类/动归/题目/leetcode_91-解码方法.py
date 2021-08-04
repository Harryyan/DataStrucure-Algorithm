class Solution:
    def numDecodings(self, s: str) -> int:            
        dp = [0] * len(s)
  
        if s[0] == '0': return 0
        
        if len(s) <= 1:
            return 1
        
        dp[0] = 1
         
        if 10 <= int(s[:2]) <= 26:
            if int(s[:2]) == 20 or int(s[:2]) == 10:
                dp[1] = 1
            else:
                dp[1] = 2
        elif s[1] == '0' and int(s[0]) > 2:
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s)):
            if s[i] != '0' and s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                if (s[i-1] == '0'and s[i] == '0') or (s[i] == '0' and int(s[i-1]) > 2):
                    dp[i] = 0
                elif s[i] == '0':
                    dp[i] = max(dp[i-2], 0)
                else:
                    dp[i] = dp[i-1]
            print(dp)    
        return dp[-1]
    
    
s = "301"
test = Solution()

r = test.numDecodings(s)

print(r)