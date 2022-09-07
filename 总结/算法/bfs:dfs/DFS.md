# DFS总结

深度优先搜索, 常用来解决可达性问题:

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

## 子集 (Leetcode-78)

```swift

```