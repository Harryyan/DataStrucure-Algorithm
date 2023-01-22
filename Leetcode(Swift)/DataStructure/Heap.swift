//
//  Heap.swift
//  Leetcode
//
//  Created by Harry on 22/01/22.
//

import Foundation

struct Heap<T> {
    var nodes = [T]()
    
    private var orderCriteria: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool, array: [T]) {
        orderCriteria = sort
        heapify(array: array)
    }
    
    // MARK: Public Operations
    
    mutating func insert(_ value: T) {
        nodes.append(value)
        
        heapify(array: nodes)
        shiftUp(from: nodes.count - 1)
    }
    
    mutating func removeTop() -> T? {
        guard !nodes.isEmpty else { return nil }
        
        if nodes.count == 1 {
            return nodes.removeLast()
        } else {
            let value = nodes[0]
            nodes[0] = nodes.removeLast()
            shiftDown(from: 0, until: nodes.count)
            
            return value
        }
    }
    
    func peek() -> T? {
        return nodes.first
    }
    
    // MARK: - Private
    
    private mutating func shiftUp(from index: Int) {
        var childIndex = index
        let child = nodes[childIndex]
        var parentIndex = childIndex / 2
        
        while parentIndex > 0 && orderCriteria(child, nodes[parentIndex]) {
            nodes.swapAt(childIndex, parentIndex)
            childIndex = parentIndex
            parentIndex = childIndex / 2
        }
    }
    
    private mutating func shiftDown(from index: Int, until endIndex: Int) {
        let leftChildIndex = index * 2 + 1
        let rightChildIndex = leftChildIndex + 1
        
        var first = index
        if leftChildIndex < endIndex && orderCriteria(nodes[leftChildIndex], nodes[first]) {
            first = leftChildIndex
        }
        
        if rightChildIndex < endIndex && orderCriteria(nodes[rightChildIndex], nodes[first]) {
            first = rightChildIndex
        }
        
        if first == index { return }
        
        nodes.swapAt(index, first)
        shiftDown(from: first, until: endIndex)
    }
    
    private mutating func heapify(array: [T]) {
        nodes = array
        
        // Start from non-leaf nodes
        for i in stride(from: (nodes.count/2-1), through: 0, by: -1) {
            shiftDown(from: i, until: nodes.count)
        }
    }
}

extension Heap where T: Comparable {}
