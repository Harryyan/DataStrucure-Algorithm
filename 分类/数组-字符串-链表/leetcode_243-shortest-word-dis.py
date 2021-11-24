from typing import List

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.

class Solution:
    # tc: O(n)
    # sc: O(1)
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        dict = {}

        dict[word1] = -1
        dict[word2] = -1
        dis = 10 ** 5

        for i in range(n):
            if wordsDict[i] == word1:
                dict[word1] = i

            if wordsDict[i] == word2:
                dict[word2] = i

            if dict[word2] != -1 and dict[word1] != -1:
                dis = min(dis, abs(dict[word2] - dict[word1]))

        return dis

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

s = Solution()
r = s.shortestDistance(wordsDict, word1, word2)

print(r)