// Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
//
// Implement the LRUCache class:
//
// LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
// int get(int key) Return the value of the key if the key exists, otherwise return -1.
// void put(int key, int value) Update the value of the key if the key exists. Otherwise,
// add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
// evict the least recently used key.
// The functions get and put must each run in O(1) average time complexity.


import Foundation

final class LRUCache {
    private(set) var capacity: Int = 0
    private(set) var dictionary = [Int: Node]()
    var first: Node!
    var last: Node!
    
    init(_ capacity: Int) {
        self.capacity = capacity
        dictionary = [Int:Node]()
        
        first = Node()
        last = Node()
        
        first.next = last
        last.prev = first
    }
    
    func get(_ key: Int) -> Int {
        guard let node = dictionary[key] else {
            return -1
        }
        
        removeNode(node)
        addAtFirst(node)
        
        return node.val
    }
    
    func put(_ key: Int, _ value: Int) {
        let node = dictionary[key]
        if node != nil {
            //! 更新 key
            node!.val = value
            removeNode(node!)
            addAtFirst(node!)
        } else {
            if dictionary.keys.count == capacity {
                //! 淘汰最近最少使用
                let prevNode = dictionary.removeValue(forKey: last.prev!.key)!
                removeNode(prevNode)
            }
            
            let newNode = Node(key, value)
            dictionary[key] = newNode
            addAtFirst(newNode)
        }
    }
    
    //! 双向链表 -> 删除 自身
    private func removeNode(_ node: Node) {
        node.next!.prev = node.prev
        node.prev!.next = node.next
    }
    
    //! 双向链表 -> 插入节点到头节点后面
    private func addAtFirst(_ node: Node) {
        node.next = first.next
        first.next!.prev = node
        
        first.next = node
        node.prev = first
    }
}

class Node {
    var key:Int = 0
    var val: Int = 0
    
    var prev: Node?
    var next: Node?
    
    var left: Node?
    var right: Node?
    
    
    init(_ key: Int = 0, _ value: Int = 0) {
        self.key = key
        self.val = value
    }
}
