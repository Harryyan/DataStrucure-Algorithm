//
//  UnionFind.swift
//  Leetcode
//
//  Created by Harry on 15/01/22.
//

import Foundation

// 并查集
final class UnionFind {
    var dict: [Int:Int] = [:]   // Record parent node; parent is self at the beginning
    
    init(n: Int) {
        for i in 0..<n {
            dict[i] = i
        }
    }
    
    // Find root parent node
    func find(_ a: Int) -> Int {
        var x: Int = a
        
        while x != dict[x] {
            x = dict[x] ?? x
        }
        
        return x
    }
    
    func union(a: Int, b: Int) {
        guard !isConnected(a: a, b: b) else { return }
        
        let parent_a = find(a)
        let parent_b = find(b)
        
        dict[parent_b] = parent_a
    }
    
    func isConnected(a: Int, b: Int) -> Bool {
        return find(a) == find(b)
    }
}


final class UnionFind2 {
    var dict: [Int:Int] = [:]
    
    init(n: Int) {
        for i in 0..<n {
            dict[i] = i
        }
    }
    
    // Find root parent node
    func find(_ a: Int) -> Int {
        if dict[a] == a {
            return a
        }
        
        dict[a] = find(dict[a]!)
        return dict[a]!
    }
    
    func union(a: Int, b: Int) {
        guard !isConnected(a: a, b: b) else { return }
        
        var parent_a = find(a)
        var parent_b = find(b)
        
        if parent_a > parent_b {
            let temp = parent_a
            parent_a = parent_b
            parent_b = temp
        }
        
        dict[parent_b] = parent_a
    }
    
    func isConnected(a: Int, b: Int) -> Bool {
        return find(a) == find(b)
    }
}
