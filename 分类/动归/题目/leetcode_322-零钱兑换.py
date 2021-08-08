# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，
# 返回 -1。

# 你可以认为每种硬币的数量是无限的。

from typing import List
import math

class Solution_Advanced:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort()
        if amount < coins[0]: return -1
        
        dp = [math.inf for _ in range(0, amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
                    
        return dp[-1] if dp[-1] != math.inf else -1
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        
        if amount in coins:
            return 1
        
        state = [[False] * (amount + 1) for _ in range(amount+1)]
       
        # Init states
        for coin in coins:
            if amount >= coin:
                state[0][coin] = True  

        for i in range(1, amount+1):
            for j in range(1, amount+1):
                if state[i-1][j]:
                    
                    for coin in coins:
                        if j + coin == amount:
                            return i + 1
                        
                        if j + coin < amount:
                            state[i][j+coin] = True
                            
        return -1
                    
                    
test = Solution_Advanced()
coins = [2,3,6,7]
amount = 7

result = test.coinChange(coins, amount)

print(result)
