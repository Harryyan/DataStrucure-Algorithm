# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every character 
# in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

class Solution:
    # tc: O(m + n)
    # sc: O(c)  - 不同字符个数
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        need, window = {}, {}

        for c in t:
            need[c] = need.setdefault(c, 0) + 1    # need = {字符:出现次数}
        
        left, right = 0, 0
        valid = 0     # 验证window是否满足need条件，valid表示满足条件的字符个数
        start, length = 0, len(s)+1

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:         # 更新窗口数据
                window[c] = window.setdefault(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:   # 优化结果
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:     # 更新窗口数据
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start:start+length] if length != len(s)+1 else ''

s = "ADOBECODEBANC"
t = "ABC"

solution = Solution()
r = solution.minWindow(s,t)

print(r)