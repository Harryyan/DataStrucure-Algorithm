//
//  Leetcode_6076.swift
//  Leetcode
//
//  Created by Harry on 22/05/22.
//

import Foundation

class Solution_6076 {
    func minimumLines(_ stockPrices: [[Int]]) -> Int {
        var count = 0
        var preK = [Int.max, Int.max]
        
        if stockPrices.count == 1 {
            return 0
        }
        
        let stockPrices = stockPrices.sorted(by: {$0[0] <= $1[0]})
        
        
        for i in 1..<stockPrices.count {
            let point1 = stockPrices[i-1]
            let point2 = stockPrices[i]
            
            let x1 = point1[0]
            let y1 = point1[1]
            
            let x2 = point2[0]
            let y2 = point2[1]
            
            let k = slope(y2 - y1, x2 - x1)
            
            if preK != k {
                preK = k
                count += 1
            }
        }
        
        return count
    }

    func slope(_ dy: Int, _ dx: Int) -> [Int] {
        return [dy / gcd(dy, dx), dx / gcd(dy,dx)]
    }

   func gcd(_ a: Int, _ b: Int) -> Int {
        if (a % b == 0) {
            return b
        }
        
        return gcd(b, a % b)
    }
}
