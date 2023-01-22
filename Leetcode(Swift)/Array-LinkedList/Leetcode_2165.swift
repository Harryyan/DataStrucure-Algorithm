/*
 You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.
 
 Return the rearranged number with minimal value.
 
 Note that the sign of the number does not change after rearranging the digits.
 */

import Foundation

class Solution_2165 {
    
    func smallestNumber(_ num: Int) -> Int {
        guard num != 0 else { return 0 }
        
        var stack: [Int] = []
        var temp = num < 0 ? -num : num
        
        if num < 0 {
            while temp > 0 {
                let value = temp % 10
                stack.append(value)
                
                temp /= 10
            }
            
            stack = stack.sorted(by: { $0 >= $1 })
            var result = 0
            
            for (index, value) in stack.enumerated() {
                let test = pow(10, stack.count-1-index).intValue
                result += value * test
            }
            
            return -result
        } else {
            while temp > 0 {
                let value = temp % 10
                stack.append(value)
                
                temp /= 10
            }
            
            stack = stack.sorted()
            var result = 0
            
            if stack[0] == 0 {
                if let firstNoneZeroIndex = stack.firstIndex(where: {$0 > 0}) {
                    stack.swapAt(0, firstNoneZeroIndex)
                }
                
                for (index, value) in stack.enumerated() {
                    let test = pow(10, stack.count-1-index).intValue
                    result += value * test
                }
                
                return result
            } else {
                for (index, value) in stack.enumerated() {
                    let test = pow(10, stack.count-1-index).intValue
                    result += value * test
                }
                
                return result
            }
        }
    }
}

extension Decimal {
    var intValue: Int {
        return NSDecimalNumber(decimal: self).intValue
    }
}
