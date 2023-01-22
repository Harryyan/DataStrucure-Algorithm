//
//  Leetcode_169.swift
//  Leetcode
//
//  Created by Harry on 1/06/22.
//

import Foundation

class Solution_169 {
    func majorityElement(_ nums: [Int]) -> Int {
        var vote = 0
        var element = 0
        
        for num in nums {
            if vote == 0 {
                element = num
            }
            
            vote += element != num ? -1 : 1
        }
        
        return element
    }
}
