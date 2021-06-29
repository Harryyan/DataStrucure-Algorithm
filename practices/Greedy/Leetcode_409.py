# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

import collections
from typing import DefaultDict, List

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        
        hash_table = collections.defaultdict(int)
        
        # 可以使用collection counter简化
        for i in s:
            hash_table[i] += 1
        
        count = 0
        added = False
        odd = False
        
        ordered = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
        hash_table = dict(ordered)
        
        for _, value in hash_table.items():
            if value > 1:
                if value % 2 == 0:
                    count += value
                else:
                    count += value - 1
                    odd = True
            else:
                if not added and not odd:
                    count += 1
                    added = True
                    
        if odd: count += 1
        
        return count

class Solution_1:
    def longestPalindrome(self, s: str) -> int:
        import collections
        # 1.统计各字符次数，eg:"ddsad":[3, 1, 1]
        count = collections.Counter(s).values()
        # 2.统计两两配对的字符总个数，eg: {"ddass":4,"ddsss":4}
        x = sum([item//2*2 for item in count if (item//2 > 0)])
        # 3.判断是否有没配对的单字符，有结果加一。 eg: {"ddss":4, "ddhjSS":4+1}-->{"ddss":4, "ddhjSS":5}
        return x if x == len(s) else x+1
           
        
        
s = Solution()
sample = "cccssds"
result = s.longestPalindrome(sample)

a = 9
print(a // 2)
count = collections.Counter(sample).values()
print(count)

print(result)