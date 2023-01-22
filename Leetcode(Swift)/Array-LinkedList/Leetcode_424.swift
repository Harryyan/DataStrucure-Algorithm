//
//  Leetcode_424.swift
//  Leetcode
//
//  Created by Harry on 9/05/22.
//

import Foundation

class Solution_424 {
    func characterReplacement(_ s: String, _ k: Int) -> Int {
        guard s.count > 1 else { return 1 }
        
        var items: [Int] = Array(repeating: 0, count: 26)
        let list = Array(s)
        var left = 0
        var curMax = 0
        var result = 0
        
        for i in 0..<list.count {
            let idx = index(of: list[i])
            items[idx] += 1
            curMax = max(curMax, items[idx])
            
            if i - left + 1 > curMax + k {
                let leftIndex = index(of:list[left])
                items[leftIndex] -= 1
                left += 1
            } else {
                result = max(result, i - left + 1 )
            }
        }
        
        return result
    }
    
    private func index(of ch: Character) -> Int {
        return Int(ch.asciiValue!) - Int(Character("A").asciiValue!)
    }
}
