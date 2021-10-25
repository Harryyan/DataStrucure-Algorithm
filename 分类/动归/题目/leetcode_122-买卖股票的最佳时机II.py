
from typing import DefaultDict, List

class Solution:
     def maxProfit(self, prices: List[int]) -> int:
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
            dp[0] = max(first, second + prices[i])
            dp[1] = max(second, first - prices[i])

        return dp[0]
    
s = Solution()
prices =  [7,6,4,3,1]

result = s.maxProfit(prices)
print(result)