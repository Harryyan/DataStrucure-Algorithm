//
//  PrefixSum.swift
//  Templates
//
//  Created by Harry Yan on 18/09/22.
//

import Foundation

// 设我们需要求和的矩形区域的左上角为 (x1, y1)，右下角为 (x2, y2)，则该矩形区域的元素之和可以表示为：
// sum = A[x1..x2][y1..y2] = P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]


func test() {
    let m = 5
    let n = 4
    let mat = Array(repeating: Array(repeating: 0, count: n), count: m)

    var prefixSum: [[Int]] = Array(repeating: Array(repeating: 0, count: n+1), count: m+1)

    for i in 1...m {
        for j in 1...n {
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1]
        }
    }
}
