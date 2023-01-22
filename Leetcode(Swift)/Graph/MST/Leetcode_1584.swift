//
//  Leetcode_1584.swift
//  Leetcode
//
//  Created by Harry Yan on 28/07/22.
//

import Foundation

class Solution_1584 {
    
    func minCostConnectPoints(_ points: [[Int]]) -> Int {
        guard points.count > 1 else { return 0 }
        
        let n = points.count
        
        // adj matrix for dense graph
        var graph = Array(repeating: Array(repeating: 0, count: n), count: n)
        
        // build graph
        for i in 0..<n {
            for j in 0..<n {
                graph[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            }
        }
        
        var seen = Set<Int>()
        var distance = Array(repeating: Int.max, count: n)
        distance[0] = 0
        
        for _ in 0..<n {
            var newEnd = -1
            
            for j in 0..<n {
                guard !seen.contains(j) else { continue }
                
                if newEnd == -1 || distance[j] < distance[newEnd] {
                    newEnd = j
                }
            }
            
            seen.insert(newEnd)
            
            for k in 0..<n {
                guard !seen.contains(k) else { continue }
                
                distance[k] = min(distance[k], graph[newEnd][k])
            }
        }
        
        return distance.reduce(.zero, +)
    }
}
