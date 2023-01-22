//
//  Leetcode_200.swift
//  Leetcode
//
//  Created by Harry on 2/06/22.
//

import Foundation

class Solution_200_DSU {
    func numIslands(_ grid: [[Character]]) -> Int {
        var zeros = 0
        let cols = grid[0].count
        let rows = grid.count
        let dsu = DSU(rows * cols)

        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == "1" {
                    // only check right and bottom
                    let directions = [[0,1], [1,0]]

                    for direction in directions {
                        let newX = i + direction[0]
                        let newY = j + direction[1]

                        let index1 = i * cols + j
                        let index2 = newX * cols + newY

                        if newX<rows && newY < cols && grid[newX][newY] == "1" {
                            dsu.union(index1, index2)
                        }
                    }
                } else {
                    zeros += 1
                }
            }
        }

        return dsu.count - zeros
    }
}

final class DSU {
    var parents: [Int] = []
    var count = 0

    init(_ n: Int) {
        parents = Array(repeating: 0, count: n)
        count = n

        for i in 0..<n {
            parents[i] = i
        }
    }

    func union(_ x: Int, _ y: Int) {
        let rootX = find(x)
        let rootY = find(y)

        guard rootX != rootY else { return }

        parents[rootY] = rootX
        count -= 1
    }

    func find(_ x: Int) -> Int {
        guard x != parents[x] else { return x }

        var current = x

        while current != parents[current] {
            current = parents[current]
        }

        return current
    }
}
