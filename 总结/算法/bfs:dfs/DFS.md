# DFS总结

深度优先搜索, 常用来解决可达性问题. 

深度优先遍历的主要思想就是：首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点；当没有未访问过的顶点时，则回到上一个顶点，继续试探访问别的顶点，直到所有的顶点都被访问。
沿着某条路径遍历直到末端，然后回溯，再沿着另一条进行同样的遍历，直到所有的顶点都被访问过为止。


1. 用递归栈存节点信息，按需pop
2. 类似BFS，做标记

**DFS 一般使用场景:**

1. 模板dfs, mask举例dfs
2. 外部空间dfs(写成迭代)
3. dfs+memo(top down)
4. 全排列类似题目

## 递归栈

以下代码片段是递归删除某文件夹下所有文件实现; 使用递归栈存取文件夹指针，直到为空再popLast.

```objc
while([stack count] > 0) {
    NSEnumerator *top = stack.lastObject;
    NSString *fileName = [top nextObject];
    
    if (fileName) {
        NSDictionary *attributesDictionary = [self attributesOfItemAtPath:[currentPath stringByAppendingPathComponent:fileName] error:nil];
        
        if ([attributesDictionary objectForKey:NSFileType] == NSFileTypeDirectory) {
            currentPath = [currentPath stringByAppendingPathComponent:fileName];
            NSArray *contents = [self contentsOfDirectoryAtPath: currentPath error:nil];
            NSEnumerator *enumerator = [contents objectEnumerator];
            
            if (enumerator) {
                [stack addObject:enumerator];
            }
        } else {
            if ([fileName.pathExtension.lowercaseString isEqualToString:itemsExtension]) {
                [self mnz_removeItemAtPath:[currentPath stringByAppendingPathComponent:fileName]];
            }
        }
    } else {
        NSArray *contents = [self contentsOfDirectoryAtPath:currentPath error:nil];
        
        if (contents.count == 0 && currentPath != folderPath) {
            [self mnz_removeItemAtPath:currentPath];
        }
        
        currentPath = [currentPath stringByDeletingLastPathComponent];
        [stack removeLastObject];
    }
}
```

## 子集 (Leetcode-78)
模板dfs: 迭代或者递归.

递归：

```swift
class Solution {
    var res: [[Int]] = []
    var nums: [Int] = []

    func subsets(_ nums: [Int]) -> [[Int]] {
        self.nums = nums

        dfs(0, [])

        return res
    }

    private func dfs(_ index: Int, _ temp: [Int]) {
        guard index < nums.count else { 
            res.append(temp)
            return 
        }

        // 选当前值
        dfs(index+1, [nums[index]] + temp)

        // 不选当前值
        dfs(index+1, temp)
    }
}
```

迭代：

```swift
class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        var res: [[Int]] = [[]]

        for num in nums {
            for item in res {
                res.append([num]+item)
            }
        }

        return res
    }
}
```

mask(位运算):

```swift
class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        var total = 1 << nums.count
        var res: [[Int]] = []

        for i in 0..<total {
            var list: [Int] = []

            for j in 0..<nums.count {
                // 关键
                if i & (1<<j) != 0 {
                    list.append(nums[j])
                }
            }

            res.append(list)
        }

        return res
    }
}
```

## 子集II (Leetcode-90)
和子集题目唯一区别就是**排序，去重**

```swift
class Solution {
    func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
        var nums = nums.sorted()
        var res: [[Int]] = [[]]
        var middle: [[Int]] = []

        for i in 0..<nums.count {
            if i > 0 && nums[i-1] == nums[i] {
                var temp: [[Int]] = [] 
                for item in middle {
                    temp.append([nums[i]] + item)
                } 

                middle = temp
            } else {
                var temp: [[Int]] = []
                for item in res {
                    temp.append([nums[i]] + item)
                }

                middle = temp
            }

            res += middle
        }

        return res
    }
} 

```

## 全排列 (Leetcode-46)
和子集题目一样，要先判断元素是否有重复:

```swift
class Solution {
    var res: [[Int]] = []
    var visited: [Int] = []

	 // tc: O(N!)
    func permute(_ nums: [Int]) -> [[Int]] {
        visited = Array(repeating: 0, count: nums.count)

        dfs(nums, [])

        return res
    }

    private func dfs(_ nums: [Int], _ temp: [Int]) {
        var temp = temp

        if temp.count == nums.count {
            res.append(temp)
        }

        for i in 0..<nums.count {
            if visited[i] == 1 { continue }

            visited[i] = 1
            dfs(nums, temp + [nums[i]])
            visited[i] = 0
        }
    }
}
```

## 组合 (Leetcode-77)
类似子集模板，区别就是停止条件: 这里是选购K个即可停止.

