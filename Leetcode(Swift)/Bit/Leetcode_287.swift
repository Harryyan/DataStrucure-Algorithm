import Foundation

class Solution_287 {
    func findDuplicate(_ nums: [Int]) -> Int {
        let n = nums.count - 1
        var res = -1
        
        for p in 0..<32 {
            let bit = 1 << p
            var a = 0
            var b = 0
            
            for i in 0...n {
                if i > 0 && (i & bit) > 0 {
                    a += 1
                }
                
                if (nums[i] & bit) > 0 {
                    b += 1
                }
            }
            
            if b > a {
                res += bit
            }
        }
        
        return res
    }
}
