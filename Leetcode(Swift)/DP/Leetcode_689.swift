//
//  Leetcode_689.swift
//  Leetcode
//
//  Created by Harry on 19/03/22.
//

import Foundation

class Solution_689 {
    func maxSumOfThreeSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        let rows = (nums.count / k) + 1
        let cols = nums.count
        var result: [Int] = []

        var dp = Array(repeating: Array(repeating: 0, count: cols), count: rows)

        for i in 1..<rows {
            dp[i][k-1]=nums[0...k-1].reduce(.zero,+)
        }

        for i in 1..<rows {
            for j in k..<cols {
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + sumBetween(j, j-k, nums))
            }
        }

        var count = 0
        var max = dp[3].max() ?? 0

        while count < 3 {
            let endIndex = dp[3].firstIndex(where: { $0 == max}) ?? -1
            let startIndex = endIndex - k + 1
            result.append(startIndex)
            
            max -= nums[startIndex...endIndex].reduce(.zero,+)
            count += 1
        }

        result = result.reversed()

        return result
    }

    func sumBetween(_ end: Int, _ start: Int, _ nums: [Int]) -> Int {
        let a = nums[0...end].reduce(.zero,+)
        let b = nums[0...start].reduce(.zero,+)

        return a - b
    }
}
