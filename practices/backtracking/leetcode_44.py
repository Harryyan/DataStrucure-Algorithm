# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）

# 两个字符串完全匹配才算匹配成功。

# 说明:
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。


class Solution:
    matched = False
    pattern = ""
    
    def isMatch(self, s: str, p: str) -> bool:
        if not s and p: return False
        if not p and s: return False
        if not p and not s: return True
        
        self.pattern = p
        
        self.rMatch(0,0,s,len(s))
        
        return self.matched
    
    def rMatch(self, ti, pj, s, tlen):
        if self.matched: return
        if pj == len(self.pattern):
            if ti == tlen-1: self.matched = True
            return
        
        if self.pattern[pj] == "*":
            for k in range(0, tlen-ti):
                self.rMatch(ti+k, pj+1, s, tlen)
            
        elif ti < tlen and self.pattern[pj] == s[ti] or self.pattern[pj] == "?":
            self.rMatch(ti+1,pj+1,s,tlen)
            
        
s = Solution()
text = "a"
pattern = "***"

print(s.isMatch(text,pattern))