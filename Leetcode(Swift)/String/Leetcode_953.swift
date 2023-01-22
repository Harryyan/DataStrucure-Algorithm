/*
 In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
 The order of the alphabet is some permutation of lowercase letters.
 
 Given a sequence of words written in the alien language, and the order of the alphabet,
 return true if and only if the given words are sorted lexicographically in this alien language.
 
 */


import Foundation

class Solution_953 {
    
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        var dict: [Character: Int] = [:]
        var value = 0
        
        for i in order {
            dict[i] = value
            value += 1
        }
        
        for i in 0..<words.count-1 {
            if compare(words[i], words[i+1], dict: dict) {
                return false
            }
        }
        
        return true
    }
    
    private func compare(_ first: String, _ second: String, dict: [Character:Int]) -> Bool {
        let input0 = Array(first)
        let input1 = Array(second)
        
        for i in 0..<first.count {
            if i >= second.count || dict[input0[i]]! > dict[input1[i]]! {
                return true
            }
            
            if dict[input0[i]]! < dict[input1[i]]! {
                return false
            }
        }
        
        return false
    }
}
