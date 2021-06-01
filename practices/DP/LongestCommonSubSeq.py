


# 给定两个字符串 text1 和 text2，
# 返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        if n == m == 1 and text1 == text2:
            return 1
        
        
        dp = [[ 0 for _ in range(0,n) ] for _ in range(0,m)]
        
        
        return 0