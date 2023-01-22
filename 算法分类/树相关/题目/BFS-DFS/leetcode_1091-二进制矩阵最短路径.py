from typing import List

# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:  # 若起始点或终点堵塞，则不可能有这样的路径
            return -1
        if n == 1:
            return 1
        res = 1  # 注意题目的描述，是返回从 1 到 k 的路径，第一个节点被定为下标 1，
        path = deque()
        path.append([0, 0])  # 先压入起点
        while path:  # BFS模板
            for _ in range(len(path)):  # 对BFS的某一层的中所有点向8个方向进行扩展
                x, y = path.popleft()
                for new_x, new_y in [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1],
                                     [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]:
                    # 下面几种continue可以合并一行，这里为看的清楚就分开写了
                    if new_x == n - 1 and new_y == n - 1:  # 如果扩展的点到达了终点
                        return res + 1
                    if not 0 <= new_x < n or not 0 <= new_y < n:  # 扩展的点超出边界，则跳过
                        continue
                    if grid[new_x][new_y] == 1:  # 若扩展的点为阻塞，则跳过
                        continue
                    if grid[new_x][new_y] == -1:  # 若扩展的点已经访问过，则跳过
                        continue
                    if grid[new_x][new_y] == 0:  # 若为通畅点
                        grid[new_x][new_y] = -1  # 当前层次下已经访问该点
                        path.append([new_x, new_y])  # 将扩展的点加入path，到下一层的时候继续扩展
            res += 1  # 对某一层的元素都求判定过后，距离加1(同一个层次中的所有点的距离距离起点都是相等的）
        return -1
