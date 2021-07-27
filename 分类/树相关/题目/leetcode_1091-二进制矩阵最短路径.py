from typing import List

# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        count = 0
        
        m = len(grid)
        
        for i in range(m):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    count += 1
        
        return count