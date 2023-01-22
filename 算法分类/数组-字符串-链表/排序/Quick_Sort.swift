import Foundation

class Solution {
    
    func sortArray(_ nums: [Int]) -> [Int] {
        guard nums.count > 0 else {
            return []
        }
        
        var sortNums = nums
        quickSort(start: 0, end: nums.count - 1, &sortNums)
        
        return sortNums
    }
    
    private func quickSort(start: Int, end: Int, _ nums: inout [Int]) {
        if start < end {
            let mid = partition(start, end, &nums)
            quickSort(start: start, end: mid-1, &nums)
            quickSort(start: mid+1, end: end, &nums)
        }
    }
    
    private func partition(_ start: Int, _ end: Int, _ nums: inout [Int]) -> Int {
        let pivot: Int = Int.random(in: start...end)
        
        // 交换起始值和选中值位置
        nums.swapAt(start, pivot)
        
        // 快, 慢指针
        var slow = start
        var fast = slow + 1
        
        while fast <= end {
            if nums[fast] < nums[start] {
                (nums[slow+1], nums[fast]) = (nums[fast], nums[slow+1])
                slow += 1
            }
            
            fast += 1
        }
        
        nums.swapAt(start, slow)
        
        return slow
    }
}

let s = Solution()
let result = s.sortArray([6,7,5,4,2,9])

print(result)
