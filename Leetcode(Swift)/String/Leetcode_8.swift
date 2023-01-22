import Foundation

/*
 Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
 
 The algorithm for myAtoi(string s) is as follows:
 
 Read in and ignore any leading whitespace.
 Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
 Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
 If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
 Return the integer as the final result.
 Note:
 
 Only the space character ' ' is considered a whitespace character.
 Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 
 */

final class Solution_8 {
    func myAtoi(_ s: String) -> Int {
        var characters: [Character] = []
        var isNegative: Bool?
        
        for c in s {
            if c.isWhitespace && characters.count == 0 && isNegative == nil {
                continue
            }
            if c.isNumber {
                characters.append(c)
            } else if c == "-" {
                if characters.count > 0 || isNegative != nil {
                    break
                } else {
                    isNegative = true
                }
            } else if c == "+" {
                if characters.count > 0 || isNegative != nil {
                    break
                } else {
                    isNegative = false
                }
            } else {
                break
            }
        }
        
        if characters.count == 0 {
            return 0
        }
        var num = Int(String(characters)) ?? Int.max
        if let neg = isNegative,
           neg == true {
            num = -num
            if num < Int32.min {
                return Int(Int32.min)
            }
        }
        if num > Int32.max {
            return Int(Int32.max)
        }
        
        return num
    }
}
