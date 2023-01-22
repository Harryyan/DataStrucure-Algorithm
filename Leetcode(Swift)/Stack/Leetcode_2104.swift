//
//  Leetcode_2104.swift
//  Leetcode
//
//  Created by Harry on 24/05/22.
//

import Foundation

class Solution_2104 {
    // tc: O(n)
    // sc: O(n)
    // time: 1 + 3（暴力）
    // time： 1 + 17 (单调栈)
    func subArrayRanges(_ nums: [Int]) -> Int {
        // 元素作为最小值
        var lsmall = Array(repeating: 0, count:nums.count)
        var rsmall = Array(repeating: 0, count:nums.count)

        // 元素作为最大值
        var llarge = Array(repeating: 0, count:nums.count)
        var rlarge = Array(repeating: 0, count:nums.count)

        var stack: [Int] = []

        // 找每个元素左边第一个小于其的元素坐标，如果左侧没有，则为-1
        stack.append(-1)

        for i in 0..<nums.count {
            while stack.last! != -1 && nums[stack.last!] >= nums[i] {
                stack.removeLast()
            }

            lsmall[i] = stack.last!
            stack.append(i)
        }

        // 找每个元素右边第一个小于或者等于其的元素坐标，如果右侧没有，则为数组长度n (避免重复计算)
        stack = []
        stack.append(nums.count)

        for i in stride(from: nums.count-1, through: 0, by: -1) {
            while stack.last! != nums.count && nums[stack.last!] > nums[i] {
                stack.removeLast()
            }

            rsmall[i] = stack.last!
            stack.append(i)
        }

        // 找每个元素左边第一个大于其的元素坐标，如果左侧没有，则为-1
        stack = []
        stack.append(-1)

        for i in 0..<nums.count {
            while stack.last! != -1 && nums[stack.last!] <= nums[i] {
                stack.removeLast()
            }

            llarge[i] = stack.last!
            stack.append(i)
        }

        // 找每个元素右边第一个大于或者等于其的元素坐标，如果左侧没有，则为数组长度n (避免重复计算)
        stack = []
        stack.append(nums.count)

       for i in stride(from: nums.count-1, through: 0, by: -1) {
            while stack.last! != nums.count && nums[stack.last!] < nums[i] {
                stack.removeLast()
            }

            rlarge[i] = stack.last!
            stack.append(i)
        }

        var ans = 0
        for i in 0..<nums.count {
            ans += nums[i] * (i-llarge[i]) * (rlarge[i]-i)
            ans -= nums[i] * (i-lsmall[i]) * (rsmall[i]-i)
        }

        return ans
    }
}
