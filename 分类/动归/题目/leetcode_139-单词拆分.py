from typing import List
from Trie import Trie

# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree = Trie()
        for word in wordDict:
            tree.insert(word)
                
        result = tree.search(s)
        print(result)
        
        return False



s = "applepenapple"
wordDict = ["apple", "pen"]

result = Solution()

result.wordBreak(s, wordDict)