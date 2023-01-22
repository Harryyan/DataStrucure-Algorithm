/*
 A peak element is an element that is strictly greater than its neighbors.
 Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
 You may imagine that nums[-1] = nums[n] = -∞.
 You must write an algorithm that runs in O(log n) time.
 */

import Foundation

final class Solution_162 {
    
    func findPeakElement(_ nums: [Int]) -> Int {
        if nums.count == 1 {
            return 0
        }
        
        if nums.count == 2 {
            if nums[0] < nums[1] {
                return 1
            } else {
                return 0
            }
        }
        
        var left = 0
        var right = nums.count - 1
        
        while left < right {
            let mid = left + (right - left) / 2
            
            if nums[mid] > nums[mid+1] {
                right = mid
            } else {
                left = mid+1
            }
        }
        
        return left
    }
}
