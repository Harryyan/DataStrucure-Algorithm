import Foundation

/*
 You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
 
 Every post must be painted exactly one color.
 There cannot be three or more consecutive posts with the same color.
 Given the two integers n and k, return the number of ways you can paint the fence.
 */

final class Solution_276 {
    
    func numWays(_ n: Int, _ k: Int) -> Int {
        var dp: [Int] = Array(repeating: 0, count: n)
        
        dp[0] = k
        
        if n == 1 {
            return dp[0]
        }
        
        dp[1] = k * k
        
        for i in 2..<n {
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        }
        
        return dp[n-1]
    }
}
