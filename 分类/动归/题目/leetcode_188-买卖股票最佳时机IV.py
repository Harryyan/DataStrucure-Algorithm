from typing import List

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day,
#  and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions.
# Note: You may not engage in multiple transactions simultaneously 
# (i.e., you must sell the stock before you buy again).

# leetcode - 188

class Solution:
    # tc: O(nk)
    # sc: O(k)
    def _maxProfit(self, prices: List[int]) -> int:
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

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0: return 0

        if k >= n // 2:
            return self._maxProfit(prices)


        dp = [[0,0] for _ in range(k+1)]
        for i in range(k+1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]

        for i in range(1,n):
            for j in range(1, k+1):
                # 属于同一交易范畴
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])

        return dp[k][0]

k = 1
prices = [6,1,6,4,3,0,2]
s = Solution()

r = s.maxProfit(k, prices)
print(r)