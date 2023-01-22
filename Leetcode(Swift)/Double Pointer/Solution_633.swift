/*
 Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.
 */
import Foundation

final class Solution_633 {
    
    func judgeSquareSum(_ c: Int) -> Bool {
        var left = 0
        var right: Int = Int(Double(c).squareRoot()) + 1
        
        while left <= right {
            let total = pow(Double(left), 2) + pow(Double(right), 2)
            
            if total == Double(c) {
                return true
            } else if total < Double(c) {
                left += 1
            } else {
                right -= 1
            }
        }
        
        return false
    }
}
