//
//  Tarjan.swift
//  Templates
//
//  Created by Harry Yan on 6/10/22.
//

import Foundation

// tarjan算法
// 割点和桥

var graph: [Int: [Int]] = [:]
let n = 10
var dfn = Array(repeating: -1, count: n) // x被访问到的时间戳
var low = Array(repeating: -1, count: n) // x周围能访问到的最早时间
var result: [[Int]] = []

private func tarjan(_ node: Int, _ parent: Int, _ depth: Int) {
    dfn[node] = depth
    low[node] = depth

    for next in graph[node]! {
        if next == parent { continue }
        
        if dfn[next] == -1 {
            tarjan(next, node, depth+1)

            if dfn[node] < low[next] {
                result.append([node,next])
            }
        }
        
        // 更新当前节点的最小时间戳
        low[node]=min(low[node],low[next])
    }
}
