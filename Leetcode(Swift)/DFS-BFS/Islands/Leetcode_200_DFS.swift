//
//  Leetcode_200_DFS.swift
//  Leetcode
//
//  Created by Harry on 2/06/22.
//

import Foundation

class Solution_200_DFS {
    var grid: [[Character]] = []
    
    func numIslands(_ grid: [[Character]]) -> Int {
        guard grid.count > 0 else { return 0 }
        
        var res = 0
        self.grid = grid
        
        for i in 0..<self.grid.count {
            for j in 0..<self.grid[0].count {
                if String(self.grid[i][j]) == "1" {
                    dfs(i,j)
                    
                    res += 1
                }
            }
        }
        
        return res
    }
    
    private func dfs(_ x: Int, _ y: Int) {
        let directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        grid[x][y] = Character("0")
        
        for direction in directions {
            let newX = x + direction[0]
            let newY = y + direction[1]
            
            if newX >= 0 && newX < grid.count && newY >= 0 && newY < grid[0].count && String(self.grid[newX][newY]) == "1" {
                dfs(newX, newY)
            }
        }
    }
}
