from typing import List

# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, 
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: None

        row = len(triangle)
        if row == 1: triangle[0][0]

        # save minimum value for each row
        dp = [0] * row

        # save minimum path
        path = [0] * row
        
        dp[0] = triangle[0][0]

        for i in range(1, row):
            column = len(triangle[i])

            for j in range(column):
                if i == j:
                    triangle[i][j] += triangle[i-1][j-1]
                elif j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])

            dp[i] = min(triangle[i])
            path[i] = triangle[i].index(dp[i])

        return dp[-1]


triangle = [[-1],[3,2],[-3,1,-1]]
s = Solution()

r = s.minimumTotal(triangle)

print(r)