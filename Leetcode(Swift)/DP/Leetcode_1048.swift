//
//  Leetcode_1048.swift
//  Leetcode
//
//  Created by Harry on 10/06/22.
//

import Foundation

class Solution_1048 {
    // tc: O(n^2 * k) - k is average length of each word
    // sc: O(n)
    func longestStrChain(_ words: [String]) -> Int {
        var words = words.sorted(by: { $0.length <= $1.length })
        var dp = Array(repeating: 1, count: words.count)
        var res = 0

        for i in 0..<words.count {
            for j in 0..<i {
                if check(words[j],words[i]) {
                    dp[i] = max(dp[i], dp[j] + 1)
                }
            }

            res = max(res, dp[i])
        }

        return res
    }

    private func check(_ word1: String, _ word2: String) -> Bool {
        let m = word1.count
        let n = word2.count

        guard m + 1 == n else { return false }

        let list1 = Array(word1)
        let list2 = Array(word2)
        var left = 0
        var right = 0

        while left < m && right < n {
            if list1[left] == list2[right] {
                left += 1
            }

            right += 1
        }

        return left == word1.count
    }
}
