//
//  Leetcode_6059.swift
//  Leetcode
//
//  Created by Harry on 8/05/22.
//

import Foundation

class Solution_6059 {
    func hasValidPath(_ grid: [[Character]]) -> Bool {
        let rows = grid.count
        let cols = grid[0].count

        guard String(grid[0][0]) == "(" else {
            return false
        }

        guard String(grid[rows-1][cols-1]) == ")" else {
            return false
        }

        var dp: [[Set<Int>]] = Array(repeating: Array(repeating: Set<Int>(), count: cols), count: rows)
        dp[0][0] = [1]

        for i in 1..<cols {
            let value = val(grid[0][i])

            for item in dp[0][i-1] {
                if value + item >= 0 {
                    dp[0][i].insert(value + item)
                }
            }
        }

        for i in 1..<rows {
            let value = val(grid[i][0])

            for item in dp[i-1][0] {
                if value + item >= 0 {
                    dp[i][0].insert(value + item)
                }
            }
        }

        for i in 1..<rows {
            for j in 1..<cols {
                let value = val(grid[i][j])

                for item in dp[i][j-1] {
                    if value + item >= 0 {
                        dp[i][j].insert(value + item)
                    }
                }

                for item in dp[i-1][j] {
                    if value + item >= 0 {
                        dp[i][j].insert(value + item)
                    }
                }
            }
        }

        if dp[rows-1][cols-1].contains(0) {
            return true
        } else {
            return false
        }
    }

    func val(_ ch: Character) -> Int {
        if String(ch) == "(" {
            return 1
        } else {
            return -1
        }
    }
}
