//
//  Leetcode_85.swift
//  Leetcode
//
//  Created by Harry on 19/03/22.
//

import Foundation

class Solution_85_DP {
    
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        guard matrix.count > 0 else { return 0 }
        
        var dp = Array(repeating: Array(repeating: 0, count: matrix[0].count+1), count: matrix.count+1)
        var res = 0
        
        for i in 1...matrix.count {
            for j in 1...matrix[0].count {
                if matrix[i-1][j-1] == "1" {
                    dp[i][j] = dp[i][j-1] + 1
                    
                    var width = dp[i][j]
                    
                    for k in stride(from: i, to: 0, by: -1) {
                        width = min(width, dp[k][j])
                        
                        res = max(res, width * (i-k+1))
                    }
                }
            }
        }
        
        return res
    }
}
