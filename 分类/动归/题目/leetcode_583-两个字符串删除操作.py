
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        
        # 多加一个哨兵，简化搜索
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        
        for i in range(1,len1+1):
            dp[i][0] = i
        for i in range(1,len2+1):
            dp[0][i] = i
            
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]
    
    
s1 = 'horse'
s2 = 'ros'

s = Solution()
r = s.minDistance(s1, s2)

print(r)