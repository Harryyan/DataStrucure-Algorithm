//
//  Leetcode_221.swift
//  Leetcode
//
//  Created by Harry on 15/03/22.
//

import Foundation

class Solution_221 {
    
    func maximalSquare(_ matrix: [[Character]]) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: matrix[0].count+1), count: matrix.count+1)
        let rows = matrix.count
        let cols = matrix[0].count
        var edge = 0
        
        for i in 1..<rows+1 {
            for j in 1..<cols+1 {
                if String(matrix[i-1][j-1]) == "1" {
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]), dp[i-1][j-1]) + 1
                    edge = max(edge, dp[i][j])
                }
            }
        }
        
        return edge * edge
    }
}
