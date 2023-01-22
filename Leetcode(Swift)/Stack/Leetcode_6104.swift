/*
 You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

 Return the lexicographically largest repeatLimitedString possible.

 A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.
 */
import Foundation

// 超时：
// Swift 计算字典key出现次数超时，python不超
class Solution_6104 {
    
    func repeatLimitedString(_ s: String, _ repeatLimit: Int) -> String {
        let dict = Counter().count(s)
        var res = ""
        var q = dict.sorted(by: {$0.0 < $1.0} )

        while !q.isEmpty {
            let (ch, cnt) = q.removeLast()
            var limit = repeatLimit
            
            if res.count > 0, String(res.last!) == String(ch) {
                limit -= 1
            }
            
            let count = min(repeatLimit, cnt)
            for _ in 0..<count {
                res.append(ch)
            }
            
            if !q.isEmpty {
                var (ch, cnt) = q.removeLast()
                res.append(ch)
                cnt -= 1
                
                if cnt > 0 {
                    q.append((ch, cnt))
                }
            } else {
                break
            }
            
            if cnt > 0 {
                q.append((ch,cnt))
            }
        }
        
        return res
    }
}
