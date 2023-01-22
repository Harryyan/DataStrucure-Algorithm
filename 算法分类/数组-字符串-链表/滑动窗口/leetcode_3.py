
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = maxLen = 0
        for i, c in enumerate(s):
            if c in hashmap:
                left = max(left, hashmap[c] + 1)
                print(left)
            hashmap[c] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen


s = "abba"
so = Solution()

r = so.lengthOfLongestSubstring(s)

print(r)