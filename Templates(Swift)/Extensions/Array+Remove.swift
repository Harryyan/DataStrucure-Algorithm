//
//  Array+Remove.swift
//  Templates
//
//  Created by Harry Yan on 12/04/23.
//

import Foundation

extension Array where Element: Equatable {
    /// Remove the object from array
    ///
    /// - parameter object: The element need to remove
    ///
    /// Time Complexity: O(n)
    mutating func remove(object: Element) {
        guard let index = firstIndex(of: object) else { return }
        remove(at: index)
    }
}
