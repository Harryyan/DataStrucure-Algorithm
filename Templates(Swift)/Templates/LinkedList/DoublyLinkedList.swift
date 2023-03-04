//
//  DoublyLinkedList.swift
//  Templates
//
//  Created by Harry Yan on 5/03/23.
//

import Foundation

public class CacheNode {
    var next: CacheNode?
    var pre: CacheNode?
    var key: Int
    var time: Int
    var val: Int
    init(_ key: Int, _ val: Int) {
        self.key = key
        self.val = val
        self.val = val
        self.time = 0
        self.next = nil
        self.pre = nil
    }
}

final class DoublyLinkedList {
    var head: CacheNode
    var tail: CacheNode
    var count: Int
    init() {
        self.head = CacheNode(0,0)
        self.tail = CacheNode(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0
    }
    
    //插入一个节点
    func insert(_ node: CacheNode) {
        node.next = head.next
        node.pre = head
        head.next?.pre = node
        head.next = node
        count += 1
    }
    
    //删除一个节点
    func delete(_ node: CacheNode) {
        if count == 0 {return}
        node.next?.pre = node.pre
        node.pre?.next = node.next
        count -= 1
    }
    
    //删除尾部节点
    func deleteLast() -> Int? {
        if count == 0 {return nil}
        //删除尾部
        let temp = tail.pre
        temp?.pre?.next = tail
        tail.pre = temp?.pre
        count -= 1
        return temp!.key
    }
}
