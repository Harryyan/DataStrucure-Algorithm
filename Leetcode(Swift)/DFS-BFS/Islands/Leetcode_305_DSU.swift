//
//  Leetcode_305.swift
//  Leetcode
//
//  Created by Harry on 2/06/22.
//

import Foundation

class Solution_305_DSU {
    // tc: O(k log(mn))
    // sc: O(mn)
    // time: 4 + 31
    func numIslands2(_ m: Int, _ n: Int, _ positions: [[Int]]) -> [Int] {
        var grid: [[Int]] = Array(repeating: Array(repeating: 0, count: n), count: m)
        let dsu = DSU(m * n)
        let directions = [[0,1], [0,-1], [1,0], [-1,0]]
        var res = [Int]()
        var count = 0
        var set = Set<[Int]>()
        
        for position in positions {
            let x = position[0]
            let y = position[1]
            
            if !set.contains(position) {
                set.insert(position)
                count += 1
            } else {
                res.append(count)
                continue
            }
            
            grid[x][y] = 1

            var parents = Set<Int>()
            
            for direction in directions {
                let newX = x + direction[0]
                let newY = y + direction[1]
                
                // check 4 directions if any 1 can be connected
                if newX < m && newY < n && newY >= 0 && newX >= 0 && grid[newX][newY] == 1 {
                    let index1 = x * n + y
                    let index2 = newX * n + newY

                    let pId = dsu.find(index2)
                    parents.insert(pId)

                    dsu.union(index2, index1)
                }
            }
            
            count -= parents.count
            
            res.append(count)
        }
        
        return res
    }
}
