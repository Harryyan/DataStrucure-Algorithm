import Foundation

class Solution_2031 {
    // dp[i][0]: number of subarrays where have equal 0s and 1s, using preSum to get
    // dp[i][1] = dp[i-1][0] + dp[i-1][1] + 1 (if nums[i] == 1)
    // dp[i][1] = dp[i-1][1] - dp[i][0]       (if nums[i] == 0)
    
    // tc: O(n)
    // sc: O(n)
    func subarraysWithMoreZerosThanOnes(_ nums: [Int]) -> Int {
        let mod = 1000000007
        
        var sum = 0
        var res = 0
        let N = nums.count
        var dp = Array(repeating:Array(repeating:0,count:2),count:N+1)
        var dict: [Int:Int] = [:]
        dict[0] = 1 // prefix sum placeholder to avoid miss 1st
        
        for i in 1...N {
            let num = nums[i-1]
            sum += num == 1 ? 1 : -1
            
            dp[i][0] = dict[sum, default:0]
            
            if num == 1 {
                dp[i][1] = (dp[i-1][1] + dp[i-1][0] + 1) % mod
            } else {
                // avoid negative
                dp[i][1] = (dp[i-1][1] - dp[i][0] + mod) % mod
            }
            
            dict[sum, default:0] += 1
            
            res = (res+dp[i][1]) % mod
        }
        
        return res
    }
}
