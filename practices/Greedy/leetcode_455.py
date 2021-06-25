
from typing import DefaultDict, List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s: return 0
        
        g.sort()
        s.sort()
        
        step = 0
        n = len(g)
        m = len(s)
        i = j = 0
        
        while i < n and j < m:
            if s[j] >= g[i]:
                i +=1
                j +=1
                
                step += 1
                continue

            if s[j] < g[i]:
                j += 1
                
        return step
    

g = [1,2]
s = [1,2,3]
so = Solution()

result = so.findContentChildren(g,s)

print(result)