```swift
class Solution {
    var res: [[Int]] = []
    var n = 0
    
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        self.n = n

        dfs(1, k, [])

        return res
    }

    private func dfs(_ index: Int, _ k: Int,  _ temp: [Int]) {
        guard index <= n + 1 else { return }

        if temp.count == k {
            res.append(temp)
            return
        }

        // 选当前值
        dfs(index+1, k, [index] + temp)

        // 不选当前值
        dfs(index+1, k, temp)
    }
}
```

## 数独 (Leetcode-37)
暴力解，遍历每行，每列，每个3X3的矩阵:

无优化版本，不做cache记录(136ms):

```swift
class Solution {
    func solveSudoku(_ board: inout [[Character]]) {
        _ = solve(&board)
    }
    
    private func solve(_ board: inout [[Character]]) -> Bool {
        for i in 0..<board.count {
            for j in 0..<board[0].count {
                if board[i][j] == Character(".") {
                    for value in 1...9 {
                        if isValid(value, board, i, j) {
                            board[i][j] = Character("\(value)")
                            
                            if solve(&board) { return true }
                            else { board[i][j] = Character(".") }
                        }
                    }

                    return false
                }
            }
        }
        
        return true
    }
    
    private func isValid(_ ch: Int, _ board: [[Character]], _ i: Int, _ j: Int) -> Bool {
        
        for row in 0..<9 {
            if board[row][j].isWholeNumber && board[row][j].wholeNumberValue! == ch {
                return false
            }
        }
        
        for col in 0..<9 {
            if board[i][col].isWholeNumber && board[i][col].wholeNumberValue! == ch {
                return false
            }
        }
        
        for row in (i/3)*3..<(i/3)*3+3 {
            for col in (j/3)*3..<(j/3)*3+3 {
                if board[row][col].isWholeNumber && board[row][col].wholeNumberValue! == ch {
                    return false
                }
            }
        }
        
        return true
    }
}
```

## N皇后 (Leetcode-51)
经典dfs，暴力解，一行一行遍历; 类似的还有8皇后；思路简单，实现难点在validate or isOK 函数，要每行，每列，每个对角线判断是否符合:

这里有个小技巧：判断两个点: (i,j) 和 (x,y) 是否在同一条对角线上，可以按照以下规则:

x + y == i + j (在同一反对角线上)

x + i == y + j (在同一对角线上)

```swift
final class Solution {
    var result: [Int] = []
    var result2: [[String]] = []
    
    func solveNQueens(_ n: Int) -> [[String]] {
        result = Array(repeating: 0, count: n)
        
        dfs(0, n)
        
        return result2
    }
    
    private func dfs(_ row: Int, _ size: Int) {
        if row == size {
            printNQueen(size)
            return
        }
        
        for col in 0..<size {
            if isOK(row: row, col: col, size: size) {
                result[row] = col
                dfs(row+1, size)
            }
        }
    }
    
    private func isOK(row: Int, col: Int, size: Int) -> Bool {
        var leftUp = col - 1
        var rightUp = col + 1
        
        for i in stride(from: row-1, to: -1, by: -1)  {
            if result[i] == col {
                return false
            }
            
            if leftUp >= 0 && result[i] == leftUp {
                return false
            }
            
            if rightUp < size && result[i] == rightUp {
                return false
            }
            
            leftUp -= 1
            rightUp += 1
        }
        
        return true
    }
    
    private func printNQueen(_ size: Int) {
        var s: [String] = []
        
        for i in 0..<size {
            var r = ""
            
            for j in 0..<size {
                if result[i] == j {
                    r += "Q"
                } else {
                    r += "."
                }
            }
            
            s.append(r)
        }

         result2.append(s)
    }
}
```

# DFS剪枝优化

todo:

## 全排列II (Leetcode-47)
和46类似，加排序去重:

```swift
class Solution {
    var visited: [Int] = []
    var res: [[Int]] = []

    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        visited = Array(repeating: 0, count: nums.count)
        var nums = nums.sorted()

        dfs(nums, nums.count, [])

        return res
    }

    private func dfs(_ list: [Int], _ n : Int, _ temp: [Int]) {
        if temp.count == n {
            res.append(temp)
            return
        }
        
        for i in 0..<n {
            if visited[i] == 1 { continue }
				
			  // 去重关键
            if i > 0 && list[i-1] == list[i] && visited[i-1] == 0 {
                continue
            }

            visited[i] = 1
            dfs(list, n, temp + [list[i]])
            visited[i] = 0
        }
    }
}
```

## 数独 (Leetcode-37)
优化版本，有cache记录(20ms): 分别记录该数字在行，列，九宫格的存在与否:

