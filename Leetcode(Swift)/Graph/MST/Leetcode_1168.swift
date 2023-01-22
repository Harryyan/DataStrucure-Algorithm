//
//  Leetcode_1168.swift
//  Leetcode
//
//  Created by Harry Yan on 28/07/22.
//

import Foundation

class Solution_1168 {
    // tc: O(ElogV)
    // sc: O(V)
    func minCostToSupplyWater(_ n: Int, _ wells: [Int], _ pipes: [[Int]]) -> Int {
        var pq = Heap<Vertex>(priorityFunction: { $0.cost < $1.cost })
        var seen = Set<Int>()
        var cost = 0
        var graph: [Int: [Int:Int]] = [:]

        // build virtual vertex from 0
        for i in 1...n {
            graph[0, default: [:]][i] = wells[i-1]
        }

        // build graph
        for pipe in pipes {
            let start = pipe[0]
            let end = pipe[1]
            let cost = pipe[2]

            if graph[start, default:[:]][end] != nil {
                graph[start]![end]! = min(graph[start]![end]!, cost)
            } else {
                graph[start, default:[:]][end] = cost
            }

            if graph[end, default:[:]][start] != nil {
                graph[end]![start]!  = min(graph[end]![start]!, cost)
            } else {
                graph[end, default:[:]][start] = cost
            }
        }

        pq.enqueue(Vertex(start: 0, end: 0, cost: 0))

        while !pq.isEmpty {
            let cur = pq.dequeue()!
            
            if !seen.contains(cur.end) {
                cost += cur.cost
                
                if let dict = graph[cur.end] {
                    for (end, cost) in dict {
                        pq.enqueue(Vertex(start: cur.end, end: end, cost: cost))
                    }
                }
                
                seen.insert(cur.end)
            }
        }

        return cost
    }
}
