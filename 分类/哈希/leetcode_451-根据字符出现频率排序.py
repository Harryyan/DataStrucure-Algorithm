from typing import Counter

# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

class Solution:
    def frequencySort(self, s: str) -> str:
        dict = Counter(s).most_common(len(s))
        result = ""

        for item in dict:
            for i in range(0, item[1]):
                result += item[0]

        return result


s = Solution()
str = "cccaaa"

s.frequencySort(str)