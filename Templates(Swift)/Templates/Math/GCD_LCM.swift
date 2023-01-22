//
//  GCD_LCM.swift
//  Templates
//
//  Created by Harry Yan on 18/09/22.
//

import Foundation

// iteration
func greatestCommonDivisor(m: Int, n: Int) -> Int {
    var min = min(m, n)
    var max = max(m, n)
    var temp = 0
    
    while max % min != 0 {
        temp = max % min
        max = min
        min = temp
    }
    
    return min
}

// recursion
func gcd(_ a: Int, _ b: Int) -> Int {
    let r = a % b
    
    if r != 0 {
        return gcd(b, r)
    } else {
        return b
    }
}

func leastCommonMultiple(m: Int, n: Int) -> Int {
    return m*n/greatestCommonDivisor(m: m, n: n)
}
