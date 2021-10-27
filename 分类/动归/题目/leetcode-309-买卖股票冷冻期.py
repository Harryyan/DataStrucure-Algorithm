from typing import List

# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

# leetcode - 309

class Solution:

    # 时间复杂度: O(n)
    # 空间复杂度: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [0] * 5
        
        # dp[0]代表: 持有/当天买
        # dp[1]代表: 持有/之前买
        # dp[2]代表: 不持有/当天卖
        # dp[3]代表: 不持有/不买不卖
        # dp[4]代表: 冷冻
        dp[0] = -prices[0]
        dp[1] = -prices[0]
        dp[2] = 0
        dp[3] = 0
        dp[4] = 0

        for i in range(1, n):
            buy_today = dp[0]
            buy_before = dp[1]
            sell_today = dp[2]
            do_nothing = dp[3]
            frezze = dp[4]

            dp[0] = max(-prices[i], frezze - prices[i], do_nothing - prices[i])
            dp[1] = max(buy_today, buy_before)
            dp[2] = max(prices[i] + buy_today, prices[i] + buy_before, sell_today)
            dp[3] = max(0, sell_today)
            dp[4] = sell_today

        return dp[2]
    

prices = [1,0,2,3,0,4,2,0]
s = Solution()

r = s.maxProfit(prices)
print(r)