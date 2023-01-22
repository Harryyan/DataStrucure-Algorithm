//
//  Leetcode_22.swift
//  Leetcode
//
//  Created by Harry on 19/04/22.
//

import Foundation

class Solution_22 {
    var len = 0
    var result:[String] = []
    
    func generateParenthesis(_ n: Int) -> [String] {
        var resultString = ""
        len = n
        
        backtrack(&resultString, 0, 0)
        
        return result
    }
    
    private func backtrack(_ resultString: inout String, _ left: Int, _ right: Int) {
        if resultString.count == 2 * len {
            result.append(resultString)
            return
        }
        
        if left < len {
            resultString.append("(")
            backtrack(&resultString, left+1, right)
            _ = resultString.popLast()
        }
        
        if right < left {
            resultString.append(")")
            backtrack(&resultString, left, right+1)
            _ = resultString.popLast()
        }
    }
}
