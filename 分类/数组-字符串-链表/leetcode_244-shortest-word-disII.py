# Design a data structure that will be initialized with a string array, and then it should answer queries of the 
# shortest distance between two different strings from the array.
# Implement the WordDistance class:

# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

from typing import List
import collections, bisect


class WordDistance:
    # tc: O(n)
    # sc: O(n)
    def __init__(self, wordsDict: List[str]):
        self.dic = collections.defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.dic[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        lst1 = self.dic[word1]
        lst2 = self.dic[word2]
        res = float('inf')
        for i in lst1:
            idx = bisect.bisect_left(lst2, i)
            if idx == 0:
                res = min(res, abs(lst2[0] - i))
            elif idx == len(lst2):
                res = min(res, abs(lst2[-1] - i))
            else:
                res = min(res, abs(lst2[idx] - i), abs(lst2[idx-1] - i))
        return res


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
obj = WordDistance(wordsDict)
r = obj.shortest(word1,word2)

print(r)