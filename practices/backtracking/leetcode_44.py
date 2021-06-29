# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）

# 两个字符串完全匹配才算匹配成功。

# 说明:
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s = '0' + s # 便于初始化dp数组
        p = '0' + p
        s_len, p_len = len(s), len(p)

        # 初始化p_len * s_len的数组(dp[i][j]为处理至s[i]和p[j]处的匹配情况)
        dp = [[False for _ in range(p_len)] for _ in range(s_len)] # 不可以使用[[False] * m] * n !!
        # dp[0][0] = True，当s和p均为空时，恰好匹配
        # 其余的dp[i][0]保持为False，因为使用空p匹配非空字符串，结果为False
        dp[0][0] = True
        # dp[0][j]，因为只有星号可以匹配空字符串，当p的前j个均为星号时，dp[0][j] = True
        j = 1
        while j < p_len and p[j] == "*":
            dp[0][j] = True
            j += 1

        for i in range(1, s_len): # 遍历字符串s，需从1开始因为之前额外加了一个0
            for j in range(1, p_len): # 遍历pattern，需从1开始因为之前额外加了一个0
                if p[j] == s[i] or p[j] == '?': # 如相应字符相同，或对应pattern为'?'，匹配成功
                    dp[i][j] = dp[i-1][j-1] # 转移i-1,j-1到i,j
                elif p[j] == '*': # 以下情况都可以成功匹配，然后转移至dp[i][j]
                    # dp[i][j-1]： p[j-1]匹配了0个字符后更新一格变为p[j]，s[i]保持不变
                    # dp[i-1][j]： p[j]匹配了s[i-1]后不动，等待和下一个字符比较（下一轮也可以选择匹配0或1个），s[i-1]更新一格
                    dp[i][j] = (dp[i][j-1] or dp[i-1][j])
                # 不写else，即p[j]其余的情况。因为需要多轮比对，只有最终dp[-1][-1]还是无法得到True，才确认失败
                # 因为本例中星号可以“贪婪”或“非贪婪”匹配，即*a中的*可以匹配xabac中的x，也可以匹配xab，只有全部尝试后，才能确认最终结果
        return dp[-1][-1] # 进行了所有的尝试后，最终dp[-1][-1]是否可以得到True
        
s = Solution()
text = "aa"
pattern = "*"

print(s.isMatch(text,pattern))