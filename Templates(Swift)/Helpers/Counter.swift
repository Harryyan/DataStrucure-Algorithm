//
//  Counter.swift
//  Templates
//
//  Created by Harry Yan on 12/04/23.
//

import Foundation

struct HashMapBuilder {
    static func charFrequency(_ str: String) -> [String:Int] {
        let letters = str.map { String($0) }
        var countedLetters = [String:Int]()
        
        letters.forEach { countedLetters[$0, default: 0] += 1 }
        
        return countedLetters
    }
    
    func inDegree(_ list: [[Int]]) -> [Int: [Int]] {
        var countDict = [Int: [Int]]()
        
        list.forEach { countDict[$0.first!, default: []].append($0.last!) }
        
        return countDict
    }
    
    func outDegree(_ list: [[Int]]) -> [Int: [Int]] {
        var countDict = [Int: [Int]]()
        
        list.forEach { countDict[$0.last!, default: []].append($0.first!) }
        
        return countDict
    }
}
