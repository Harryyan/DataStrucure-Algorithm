from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if not s: return res

        def backtrack(lastStr, paths):
            if len(lastStr) == 0:  # 如果字符串没有了，就代表分割完了
                res.append(paths[:])
                return
            for i in range(len(lastStr)):
                first = lastStr[:i+1]
                last = lastStr[i+1:]
                if not self.isPalindrome(first):continue
                paths.append(first)
                backtrack(last,paths)
                paths.pop()

        backtrack(s,[])
        return res
        
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True