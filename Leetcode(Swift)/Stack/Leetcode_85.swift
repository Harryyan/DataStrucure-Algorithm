//
//  Leetcode_85.swift
//  Leetcode
//
//  Created by Harry on 19/03/22.
//

import Foundation

class Solution_85 {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        var heights: [[Int]] = []
        for row in 0..<matrix.count {
            heights.append([])
            for col in 0..<matrix[0].count {
                if row == 0 {
                    heights[row].append(matrix[row][col] == "1" ? 1 : 0)
                } else {
                    if matrix[row][col] == "0" {
                        heights[row].append(0)
                    } else {
                        heights[row].append(heights[row - 1][col] + 1)
                    }
                }
            }
        }
        
        var maxArea = 0
        for height in heights {
            maxArea = max(maxArea, calcMaxArea(row: height))
        }
        return maxArea
    }
    
    func calcMaxArea(row: [Int]) -> Int {
        var stack = [Int]()
        
        var maxArea = 0
        for index in 0..<row.count {
            let height = row[index]
            
            while let last = stack.last, row[last] >= height {
                _ = stack.popLast()
                let width = index - (stack.last ?? -1) - 1
                maxArea = max(maxArea, row[last] * width)
            }
            
            stack.append(index)
        }
        
        while let pop = stack.popLast() {
            let height = row[pop]
            let width = row.count - (stack.last ?? -1) - 1
            maxArea = max(maxArea, height * width)
        }
        
        return maxArea
    }
}
