//
//  Leetcode_688.swift
//  Leetcode
//
//  Created by Harry on 10/06/22.
//

import Foundation

class Solution_688 {
    func knightProbability(_ n: Int, _ k: Int, _ row: Int, _ column: Int) -> Double {
        let directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        var dp: [[Double]] = Array(repeating: Array(repeating: 0, count: n), count: n)
        dp[row][column] = 1

        for _ in 0..<k {
            var temp: [[Double]] = Array(repeating: Array(repeating: 0.0, count: n), count: n)

            for m in 0..<n {
                for j in 0..<n {
                    for direction in directions {
                        let newX = m + direction.0
                        let newY = j + direction.1

                        guard newX >= 0 && newX < n && newY < n && newY >= 0 else { continue }

                        temp[newX][newY] += dp[m][j] / 8.0
                    }
                }
            }

            dp = temp
        }

        return dp.flatMap({$0}).reduce(.zero,+)
    }
}
