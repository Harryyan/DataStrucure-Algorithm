//
//  Leetcode_526.swift
//  Leetcode
//
//  Created by Harry on 31/03/22.
//

import Foundation

class Solution_526 {
    
    func countArrangement(_ n: Int) -> Int {
        return dfs(n, 1, visited: 0)
    }
    
    private func dfs(_ n: Int, _ i: Int, visited: Int) -> Int {
        guard i <= n else { return 1 }
        
        var ans = 0
        
        for j in 1...n {
            if ((1 << j) & visited) == 0 && (j % i == 0 || i % j == 0) {
                ans += dfs(n, i+1, visited: visited | i << j)
            }
        }
        
        return ans
    }
}
