/*
 Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
 is the number of days you have to wait after the ith day to get a warmer temperature.
 If there is no future day for which this is possible, keep answer[i] == 0 instead.
 */

import Foundation

final class Solution_739 {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        guard temperatures.count > 1 else { return [0] }
        
        var stack: [Int] = []
        var result: [Int] = []
        
        for i in stride(from: temperatures.count-1, through: 0, by: -1) {
            var count = 0
            
            while stack.count > 0, temperatures[stack.last!] <= temperatures[i] {
                let last = stack.popLast()
                count = last! - i
            }
            
            if stack.count == 0 {
                result.append(0)
            } else {
                result.append(stack.last! - i)
            }
            
            stack.append(i)
        }

        return result.reversed()
    }
}

final class Solution_739_1 {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        guard temperatures.count > 1 else { return [0] }
        
        // 单调递减栈
        // [73,74,75,71,69,72,76,73]
        var stack: [Int] = []
        var res: [Int] = Array(repeating: 0, count: temperatures.count)
        
        for i in 0..<temperatures.count {
            while !stack.isEmpty && temperatures[i] > temperatures[stack.last!] {
                let lastIndex = stack.removeLast()
                res[lastIndex] = i - lastIndex
            }
            
            stack.append(i)
        }

        return res
    }
}
