import Foundation

/*
 You are given an integer array nums and an integer target.
 
 You want to build an expression out of nums by adding one of the symbols '+' and '-'
 before each integer in nums and then concatenate all the integers.
 
 For example, if nums = [2, 1], you can add a '+' before 2 and a '-'
 before 1 and concatenate them to build the expression "+2-1".
 Return the number of different expressions that you can build, which evaluates to target.
 */


final class Solution_494 {
    
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        if nums.count == 1 {
            return nums[0] == target || -nums[0] == target ? 1 : 0
        }
        
        // 初始化dp
        var dp: [Int] = []
        dp.append(nums[0])
        dp.append(-nums[0])
        
        for i in 1..<nums.count {
            let positive = nums[i]
            let negative = -nums[i]
            var temp: [Int] = []
            let n = dp.count
            
            for j in 0..<n {
                let newValue = positive + dp[j]
                temp.append(newValue)
            }
            
            for j in 0..<n {
                let newValue = negative + dp[j]
                temp.append(newValue)
            }
            
            dp = temp
        }
        
        return dp.filter { $0 == target }.count
    }
}

// dp[ i ][ j ] = dp[ i - 1 ][ j - nums[ i ] ] + dp[ i - 1 ][ j + nums[ i ] ]
class Solution_494_Opt {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        if target < -1000 || target > 1000 { return 0 }
        
        var dp = [Int](repeating: 0, count: 2001)
        dp[1000] = 1
        
        for i in 0..<nums.count {
            let num = nums[i]
            var dp2 = [Int](repeating: 0, count: 2001)
            
            for j in 0...2000 {
                if dp[j] != 0 {
                    dp2[j + num] += dp[j]
                    dp2[j - num] += dp[j]
                }
            }
            
            dp = dp2
        }
        
        return dp[1000 + target]
    }
}
