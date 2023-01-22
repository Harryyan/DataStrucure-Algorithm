////
////  MonotonicQueue.swift
////  Templates
////
////  Created by Harry Yan on 24/10/22.
////
//
//import Foundation
//import DequeModule
//
//func monotonicQueue(_ nums: [Int], _ k: Int) -> [Int] {
//    let size = nums.count
//    var queue = Deque<Int>() // 存放index
//    var res: [Int] = Array(repeating: 0, count: size-k+1)
//    
//    for i in 0..<size {
//        // 也可以用if，while能保证一定work
//        while !queue.isEmpty && i - queue.first! >= k {
//            queue.removeFirst()  // 保证窗口大小不超过k - 左出
//        }
//        
//        // 维护递减队列
//        while !queue.isEmpty && nums[queue.last!] < i {
//            queue.removeLast()  // 保证递减队列 - 右出
//        }
//        
//        queue.append(i)
//        
//        // if condition meets. add queue[0] to res
//        res.append(nums[queue[0]])
//    }
//    
//    return res
//}
