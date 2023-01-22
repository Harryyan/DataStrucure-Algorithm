//
//  MergeSort.swift
//  Templates
//
//  Created by Harry Yan on 1/10/22.
//

import Foundation

func mergeSort(_ nums: [Int], _ start: Int, _ end: Int) -> [Int] {
    guard start < end else { return nums }
    
    let mid = start + (end - start) / 2
    let left = mergeSort(nums, start, mid)
    let right = mergeSort(nums, mid+1, end)
    
    var sortedList: [Int] = []
    var p1 = 0
    var p2 = 0
    
    while p1 < left.count || p2 < right.count {
        if p1 == left.count {
            sortedList.append(right[p2])
            p2 += 1
        } else if p2 == right.count {
            sortedList.append(right[p1])
            p1 += 1
        } else {
            if nums[p1] < nums[p2] {
                sortedList.append(right[p1])
                p1 += 1
            } else {
                sortedList.append(right[p2])
                p2 += 1
            }
        }
    }
    
    return sortedList
}
