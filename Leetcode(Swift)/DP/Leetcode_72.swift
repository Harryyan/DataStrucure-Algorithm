/*
 Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
 
 You have the following three operations permitted on a word:
 
 Insert a character
 Delete a character
 Replace a character
 */

import Foundation

class Solution_72 {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        guard word1.count > 0, word2.count > 0 else {
            if word1.count > 0 && word2.count == 0 {
                return word1.count
            } else if word2.count > 0 && word1.count == 0 {
                return word2.count
            } else {
                return 0
            }
        }
        
        let len1 = word1.count
        let len2 = word2.count
        
        let word1_list = Array(word1)
        let word2_list = Array(word2)
        
        // Add sentinel
        var dp = Array(repeating: Array(repeating: 0, count: len2+1), count: len1+1)
        
        // Init first row and column
        for i in 1...len1 {
            dp[i][0] = i
        }
        
        for j in 1...len2 {
            dp[0][j] = j
        }
        
        for i in 1...len1 {
            for j in 1...len2 {
                if word1_list[i-1] == word2_list[j-1] {
                    // check diagonal when equal
                    dp[i][j] = dp[i-1][j-1]
                } else {
                    let temp = min(dp[i-1][j], dp[i][j-1]) + 1
                    dp[i][j] = min(temp, dp[i-1][j-1]) + 1
                }
            }
        }
        
        return dp[len1][len2]
    }
}
