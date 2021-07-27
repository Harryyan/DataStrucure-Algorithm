from typing import List

class Solution:
    
    def dfs(self, grid, i, j):
        if not ( 0 <= i < len(grid) and 0 <= j < len(grid[i])):
            return
        
        if grid[i][j] != '1':
            return 
             
        grid[i][j] = -1
        
        self.dfs(grid, i-1,j)
        self.dfs(grid, i+1,j)
        
        self.dfs(grid, i,j-1)
        self.dfs(grid, i,j+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        m = len(grid)
        
        for i in range(m):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    
    
nums =  [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()

r = s.numIslands(nums)

print(r)