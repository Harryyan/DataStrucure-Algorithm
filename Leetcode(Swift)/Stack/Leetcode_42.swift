//
//  Leetcode_42.swift
//  Leetcode
//
//  Created by Harry on 14/03/22.
//

import Foundation

class Solution_42 {
    func trap(_ height: [Int]) -> Int {
        var stack: [Int] = []
        var total = 0
        var pre = 0
        
        for i in 0..<height.count {
            while !stack.isEmpty && height[i] > height[stack.last!] {
                let last = stack.removeLast()
                pre = height[last]

                if stack.isEmpty { break }
                
                let curWidth = i - stack.last! - 1
                let relativeMinBarHeight = min(height[i], height[stack.last!])
                let curHeight = max(relativeMinBarHeight - pre, 0)

                total += curWidth * curHeight
            }
            
            stack.append(i)
        }
        
        return total
    }
}
