//
//  Leetcode_140.swift
//  Leetcode
//
//  Created by Harry Yan on 2/08/22.
//

import Foundation

class Solution_140 {
    var cache: [String: [String]] = [:]
    
    func wordBreak(_ s: String, _ wordDict: [String]) -> [String] {
        var res: [String] = []
        
        for word in wordDict {
            if s.hasPrefix(word) {
                if s.count == word.count {
                    res.append(word)
                } else {
                    let items = wordBreak(String(s[word.endIndex...]), wordDict)
                    
                    for subWord in items {
                        res.append(word + " " + subWord)
                    }
                }
            }
        }
        
        cache[s] = res
        return res
    }
}
