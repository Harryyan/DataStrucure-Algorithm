//
//  Leetcode_647.swift
//  Leetcode
//
//  Created by Harry on 17/03/22.
//

import Foundation

class Solution_647 {
    func countSubstrings(_ s: String) -> Int {
        var dp = Array(repeating: Array(repeating: false, count: s.count), count: s.count)
        let list = Array(s)
        var result = 0
        
        for i in 0..<list.count {
            for j in 0...i {
                if String(list[i]) == String(list[j]) && (i - j <= 1 || dp[i-1][j+1]){
                    dp[i][j] = true
                    result += 1
                }
            }
        }
        
        return result
    }
}
