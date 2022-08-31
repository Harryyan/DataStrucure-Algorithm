# BFS总结

BFS, 广度优先搜索，常用于层序遍历和最短路径问题.

## 层序遍历
伪代码模板:

```swift
procedure BFS(g,v):
  create a queue Q
  enqueue V to Q
  mark v as visited
  
  while Q is not empty:
     t <- dequque Q(pop first)
     
     if t is what we are looking for:
     		return t
     
     for all vertext v in G.adjcentVertext(t):
     		if v is not visited:
     			mark v
     			enqueue v into Q
```

## 最短路径

BFS有个特性就是按层次遍历所连接的节点，由于是从原点出发，那自然最先遍历到符合条件的节点，故而可求最短路径. 最短路径题不一定非得是 树形，或者图，网格结构也很常见.

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1649454303/algorithm/BFS/BFS_oufmr3.jpg)

### K 站中转内最便宜的航班 (leetcode-787)

无负数，无环，可用BFS.

```swift
class Solution {
    func findCheapestPrice(_ n: Int, _ flights: [[Int]], _ src: Int, _ dst: Int, _ k: Int) -> Int {
        let INF = 100000
        var dist: [Int] = Array(repeating: INF, count: n)
        var dict: [Int: [(Int, Int)]] = [:]     // Adj table to save graph
        
        dist[src] = 0
        
        for flight in flights {
            let src = flight[0]
            let des = flight[1]
            let value = flight[2]
            
            if dict[src] == nil {
                dict[src] = []
                dict[src]?.append((des, value))
            } else {
                dict[src]!.append((des, value))
            }
        }
        
        var queue: [(Int, Int, Int)] = []

        // (source, count, price)
        queue.append((src, -1, 0))
        
        while queue.count > 0 {
            let item = queue.remove(at: 0)
            let src = item.0
            let count = item.1
            let price = item.2
            
            if count + 1 > k {
                break
            }
            
            if dict[src] != nil {
                for (des, value) in dict[src]! {
                    if dist[des] > price + value {
                        dist[des] =  price + value
                        queue.append((des, count+1, dist[des]))
                    }
                }
            }
        }

        return dist[dst] == 100000 ? -1 : dist[dst] 
    }
}
```

### 网格中的最短路径 (leetcode-1293)

```swift
 class Solution {
    
    private struct State {
        var x: Int
        var y: Int
        var remain: Int
    }
    
    typealias Direction = (dx:Int,dy:Int)
    private let directions: [Direction] = [(0,1),(0,-1),(1,0),(-1,0)]
    
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        let M = grid.count
        let N = grid[0].count
        
        guard M != 1 || N != 1 else {
            return 0
        }
        
        func valid(x: Int, y: Int) -> Bool {
            return x >= 0 && x <  M && y >= 0 && y < N
        }
        
        var queue = [State]()
        var visited = Array<Array<Int>>(repeating: Array<Int>(repeating: -1, count: N), count: M)
        queue.append(State(x: 0, y: 0, remain: k))
        visited[0][0] = k
        
        var depth = 0
        while !queue.isEmpty {
            depth += 1
            var nextLevel = [State]()
            for state in queue {
                for dir in directions {
                    
                    let nextX = state.x + dir.dx
                    let nextY = state.y + dir.dy
                    guard nextX != M - 1 || nextY != N - 1  else{
                        return depth
                    }
                    if valid(x: nextX, y: nextY) {
                        var nextState = State(x: nextX, y: nextY, remain: state.remain)
                        if grid[nextX][nextY] == 1 {
                            nextState.remain = state.remain - 1
                        }
                        if nextState.remain >= 0 && visited[nextX][nextY] < nextState.remain {
                            nextLevel.append(nextState)
                            visited[nextX][nextY] = nextState.remain
                        }
                        
                    }
                }
            }
            queue = nextLevel
        }
        return -1
    }
 }
```

### 地图分析 (leetcode-1162)

多源BFS

```swift
class Solution {
    func maxDistance(_ grid: [[Int]]) -> Int {
        var grid = grid
        var queue: [(Int,Int)] = []
        let rows = grid.count
        let cols = grid[0].count
        let directions = [(0,1),(0,-1),(1,0),(-1,0)]

        var res = -1

        for i in 0..<rows {
            for j in 0..<cols {
                if grid[i][j] == 1 {
                    queue.append((i,j))
                }
            }
        }

        // all lands or sea
        if queue.isEmpty || queue.count == rows * cols {
            return -1
        }

        while !queue.isEmpty {
            res += 1
            var neibours: [(Int,Int)] = []

            for item in queue {
                let x = item.0
                let y = item.1

                for direction in directions {
                    let nextX = x + direction.0
                    let nextY = y + direction.1

                    if nextX >= 0 && nextX < rows && nextY < cols && nextY >= 0 && grid[nextX][nextY] == 0 {
                        grid[nextX][nextY] = 2
                        neibours.append((nextX, nextY))
                    }
                }
            }

            queue = neibours
        }

        return res
    }
}
```

