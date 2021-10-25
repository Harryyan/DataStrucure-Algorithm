# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 提示：a + b 意味着字符串 a 和 b 连接。

# leetcode - 97
class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)

        if(len1+len2 != len3):
            return False

        dp=[[False]*(len2+1) for i in range(len1+1)]

        # 哨兵
        dp[0][0]=True

        # 初始化第一行
        for i in range(1,len2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1]

        # 初始化第一列
        for j in range(1,len1+1):
            dp[j][0] = dp[j-1][0] and s1[j-1]==s3[j-1]

        # 动归方程
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                # 因为有两种选择方式: 哪个减1，就意味着哪个先选;
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        
        return dp[-1][-1]


s = Solution()
s1 = "aabcc"
s2 = "dbbca" 
s3 = "aadbbcbcac"

r = s.isInterleave(s1,s2,s3)

print(r)