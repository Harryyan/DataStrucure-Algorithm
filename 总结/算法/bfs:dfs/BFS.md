- [BFS总结](#bfs%E6%80%BB%E7%BB%93)
  - [二叉树最小深度(leetcode-111)](#%E4%BA%8C%E5%8F%89%E6%A0%91%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6leetcode-111)
  - [二叉树的层序遍历 (leetcode-102)](#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86-leetcode-102)
  - [单词接龙 (leetcode-127)](#%E5%8D%95%E8%AF%8D%E6%8E%A5%E9%BE%99-leetcode-127)
  - [迷宫 (leetcode-490)](#%E8%BF%B7%E5%AE%AB-leetcode-490)
  - [迷宫II (leetcode-505)](#%E8%BF%B7%E5%AE%ABii-leetcode-505)
  - [最短路径](#%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84)
    - [K 站中转内最便宜的航班 (leetcode-787)](#k-%E7%AB%99%E4%B8%AD%E8%BD%AC%E5%86%85%E6%9C%80%E4%BE%BF%E5%AE%9C%E7%9A%84%E8%88%AA%E7%8F%AD-leetcode-787)
    - [网格中的最短路径 (leetcode-1293)](#%E7%BD%91%E6%A0%BC%E4%B8%AD%E7%9A%84%E6%9C%80%E7%9F%AD%E8%B7%AF%E5%BE%84-leetcode-1293)
  - [地图分析 (leetcode-1162)](#%E5%9C%B0%E5%9B%BE%E5%88%86%E6%9E%90-leetcode-1162)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# BFS总结

BFS, 广度优先搜索，常用于层序遍历和最短路径问题.

BFS有个特性就是按层次遍历所连接的节点，由于是从原点出发，那自然最先遍历到符合条件的节点，故而可求最短路径. 最短路径题不一定非得是 树形，或者图，网格结构也很常见.

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1649454303/algorithm/BFS/BFS_oufmr3.jpg)

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

## 二叉树最小深度(leetcode-111)
层序遍历，while循环里套for循环，是上边伪代码的直接应用。注意，这种二叉树求最小值的题目，要遍历每一层，遍历完后，才能将层数加一:

```swift
class Solution {
    func minDepth(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }

        var depth = 1
        var queue: [TreeNode] = []
        queue.append(node)

        while !queue.isEmpty {
            let size = queue.count

            for i in 0..<size {
                let curr = queue.removeFirst()

                if curr.left == nil && curr.right == nil { return depth}
                if curr.left != nil { queue.append(curr.left!) }
                if curr.right != nil { queue.append(curr.right!)}
            }

            depth += 1
        }

        return depth
    }
}
```

DFS版本: 空间使用度比BFS更优, 个人感觉是Swift编译器针对尾递归的优化，以及没有额外堆内存的开销(BFS额外声明了queue数组，在堆上)

```swift
class Solution {
    func minDepth(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }

        if node.left == nil { return minDepth(node.right) + 1 }
        if node.right == nil { return minDepth(node.left) + 1 }
        return min(minDepth(node.left), minDepth(node.right)) + 1
    }
}
```

## 二叉树的层序遍历 (leetcode-102)
基本模板题，需要熟练掌握.
其变种问题有：zig-zag遍历； 树的left order view 和 right order view； 还有顺时针，逆时针打印.(先求left和right order view，然后找到没有访问过的leaf节点，打印); 纵向打印.

```swift
class Solution {
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        
        var queue = [TreeNode]()
        var result: [[Int]] = []
        
        queue.append(root)
        
        while !queue.isEmpty {
            var values: [Int] = []
            let size = queue.count

            for i in 0..<size {
                let node = queue.removeFirst()
                values.append(node.val)

                if node.left != nil {
                    queue.append(node.left!)
                }

                if node.right != nil {
                    queue.append(node.right!)
                }
            }

            result.append(values)
        }
        
        return result
    }
}
```

## 单词接龙 (leetcode-127)
普通BFS: 将begin word入队，依次使用26个字母替换beginword的每个位置，看看字典中是否有同样字母；若有，则返回层数；使用BFS能最快返回结果, 最差结果就是没有，则返回0.

```swift
class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var seen = Set(wordList)
        var steps = 1
        var queue: [String] = []
        let wordLen = beginWord.count
        let charList = "abcdefghijklmnopqrstuvwxyz"

        queue.append(beginWord)

        // tc: O(m * n) 
        // 普通BFS
        while !queue.isEmpty {
            let size = queue.count

            for i in 0..<size {
                let cur = queue.removeFirst()
                
                if cur == endWord {
                    return steps
                }

                for j in 0..<wordLen {
                    for ch in charList {
                        var next = cur
                        next[j] = ch

                        if seen.contains(next) {
                            seen.remove(next)
                            queue.append(next)
                        }
                    }
                }
            }

            steps += 1
        }
        
        return 0
    }
}
```

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1662351986/algorithm/BFS/bfs_wrjm4y.png)

双向BFS：

从begin和end两边同时宽搜，额外创建nextSet存储中间符合条件的节点；每次求出nextSet后，对比next和end set大小，选择小的那个为新的beginSet. 多源BFS是常见的宽搜优化方式.

```swift
class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var beginSet = Set<String>()
        var endSet = Set<String>()
        var seen = Set<String>()
        var words = Set(wordList)
        var steps = 1
        let len = beginWord.count
        let charList = "abcdefghijklmnopqrstuvwxyz"

        guard words.contains(endWord) else { return 0 }

        beginSet.insert(beginWord)
        endSet.insert(endWord)

        // tc: O(mn)
        // 双向 BFS： 效率更高
        while !beginSet.isEmpty && !endSet.isEmpty {
            var nextSet = Set<String>()

            for word in beginSet {
                for i in 0..<len {
                    for ch in charList {
                        var nextWord = word
                        nextWord[i] = ch

                        if endSet.contains(nextWord) { return steps + 1}
                        if words.contains(nextWord) && !seen.contains(nextWord) {
                            nextSet.insert(nextWord)
                            seen.insert(nextWord)
                        }
                    }
                }
            }

            // beginSet和endSet的交替；属于核心优化
            if endSet.count < nextSet.count {
                beginSet = endSet
                endSet = nextSet
            } else {
                beginSet = nextSet
            }

            steps += 1
        }

        return 0
    }
}
```

## 迷宫 (leetcode-490)
巧用direction数组: 根据题意，小球遇到墙壁才能停下，添加visited数组，避免重复访问.

```swift
class Solution {
    // tc: O(mn)
    // sc: O(mn)
    // BFS
    func hasPath(_ maze: [[Int]], _ start: [Int], _ destination: [Int]) -> Bool {
        let directions: [(x: Int, y: Int)] = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        var visited = [[Bool]](repeating: [Bool](repeating: false, count: maze[0].count), count: maze.count)
        var queue = [(x: Int, y: Int)]()
        queue.append((start[0], start[1]))

        let destination = (x: destination[0], y: destination[1])
        visited[start[0]][start[1]] = true

        while !queue.isEmpty {
            let curr = queue.removeFirst()

            guard curr.x != destination.x || curr.y != destination.y else {
                return true
            }

            for direction in directions {
                var x = curr.x + direction.x
                var y = curr.y + direction.y

                while x >= 0, y >= 0, x < maze.count, y < maze[x].count, maze[x][y] == 0 {
                    x += direction.x
                    y += direction.y
                }

                guard !visited[x - direction.x][y - direction.y] else { continue }
                queue.append((x - direction.x, y - direction.y))
                visited[x - direction.x][y - direction.y] = true
            }

        }

        return false
    }
}
```

## 迷宫II (leetcode-505)

490变体，需要求最短路径长度，典型的单源最短路径，可使用堆优化的dijkstra；以下算法使用普通BFS+distance数组，关键在于: 后访问的路径长度可能小于先访问的,所以不设seen数组.

```swift
class Solution {
    func shortestDistance(_ maze: [[Int]], _ start: [Int], _ destination: [Int]) -> Int {
        let directions: [(x: Int, y: Int)] = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        let destination = (x: destination[0], y: destination[1])
        var distance = Array(repeating: Array(repeating: Int.max, count: maze[0].count), count: maze.count)
        var queue = [(x: Int, y: Int, z: Int)]()
        var result = Int.max

        distance[start[0]][start[1]] = 0
        queue.append((start[0], start[1], 0))

        // tc: O(mn*max(m,n))
        while !queue.isEmpty {
            let size = queue.count

            for i in 0..<size {
                let curr = queue.removeFirst()
                let value = curr.z

                for direction in directions {
                    var count = 0
                    var x = curr.x + direction.x
                    var y = curr.y + direction.y

                    while x >= 0, y >= 0, x < maze.count, y < maze[x].count, maze[x][y] == 0 {
                        x += direction.x
                        y += direction.y
                        count += 1
                    } 

                    // 存在重入
                    if distance[x - direction.x][y - direction.y] > value + count {
                        queue.append((x - direction.x, y - direction.y, value+count))
                        distance[x - direction.x][y - direction.y] = value+count
                    }
                }
            }
        }

        return distance[destination.x][destination.y] == Int.max ? -1 : distance[destination.x][destination.y]
    }
}
```

## 最短路径

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

## 地图分析 (leetcode-1162)

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

