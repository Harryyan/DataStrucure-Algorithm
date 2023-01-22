import Foundation

// 将比pivot小的放到左边
// tc: O(NlogN)
func quickSort_2Ways(_ list: inout [Int], _ start: Int, _ end: Int) {
    guard end >= start else { return }
    
    let pivot = list[start]
    var left = start
    var right = end
    
    while left < right {
        // 若右侧比选出的值大，则继续，否则停止
        while left < right && list[right] >= pivot {
            right -= 1
        }
        
        list[left] = list[right]
        
        // 若左侧比选出的值小，则继续，否则停止
        while left < right && list[left] < pivot {
            left += 1
        }
        
        list[right] = list[left]
    }
    
    list[left] = pivot
    
    // 这里若是查找第K大元素，可以提前退出 -> 快速选择
    //    if left + 1 == k {
    //        return
    //    }
    
    quickSort_2Ways(&list, left, right-1)
    quickSort_2Ways(&list, left+1, right)
}

// 单向快速排序
func quickSort_1Way(start: Int, end: Int, _ nums: inout [Int]) {
    guard start < end else { return }
    
    let mid = partition(start, end, &nums)
    quickSort_1Way(start: start, end: mid-1, &nums)
    quickSort_1Way(start: mid+1, end: end, &nums)
}

func partition(_ start: Int, _ end: Int, _ nums: inout [Int]) -> Int {
    let pivot: Int = Int.random(in: start...end)
    
    // 交换起始值和选中值位置
    nums.swapAt(start, pivot)
    
    // 快, 慢指针
    var slow = start
    var fast = start + 1
    
    while fast <= end {
        if nums[fast] < nums[start] {
            nums.swapAt(slow+1, fast)
            slow += 1
        }
        
        fast += 1
    }
    
    nums.swapAt(start, slow)
    
    return slow
}

// 三向快排
func threeWayQuickSort(_ nums: [Int], _ l: Int, _ r: Int) {
    guard l < r else { return }
    
    let (lt, gt) = partition(nums, l, r)
    
    threeWayQuickSort(nums, l, lt - 1)
    threeWayQuickSort(nums, gt, r)
}

private func partition(_ nums: [Int], _ l: Int, _ r: Int) -> (Int, Int) {
    var nums = nums
    let ind = Int.random(in: l...r)
    
    nums.swapAt(l, ind)
    let base = nums[l]
    
    var lt = l
    var gt = r + 1
    var i = l + 1
    
    while i < gt {
        if nums[i] < base {
            nums.swapAt(i, lt + 1)
            lt += 1
            i += 1
        } else if nums[i] > base {
            nums.swapAt(i, gt - 1)
            gt -= 1
        } else {
            i += 1
        }
    }
    
    nums.swapAt(l, lt)
    
    return (lt, gt)
}
