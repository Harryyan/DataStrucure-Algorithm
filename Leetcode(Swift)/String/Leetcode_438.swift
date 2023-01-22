//
//  Leetcode_438.swift
//  Leetcode
//
//  Created by Harry on 15/04/22.
//

import Foundation

class Solution_438 {
    // tc: O(n)
    // sc: O(n)
    // time: 2 + 7
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        var res: [Int] = []
        
        guard p.count <= s.count else { return res }
        
        let sLen = s.count
        let pLen = p.count
        let sList = Array(s)
        let pList = Array(p)
        
        // 频次数组
        var sCnt: [Int] = Array(repeating: 0, count: 26)
        var pCnt: [Int] = Array(repeating: 0, count: 26)
        
        for i in 0..<pLen {
            sCnt[index(of: sList[i])] += 1
            pCnt[index(of: pList[i])] += 1
        }

        if sCnt == pCnt {
            res.append(0)
        }
        
        guard pLen < sLen else { return res }
        
        for i in pLen..<sLen {
            let preCh = sList[i - pLen]
            let currentCh = sList[i]
            
            sCnt[index(of: preCh)] -= 1
            sCnt[index(of: currentCh)] += 1
            
            if sCnt == pCnt {
                res.append(i - pLen + 1)
            }
        }
        
        return res
    }
    
    private func index(of ch: Character) -> Int {
        return Int(ch.asciiValue!) - Int(Character("a").asciiValue!)
    }
}
