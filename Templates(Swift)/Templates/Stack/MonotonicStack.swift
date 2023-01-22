//
//  MonotonicStack.swift
//  Templates
//
//  Created by Harry Yan on 4/10/22.
//

import Foundation

// next greater element template I
func monotonicStackTemplate(_ nums: [Int]) -> [Int] {
    var res: [Int] = []
    var stack: [Int] = []
    
    for i in 0..<nums.count {
        while !stack.isEmpty && nums[stack.last!] < nums[i] {
            let index = stack.removeLast()
            res[index] = nums[i]
        }
        
        stack.append(i)
    }
    
    return res
}

// 还有一种是环形array, 需要取模
// next greater element template II
func nextGreaterElements(_ nums: [Int]) -> [Int] {
    let count = nums.count
    var stack: [Int] = []
    var result: [Int] = Array(repeating: -1, count: count)
    
    for i in 0..<count*2 {
        while stack.count > 0 && nums[stack.last!] < nums[i % count] {
            result[stack.popLast()!] = nums[i % count]
        }
        
        // 加入的index要取模
        stack.append(i % count)
    }
    
    return result
}
