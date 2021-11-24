from typing import List

# Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, 
# return the shortest distance between these two words in the list.
# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

class Solution:
    def shortestDistance_diff(self, wordsDict: List[str], word1: str, word2: str) -> int:
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

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 != word2:
            return self.shortestDistance_diff(wordsDict, word1, word2)
        else:
            p1 = -1
            p2 = -1
            n = len(wordsDict)
            result = 10 ** 6

            for i in range(n):
                if wordsDict[i] == word1 and p1 == -1:
                    p1 = i
                    continue

                if wordsDict[i] == word2 and p2 == -1:
                    p2 = i

                if p1 != -1 and p2 != -1:
                    result = min(result, abs(p1 - p2))
                    p1 = p2
                    p2 = -1

            return result

wordsDict = ["practice", "makes", "perfect", "coding", "makes", "makes"]
word1 = "makes"
word2 = "makes"


s = Solution()
r = s.shortestWordDistance(wordsDict, word1, word2)

print(r)