//
//  8-Queen.swift
//  Leetcode
//
//  Created by Harry on 3/01/22.
//

import Foundation

final class Queen_N {
    var result: [Int] = []
    var result2: [[String]] = []
    
    func solveNQueens(_ n: Int) -> [[String]] {
        result = Array(repeating: 0, count: n)
        
        dfs(0, n)
        
        return result2
    }
    
    private func dfs(_ row: Int, _ size: Int) {
        if row == size {
            printNQueen(size)
            return
        }
        
        for col in 0..<size {
            if isOK(row: row, col: col, size: size) {
                result[row] = col
                dfs(row+1, size)
            }
        }
    }
    
    private func isOK(row: Int, col: Int, size: Int) -> Bool {
        var leftUp = col - 1
        var rightUp = col + 1
        
        for i in stride(from: row-1, to: -1, by: -1)  {
            if result[i] == col {
                return false
            }
            
            if leftUp >= 0 && result[i] == leftUp {
                return false
            }
            
            if rightUp < size && result[i] == rightUp {
                return false
            }
            
            leftUp -= 1
            rightUp += 1
        }
        
        return true
    }
    
    private func printNQueen(_ size: Int) {
        var s: [String] = []
        
        for i in 0..<size {
            var r = ""
            
            for j in 0..<size {
                if result[i] == j {
                    r += "Q"
                } else {
                    r += "."
                }
            }
            
            s.append(r)
        }
        
        result2.append(s)
    }
}
