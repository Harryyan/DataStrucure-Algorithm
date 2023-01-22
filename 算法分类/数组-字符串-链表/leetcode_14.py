from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    # tc: O(c * n)
    # sc: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        count = len(strs[0])
        result = ""

        for str in strs:
            count = min(len(str), count)

        for i in range(count):
            anchor = strs[0][i]
            temp = 0

            for str in strs:
                if str[i] == anchor:
                    temp += 1

            if temp == n:
                result += anchor
            else: 
                break

        return result

strs = ["flower","flower","flower","flower"]
s = Solution()

r = s.longestCommonPrefix(strs)
print(r)