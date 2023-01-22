from typing import DefaultDict, List

# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

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
prices =  [7,1,5,3,6,4]

result = s.maxProfit(prices)
print(result)