//
//  Leetcode_238.swift
//  Leetcode
//
//  Created by Harry Yan on 31/07/22.
//

import Foundation


class Solution_238 {
    
    // tc: O(n)
    // sc: O(n)
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        
        left[0] = 1
        for i in 1..<n {
            left[i] = left[i-1] * nums[i-1]
        }
        
        right[n-1] = 1
        for j in stride(from: n-2, through:0, by:-1) {
            right[j] = right[j+1] * nums[j+1]
        }
        
        var ans: [Int] = []
        
        for i in 0..<n {
            ans.append(left[i] * right[i])
        }
        
        return ans
    }
    
    // tc: O(n)
    // sc: O(1)
    func productExceptSelf2(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        
        ans[0] = 1
        // 先初始化 - 从左到右
        for i in 1..<n {
            ans[i] = ans[i-1] * nums[i-1]
        }
        
        // 从右到左遍历一遍
        var right = 1
        for j in stride(from: n-1, through:0, by:-1) {
            ans[j] *= right
            right *= nums[j]
        }
        
        return ans
    }
}
