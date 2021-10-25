from typing import List

# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0.

# leetcode - 121

class Solution:

    # 时间复杂度: O(n)
    # 空间复杂度: O(1)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return None

        maxProfit = 0
        minPrice = float('inf')

        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProfit

prices = [7,1,5,3,6,4]

s = Solution()

r = s.maxProfit(prices)

print(r)