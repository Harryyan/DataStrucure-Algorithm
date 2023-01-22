/*
 There is an integer array nums sorted in ascending order (with distinct values).
 
 Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
 
 Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
 
 You must write an algorithm with O(log n) runtime complexity.
 */

import Foundation

final class Solution_33 {
    
    func search(_ nums: [Int], _ target: Int) -> Int {
        if nums.count == 1 {
            if nums[0] == target {
                return 0
            } else {
                return -1
            }
        }
        
        let left = 0
        let right = nums.count - 1
        
        return rotateSearch(left: left, right: right, nums: nums, target: target)
    }
    
    private func rotateSearch(left: Int, right: Int, nums: [Int], target: Int) -> Int {
        guard left <= right else { return -1 }
        
        let mid = left + (right - left) / 2
        var result = 0
        
        if nums[mid] == target {
            return mid
        }
        
        if nums[mid] > nums[left] {
            if target < nums[mid], target >= nums[left] {
                result = biSearch(left: left, right: mid, nums: nums, target: target)
            } else {
                result = rotateSearch(left: mid+1, right: right, nums: nums, target: target)
            }
        } else if nums[mid] < nums[right] {
            if target <= nums[right], target > nums[mid]  {
                result = biSearch(left: mid+1, right: right, nums: nums, target: target)
            } else {
                result = rotateSearch(left: left, right: mid-1, nums: nums, target: target)
            }
        }
        
        if result == -1 {
            return result
        }
        
        if nums[result] == target {
            return result
        } else {
            return -1
        }
    }
    
    private func biSearch(left: Int, right: Int, nums: [Int], target: Int) -> Int {
        var l = left
        var r = right
        
        while l < r {
            let mid = l + (r-l) / 2
            
            if nums[mid] == target {
                return mid
            }
            
            if nums[mid] < target {
                l = mid+1
            } else {
                r = mid-1
            }
        }
        
        return l
    }
}
