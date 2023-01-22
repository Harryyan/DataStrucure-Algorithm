//
//  Leetcode_718.swift
//  Leetcode
//
//  Created by Harry on 15/04/22.
//

import Foundation


class Solution_718 {
    // tc: O((m+n) * min(m,n))
    // sc: O(1)
    // time: 1 + 4 dp way
    // time 1 + 15 slide window
    func findLength(_ A: [Int], _ B: [Int]) -> Int {
        if A.count < B.count {
            return _findLength(A,B)
        } else {
            return _findLength(B,A)
        }
    }
    
    func _findLength(_ A: [Int], _ B: [Int]) -> Int {
        let alen = A.count
        let blen = B.count
        let totalRunTimes = alen + blen - 1
        
        var res = 0
        
        for i in 0..<totalRunTimes {
            var aStart = 0
            var bStart = 0
            var len = 0
            
            if i < alen {
                aStart = alen - i - 1
                bStart = 0
                len = i + 1
            } else {
                aStart = 0
                bStart = i - alen + 1
                len = min(blen - bStart, alen)
            }
            
            let middleResult = maxlen(A, B, aStart, bStart, len)
            res = max(res, middleResult)
        }
        
        return res
    }
    
    //计算A和B在重叠区域最长子数组
    private func maxlen(_ A: [Int], _ B: [Int], _ aStart: Int, _ bStart: Int, _ len: Int) -> Int {
        var res = 0
        var count = 0
        
        for i in 0..<len {
            if A[aStart+i] == B[bStart+i] {
                count += 1
                res = max(res, count)
            } else {
                count = 0
            }
        }
        
        return res
    }
}
