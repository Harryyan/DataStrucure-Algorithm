from typing import Counter

# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

class Solution:
    def frequencySort(self, s: str) -> str:
        dict = Counter(s).most_common()
        result = ''.join(c*x for x,c in dict)
        return result


s = Solution()
str = "cccaaa"

r = s.frequencySort(str)

print(r)