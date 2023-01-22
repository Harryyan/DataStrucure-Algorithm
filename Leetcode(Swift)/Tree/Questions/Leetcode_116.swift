//
//  Leetcode_116.swift
//  Leetcode
//
//  Created by Harry on 21/02/22.
//

import Foundation

class Solution_116 {
    
    func connect(_ root: Node?) -> Node? {
        guard root != nil else { return nil }
        
        var queue: [Node] = []
        queue.append(root!)
        
        while queue.count > 0 {
            var temp: [Node] = []
            var pre: Node? = nil
            
            for node in queue {
                if let right = node.right {
                    temp.append(right)
                }
                
                if let left = node.left {
                    temp.append(left)
                }
                
                node.next = pre
                pre = node
            }
            
            _ = queue.popLast()
            queue = temp
        }
        
        return root
    }
    
}


class Solution_116_Constant_Space_recursive {
    
    func connect(_ root: Node?) -> Node? {
        guard let _ = root else { return nil }
        
        if let left = root?.left {
            left.next = root?.right
            
            if let next = root?.next {
                root?.right?.next = next.left
            }
        }
        
        _ = connect(root?.left)
        _ = connect(root?.right)
            
        return root
    }
}

class Solution_116_Constant_Space_loop {
    
    func connect(_ root: Node?) -> Node? {
        guard var node = root else { return nil }
        
        while node != nil {
            var temp = node
            
            while temp != nil {
                temp.left?.next = temp.right
                
                if temp.next != nil {
                    temp.right?.next = temp.next?.left
                }
                
                temp = temp.next
            }
            
            node = node.left
        }
        
        return root
    }
}
