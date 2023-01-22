import Foundation

class Solution_329 {
    // tc: O(m²n²)
    // sc: O(mn)
    // time: 11 mins finish DFS, but timeout
    var visited: [[Bool]] = []
    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        let m = matrix.count
        let n = matrix[0].count
        var res = 0
        visited = Array(repeating: Array(repeating: false, count: n), count: m)

        for i in 0..<m {
            for j in 0..<n {
                visited[i][j] = true
                let result = dfs(i,j, 1, m, n, matrix)
                res = max(res, result)
                visited = Array(repeating: Array(repeating: false, count: n), count: m)
            }
        }

        return res
    }

    private func dfs(_ i: Int, _ j: Int, _ count: Int, _ m: Int, _ n: Int, _ matrix: [[Int]]) -> Int {
        let directions: [(x: Int, y: Int)] = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        var temp = count

        for direction in directions {
            let x = i + direction.x
            let y = j + direction.y

            if x>=0 && y>=0 && x<m && y<n && matrix[x][y]>matrix[i][j] {
                if visited[x][y] {
                    continue
                } else {
                    visited[x][y] = true
                    let a = dfs(x,y, count+1, m, n, matrix)
                    visited[x][y] = false
                    temp = max(temp, a)
                }
            }
        }

        return temp
    }
}

class Solution_329_Memo {
    var memo: [[Int]] = []
    var res = 0
    
    func longestIncreasingPath(_ matrix: [[Int]]) -> Int {
        let m = matrix.count
        let n = matrix[0].count
        memo = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        for i in 0..<m {
            for j in 0..<n {
                _ = dfs(i,j, m, n, matrix)
            }
        }
        
        return res
    }
    
    private func dfs(_ i: Int, _ j: Int, _ m: Int, _ n: Int, _ matrix: [[Int]]) -> Int {
        let directions: [(x: Int, y: Int)] = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        var distances: [Int] = []
        
        for direction in directions {
            let x = i + direction.x
            let y = j + direction.y
            
            if x>=0 && y>=0 && x<m && y<n && matrix[x][y]>matrix[i][j] {
                if memo[x][y] > 0 {
                    distances.append(memo[x][y])
                } else {
                    distances.append((dfs(x, y, m, n, matrix)))
                }
            }
        }
        
        if let value = distances.max() {
            memo[i][j] = value + 1
        } else {
            memo[i][j] = 1
        }
        
        res = max(res, memo[i][j])
        
        return memo[i][j]
    }
}
