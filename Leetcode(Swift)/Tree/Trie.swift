import Foundation

final class Trie {
    let root: TrieNode<Character>
    
    init() {
        root = TrieNode<Character>()    // sentinel
    }
    
    func insert(_ word: String) {
        guard !word.isEmpty else { return }
        
        var currentNode = root
        
        let characters = Array(word)
        let length = characters.count
        var index = 0
        
        while index < length {
            let character = characters[index]
            
            // if already exists
            if let child = currentNode.children[character] {
                currentNode = child
            } else {
                currentNode.addChild(character)
                currentNode = currentNode.children[character]!
            }
            
            index += 1
            
            if index == length {
                currentNode.isLeaf = true
            }
        }
    }
    
    func contains(_ word: String) -> Bool {
        guard !word.isEmpty else { return false }
        
        var currentNode = root
        
        let characters = Array(word)
        let length = characters.count
        var index = 0
        
        while index < length, let child = currentNode.children[characters[index]] {
            index += 1
            currentNode = child
        }
        
        if index == length && currentNode.isLeaf {
            return true
        } else {
            return false
        }
    }
    
    func hasPrefix(_ prefix: String) -> Bool {
        guard !prefix.isEmpty else { return false }
        
        var currentNode = root
        let characters = Array(prefix)
        let length = characters.count
        var index = 0
        
        while index < length, let child = currentNode.children[characters[index]] {
            index += 1
            currentNode = child
        }
        
        if index == length {
            return true
        } else {
            return false
        }
    }
}

final class TrieNode<T: Hashable> {
    var value: T?
    var isLeaf = false
    var children: [T: TrieNode] = [:]
    
    init(value: T? = nil) {
        self.value = value
    }
    
    func addChild(_ value: T) {
        guard children[value] == nil else { return }
        
        children[value] = TrieNode(value: value)
    }
}
