/*
 The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
 
 You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
 
 For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
 
 Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
 
 Follow up: Could you find an O(nums1.length + nums2.length) solution?
 
 */

import Foundation

final class Solution_496 {
    
    func nextGreaterElement(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var stack: [Int] = []
        var dict: [Int:Int] = [:]
        
        for i in stride(from: nums2.count-1, through: 0, by: -1) {
            while stack.count > 0, let last = stack.last, last <= nums2[i] {
                _ = stack.popLast()
            }
            
            if stack.count > 0, let last = stack.last {
                dict[nums2[i]] = last
            }
            
            stack.append(nums2[i])
        }
        
        let result: [Int] = nums1.map {
            if let value = dict[$0] {
                return value
            } else {
                return -1
            }
        }
        
        return result
    }
}
