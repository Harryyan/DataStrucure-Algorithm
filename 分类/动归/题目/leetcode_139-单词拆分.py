from typing import List

# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for i in range(len(s)+1)]
        dp[0]=True

        for i in range(len(s)):
            if dp[i]==True:
                for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j]=True
        
        return dp[-1]