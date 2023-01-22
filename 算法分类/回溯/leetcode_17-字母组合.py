from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def backtrack(conbination,nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter,nextdigit[1:])

        res = []
        backtrack('',digits)
        return res
    

 
digits = "23"    
s = Solution()

r = s.letterCombinations(digits)

print(r)
     