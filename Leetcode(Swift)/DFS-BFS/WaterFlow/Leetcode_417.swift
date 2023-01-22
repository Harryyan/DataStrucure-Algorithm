//
//  Leetcode_417.swift
//  Leetcode
//
//  Created by Harry on 6/06/22.
//

import Foundation

class Solution_417 {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        let m = heights.count, n = heights[0].count
        var pac = Array(repeating: Array(repeating: false, count: n), count: m) //表示可以流向太平洋
        var atl = Array(repeating: Array(repeating: false, count: n), count: m) //表示可以流向大西洋
        var ans = [[Int]]()
        let dire = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in 0..<n {
            //上边界（可以流向太平洋）
            dfs(0, i, &pac)
            
            //下边界（可以流向大西洋）
            dfs(m-1, i, &atl)
        }
        
        for i in 0..<m {
            //左边界（可以流向太平洋）
            dfs(i, 0, &pac)
            
            //右边界（可以流向大西洋）
            dfs(i, n-1, &atl)
        }
        
        for i in 0..<m {
            for j in 0..<n {
                if pac[i][j] && atl[i][j] {
                    ans.append([i, j])
                }
            }
        }
        
        func dfs(_ x: Int, _ y: Int, _ grid: inout [[Bool]]) {
            if grid[x][y] {
                //已经访问过了
                return
            }
            grid[x][y] = true
            for d in dire {
                //访问上下左右，限制只能向高处访问
                let tx = x + d.0, ty = y + d.1
                if tx >= 0 && tx < m && ty >= 0 && ty < n && heights[x][y] <= heights[tx][ty] {
                    dfs(tx, ty, &grid)
                }
            }
        }
        
        return ans
    }
}
