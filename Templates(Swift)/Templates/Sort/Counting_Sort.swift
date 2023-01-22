//
//  Counting_Sort.swift
//  Templates
//
//  Created by Harry Yan on 13/11/22.
//

import Foundation

func counting_sort(_ list: [Int]) -> [Int] {
    var output = Array(repeating: 0, count: list.count)
    var count = Array(repeating: 0, count: 256)  // list取值范围是[0,255]
    
    // 1. 求每个元素个数
    for value in list {
        count[value] += 1
    }
    
    // 2. 求presum,计算放置位置
    for i in 1...255 {
        count[i] += count[i-1]
    }
    
    // 3. 构建output
    for i in stride(from: list.count-1, through: 0, by: -1) {
        output[count[list[i]]-1] = list[i]
        count[list[i]] -= 1
    }
    
    return output
}
