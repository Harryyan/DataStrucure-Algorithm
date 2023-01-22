//
//  Leetcode_474.swift
//  Leetcode
//
//  Created by Harry on 17/03/22.
//

import Foundation


class Solution_474 {
    
    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n+1), count: m+1)
        
        for str in strs {
            let result = getZerosAndOnes(str: str)
            let zeros = result.0
            let ones = result.1
            for j in stride(from: m, through: zeros, by: -1) {
                for k in stride(from: n, through: ones, by: -1) {
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones] + 1)
                }
            }
        }
        
        return dp[m][n]
    }
    
    private func getZerosAndOnes(str: String) -> (Int, Int) {
        var count = 0
        for ch in str {
            if ch.wholeNumberValue == 1 {
                count += 1
            }
        }
        
        return (str.count - count, count)
    }
}
