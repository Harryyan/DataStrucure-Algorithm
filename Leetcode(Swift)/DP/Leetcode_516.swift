//
//  Leetcode_516.swift
//  Leetcode
//
//  Created by Harry on 10/05/22.
//

import Foundation

class Solution_516 {
    func longestPalindromeSubseq(_ s: String) -> Int {
        let len = s.count
        var dp = Array(repeating: Array(repeating: 0, count: len), count: len)
        var list = Array(s)

        for i in 0..<len {
            dp[i][i] = 1

            for j in stride(from: i-1, through: 0, by: -1) {
                if i > 0 {
                    if list[i] == list[j] {
                        dp[j][i] = dp[j+1][i-1] + 2
                    } else {
                        dp[j][i] = max(dp[j+1][i], dp[j][i-1])
                    }
                }
            }
        }

        return dp[0][len-1]
    }
}
