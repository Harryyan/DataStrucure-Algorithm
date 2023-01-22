/*
 Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

 A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

 For example, "ace" is a subsequence of "abcde".
 A common subsequence of two strings is a subsequence that is common to both strings.
 */

import Foundation

final class Solution_1143 {
    
    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        let len1 = text1.count
        let len2 = text2.count
        
        let t1 = Array(text1)
        let t2 = Array(text2)
        
        var dp = Array(repeating: Array(repeating: 0, count: len2), count: len1)
        
        // 初始化行
        for i in 0..<len2 {
            if t1[0] == t2[i] || (i > 0 && dp[0][i-1] == 1) {
                dp[0][i] = 1
            }
        }
        
        // 初始化列
        for i in 0..<len1 {
            if t2[0] == t1[i] || (i > 0 && dp[i-1][0] == 1) {
                dp[i][0] = 1
            }
        }
        
        // 构建状态转移表
        for i in 1..<len1 {
            for j in 1..<len2 {
                if t1[i] == t2[j] {
                    dp[i][j] = dp[i-1][j-1] + 1
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                }
            }
        }

        return dp[len1-1][len2-1]
    }
}
