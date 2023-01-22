//
//  Leetcode_464.swift
//  Leetcode
//
//  Created by Harry on 11/04/22.
//

import Foundation

class Solution_464 {
    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        if maxChoosableInteger >= desiredTotal {
            return true
        }
            
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal {
            return false
        }
        
        var dp: [Bool?] = Array(repeating: nil, count: 1 << maxChoosableInteger)
        
        return dfs(0, maxChoosableInteger, desiredTotal, &dp)
    }
    
    private func dfs(_ state: Int, _ maxChoosableInteger: Int, _ desiredTotal: Int, _ dp: inout [Bool?]) -> Bool {
        if dp[state] != nil {
            return dp[state]!
        }
        
        for i in 1...maxChoosableInteger {
            let cur = 1 << (i - 1)
            
            if cur & state != 0 {
                continue
            }
            
            if i >= desiredTotal || dfs(cur | state, maxChoosableInteger, desiredTotal - i, &dp) == false {
                dp[state] = true
                
                return true
            }
        }
        
        dp[state] = false
        
        return false
    }
}
