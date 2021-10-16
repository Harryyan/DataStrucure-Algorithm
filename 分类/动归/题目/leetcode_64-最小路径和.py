from typing import List

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。

class Solution:
    # 时间复杂度: O(mn)
    # 空间复杂度: O(mn)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        # 行
        m = len(grid)
        # 列
        n = len(grid[0])  

        min_dist = [[0] * n for _ in range(m)]
        min_dist[0][0] = grid[0][0]

        # 初始化第0行数据
        for j in range(1, n):
            min_dist[0][j] = grid[0][j] + min_dist[0][j-1]

        # 初始化第0列数据
        for i in range(1, m):
            min_dist[i][0] = grid[i][0] + min_dist[i-1][0]

        # 从(1,1)开始逐步计算局部最优解
        for i in range(1, m):
            for j in range(1, n):
                min_dist[i][j] = grid[i][j] + min(min_dist[i][j-1], min_dist[i-1][j])
        
        return min_dist[-1][-1]

class Solution_Ace:
    # 时间复杂度: O(n)
    # 空间复杂度: O(mn)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        # 行
        m = len(grid)
        # 列
        n = len(grid[0]) 

        min_dis = [0] * n
        min_dis[0] = grid[0][0]

        for j in range(1,n):
            min_dis[j] = min_dis[j-1] + grid[0][j]

        for i in range(1,m):
            min_dis[0] += grid[i][0]

            for j in range(1,n):
                min_dis[j] = min(min_dis[j-1], min_dis[j]) + grid[i][j]
               
        return min_dis[-1]

# 第三种: 直接原地，每次更新grid[i][j]值

grid = [[1]]
s = Solution_Ace()

r = s.minPathSum(grid)
print(r)