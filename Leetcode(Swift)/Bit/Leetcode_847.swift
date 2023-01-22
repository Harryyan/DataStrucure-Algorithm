//
//  Leetcode_847.swift
//  Leetcode
//
//  Created by Harry on 29/03/22.
//

import Foundation

class Solution_847 {
    func shortestPathLength(_ graph: [[Int]]) -> Int {
        let n:Int = graph.count
        let fullMask:Int = (1 << n) - 1
        var visited:Set<String> = Set<String>()
        var que:[Node] = [Node]()
        for i in 0..<n
        {
            let node:Node = Node(i, 1<<i)
            que.append(node)
            visited.insert(node.toString())
        }
        var level:Int = 0
        while(!que.isEmpty)
        {
            let size:Int = que.count
            for _ in 0..<size
            {
                let node = que.removeFirst()
                if node.mask == fullMask {return level}
                for next in graph[node.id]
                {
                    let nextNode:Node = Node(next, node.mask | (1 << next))
                    print(visited)
                    if visited.contains(nextNode.toString()) {continue}
                    que.append(nextNode)
                    visited.insert(nextNode.toString())
                }
            }
            level += 1
        }
        return level
    }
}

class Node {
    var id:Int = 0
    var mask:Int = 0
    
    init(_ id:Int,_ mask:Int)
    {
        self.id = id
        self.mask = mask
    }
    
    func toString() -> String
    {
        return String(id) + " " + String(mask)
    }
}
