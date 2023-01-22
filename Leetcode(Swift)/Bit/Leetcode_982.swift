//
//  Leetcode_982.swift
//  Leetcode
//
//  Created by Harry on 31/03/22.
//

import Foundation

class Solution_982 {
    func countTriplets(_ nums: [Int]) -> Int {
        var list = Array(repeating: 0, count: pow(2,16).intValue)
        var res = 0
        
        for i in nums {
            for j in nums {
                list[i&j] += 1
            }
        }
        
        let mask = pow(2,16).intValue - 1
        
        for i in nums {
            let temp = mask ^ i
            var temp2 = temp
            
            while temp2 != 0 {
                res += list[temp2]
                temp2 = (temp2-1) & temp
            }
            
            res += list[0]
        }
        
        return res
    }
}


extension Decimal {
    var intValue: Int {
        return NSDecimalNumber(decimal: self).intValue
    }
}
