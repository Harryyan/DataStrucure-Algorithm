//
//  FindRoot.swift
//  Leetcode
//
//  Created by Harry on 19/02/22.
//

import Foundation

class RootFind {
    func getRoot(_ value: Double, _ n: Double) {
        var number: Double = 7
        var low: Double = 0
        var high = number
        var middle: Double = Double(number / 2)
        var times: Double = 3.0

        var result: Double = middle

        while abs(pow(middle, times) - number) > 0.001 {
            if pow(middle, times) == number { break }
            
            if pow(middle, times) > number {
                high = (Double(low) + high) / 2
            } else {
                low = middle
            }
            
            middle = (low + high) / 2
            
            result = middle
        }

        print(result)
    }
}
