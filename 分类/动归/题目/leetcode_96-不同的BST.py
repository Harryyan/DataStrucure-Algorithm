# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

class Solution_brute:
    # 时间复杂度：O(n的m次方) - m是层数 - 指数级复杂度
    # 空间复杂度：O(1)
    def numTrees(self, n: int) -> int:
        def dfs(n):
            if n <= 1:
                return 1
            ret = 0
            for i in range(1, n+1):
                ret += dfs(i-1) * dfs(n-i)
            return ret

        return dfs(n)

class Solution:
    # 时间复杂度：O(n²)
    # 空间复杂度：O(n)
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+2)]
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

# 也可利用数学公式，卡特兰数
# 时间复杂度: O(n)
# 空间复杂度: O(1)