```swift
class Solution {
    let choiceCharacter: [Character] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    //  把每行每列每个格子已经填充的数保存起来
    var rows = Array.init(repeating: Array(repeating: 0, count: 10), count: 9)
    var cols = Array.init(repeating: Array(repeating: 0, count: 10), count: 9)
    var grides = Array.init(repeating: Array(repeating: 0, count: 10), count: 9)
    var spaces = [(Int, Int)]()
    
    func solveSudoku(_ board: inout [[Character]]) {
        // 数据预处理
        for i in 0..<9 {
            for j in 0..<9 {
                let c = board[i][j]
                if c == "." {
                    spaces.append((i, j))
                } else {
                    let intC = Int(String(c))!
                    rows[i][intC] = 1
                    cols[j][intC] = 1
                    grides[i / 3 * 3 + j / 3][intC] = 1
                }
            }
        }
        dfs(&board, index: 0)
    }
    
    func dfs(_ board: inout [[Character]], index: Int) -> Bool {
        guard index < spaces.count else {
            return true
        }
        
        let (i , j) = spaces[index]
        let grid = i / 3 * 3 + j / 3
        
        for choice in 1...9 {
            //  填充的数已经存在
            if rows[i][choice] == 1 || cols[j][choice] == 1 || grides[grid][choice] == 1  {
                continue
            }
            board[i][j] = choiceCharacter[choice]
            rows[i][choice] = 1
            cols[j][choice] = 1
            grides[i / 3 * 3 + j / 3][choice] = 1
            
            if (dfs(&board, index: index + 1)) {
                return true
            }
            
            board[i][j] = "."
            rows[i][choice] = 0
            cols[j][choice] = 0
            grides[i / 3 * 3 + j / 3][choice] = 0
            
        }
        return false
    }
}
```

## 完成所有工作的最短时间 (Leetcode-1723)
这道题是dfs和二分结合题，这里主要讨论dfs剪枝策略:

1. 对数组排序，从大的那头开始遍历，让循环结束快点
2. 如果result > max, 跳过
3. 如果撤销选择后，值为0，直接跳出循环(相当于又来一遍)

```swift
class Solution {
    func minimumTimeRequired(_ jobs: [Int], _ k: Int) -> Int {
        var left = jobs.max()!
        var right = jobs.reduce(.zero, +)
        var jobs = jobs.sorted()

        while left < right {
            let mid = left + (right - left) / 2

            if valid(k,mid,jobs) {
                right = mid
            } else {    
                left = mid + 1
            }
        }

        return left
    }

    private func valid(_ k: Int, _ limit: Int, _ jobs: [Int])-> Bool {
        var groups = Array(repeating: 0, count: k)

        if dfs(jobs, k, limit, groups) {
            return true
        } else {
            return false
        }
    }

    private func dfs(_ jobs: [Int], _ k: Int, _ limit: Int, _ groups: [Int]) -> Bool {
        guard jobs.count > 0 else { return true }

        var jobs = jobs
        var groups = groups
        let cur = jobs.removeLast()

        for i in 0..<k {
            if groups[i] + cur <= limit {
                groups[i] += cur

                if dfs(jobs, k, limit, groups) {
                    return true
                }

                groups[i] -= cur

                if groups[i] == 0 {
                    break
                }
            }
        }

        return false
    }
}
```

## 完成所有工作的最短时间 (Leetcode-1986)
和1723类似，这里不能用贪心，例如[10,8,7,4,3], sessionTime = 12; 贪心无法保证正确分配; 得使用dfs遍历所有情况，有一个返回true，即可:

```swift
class Solution {
    var tasks: [Int] = []

    // tc: O(bucket ^ n)
    func minSessions(_ tasks: [Int], _ sessionTime: Int) -> Int {
        var left = 1
        var right = 0

        for task in tasks {
            right += (task + sessionTime - 1) / sessionTime
        }

        self.tasks = tasks.sorted(by: >)

        while left < right {
            let mid = left + (right - left) / 2

            // 放得下
            if !check(mid, sessionTime) {
                left = mid + 1
            } else {
                right = mid
            }
        } 

        return left
    }

    private func check(_ mid: Int, _ sessionTime: Int) -> Bool {
        // Session buckets
        var groups = Array(repeating: 0, count: mid)
        return dfs(mid, &groups, sessionTime, 0)
    }

    private func dfs(_ mid: Int, _ bucket: inout [Int], _ sessionTime: Int, _ index: Int) -> Bool {
        guard index < tasks.count else { return true }

        for i in 0..<bucket.count {
            if bucket[i] + tasks[index] <= sessionTime {
                bucket[i] += tasks[index]

                if dfs(mid, &bucket, sessionTime, index+1) {
                    return true
                }

                bucket[i] -= tasks[index]

                if bucket[i] == 0 {
                    break
                }
            }
        }

        return false
    }
}
```

## 完成所有工作的最短时间 (Leetcode-1723)

# 总结
BFS:对于解决最短或最少问题特别有效，而且寻找深度小，但缺点是内存耗费量大（需要开大量的数组单元用来存储状态）。

DFS：对于解决遍历和求所有问题有效，对于问题搜索深度小的时候处理速度迅速，然而在深度很大的情况下效率不高

DFS的优点:

内存开销较小，每次只需维护一个结点
能处理子节点较多或树层次过深的情况(相对BFS)， **一般用于解决连通性问题（是否有解）**

DFS的缺点:

只能寻找有解但无法找到最优解（寻找最优解要遍历所有路径）

