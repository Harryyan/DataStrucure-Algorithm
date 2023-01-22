from typing import Counter, List
# 滑动窗口 + 数组

# 因为字符串中的字符全是小写字母，可以用长度为26的数组记录字母出现的次数
# 设n = len(s), m = len(p)。记录p字符串的字母频次p_cnt，和s字符串前m个字母频次s_cnt
# 若p_cnt和s_cnt相等，则找到第一个异位词索引 0
# 继续遍历s字符串索引为[m, n)的字母，在s_cnt中每次增加一个新字母，去除一个旧字母
# 判断p_cnt和s_cnt是否相等，相等则在返回值res中新增异位词索引 i - m + 1

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for i in range(m):
            # ord函数找到对应字母的ascii值
            p_cnt[ord(p[i]) - ord('a')] += 1
            s_cnt[ord(s[i]) - ord('a')] += 1
        if s_cnt == p_cnt:
            res.append(0)
        
        for i in range(m, n):
            s_cnt[ord(s[i - m]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1
            if s_cnt == p_cnt:
                res.append(i - m + 1)
        return res
    