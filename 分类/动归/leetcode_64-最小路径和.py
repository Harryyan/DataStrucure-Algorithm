from typing import List

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        # 列
        m = len(grid[0])
        # 行
        n = len(grid)  

        min_dist = [[0] * m for _ in range(n)]
        
        min_dist[0][0] = grid[0][0]

        for j in range(1, m):
            min_dist[0][j] = grid[0][j] + min_dist[0][j-1]

        for i in range(1, n):
            min_dist[i][0] = grid[i][0] + min_dist[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                min_dist[i][j] = grid[i][j] + min(min_dist[i][j-1], min_dist[i-1][j])
        
        return min_dist[-1][-1]

grid = [[1,2,3],[4,5,6]]
s = Solution()

r = s.minPathSum(grid)