//
//  Leetcode_403.swift
//  Leetcode
//
//  Created by Harry Yan on 31/07/22.
//

import Foundation

class Solution_403 {
    var visited: [Int:Bool] = [:]
    
    // tc: O(n^2)
    // sc: O(n)
    func canCross(_ stones: [Int]) -> Bool {
        return dfs(stones, 0, 0)
    }
    
    private func dfs(_ stones: [Int], _ index: Int, _ k: Int) -> Bool {
        let key = index * 1000 + k
        
        if visited[key] != nil {
            return false
        } else {
            visited[key] = true
        }
        
        guard index < stones.count - 1 else { return true }
        
        for i in index+1..<stones.count {
            let gap = stones[i] - stones[index]
            
            if gap >= k-1 && gap <= k+1 {
                if dfs(stones, i, gap) {
                    return true
                }
            } else if gap > k+1 {
                return false
            }
        }
        
        return false
    }
}
