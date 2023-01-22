/*
 There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
 
 You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted
 lexicographically by the rules of this new language.
 
 Return a string of the unique letters in the new alien language sorted in lexicographically
 increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions,
 return any of them.
 
 A string s is lexicographically smaller than a string t if at the first letter where they differ,
 the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length
 */

// words = ["wrt","wrf","er","ett","rftt"]

import Foundation

final class Solution_269 {
    
    func alienOrder(_ words: [String]) -> String {
        var dict: [Character: Set<Character>] = [:]
        let count = words.count
        var allCharacters: Set<Character> = Set<Character>()
        var result: [Character] = []
        
        for word in words {
            for w in word {
                allCharacters.insert(w)
            }
        }
        
        for i in 0..<count-1 {
            let word1: [Character] = Array(words[i])
            let word2: [Character] = Array(words[i+1])
            
            let n1 = word1.count
            let n2 = word2.count
            
            let length = min(n1,n2)
            
            for x in 0..<length {
                if word1[x] == word2[x] {
                    continue
                } else {
                    if dict[word1[x]] == nil {
                        dict[word1[x]] = Set<Character>()
                    }
                    
                    dict[word1[x]]!.insert(word2[x])

                    break
                }
            }
        }
        
        print(dict)
        
        // Build queue
        var queue: [Character] = []
        
        for ch in allCharacters {
            if dict[ch] == nil {
                queue.append(ch)
            }
        }
        
        if queue.count == 0 {
            return ""
        }
        
        while queue.count > 0 {
            let item = queue.removeLast()
            result.append(item)
            
            for (key, value) in dict {
                if value.contains(item) {
                    dict[key]?.remove(item)
                    
                    if dict[key]!.count == 0 {
                        queue.append(key)
                    }
                }
            }
        }
        
        return String(result.reversed())
    }
}
