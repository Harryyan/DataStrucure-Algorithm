from typing import List

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0

        m = len(obstacleGrid)
        dp = [[0 for _ in range(len(obstacleGrid[i]))] for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            n = len(obstacleGrid[i])
            for j in range(n):
                if not (i == 0 and j == 0):
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)    
                    else:
                        dp[i][j] = 0         

        return dp[-1][-1]


obstacleGrid = [[0,0],[1,1],[0,0]]
s = Solution()
r = s.uniquePathsWithObstacles(obstacleGrid)

print(r)