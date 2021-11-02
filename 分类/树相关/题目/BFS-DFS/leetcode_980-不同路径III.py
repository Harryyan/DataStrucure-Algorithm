# 在二维网格 grid 上，有 4 种类型的方格：

# 1  表示起始方格。且只有一个起始方格。
# 2  表示结束方格，且只有一个结束方格。
# 0  表示我们可以走过的空方格。
# -1 表示我们无法跨越的障碍。
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
# 每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

# leetcode - 980

from typing import List

class Solution:
    # 时间复杂度: O(row * col)
    # 空间复杂度: O(1)
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # 计算行数和列数

        def neighbours(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] % 2 == 0:  # 返回可以到达的位置
                    yield nr, nc

        # 非障碍格子数量
        zeros = 0
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value != -1: 
                    zeros += 1
                if value == 1:  
                    # 起始位置 
                    sr, sc = r, c
                if value == 2:   
                    # 结束位置
                    tr, tc = r, c

        self.path = 0

        def dfs(r, c, zeros):
            zeros -= 1

            if zeros < 0: 
                return
            if r == tr and c == tc:
                if zeros == 0:  
                    self.path += 1

                return

            # 访问过的
            grid[r][c] = -1

            for nr, nc in neighbours(r, c):
                dfs(nr, nc, zeros)
            
            # 重置
            grid[r][c] = 0 

        dfs(sr, sc, zeros)

        return self.path