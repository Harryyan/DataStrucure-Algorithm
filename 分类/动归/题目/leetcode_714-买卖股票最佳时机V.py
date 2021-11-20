from typing import List

# You are given an array prices where prices[i] is the price of a given stock on the ith day, 
# and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete 
# as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# leetcode - 714

class Solution:
    # tc: O(n)
    # sc: O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        if n == 0: return 0

        profit_0 = 0
        profit_1 = -prices[0] - fee

        for i in range(1, n):
            temp_0 = max(profit_0, profit_1+prices[i])
            temp_1 = max(profit_1, profit_0 - prices[i] - fee)

            profit_0 = temp_0
            profit_1 = temp_1

        return profit_0


prices = [1, 3, 2, 8, 4, 9]
fee = 2

s = Solution()
r = s.maxProfit(prices, fee)

print(r)