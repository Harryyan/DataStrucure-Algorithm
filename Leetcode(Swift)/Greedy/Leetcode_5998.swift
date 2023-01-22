/*
 You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.
 
 For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
 Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.
 */

import Foundation

// 贪心
class Solution_5998 {
    func maximumEvenSplit(_ finalSum: Int) -> [Int] {
        guard finalSum % 2 == 0 else { return [] }
        
        var sum = 0
        var x = 2
        var res: [Int] = []
        
        while x + sum <= finalSum {
            sum += x
            res.append(x)
            x += 2
        }
        
        let diff = finalSum - sum
        var newValue = res.removeLast()
        newValue += diff
        res.append(newValue)
        
        return res
    }
}
