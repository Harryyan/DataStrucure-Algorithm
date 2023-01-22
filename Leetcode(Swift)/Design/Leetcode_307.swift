//
//  Leetcode_307.swift
//  Leetcode
//
//  Created by Harry on 19/05/22.
//

import Foundation

class NumArray {
    let tree: BIT
    var nums: [Int]
    
    init(_ nums: [Int]) {
        self.nums = nums
        tree = BIT(nums.count + 1)
        
        for i in 0 ..< nums.count {
            tree.update(i + 1, nums[i])
        }
    }
    
    func update(_ index: Int, _ val: Int) {
        tree.update(index + 1, val - nums[index])
        nums[index] = val
    }
    
    func sumRange(_ left: Int, _ right: Int) -> Int {
        return tree.query(right + 1) - tree.query(left)
    }
}

final class BIT {
    var tree: [Int]
    init(_ capacity: Int) {
        tree = Array(repeating: 0, count: capacity)
    }
    
    // parent = son + 2 ^ k (lowbit)
    func update(_ i: Int, _ delta: Int) {
        var index = i
        
        while index < tree.count {
            tree[index] += delta
            index += Self.lowbit(index)
        }
    }
    
    func query(_ i: Int) -> Int {
        var index = i
        var sum = 0
        
        while index > 0 {
            sum += tree[index]
            index -= Self.lowbit(index)
        }
        return sum
    }
    
    static func lowbit(_ i: Int) -> Int {
        return i & -i
    }
}
