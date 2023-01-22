//
//  Leetcode_47.swift
//  Leetcode
//
//  Created by Harry on 19/04/22.
//

import Foundation

class Solution_47 {
    var res: [[Int]] = []
    
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        var selected: [Int] = Array(repeating: 0, count: nums.count)
        
        backtrack([], &selected, nums)
        
        return res
    }
    
    private func backtrack(_ sol: [Int], _ selected: inout [Int], _ nums: [Int]) {
        if sol.count == nums.count {
            res.append(sol)
            return
        }
        
        for i in 0..<nums.count {
            if selected[i] == 1 {
                continue
            }
            
            // avoid duplicated elements
            if i > 0 && nums[i] == nums[i-1] && selected[i-1] == 0 {
                continue
            }
            
            var solCopy = sol
            solCopy.append(nums[i])
            
            selected[i] = 1
            backtrack(solCopy, &selected, nums)
            selected[i] = 0
        }
    }
}
