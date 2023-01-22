/*
 Write a function to find the longest common prefix string amongst an array of strings.

 If there is no common prefix, return an empty string "".
 */

import Foundation

final class Solution_14 {
    var stack: [Character] = []
    var flag = true
    
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard strs.count > 0 else { return "" }
                
        dfs(strs)
        
        return String(stack)
    }
    
    private func dfs(_ strs: [String]) {
        guard flag else { return }
        
        var str_cy = strs
        var set: Set<Character> = []
        
        for i in 0..<str_cy.count {
            var ch: Character?
            
            if str_cy[i].count > 0 {
                ch = str_cy[i].removeFirst()
            }
            
            if let ch = ch {
                set.insert(ch)
            } else {
                if set.count > 0 {
                    flag = false
                    break
                }
            }
            
            if set.count > 1 {
                flag = false
                break
            }
            
            if set.count == 0 {
                flag = false
                break
            }
        }
        
        if let first = set.first, flag {
            stack.append(first)
        }
        
        dfs(str_cy)
    }
}
