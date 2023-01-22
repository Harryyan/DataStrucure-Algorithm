import Foundation

class BinarySearch {
    
    // 只判断是否存在
    func search(_ list: [Int], _ target: Int) -> Bool {
        var left = 0
        var right = list.count
        
        while left < right {
            let mid = left + (right - left) / 2
            
            if list[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        
        return list[left] == target
    }
    
    // 找左边第一个出现位置
    func search_lower_bound(_ list: [Int], _ target: Int) -> Int {
        var left = 0
        var right = list.count - 1
        
        while left < right {
            let mid = left + (right - left) / 2
            
            if list[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        
        return list[left] == target ? left : -1
    }
    
    // 找右边最后一个出现位置
    func search_upper_bound(_ list: [Int], _ target: Int) -> Int {
        var left = 0
        var right = list.count - 1
        
        while left < right {
            // 关键
            let mid = left + (right - left + 1) / 2
            
            if list[mid] > target {
                right = mid - 1
            } else {
                left = mid
            }
        }
        
        return list[left] == target ? left : -1
    }
}
