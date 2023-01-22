//
//  Leetcode_711.swift
//  Leetcode
//
//  Created by Harry on 3/06/22.
//

import Foundation

class Solution_711_DFS {
    var visited = Set<[Int]>()
    var res = Set<Double>()
    var grids: [[Int]] = []
    let directions = [[0,1],[0,-1], [-1,0], [1,0]]

    func numDistinctIslands2(_ grid: [[Int]]) -> Int {
        grids = grid

        for i in 0..<grids.count {
            for j in 0..<grids[0].count {
                if grids[i][j] == 1 {
                    dfs(i,j)
                    hash()

                    visited = Set<[Int]>()
                }
            }
        }

        return res.count
    }

    private func dfs(_ x: Int, _ y: Int) {
        grids[x][y] = 0
        visited.insert([x,y])

        for direction in directions {
            let newX = x + direction[0]
            let newY = y + direction[1]

            if newX >= 0 && newX < grids.count && newY >= 0 && newY < grids[0].count && grids[newX][newY] == 1 {
                dfs(newX, newY)
            }
        }
    }

    private func hash() {
        var dist: Double = 0
        let list = Array(visited)

        for i in 0..<list.count {
            let x1 = list[i][0]
            let y1 = list[i][1]

            for j in i+1..<list.count {
                let x2 = list[j][0]
                let y2 = list[j][1]

                dist += sqrt(Double((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)))
            }
        }

        if res.count == 0 {
            res.insert(dist)
            return
        }

        for item in res {
            // 精度问题
            if String(item) == String(dist) { break }
            else {
                res.insert(dist)
            }
        }
    }
}
