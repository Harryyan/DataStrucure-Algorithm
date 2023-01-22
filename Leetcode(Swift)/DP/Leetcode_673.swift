/*
 Given an integer array nums, return the number of longest increasing subsequences.
 
 Notice that the sequence has to be strictly increasing.
 */

import Foundation

class Solution_673 {
    func findNumberOfLIS(_ nums: [Int]) -> Int {
        let len = nums.count
        
        guard len > 1 else { return 1 }
        
        var dp = Array(repeating: 1, count: len)
        var count =  Array(repeating: 1, count: len)
        var max_len = 0
        
        for i in 1..<len {
            for j in 0..<i {
                var temp: [Int] = []
                if nums[i] > nums[j] {
                    if dp[i] < dp[j] + 1 {
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                        
                        temp.append(nums[j])
                    } else if dp[i] == dp[j] + 1 {
                        count[i] += count[j]
                    }
                }
            }
            
            max_len = max(max_len, dp[i])
        }
        
        var res = 0
        for i in 0..<len {
            if dp[i] == max_len {
                res += count[i]
            }
        }
        
        return res
    }
}
