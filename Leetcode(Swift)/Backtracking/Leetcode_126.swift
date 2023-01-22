//
//  Leetcode_126.swift
//  Leetcode
//
//  Created by Harry on 22/04/22.
//

import Foundation

class Solution_126 {
    
    // tc: O()
    // sc: O(n ^ 2)
    // time: 3 + 23
    func findLadders(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> [[String]] {
        let n = wordList.count
        
        guard wordList.contains(endWord) else { return [] }
        
        var graph: [Int: [Int]] = [:]
        
        for i in 0..<n {
            graph[i] = []
        }
        
        // build undirected graph
        for i in 0..<n {
            for j in i+1..<n {
                if check(wordList[i], wordList[j]) {
                    graph[i]!.append(j)
                    graph[j]!.append(i)
                }
            }
        }
        
        var neighbours: [Int] = []
        
        for i in 0..<n {
            if check(beginWord, wordList[i]) {
                neighbours.append(i)
            }
        }
        
        guard neighbours.count > 0 else { return [] }
        
        // BFS to get shortest path
        var allShortestPaths: [[Int]] = []
        var queue: [[Int]] = neighbours.map { [$0] }
        var visited = Set<Int>()
        
        while !queue.isEmpty {
            var visitedAdd = Set<Int>()
            
            for _ in 0..<queue.count {
                let currentPath = queue.removeFirst()
                let lastPos = currentPath.last!
                
                if wordList[lastPos] == endWord {
                    allShortestPaths.append(currentPath)
                } else {
                    for i in graph[lastPos]! {
                        if visited.contains(i) { continue }
                        
                        queue.append(currentPath + [i])
                        visitedAdd.insert(i)
                    }
                }
            }
            
            visited = visited.union(visitedAdd)
            
            if allShortestPaths.count > 0 { break }
        }
        
        var res: [[String]] = []
        for path in allShortestPaths {
            var temp: [String] = [beginWord]
            
            for i in path {
                temp.append(wordList[i])
            }
            
            res.append(temp)
        }
        
        return res
    }
    
    // tc: O(len)
    private func check(_ word1: String, _ word2: String) -> Bool {
        var cnt = 0
        let words1 = Array(word1)
        let words2 = Array(word2)
        
        for i in 0..<words1.count {
            if words1[i] != words2[i] {
                cnt += 1
            }
            
            if cnt > 1 { return false}
        }
        
        return true
    }
}
