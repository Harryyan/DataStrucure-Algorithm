//
//  TextEditor.swift
//  Leetcode
//
//  Created by Harry on 5/06/22.
//

import Foundation

class TextEditor {
    var value = ""
    var cursor = 0

    init() {}
    
    func addText(_ text: String) {
        let startIndex = value.index(value.startIndex, offsetBy: cursor)
        value.insert(contentsOf: text, at: startIndex)

        cursor += text.count
    }
    
    func deleteText(_ k: Int) -> Int {
        let diff = min(k, cursor)
        cursor = max(0, cursor - k)
        
        let startIndex = value.index(value.startIndex, offsetBy: cursor)
        let endIndex = value.index(startIndex, offsetBy: diff)
        
        value.removeSubrange(startIndex..<endIndex)

        return diff
    }
    
    func cursorLeft(_ k: Int) -> String {
        cursor = max(0, cursor - k)

        let len = min(10, cursor)
        let startIndex = value.index(value.startIndex, offsetBy: cursor - len)
        let endIndex = value.index(startIndex, offsetBy: len)

        return String(value[startIndex..<endIndex])
    }
    
    func cursorRight(_ k: Int) -> String {
        cursor = min(value.count, cursor + k)
        
        let len = min(10, cursor)
        let startIndex = value.index(value.startIndex, offsetBy: cursor - len)
        let endIndex = value.index(startIndex, offsetBy: len)

        return String(value[startIndex..<endIndex])
    }
}
