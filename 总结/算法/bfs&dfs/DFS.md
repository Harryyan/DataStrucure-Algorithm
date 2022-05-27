# DFS总结

深度优先搜索, 常用来解决可达性问题.

1. 用递归栈存节点信息，按需pop
2. 类似BFS，做标记

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

## 标记

### 岛屿的最大面积 (leetcode-695)
类似题目还有130, 200, 547， 417

伪代码模板:

```swift
forLoop:
   dfs()
```

```swift
class Solution {
    var area = 0
    var result = 0

    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var grid = grid

        let m = grid.count
        let n = grid[0].count

        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    area = 0
                    dfs(i,j, &grid)
                    result = max(result, area)
                }
            }
        }

        return result
    }

    private func dfs(_ i: Int, _ j: Int, _ grid: inout [[Int]]) {
        let directions = [[0,-1],[0,1],[1,0],[-1,0]]

        grid[i][j] = 0
        area += 1

        for direction in directions {
            let x = i + direction[0]
            let y = j + direction[1]

            if x >= 0 && x < grid.count && y >= 0 && y < grid[0].count && grid[x][y] == 1 {
                dfs(x,y,&grid)
            }
        }
    }
}
```
