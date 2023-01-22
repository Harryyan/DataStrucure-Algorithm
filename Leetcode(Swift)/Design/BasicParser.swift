import Foundation

final class BasicParser {
    
    func isMatch(_ text: String, _ pattern: String) -> Bool {
        let texts = Array(text)
        let patterns = Array(pattern)
        
        return rmatch(ti: 0, pi: 0, texts: texts, patterns: patterns)
    }
    
    private func rmatch(ti: Int, pi: Int, texts: [Character], patterns: [Character]) -> Bool {
        if pi == patterns.count {
            return ti == texts.count
        }
        
        let matched = ti < texts.count && (patterns[pi] == "." || patterns[pi] == texts[ti] )
        if pi + 1 < patterns.count && patterns[pi+1] == "*" {
            return rmatch(ti: ti, pi: pi+2, texts: texts, patterns: patterns) ||
            matched && rmatch(ti: ti+1, pi: pi, texts: texts, patterns: patterns)
        }
        
        return matched && rmatch(ti: ti+1, pi: pi+1, texts: texts, patterns: patterns)
    }
}

final class BasicParser_Memo {
    var memo: [[Int]] = []
    
    func isMatch(_ text: String, _ pattern: String) -> Bool {
        let texts = Array(text)
        let patterns = Array(pattern)
        
        memo = Array(repeating: Array(repeating: -1, count: texts.count+2), count: patterns.count+2)
        
        return rmatch(ti: 0, pi: 0, texts: texts, patterns: patterns)
    }
    
    private func rmatch(ti: Int, pi: Int, texts: [Character], patterns: [Character]) -> Bool {
        if pi == patterns.count {
            return ti == texts.count
        }
        
        if ti > texts.count {
            return false
        }
        
        if memo[pi][ti] != -1 {
            return memo[pi][ti] == 1
        }
        
        let matched = ti < texts.count && (patterns[pi] == "." || patterns[pi] == texts[ti])
        
        if pi + 1 < patterns.count && patterns[pi+1] == "*" {
            let a = rmatch(ti: ti, pi: pi+2, texts: texts, patterns: patterns)
            let b = rmatch(ti: ti+1, pi: pi, texts: texts, patterns: patterns)
            
            memo[pi][ti] = (a || matched && b) == true ? 1 : 0
            return memo[pi][ti] == 1
        }
        
        memo[pi][ti] = matched && rmatch(ti: ti+1, pi: pi+1, texts: texts, patterns: patterns) == true ? 1 : 0
        
        return memo[pi][ti] == 1
    }
}


final class BasicParser_DP {
    
    func isMatch(_ text: String, _ pattern: String) -> Bool {
        let texts = Array(text)
        let patterns = Array(pattern)
        
        var dp = Array(repeating: Array(repeating: false, count: patterns.count+1), count: texts.count+1)
        dp[0][0] = true
        
        // Init first row
        for i in 1...patterns.count {
            if patterns[i-1] == "*" {
                dp[0][i] = dp[0][i-2]
            }
        }
        
        for i in 1...texts.count {
            for j in 1...patterns.count {
                if String(patterns[j-1]) == "." || String(patterns[j-1]) == String(texts[i-1]) {
                    dp[i][j] = dp[i-1][j-1]
                } else if String(patterns[j-1]) == "*" {
                    dp[i][j] = dp[i][j-2] ||
                               (
                                (patterns[j-2] == "." || texts[i-1] == patterns[j-2]) &&
                                (dp[i-1][j-1] || dp[i-1][j])
                               )
                }
            }
        }
        
        return dp[texts.count][patterns.count]
    }
}
