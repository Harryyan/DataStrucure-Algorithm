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

## 全排列II (Leetcode-47)
和46类似，加排序去重

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