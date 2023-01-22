/*
 An additive number is a string whose digits can form an additive sequence.
 
 A valid additive sequence should contain at least three numbers.
 Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
 
 Given a string containing only digits, return true if it is an additive number or false otherwise.
 
 Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
 */

import Foundation

final class Solution_306 {
    var numDigitChars = [Character]()
    var length = 0
    
    func isAdditiveNumber(_ num: String) -> Bool {
        length = num.count
        
        guard length >= 3 else { return false }
        
        numDigitChars = Array(num)
        
        for i in 1..<length-2 {
            let firstNum = Int64(String(numDigitChars[0...i]))!
            
            if i > 1, numDigitChars[0] == Character("0") {
                break
            }
            
            for j in i+1..<length-1 {
                let secondNum = Int64(String(numDigitChars[i...j]))!
                
                if check(j, secondNum, firstNum) {
                    return true
                } else { // 不满足
                    // 第二个数不能以 0 开头，否则结束当前内层循环。
                    if numDigitChars[i] == Character("0") {
                        break
                    }
                }
            }
        }
        return false
    }
    
    private func check(_ curIdx: Int, _ preVal: Int64, _ prepreVal: Int64) -> Bool {
        let curStr = String(numDigitChars[curIdx...])
        if curIdx == length {
            return true
        }
        
        let nextSum = preVal + prepreVal
        let nextSumStr = "\(nextSum)"
        if !curStr.hasPrefix(nextSumStr) {
            return false
        }
        
        return check(curIdx + nextSumStr.count, nextSum, preVal)
    }
}
