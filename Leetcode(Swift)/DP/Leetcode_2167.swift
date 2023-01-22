/*
 You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.
 
 As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:
 
 Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
 Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
 Remove a train car from anywhere in the sequence which takes 2 units of time.
 Return the minimum time to remove all the cars containing illegal goods.
 
 Note that an empty sequence of cars is considered to have no cars containing illegal goods.
 
 */

import Foundation

class Solution_2167_2Dimensions {
    
    func minimumTime(_ s: String) -> Int {
        // Category s[i] as 3 different cases:
        // 1. prefix, which will be i+1
        // 2. middle, which should be 2
        // 3. postfix, which should be 1 as well
        
        // formular:
        //
        // dp[i][0] = i+1  if s[i] == 1
        // dp[i][1] = min(dp[i-1][0] + 1, String(ch) == "1" ? 2 : 0)
        // dp[i][2] = min(dp[i-1][1],dp[i-1][2]) + 1
        
        let sArr = Array(s)
        var dp:[[Int]] = Array(repeating: Array(repeating: 0, count: 3), count: s.count)
        
        dp[0][0] = String(sArr[0]) == "1" ? 1 : 0
        dp[0][1] = String(sArr[0]) == "1" ? 2 : 0
        dp[0][2] = String(sArr[0]) == "1" ? 1 : 0
        
        for i in 1..<s.count {
            let temp = String(sArr[i]) == "1" ? 2 : 0
            
            dp[i][0] = i + 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + temp
            dp[i][2] = min(dp[i-1][1],dp[i-1][2]) + 1
        }
        
        return min3(dp[s.count-1][0], dp[s.count-1][1], dp[s.count-1][2])
    }
    
    private func min3(_ a: Int, _ b: Int, _ c: Int) -> Int {
        min(min(a,b),c)
    }
}

class Solution_2167_1Deimension {
    
    func minimumTime(_ s: String) -> Int {
        // cause s lengh is 2 * 10^5
        var dp1 = 1000000
        var dp2 = 1000000
        let n = s.count
        
        let list = Array(s)
        
        for (i, ch) in list.enumerated() {
            let middle = String(ch) == "1" ? 2 : 0
            let pre = dp1
            
            dp1 = min(dp1, i) + middle
            dp2 = min(pre, dp2) + 1
        }
        
        return min(min(dp1, dp2), n)
    }
}
