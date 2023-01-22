//
//  3Way_quickSort.swift
//  Leetcode
//
//  Created by Harry on 4/04/22.
//

import Foundation

class Solution_3way_quick_sort {
    
    func threeWayQuickSort(_ nums: [Int], _ l: Int, _ r: Int) {
        guard l < r else { return }
        
        let (lt, gt) = partition(nums, l, r)
        
        threeWayQuickSort(nums, l, lt - 1)
        threeWayQuickSort(nums, gt, r)
    }
    
    
    private func partition(_ nums: [Int], _ l: Int, _ r: Int) -> (Int, Int) {
        var nums = nums
        let ind = Int.random(in: l...r)
        
        nums.swapAt(l, ind)
        let base = nums[l]
        
        var lt = l
        var gt = r + 1
        var i = l + 1
        
        while i < gt {
            if nums[i] < base {
                nums.swapAt(i, lt + 1)
                lt += 1
                i += 1
            } else if nums[i] > base {
                nums.swapAt(i, gt - 1)
                gt -= 1
            } else {
                i += 1
            }
        }
        
        nums.swapAt(l, lt)
        
        return (lt, gt)
    }
}
