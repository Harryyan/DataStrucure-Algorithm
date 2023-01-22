/*
 Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
 
 If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
 
 */

import Foundation

class Solution_720 {
    // tc: O(nlogn)
    // sc: O(sort)
    // time: 9 mins
    func longestWord(_ words: [String]) -> String {
        let sortedWords = words.sorted()
        var res = ""
        var maxCount = 0
        var set = Set<String>()
        
        // scan
        for word in sortedWords {
            // for different group with new first letter
            if word.count == 1 || set.contains(String(word.dropLast())) {
                set.insert(word)
                
                if word.count > maxCount {
                    res = word
                    maxCount = word.count
                }
            }
        }
        
        return res
    }
}

final class Solution_720_Trie {
    var result = ""
    
    func longestWord(_ words: [String]) -> String {
        let trie = Trie()
        let sortedWords = words.sorted()
        
        for word in sortedWords {
            if word.count == 1 || trie.hasPrefix(String(word.dropLast())) {
                trie.insert(word)
            }
        }
        
        traverseTrie(trie.root, res: "")
        
        return result
    }
    
    private func traverseTrie(_ node: TrieNode<Character>, res: String) {
        for (key, node) in node.children {
            if !node.isLeaf {
                traverseTrie(node, res: res + String(key))
            } else {
                let currentStr = res + String(key)
                if result.count < currentStr.count {
                    result = currentStr
                } else if result.count == currentStr.count {
                    result = result < currentStr ? result : currentStr
                }
            }
        }
    }
}
