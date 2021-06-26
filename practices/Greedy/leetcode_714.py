
from typing import DefaultDict, List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 1: return 0
        
        n = len(prices)
        
        # 初始化dp数组
        # 第一个元素为不持有当天股票最大收益
        # 第二个元素为持有最大收益
        dp = [0, -prices[0]]
        
        for i in range(1, n):
            first = dp[0]
            second = dp[1]
            
            # 动归方程
            dp[0] = max(first, second + prices[i] - fee)
            dp[1] = max(second, first - prices[i])

        return dp[0]
    
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1] - fee
            if tmp > 0: profit += tmp
        return profit
    
    
s = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2

result = s.maxProfit(prices, fee)
print(result)