# 2Sum系列

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

## 两数之和 IV - 输入二叉搜索树 (LC-653)
这题主要考察最优空间复杂度，O(n)空间复杂度不是我们追求的，最优的空间复杂度是O(h), h是输的高度. 这题我们需要引入一个概念，那就是**BSTIterator**, 可以以O(h)的空间复杂度解决这个问题. 类似的，以后遇到BST的题目，掌握**BSTIterator**是优化空间复杂度的一个手段:

```swift
class Solution {
    // tc: O(n)
    // sc: O(h) - The height of tree, best solution
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        // left and right pointer of BST
        let left = BSTIterator(root, true)
        let right = BSTIterator(root, false)

        while left.hasNext() && right.hasNext() {
            let vl = left.peek()
            let vr = right.peek()

            guard vl < vr else { return false }

            if vl + vr == k { return true }
            else if vl + vr < k { left.next() }   // update value, but not use it
            else { right.next() }
        }

        return false
    }
}
```
我们需要左右两个iterator，类似一维数组的左右指针，分别指向最小的和最大的节点. 之后就和普通二分一样，分别根据规则移动左右指针.

```swift
final class BSTIterator {
    private var stack: [TreeNode?] = []
    private let forward: Bool
    private let invalidValue = ~0
    
    init(_ root: TreeNode?, _ forward: Bool) {
        let node = root
        self.forward = forward
        
        forward ? pushLeftNodes(of: node) : pushRightNodes(of: node)
    }
    
    func hasNext() -> Bool {
        return stack.count > 0
    }
    
    func next() -> Int {
        let node: TreeNode? = stack.removeLast()
        
        forward ? pushLeftNodes(of: node?.right) : pushRightNodes(of: node?.left)
        
        return node?.val ?? invalidValue
    }
    
    func pushLeftNodes(of root: TreeNode?) {
        var node: TreeNode? = root
        
        while node != nil {
            stack.append(node)
            node = node?.left
        }
    }
    
    func pushRightNodes(of root: TreeNode?) {
        var node: TreeNode? = root
        
        while node != nil {
            stack.append(node)
            node = node?.right
        }
    }
    
    func peek() -> Int {
        return stack.last??.val ?? invalidValue
    }
}
```

## 三数之和 (LC-15)
和两数之和类似，但要多一层for循环，for循环内部还是两数之和, 注意去重:

```swift
class Solution {
    // tc: O(n^2)
    // sc: O(logn)
    func threeSum(_ nums: [Int]) -> [[Int]] {
        var res = [[Int]]()
        var sorted = nums
        sorted.sort()

        for i in 0 ..< sorted.count {
            guard sorted[i] <= 0 else { return res }

            // skip duplicated elements
            if i > 0 && sorted[i] == sorted[i - 1] { continue }
            var left = i + 1
            var right = sorted.count - 1

            // two sum 
            while left < right {
                let sum = sorted[i] + sorted[left] + sorted[right]
                if sum < 0 {
                    left += 1
                } else if sum > 0 {
                    right -= 1
                } else {
                    res.append([sorted[i], sorted[left], sorted[right]])
                    
                    // skip duplicated elements
                    while left < right && sorted[left] == sorted[left + 1] {
                        left += 1
                    }
                    // skip duplicated elements
                    while left < right && sorted[right] == sorted[right - 1] {
                        right -= 1
                    }
                    
                    left += 1
                    right -= 1
                }
            }
        }
        return res
    }
}
```