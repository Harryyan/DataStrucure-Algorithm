class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        
        if s[0] == '0': return 0
        
        dp[0] = 1
        
        if int(s[:2]) == 10: dp[1] = 1
        
        if 10 < int(s[:2]) <= 26:
            dp[1] = 2
        
        for i in range(2, len(s)):
            if s[i] != '0' and s[i-1] != '0' and  1 <= int(s[i-1:2]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                if s[i-1] == '0' and s[i] == '0':
                    dp[i] = max(0, dp[i-1] - 2)
                elif s[i] == '0':
                    dp[i] = max(dp[i-1] - 1, 0)
                else:
                    dp[i] = dp[i-1]
                
            print(dp)
        
        return dp[-1]
    
    
s = '226'
test = Solution()

r = test.numDecodings(s)

print(r)