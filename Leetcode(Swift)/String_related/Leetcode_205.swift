/*
 Given two strings s and t, determine if they are isomorphic.

 Two strings s and t are isomorphic if the characters in s can be replaced to get t.

 All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 */

import Foundation

class Solution_205 {
    // tc: O(n)
    // sc: O(n)
    // time: 15 min
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        var dict_s: [Character: [Int]] = [:]
        var dict_t: [Character: [Int]] = [:]
        
        let sList = Array(s)
        let tList = Array(t)
        
        for (i, ch) in s.enumerated() {
            if let _ = dict_s[ch] {
                dict_s[ch]?.append(i)
            } else {
                dict_s[ch] = []
                dict_s[ch]?.append(i)
            }
        }
        
        for (i, ch) in t.enumerated() {
            if let _ = dict_t[ch] {
                dict_t[ch]?.append(i)
            } else {
                dict_t[ch] = []
                dict_t[ch]?.append(i)
            }
        }

        for i in 0..<s.count {
            let sch = sList[i]
            let tch = tList[i]

            if let count = dict_s[sch]?.count, count > 1 {
                if dict_s[sch] == dict_t[tch] {
                    continue
                } else {
                    return false
                }
            }
            
            if dict_s[sch]?.count != dict_t[tch]?.count {
                return false
            }
        }
        
        return true
    }
}

class Solution_205_Opt {
    // tc: O(n)
    // sc: O(n)
    // time: 15 min
    // optimized version
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        var dict: [Character: Character] = [:]
        for (sChar, tChar) in zip(s, t) {
            if let expect = dict[sChar] {
                guard expect == tChar else { return false }
            } else {
                guard !dict.values.contains(tChar) else { return false }
                dict[sChar] = tChar
            }
        }

        return true
    }
}
