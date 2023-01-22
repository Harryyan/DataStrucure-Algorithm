//
//  Lint_391.swift
//  Leetcode
//
//  Created by Harry Yan on 15/08/22.
//

import Foundation

class Interval {
    var start: Int
    var end: Int
    init() { start = 0; end = 0; }
    init(_ a: Int, _ b: Int) { start = a; end = b }
}
/*
 @param airplanes: An interval array
 @return: Count of airplanes are in the sky.
*/
func countOfAirplanes(_ airplanes: Array<Interval>) -> Int {
    var dict: [Int: Int] = [:]

    for airplane in airplanes {
        dict[airplane.start, default: 0] += 1
        dict[airplane.end, default: 0] -= 1
    }

    var list = dict.sorted(by: { $0.0 < $1.0 })
    var res = 0
    var total = 0

    for (_, value) in list {
        total += value
        res = max(res, total)
    }

    return res
}
