/*
 Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
 If target is not found in the array, return [-1, -1].
 You must write an algorithm with O(log n) runtime complexity.
 */

import Foundation

final class Solution_34 {
    
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        guard nums.count > 0 else { return [-1, -1] }
        
        var result = [-1, -1]
        
        result[0] = findLeftMost(nums: nums, left: 0, right: nums.count-1, target: target)
        result[1] = findRightMost(nums: nums, left: 0, right: nums.count-1, target: target)
        
        return result
    }
    
    
    private func findLeftMost(nums: [Int], left: Int, right: Int, target: Int) -> Int {
        var l = left
        var r = right
        
        while l < r {
            let mid = l + (r-l) / 2
            
            if nums[mid] < target {
                l = mid+1
            } else {
                r = mid
            }
        }
        
        if nums[l] == target {
            return l
        } else {
            return -1
        }
    }
    
    private func findRightMost(nums: [Int], left: Int, right: Int, target: Int) -> Int {
        var l = left
        var r = right
        
        while l < r - 1 {
            let mid = l + (r-l) / 2
            
            if nums[mid] <= target {
                l = mid
            } else {
                r = mid-1
            }
        }
        
        if nums[l] == target {
            return l
        } else if nums[r] == target {
            return r
        } else {
            return -1
        }
    }
}
