//
//  UpperAndLowerBound.swift
//  Leetcode
//
//  Created by Harry Yan on 9/08/22.
//

import Foundation

private func lower_bound(_ list: [Int], _ target: Int) -> Int {
    var left = 0
    var right = list.count - 1
    
    while left < right {
        let mid = left + (right - left) / 2
        
        if list[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    
    return list[left] == target ? left : -1
}

private func upper_bound(_ list: [Int], _ target: Int) -> Int {
    var left = 0
    var right = list.count - 1
    
    while left < right {
        let mid = left + (right - left + 1) / 2
        
        if list[mid] > target {
            right = mid - 1
        } else {
            left = mid
        }
    }
    
    return list[left] == target ? left : -1
}
