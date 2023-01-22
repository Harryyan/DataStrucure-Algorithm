//
//  Leetcode_84.swift
//  Leetcode
//
//  Created by Harry on 14/03/22.
//

import Foundation

class Solution_84 {
    func largestRectangleArea(_ heights: [Int]) -> Int {
        let heights = [0] + heights + [0]
        var stack: [Int] = []
        var maxArea = 0
        
        for i in 0..<heights.count {
            while !stack.isEmpty && heights[i] < heights[stack.last!] {
                let currentHeight = heights[stack.removeLast()]
                let currentWidth = i - stack.last! - 1
                maxArea = max(currentWidth * currentHeight, maxArea)
            }
            
            stack.append(i)
        }
        
        return maxArea
    }
}
