import Foundation
/*
 Given an encoded string, return its decoded string.
 
 The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
 
 You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
 
 Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
 */

final class Solution_394 {
    
    func decodeString(_ s: String) -> String {
        var stack = [(Int, String)]()
        var res = ""
        var muti = 0
        
        for c in s {
            if c == "[" {
                stack.append((muti, res))
                muti = 0
                res = ""
            } else if c == "]" {
                if let (curMutil, lastRes) = stack.popLast() {
                    res = lastRes + String(repeating: res, count: curMutil)
                }
            } else if c.isWholeNumber {
                muti = muti * 10 + c.wholeNumberValue!
            } else {
                res.append(c)
            }
        }
        
        return res
    }
    
    
}
