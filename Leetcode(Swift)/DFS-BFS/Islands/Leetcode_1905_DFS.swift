//
//  Leetcode_1905.swift
//  Leetcode
//
//  Created by Harry on 5/06/22.
//

import Foundation

class Solution_1905_DFS {
    func countSubIslands(_ grid1: [[Int]], _ grid2: [[Int]]) -> Int {
        let m = grid1.count
        let n = grid1[0].count
        var grid = grid2
        
        for i in 0..<m {
            for j in 0..<n {
                if grid1[i][j] == 0 && grid2[i][j] == 1 {
                    dfs(grid: &grid, i: i, j: j)
                }
            }
        }
        
        var res = 0
        
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    res += 1
                    dfs(grid: &grid, i: i, j: j)
                }
            }
        }
        
        return res
    }
    
    func dfs(grid: inout [[Int]], i: Int, j: Int) {
        if i < 0 || j < 0 || i >= grid.count || j >= grid[0].count {
            return
        }
        if grid[i][j] == 0 {
            return
        }
        
        grid[i][j] = 0
        
        dfs(grid: &grid, i: i, j: j+1)
        dfs(grid: &grid, i: i+1, j: j)
        dfs(grid: &grid, i: i-1, j: j)
        dfs(grid: &grid, i: i, j: j-1)
    }
}
