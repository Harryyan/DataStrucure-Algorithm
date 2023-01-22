# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# 写法1：KMP算法，前缀表统一减一的实现方式
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        # hash表内容为needle的index，但是要注意重复字符的处理
        # 重复字符保留的是最后出现的那个index，因为此时step为最小值
        dic = {needle[_]: _ for _ in range(m)}
        i = 0

        while i < n - m + 1:
            if haystack[i:i + m] == needle:
                return i
            else:
                if i < n - m and haystack[i + m] in needle:
                    # step为i指针后移的步长
                    # 当haystack[i+m]在dic存在时，直接跳出step个步长
                    step = m - dic[haystack[i + m]]
                    print(dic)
                else:
                    # 当在dic不存在时，直接跳出m+1个步长
                    step = m + 1
                i += step
        return -1


haystack = "hll0o"
needle = "ll"

s = Solution()

r = s.strStr(haystack, needle)
print(r)