from typing import List

# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.
# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.


class Solution:
    def minCostII(self,costs: List[List[int]]):
        n,k=len(costs),len(costs[0])
        dp=[[None]*k for _ in range(n)]
        # 初始化
        for j in range(k): dp[0][j]=costs[0][j]
        min_id=dp[0].index(min(dp[0]))
        # 迭代
        for i in range(1,n):
            for j in range(k):
                if j!=min_id: dp[i][j]=costs[i][j]+dp[i-1][min_id]
                else: dp[i][j]=costs[i][j]+min(dp[i-1][0:j]+ dp[i-1][j+1:])  
            min_id=dp[i].index(min(dp[i]))

        return min(dp[n-1])

costs = [[1,5,3],[2,9,4]]
s = Solution()

r  =s.minCostII(s)