//
//  Leetcode_410.swift
//  Leetcode
//
//  Created by Harry on 4/04/22.
//

import Foundation

class Solution_410 {
    func splitArray(_ nums: [Int], _ m: Int) -> Int {
        let maxItem = nums.max()!
        let sum = nums.reduce(.zero, +)
        
        var left = maxItem
        var right = sum
        
        while left < right {
            let mid = left + (right - left) / 2
            var count = 1
            var sum = 0
            
            for i in 0..<nums.count {
                sum += nums[i]
                
                if sum <= mid {
                    continue
                } else {
                    sum = nums[i]
                    count += 1
                }
            }
            
            if count <= m {
                right = mid
            } else {
                left = mid + 1
            }
        }
        
        return left
    }
}
