from typing import List

# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.=
# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        a, b, c = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            a, b, c = min(b, c) + costs[i][0], min(a, c) + costs[i][1], \
            min(a, b) + costs[i][2]   
        return min(a, b, c)



s = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]

r = s.minCost(costs)
print(r)