from typing import List

# Given a character array s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

# Your code must solve the problem in-place, i.e. without allocating extra space.


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        slow =0
        k= len(s)
        half=k//2
        for i in range(half):s[i],s[~i] =s[~i],s[i]
        
        for f in range(k):
            if s[f] ==' ':
                s[slow:f] = s[slow:f][::-1]
                slow=f+1
        s[slow:f+1] =s[slow:f+1][::-1]  

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
so = Solution

r = so.reverseWords(s)

print(r)