/*
 Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
 return the next greater number for every element in nums.
 
 The next greater number of a number x is the first greater number to
 its traversing-order next in the array, which means you could search circularly to find its next greater number.
 If it doesn't exist, return -1 for this number.
 */


import Foundation

final class Solution_503 {
    
    func nextGreaterElements(_ nums: [Int]) -> [Int] {
        let count = nums.count
        var stack: [Int] = []
        var result: [Int] = Array(repeating: -1, count: count)
        
        for i in 0..<count*2 {
            while stack.count > 0 && nums[stack.last!] < nums[i % count] {
                result[stack.popLast()!] = nums[i % count]
            }
            
            stack.append(i % count)
        }
        
        return result
    }
}
