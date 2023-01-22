//
//  Leetcode_211.swift
//  Leetcode
//
//  Created by Harry Yan on 14/08/22.
//

import Foundation

final class WordDictionary {
    var root: SimpeTrieNode
    
    init() {
        root = SimpeTrieNode()
    }
    
    func addWord(_ word: String) {
        root.insert(word)
    }
    
    func search(_ word: String) -> Bool {
        dfs(0, root, word)
    }
    
    private func dfs(_ index: Int, _ node: SimpeTrieNode, _ word: String) -> Bool {
        guard index < word.count else {
            return node.isLeaf
        }
        
        let ch = word[word.index(word.startIndex, offsetBy: index)]
        
        if String(ch) == "." {
            for (_, node) in node.children {
                if dfs(index+1, node, word) {
                    return true
                }
            }
        } else {
            let node = node.children[ch]
            
            if node != nil, dfs(index+1, node!, word) {
                return true
            }
        }
        
        return false
    }
}

class SimpeTrieNode {
    var children: [Character: SimpeTrieNode] = [:]
    var isLeaf = false
    
    func insert(_ word: String) {
        var node = self
        
        for ch in word {
            if node.children[ch] == nil {
                node.children[ch] = SimpeTrieNode()
            }
            
            node = node.children[ch]!
        }
        
        node.isLeaf = true
    }
}
