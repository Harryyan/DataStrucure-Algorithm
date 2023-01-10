# 2 Sum系列

2 sum是一类题型，还有3 sum, 4 sum 以及 k sum。

## 两数之和 (LC-1)
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

## 两数之和 II (LC-167)
和第一题类似，不过要求常数空间，意味着我们不能使用HashMap, 双指针是不二首选:

```swift
class Solution {
    // tc: O(n)
    // sc: O(1)
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
            var i: Int = 0
            var j: Int = nums.count - 1

            while i < j {
                if nums[i] + nums[j] > target {
                    j = j - 1
                } else if nums[i] + nums[j] < target {
                    i = i + 1
                } else {
                    break
                }
            }

            let left =  nums.firstIndex(of: nums[i]) ?? 0
            let right = nums.lastIndex(of: nums[j]) ?? 0

            return [left+1,right+1]  // index starts from 1
        }
}
```

## 两数之和 III (LC-170)
该题考查设计，需要根据要求设计不同时间复杂度的函数. 例如如果题目要求find函数是O(1)的时间复杂度，我们就必须让add函数计算所有的两数之和:

```swift
class TwoSum {
    var sums: Set<Int>
    var nums: Set<Int>

    init() {
        sums = Set<Int>()
        nums = Set<Int>()
    }
    
    // tc: O(n)
    func add(_ number: Int) {
        for num in nums {
            sums.insert(num+number)
        }

        nums.insert(number)
    }
    
    // tc: O(1)
    func find(_ value: Int) -> Bool {
        return sums.contains(value)
    }
}
```
如果题目要求add函数是O(1)，那么就意味着find函数得迭代寻找target:

```swift
class TwoSum {
    var dict: [Int:Int] = [:]

    init() {}
    
    // tc: O(1)
    func add(_ number: Int) {
        dict[number, default:0] += 1
    }
    
    // tc: O(n)
    func find(_ value: Int) -> Bool {
        guard dict.count > 0 else { return false }

        for (k,v) in dict {
            let diff = value - k

            if diff != k, let _ = dict[diff] { return true }
            if diff == k, let result = dict[k], result > 1 { return true }
        }

        return false
    }
}
```