# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，
# 返回 -1。

from typing import List
    
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
                    
                    
test = Solution()
coins = [1,3,5]
amount = 11

result = test.coinChange(coins, amount)

print(result)
