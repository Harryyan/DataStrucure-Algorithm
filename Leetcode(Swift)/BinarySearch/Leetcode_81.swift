import Foundation

final class Solution_81 {
    func search(_ nums: [Int], _ target: Int) -> Bool {
        if nums.count == 0 {
            return false
        } else  if nums.count == 1 {
            return nums[0] == target
        }
        
        var start = 0
        var end = nums.count - 1
        
        while start + 1 < end {
            while start + 1 < end {
                if nums[start] == nums[start + 1] {
                    start += 1
                } else {
                    break
                }
            }
            while end - 1 > start {
                if nums[end] == nums[end - 1] {
                    end -= 1
                } else {
                    break
                }
            }

            let mid = (start + end) / 2
            
            if target == nums[mid] {
                return true
            }
            
            if nums[start] <= nums[mid] {
                if target <= nums[mid] && target >= nums[start]{
                    end = mid
                }else{
                    start = mid
                }
            } else {
                if target >= nums[mid] && target <= nums[end]{
                    start = mid
                }else{
                    end = mid
                }
            }
        }
        return (nums[start] == target) || (nums[end] == target)
    }
}
