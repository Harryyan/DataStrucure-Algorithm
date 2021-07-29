from typing import Deque, List

# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

# 返回矩阵中 省份 的数量。

# DFS

class Solution:
    
    def dfs(self, grid, i, j):    
        grid[i][j] = -1
        grid[j][i] = -1
        
        for x in range(len(grid)):
            if grid[j][x] == 1:
                self.dfs(grid, j, x)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
            n = len(isConnected)
            c = 0
            
            for i in range(n):
                for j in range(n):
                    if isConnected[i][j] == 1:
                        self.dfs(isConnected, i, j)
                        c += 1
            
            return c
        
        
 # DFS - advanced

class Solution2:
        def findCircleNum(self, isConnected: List[List[int]]) -> int:
            def dfs(i: int):
                for j in range(provinces):
                    if isConnected[i][j] == 1 and j not in visited:
                        visited.add(j)
                        dfs(j)
        
            provinces = len(isConnected)
            visited = set()
            circles = 0

            for i in range(provinces):
                if i not in visited:
                    dfs(i)
                    circles += 1
        
            return circles

 # BFS       
class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        N = len(isConnected)
        unvisited = [True] * N
        de = Deque()
        for i in range(N):
            if unvisited[i]:
                unvisited[i] = False
                count += 1
                de.append(i)
                while de:
                    city = de.popleft()
                    for j in range(N):
                        if isConnected[city][j] == 1 and unvisited[j]:
                            unvisited[j] = False
                            de.append(j)
        return count


        
        
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
s = Solution()

r = s.findCircleNum(isConnected)

print(r)