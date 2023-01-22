//
//  Leetcode_297.swift
//  Leetcode
//
//  Created by Harry on 5/03/22.
//

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Codec_297 {
    func serialize(_ root: TreeNode?) -> String {
        
        let result = preOrderWithNull(root)
        
        return result
    }
    
    func preOrderWithNull(_ root: TreeNode?) -> String {
                        
        var result = ""
        if root == nil {
            result += "#,"
            return result
        }
        else{
            result = result + String(root!.val) + ","
        }
        
        result += preOrderWithNull(root?.left)
        result += preOrderWithNull(root?.right)
        
        return result
    }
    
    func deserialize(_ data: String) -> TreeNode? {
        
        var dataSplit = data.split(separator: ",")
        
        var result = recursiveBodyDeserialize(&dataSplit)
        
        
        return result
    }
    
    func recursiveBodyDeserialize( _ data: inout [Substring]) -> TreeNode? {
        
        var result:TreeNode?
        let temp = data[0]
        
        if temp == "#" {
            
            data.removeFirst()
            return nil
        }
            
        result = TreeNode(Int(String(temp))!)
            
        
        data.removeFirst()
        
        result?.left = recursiveBodyDeserialize(&data)
        result?.right = recursiveBodyDeserialize(&data)
        
        return result
    }

}



// Your Codec object will be instantiated and called as such:
// var ser = Codec()
// var deser = Codec()
// deser.deserialize(ser.serialize(root))
