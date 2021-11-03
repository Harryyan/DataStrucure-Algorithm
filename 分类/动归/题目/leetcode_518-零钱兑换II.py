from typing import List

# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 假设每一种面额的硬币有无限个。 
# 题目数据保证结果符合 32 位带符号整数。

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp 含义，前i种零钱可以凑出j种金额的方法数
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        # 初始化，前0种（没有钱）可以凑出金额为0的方法数位1种。就是啥都不凑就行
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j]+ dp[i][j-coins[i-1]]     # 注意！！这里为完全背包问题写法
                    # dp[i][j] = dp[i-1][j]+ dp[i-1][j-coins[i-1]]  # 若为0-1背包问题，应该如何写
                else:
                    dp[i][j] = dp[i-1][j]
            #print(dp)
        return dp[-1][-1]

s = Solution()
coins = [3]
amount = 3

result = s.change(amount, coins)
print(result)