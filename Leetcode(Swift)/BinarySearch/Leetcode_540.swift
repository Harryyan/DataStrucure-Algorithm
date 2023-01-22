import Foundation

/*
 You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
 
 Return the single element that appears only once.
 
 Your solution must run in O(log n) time and O(1) space.
 */


final class Solution_540 {
    
    func singleNonDuplicate(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        
        while left < right {
            var mid = left + (right - left) / 2
            
            if mid % 2 == 1 {
                mid -= 1
            }
            
            if nums[mid] == nums[mid+1] {
                left = mid + 2
            } else {
                right = mid
            }
        }
        
        return nums[left]
    }
}
