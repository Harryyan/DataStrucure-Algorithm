/*
 Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
 
 A subsequence of a string is a new string that is formed from the original
 string by deleting some (can be none) of the characters without disturbing
 the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
 */
import Foundation

class Solution_392 {
    func isSubsequence(_ s: String, _ t: String) -> Bool {
        guard s != "" else { return true }
        guard s.count < t.count else { return false }

        let len1 = s.count
        let len2 = t.count
        let s_list = Array(s)
        let t_list = Array(t)

        var dp = Array(repeating: Array(repeating: 0, count: len2+1), count: len1+1)

        for i in 1...len1 {
            for j in 1...len2 {
                if s_list[i-1] == t_list[j-1] {
                    dp[i][j] = dp[i-1][j-1] + 1
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                }
            }
        }

        return dp[len1][len2] == s.count
    }
}
