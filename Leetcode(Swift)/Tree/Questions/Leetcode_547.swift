/*
 There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is
 connected directly with city c, then city a is connected indirectly with city c.
 
 A province is a group of directly or indirectly connected cities and no other cities outside of the group.
 
 You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and
 isConnected[i][j] = 0 otherwise.
 
 Return the total number of provinces.
 */

import Foundation

// 使用dfs或者bfs遍历，修改原值或者visited数组，无论用那种遍历方法，遍历完即可
// 两层循环
class Solution_547_V1 {
    // DFS递归
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        var temp = isConnected
        let n: Int = isConnected.count
        var count: Int = 0
        
        for i in 0..<n {
            for j in 0..<n {
                if temp[i][j] == 1 {
                    dfs(&temp, row: i, column: j)
                    count += 1
                }
            }
        }
        
        return count
    }
    
    private func dfs(_ grid: inout [[Int]], row: Int, column: Int) {
        grid[row][column] = -1
        grid[column][row] = -1
        
        let n: Int = grid.count
        
        for x in 0..<n {
            if grid[column][x] == 1 {
                dfs(&grid, row: column, column: x)
            }
        }
    }
}


class Solution_547_V2 {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        let n: Int = isConnected.count
        let dsu = DSU(numbers: n)
        var results: Set<Int> = []
        
        for i in 0..<n {
            for j in 0..<n {
                if isConnected[i][j] == 1 {
                    dsu.union(a: i, b: j)
                }
            }
        }
        
        for i in 0..<n {
            results.insert(dsu.find(x: i))
        }
        
        return results.count
    }
}

// 并查集 - basic
final class DSU {
    var root: [Int] = []
    
    init(numbers: Int) {
        for i in 0..<numbers {
            root.append(i)
        }
    }
    
    // row and column
    func union(a: Int, b: Int) {
        let a = find(x: a)
        let b = find(x: b)
        
        if a != b {
            root[b] = a
        }
        
        return
    }
    
    func find(x: Int) -> Int {
        if root[x] == x {
            return root[x]
        }
        
        self.root[x] = find(x: root[x])
        
        return self.root[x]
    }
}
