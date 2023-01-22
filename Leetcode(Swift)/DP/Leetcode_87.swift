import Foundation

/*
 We can scramble a string s to get a string t using the following algorithm:
 
 If the length of the string is 1, stop.
 If the length of the string is > 1, do the following:
 Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
 Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
 Apply step 1 recursively on each of the two substrings x and y.
 Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
 
 */

// 非记忆化递归
// 超时:
//      "eebaacbcbcadaaedceaaacadccd"
//      "eadcaacabaddaceacbceaabeccd"

// 时间复杂度: 指数级 O(5 ^ n) - 宫水三叶
// 空间复杂度: O(1)
final class Solution_87_Recursion_Plain {
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        if s1 == s2 { return true }
        guard check(s1, s2) else { return false }
        
        let n = s1.count
        
        for i in 1..<n {
            let index_s1 = s1.index(s1.startIndex, offsetBy: i)
            let a = s1[..<index_s1]             // s1的 [0,i)
            let b = s1[index_s1..<s1.endIndex]  // s1的 [i,n)
            
            // 保持原有顺序
            let index_s2 = s2.index(s2.startIndex, offsetBy: i)
            let c = s2[..<index_s2]                // s2的 [0,i)
            let d = s2[index_s2..<s2.endIndex]  // s2的 [i,n)
            
            if isScramble(String(a), String(c)) && isScramble(String(b), String(d)) { return true }
            
            // 改变顺序
            let index_s2_2 = s2.index(s2.endIndex, offsetBy: -i)
            let e = s2[..<index_s2_2]           // s2的 [0,n-i)
            let f = s2[index_s2_2..<s2.endIndex]  // s2的 [n-i,n)
            
            if isScramble(String(a), String(f)) && isScramble(String(b), String(e)) { return true }
        }
        
        return false
    }
    
    // 检测词频
    private func check(_ s1: String, _ s2: String) -> Bool {
        guard s1.count == s2.count else { return false }
        
        if s1 == s2 { return true }
        
        let dict_s1 = Counter().count(s1)
        let dict_s2 = Counter().count(s2)
        
        var result = true
        
        let _ = "abcdefghijklmnopqrstuvwxyz".map {
            if dict_s1[String($0)] != dict_s2[String($0)] {
                result = false
            }
        }
        
        return result
    }
}

// 引入cache, 记录中间值， 减少无效递归
final class Solution_87_Recursion_Memo {
    private var caches: [[[Int]]] = [[[Int]]]()
    
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        if s1 == s2 { return true }
        
        let n = s1.count
        
        // 第一个维度: s1起始值；
        // 第二个维度: s2起始值
        // 第三个维度: 它们的长度
        // 这个三个维度确认了唯一区间
        caches = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: n), count: n), count: n)
        
        return dfs(Array(s1), 0, n-1, Array(s2), 0, n-1)
    }
    
    private func dfs(_ s1: [Character],
                     _ start_s1: Int,
                     _ end_s1: Int,
                     _ s2: [Character],
                     _ start_s2: Int,
                     _ end_s2: Int) -> Bool {
        if start_s1 == end_s1 {
            return s1[start_s1] == s2[start_s2]
        }
        
        // 剪枝
        // 注意这里: 等于1是true，等于-1是false，所以要先判断是否为0；否则依旧超时;
        if caches[start_s1][start_s2][end_s1-start_s1] != 0 {
            return caches[start_s1][start_s2][end_s1-start_s1] > 0
        }
        
        for i in 0..<end_s1-start_s1 {
            // 保持顺序
            if dfs(s1, start_s1, start_s1+i, s2, start_s2, start_s2+i) &&
                dfs(s1, start_s1+i+1, end_s1, s2, start_s2+i+1, end_s2) {
                caches[start_s1][start_s2][end_s1-start_s1] = 1
                return true
            }
            
            // 改变顺序
            if dfs(s1, start_s1, start_s1+i, s2, end_s2-i, end_s2) &&
                dfs(s1, start_s1+i+1, end_s1, s2, start_s2, end_s2-i-1) {
                caches[start_s1][start_s2][end_s1-start_s1] = 1
                return true
            }
        }
        
        caches[start_s1][start_s2][end_s1-start_s1] = -1
        
        return false
    }
}


// 动态规划
// tc: O(n^4）
// sc: O(n^3)
final class Solution_87_Recursion_DP {
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        if s1 == s2 { return true }
        
        guard s1.count == s2.count else { return false }
        
        let n = s1.count
        let item1 = Array(s1)
        let item2 = Array(s2)
        
        // 第一个维度: s1起始值；
        // 第二个维度: s2起始值
        // 第三个维度: 它们的长度
        // 这个三个维度确认了唯一区间
        var dp = [[[Bool]]](repeating: [[Bool]](repeating: [Bool](repeating: false, count: n+1), count: n), count: n)
        
        // s1从i开始, s2从j开始，长度为1时
        // 初始化状态矩阵
        for i in 0..<n {
            for j in 0..<n {
                dp[i][j][1] = item1[i] == item2[j]
            }
        }
        
        guard n >= 2 else { return dp[0][0][n] }
        
        for len in 2...n {
            for i in 0...n-len {
                for j in 0...n-len {
                    for k in 1..<len {
                        // 对应了「s1 的 [0,i) & [i,n)」匹配「s2 的 [0,i) & [i,n)」
                        let a = dp[i][j][k] && dp[i+k][j+k][len-k]
                        // 对应了「s1 的 [0,i) & [i,n)」匹配「s2 的 [n-i,n) & [0,n-i)」
                        let b = dp[i][j+len-k][k] && dp[i+k][j][len-k]
                        
                        if a || b {
                            dp[i][j][len] = true
                        }
                    }
                }
            }
        }
        
        return dp[0][0][n]
    }
}
