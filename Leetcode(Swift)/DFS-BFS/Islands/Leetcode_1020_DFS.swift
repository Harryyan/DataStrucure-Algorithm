//
//  Leetcode_1020.swift
//  Leetcode
//
//  Created by Harry on 5/06/22.
//

import Foundation

class Solution_1020_DFS {
    var m: Int = 0
    var n: Int = 0
    var visited: [[Bool]] = []
    
    func numEnclaves(_ grid: [[Int]]) -> Int {
        m = grid.count
        n = grid.first?.count ?? 0
        visited = Array(repeating: Array(repeating: false, count: n), count: m)
        
        var i = 0
        while i < m {
            dfs(grid, i, 0)
            dfs(grid, i, n - 1)
            i += 1
        }
        
        i = 1
        while i < n - 1 {
            dfs(grid, 0, i)
            dfs(grid, m - 1, i)
            i += 1
        }
        
        var enclaves = 0
        i = 1
        while i < m - 1 {
            var j = 1
            while j < n - 1 {
                if grid[i][j] == 1 && !visited[i][j] {
                    enclaves += 1
                }
                j += 1
            }
            i += 1
        }
        return enclaves
    }
    
    func dfs(_ grid: [[Int]], _ row: Int, _ col: Int) {
        if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == 0 || visited[row][col]) {
            return;
        }
        visited[row][col] = true;
        dfs(grid, row - 1, col);
        dfs(grid, row + 1, col);
        dfs(grid, row, col - 1);
        dfs(grid, row, col + 1);
    }
}
