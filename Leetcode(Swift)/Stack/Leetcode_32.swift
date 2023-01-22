/*
 Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
 */

import Foundation

final class Solution_32 {
    
    func longestValidParentheses(_ s: String) -> Int {
        let length = s.count
        let items = Array(s)
        var stack: [Int] = [-1]    // stack记录位置
        var result = 0
        
        for i in 0..<length {
            if items[i] == "(" {
                stack.append(i)
            } else {
                // 遇到 ')' 就出栈
                _ = stack.popLast()
                
                if stack.count == 0 {
                    stack.append(i)
                } else {
                    if let last = stack.last {
                        result = max(result, i-last)
                    }
                }
            }
        }
        
        return result
    }
}
