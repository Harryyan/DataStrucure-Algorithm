# 2 Sum系列

2 sum是一类题型，还有3 sum, 4 sum 以及 k sum。

## Two Sum(LC-1)
2Sum始祖题. 这里主要是训练我们对不同数据结构的选择以及trade-off:

1.  暴力解: O(n²)时间复杂度
2. 双指针: O(nlogn)时间复杂度 - 需要排序
3. 哈希表: O(n) 时间复杂度 - 空间复杂度高

以下是双指针版本:

```swift
class Solution {
    // tc: O(nlogn)
    // sc: O(logn)
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var sortNums = nums.sorted(by:<)
        var i: Int = 0
        var j: Int = sortNums.count - 1

        while i < j {
            if sortNums[i] + sortNums[j] > target {
                j = j - 1
            } else if sortNums[i] + sortNums[j] < target {
                i = i + 1
            } else {
                break
            }
        }

        return [nums.firstIndex(of: sortNums[i]) ?? 0,nums.lastIndex(of: sortNums[j]) ?? 0]
    }
}
```