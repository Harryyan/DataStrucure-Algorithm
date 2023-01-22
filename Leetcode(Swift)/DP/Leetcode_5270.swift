//
//  Leetcode_5270.swift
//  Leetcode
//
//  Created by Harry on 13/06/22.
//

import Foundation

class Solution {
    // tc: O(mn^2)
    // sc: O(n)
    // time: 4 + 9
    func minPathCost(_ grid: [[Int]], _ moveCost: [[Int]]) -> Int {
        var dp = Array(repeating: Int.max, count: grid[0].count)

        for i in 0..<grid[0].count {
            dp[i] = grid[0][i]
        }

        for i in 1..<grid.count {
            var tempDp = Array(repeating: Int.max, count: grid[0].count)

            for j in 0..<grid[0].count {
                for k in 0..<grid[0].count {
                    tempDp[j] = min(tempDp[j], dp[k]+moveCost[grid[i-1][k]][j]+grid[i][j])
                }
            }

            dp = tempDp
        }

        return dp.min()!
    }
}
