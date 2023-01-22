//
//  Leetcode-1135.swift
//  Leetcode
//
//  Created by Harry Yan on 28/07/22.
//

import Foundation

class Solution_1135 {
    
    // tc: O(ElogV)
    // sc: O(V)
    func minimumCost(_ n: Int, _ connections: [[Int]]) -> Int {
        guard n > 1 else { return 0 }
        
        var pq = Heap<Vertex>(priorityFunction: { $0.cost < $1.cost })
        var seen = Set<Int>()
        var cost = 0
        var graph: [Int: [(Int, Int)]] = [:]
        
        // build graph
        for connection in connections {
            graph[connection[0], default: []].append((connection[1], connection[2]))
            graph[connection[1], default: []].append((connection[0], connection[2]))
        }
        
        pq.enqueue(Vertex(start: 1, end: 1, cost: 0))
        
        while !pq.isEmpty {
            let cur = pq.dequeue()!
            
            if !seen.contains(cur.end) {
                cost += cur.cost
                
                for (end, cost) in graph[cur.end]! {
                    pq.enqueue(Vertex(start: cur.end, end: end, cost: cost))
                }
                
                seen.insert(cur.end)
            }
        }
        
        return seen.count == n ? cost : -1
    }
}

class Solution_1135_Kruskal {
    
    // tc: O(ElogE)
    // sc: O(V)
    func minimumCost(_ n: Int, _ connections: [[Int]]) -> Int {
        guard n > 1 else { return 0 }
        
        var cost = 0
        var totalCount = n
        let uf = UnionFind2(n: n+1)
        let connections = connections.sorted(by: { $0[2] < $1[2] })
        
        for connection in connections {
            guard !uf.isConnected(a: connection[0], b: connection[1]) else { continue }
            
            uf.union(a: connection[0], b: connection[1])
            cost += connection[2]
            
            totalCount -= 1
        }
        
        return totalCount == 1 ? cost : -1
    }
}

struct Vertex {
    let start: Int
    let end: Int
    let cost: Int
}

struct Heap<Element>
{
    var elements : [Element]
    let priorityFunction : (Element, Element) -> Bool
    
    init(elements: [Element] = [], priorityFunction: @escaping (Element, Element) -> Bool) {
        self.elements = elements
        self.priorityFunction = priorityFunction
        buildHeap()
    }
    
    mutating func buildHeap() {
        for index in (0 ..< count / 2).reversed() {
            siftDown(elementAtIndex: index)
        }
    }
    
    var isEmpty : Bool { return elements.isEmpty }
    var count : Int { return elements.count }
    
    func peek() -> Element? {
        return elements.first
    }
    
    mutating func enqueue(_ element: Element) {
        elements.append(element)
        siftUp(elementAtIndex: count - 1)
    }
    
    mutating func siftUp(elementAtIndex index: Int) {
        let parent = parentIndex(of: index)
        guard !isRoot(index),
              isHigherPriority(at: index, than: parent)
        else { return }
        swapElement(at: index, with: parent)
        siftUp(elementAtIndex: parent)
    }
    
    mutating func dequeue() -> Element? {
        guard !isEmpty
        else { return nil }
        swapElement(at: 0, with: count - 1)
        let element = elements.removeLast()
        if !isEmpty {
            siftDown(elementAtIndex: 0)
        }
        return element
    }
    
    mutating func siftDown(elementAtIndex index: Int) {
        let childIndex = highestPriorityIndex(for: index)
        if index == childIndex {
            return
        }
        swapElement(at: index, with: childIndex)
        siftDown(elementAtIndex: childIndex)
    }
    
    // Helper functions
    
    func isRoot(_ index: Int) -> Bool {
        return index == 0
    }
    
    func leftChildIndex(of index: Int) -> Int {
        return (2 * index) + 1
    }
    
    func rightChildIndex(of index: Int) -> Int {
        return (2 * index) + 2
    }
    
    func parentIndex(of index: Int) -> Int {
        return (index - 1) / 2
    }
    
    func isHigherPriority(at firstIndex: Int, than secondIndex: Int) -> Bool {
        return priorityFunction(elements[firstIndex], elements[secondIndex])
    }
    
    func highestPriorityIndex(of parentIndex: Int, and childIndex: Int) -> Int {
        guard childIndex < count && isHigherPriority(at: childIndex, than: parentIndex)
        else { return parentIndex }
        return childIndex
    }
    
    func highestPriorityIndex(for parent: Int) -> Int {
        return highestPriorityIndex(of: highestPriorityIndex(of: parent, and: leftChildIndex(of: parent)), and: rightChildIndex(of: parent))
    }
    
    mutating func swapElement(at firstIndex: Int, with secondIndex: Int) {
        guard firstIndex != secondIndex
        else { return }
        elements.swapAt(firstIndex, secondIndex)
    }
}

// A bonus extra for you: two extra functions, if the Element type is Equatable
extension Heap where Element : Equatable {
    
    // This function allows you to remove an element from the heap, in a similar way to how you would dequeue the root element.
    mutating func remove(_ element: Element) {
        guard let index = elements.firstIndex(of: element)
        else { return }
        swapElement(at: index, with: count - 1)
        elements.remove(at: count - 1)
        siftDown(elementAtIndex: index)
    }
    
    // This function allows you to 'boost' an element, by sifting the element up the heap. You might do this if the element is already in the heap, but its priority has increased since it was enqueued.
    mutating func boost(_ element: Element) {
        guard let index = elements.firstIndex(of: element)
        else { return }
        siftUp(elementAtIndex: index)
    }
}
