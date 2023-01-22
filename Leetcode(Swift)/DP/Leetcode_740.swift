//
//  Leetcode_740.swift
//  Leetcode
//
//  Created by Harry on 15/03/22.
//

import Foundation

class Solution_740 {
    func deleteAndEarn(_ nums: [Int]) -> Int {
        if nums.count == 1 { return nums[0] }
        
        let maxNumber = nums.max() ?? 1
        var counts: [Int] = Array(repeating: 0, count: maxNumber+1)
        
        for num in nums {
            counts[num] += 1
        }
        
        var dp = Array(repeating: 0, count: counts.count)
        dp[1] = counts[1]
        
        for i in 2..<counts.count {
            dp[i] = max(dp[i-1], dp[i-2]+i*counts[i])
        }
        
        return dp.last!
    }
}
