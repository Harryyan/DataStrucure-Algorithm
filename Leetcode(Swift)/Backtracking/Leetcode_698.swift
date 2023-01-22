//
//  Leetcode_698.swift
//  Leetcode
//
//  Created by Harry on 30/04/22.
//

import Foundation

class Solution_698 {
    func canPartitionKSubsets(_ nums: [Int], _ k: Int) -> Bool {
        let sum = nums.reduce(.zero, +)
        var group = k

        guard sum % k == 0 else { return false }

        let target = sum / k
        var nums = nums.sorted()
        var end = nums.count - 1

        guard nums[end] <= target else { return false }

        while end >= 0 && nums[end] == target {
            end -= 1
            group -= 1
        }

        let groups = Array(repeating: 0, count: group)

        return dfs(groups, end, nums, target)
    }

    private func dfs(_ groups: [Int], _ index: Int, _ nums: [Int], _ target: Int) -> Bool {
        guard index >= 0 else { return true }

        let value = nums[index]
        var index = index - 1
        var groups = groups

        for i in 0..<groups.count {
            if groups[i] + value <= target {
                groups[i] += value

                if dfs(groups, index, nums, target) { return true }

                groups[i] -= value
            }

            if groups[i] == 0 { break }
        }

        return false
    }
}
