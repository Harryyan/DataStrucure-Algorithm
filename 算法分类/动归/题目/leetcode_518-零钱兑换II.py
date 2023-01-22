from typing import List

# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 假设每一种面额的硬币有无限个。 
# 题目数据保证结果符合 32 位带符号整数。

# leetcode - 518

class Solution:
    # 时间复杂度: O(mn)
    # 空间复杂度: O(mn)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        dp[0][0] = 1

        row = len(coins)

        for i in range(1, row + 1):
            for j in range(amount + 1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

class Solution_Ace:
    # 时间复杂度: O(mn) - 但有优化
    # 空间复杂度: O(n)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]


s = Solution()
coins = [3]
amount = 3

result = s.change(amount, coins)
print(result)