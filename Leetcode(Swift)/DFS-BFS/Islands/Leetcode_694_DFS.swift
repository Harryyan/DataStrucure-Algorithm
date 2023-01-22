//
//  Leetcode_694.swift
//  Leetcode
//
//  Created by Harry on 3/06/22.
//

import Foundation

class Solution_694 {
    let directions = [[0,1], [0,-1], [1,0], [-1,0]]
    var grids: [[Int]] = []
    var set = Set<[Int]>()

    // tc: O(mn)
    // sc: O(mn)
    // time: 3 + 9
    func numDistinctIslands(_ grid: [[Int]]) -> Int {
        grids = grid
        var results = Set<Set<[Int]>>()

        for i in 0..<grids.count {
            for j in 0..<grids[0].count {
                if grids[i][j] == 1 {
                    dfs(i,j,i,j)
                    results.insert(set)

                    set = Set<[Int]>()
                }
            }
        }

        return results.count
    }

    private func dfs(_ x: Int, _ y: Int, _ originX: Int, _ originY: Int) {
        grids[x][y] = 0

        set.insert([x-originX, y-originY])

        for direction in directions {
            let newX = x + direction[0]
            let newY = y + direction[1]

            if newX >= 0 && newX < grids.count && newY >= 0 && newY < grids[0].count && grids[newX][newY] == 1 {
                dfs(newX,newY, originX, originY)
            }
        }
    }
}
