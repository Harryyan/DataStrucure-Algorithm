//
//  Leetcode_1254.swift
//  Leetcode
//
//  Created by Harry on 5/06/22.
//

import Foundation

class Solution_1254_DFS {
    func dfs(_ grid: inout [[Int]], row: Int, colum: Int) -> Bool {
        if row < 0 || colum < 0 || row >= grid.count || colum >= grid[0].count {
            return false;
        }
        
        if grid[row][colum] == 1 {
            return true;
        }

        grid[row][colum] = 1
        
        let up = dfs(&grid,row: row-1,colum: colum)
        let down = dfs(&grid,row: row+1,colum: colum)
        let left = dfs(&grid,row: row,colum: colum-1)
        let right = dfs(&grid,row: row,colum: colum+1)
        
        return up && down && left && right;
    }
    
    func closedIsland(_ grid: [[Int]]) -> Int {
        var res = 0
        var grid = grid

        for row in 0..<grid.count {
            for colum in 0..<grid[0].count {
                if grid[row][colum] == 0 {
                    if dfs(&grid, row: row, colum: colum) {
                        res += 1
                    }
                }
            }
        }
        
        return res
    }
}
