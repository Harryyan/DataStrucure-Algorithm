import Foundation

/*
 Given a string s, partition s such that every substring of the partition is a range.
 Return all possible palindrome partitioning of s.
 
 A palindrome string is a string that reads the same backward as forward.
 */


final class Solution_131 {
    func partition(_ s: String) -> [[String]] {
        var res = [[String]]()
        var temp = [String]()
        
        dfs(s, &temp, &res)
        
        return res
    }
    
    func dfs(_ s: String, _ temp: inout [String], _ res: inout [[String]]) {
        guard !s.isEmpty else { return }
        
        if isPalindrome(s) {
            let t = temp
            res.append(t + [s])
        }
        
        for i in 0 ..< s.count {
            let index = s.index(s.startIndex, offsetBy: i)
            let substr = s[s.startIndex ... index]
            
            if isPalindrome(String(substr)) {
                temp.append(String(substr))
                
                let tailstr = s[s.index(after: index) ..< s.endIndex]
                dfs(String(tailstr), &temp, &res)
                _ = temp.popLast()
                
            }
        }
    }
    
    func isPalindrome(_ s: String) -> Bool {
        var i = 0, j = s.count - 1
        let sArr = Array(s)
        while i < j {
            if sArr[i] != sArr[j] {
                return false
            }
            i += 1
            j -= 1
        }
        return true
    }
}

