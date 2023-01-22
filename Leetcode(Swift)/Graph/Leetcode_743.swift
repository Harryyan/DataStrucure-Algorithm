/*
 You are given a network of n nodes, labeled from 1 to n. You are also given times,
 a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node,
 vi is the target node, and wi is the time it takes for a signal to travel from source to target.
 
 We will send a signal from a given node k. Return the time it takes for all the n nodes to
 receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
 */

import Foundation

final class Solution_743 {
    // Find max shortest paths
    // Using SPFA to get source node to other nodes' shortest path
    
    // tc: O(VE)
    // sc: O(VE)
    func networkDelayTime(_ times: [[Int]], _ n: Int, _ k: Int) -> Int {
        var dict: [Int: [(Int, Int)]] = [:]     // Adj table to save graph
        var dist: [Int] = Array(repeating: -1, count: n+1)
        var set = Set<Int>()
        dist[k] = 0
        
        for item in times {
            let u = item[0]
            let v = item[1]
            let value = item[2]
            
            if dict[u] == nil {
                dict[u] = []
                dict[u]?.append((v, value))
            } else {
                dict[u]!.append((v, value))
            }
        }
        
        var queue: [Int] = []
        queue.append(k)
        set.insert(k)
        
        while queue.count > 0 {
            let item = queue.remove(at: 0)
            set.remove(item)
            
            if dict[item] != nil {
                for (des, value) in dict[item]! {
                    if dist[des] == -1 {
                        dist[des] = dist[item]+value
                        queue.append(des)
                        set.insert(des)
                    } else if dist[des] > dist[item]+value {
                        dist[des] = dist[item]+value
                        
                        // 避免重复添加
                        if set.contains(des) {
                            continue
                        }
                        
                        // 只有小于之前值才添加，否则会造成永久循环
                        queue.append(des)
                        set.insert(des)
                    }
                }
            }
        }
        
        if dist[1...n].contains(-1) {
            return -1
        }
        
        if dist.max() ?? 0 == 0 {
            return -1
        } else {
            return dist.max() ?? -1
        }
    }
}
