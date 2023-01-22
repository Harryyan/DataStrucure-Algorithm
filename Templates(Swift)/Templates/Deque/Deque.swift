//
//  Deque.swift
//  Templates
//
//  Created by Harry Yan on 30/10/22.
//

import Foundation

public struct Deque<T> {
    private var array:[T?]
    private var head: Int
    private var capacity: Int
    private let originalCapacity: Int
    
    public init(_ capacity: Int = 10) {
        self.capacity = max(capacity, 1)
        originalCapacity = capacity
        array = [T?](repeating: nil, count: capacity)
        head = capacity
    }
    
    public var isEmpty:Bool {
        return count == 0
    }
    
    public var count: Int {
        return array.count - head
    }
    
    public mutating func add(_ element:T) {
        array.append(element)
    }
    
    public mutating func addFront(_ element:T) {
        if head == 0 {
            capacity *= 2
            let emptySpace = [T?](repeating: nil, count: capacity)
            array.insert(contentsOf: emptySpace, at: 0)
            head = capacity
        }
        
        head -= 1
        array[head] = element
    }
    
    public mutating func poll() -> T? {
        guard head < array.count,let element = array[head] else { return nil }
        
        array[head] = nil
        head += 1
        
        if capacity >= self.originalCapacity && head >= capacity * 2 {
            let amountToRemove = capacity + capacity/2
            array.removeFirst(amountToRemove)
            head -= amountToRemove
            capacity /= 2
        }
        
        return element
    }
    
    public mutating func pollLast() -> T? {
        if isEmpty {
            return nil
        }else {
            return array.removeLast()
        }
    }
    
    public func peek() -> T? {
        if isEmpty {
            return nil
        }else {
            return array[head]
        }
    }
    
    public func peekLast() -> T? {
        if isEmpty {
            return nil
        }else {
            return array.last!
        }
    }
}
