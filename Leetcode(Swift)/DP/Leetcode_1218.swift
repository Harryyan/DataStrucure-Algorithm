//
//  Leetcode_1218.swift
//  Leetcode
//
//  Created by Harry on 17/03/22.
//

import Foundation

class Solution_1218 {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        var dict: [Int: Int] = [:]
        var result = 1
        
        _ = arr.map {
            dict[$0] = 0
        }
        
        for i in 0..<arr.count {
            let pre = arr[i] - difference
            
            if dict[pre] != nil {
                dict[arr[i]]! = dict[pre]! + 1
            } else {
                dict[arr[i]]! = 1
            }
            
            result = max(result, dict[arr[i]]!)
        }
        
        return result
    }
}
