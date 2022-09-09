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
