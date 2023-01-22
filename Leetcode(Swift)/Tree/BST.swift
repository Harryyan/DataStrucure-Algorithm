//
//  BST.swift
//  Leetcode
//
//  Created by Harry on 6/07/22.
//
import Foundation

struct BST<E: Comparable> {
    private(set) var root: BinaryTreeNode<Element>?
    
    init(){}
    
    // MARK: - 查询 O(logn)
    
    func query(_ value: E) -> Bool {
        var current = root
        
        while let node = current {
            if node.value == value { return true }
            
            current = node.value > value ? node.leftChild : node.rightChild
        }
        
        return false
    }
    
    // MARK: - 插入 O(logn)
    
    func insert(_ value: E) {
        root = insert(from: root, value)
    }
    
    // MARK: 删除 O(logn)
    
    func remove(_ value: E) {
        root = remove(from: root, value)
    }
    
    // MARK: - Private
    
    private func insert(from node: BinaryTreeNode<E>?, _ value: E) -> BinaryTreeNode<E> {
        guard let node = node else {
            return BinaryTreeNode(value)
        }
        
        if value < node.value {
            node.leftChild = insert(from: node.leftChild, value: value)
        } else {
            node.rightChild = insert(from: node.rightChild, value: value)
        }
        
        return node
    }
    
    private func remove(from node: BinaryTreeNode<E>, _ value: E) -> BinaryTreeNode<Element>? {
        guard let node = node else { return nil }
        
        if node.value == value {
            // 移除叶子结点
            if node.leftChild == nil && node.rightChild == nil {
                return nil
            }
            
            // 若只有一个子节点，则直接返回另一个子节点
            if node.leftChild == nil {
                return node.rightChild
            }
            
            if node.rightChild == nil {
                return node.leftChild
            }
            
            node.value = node.rightChild!.minNode.value
            node.rightChild = remove(node: node.rightChild, value: node.value)
        } else if node.value > value {
            node.leftChild = remove(from: node.leftChild, value)
        } else {
            node.right = remove(from: node.rightChild, value)
        }
        
        return node
    }
}

final class BinaryTreeNode<T> {
    var value: T
    var leftChild: BinaryTreeNode?
    var rightChild: BinaryTreeNode?
    
    init(_ value: T) {
        self.value = value
    }
}

extension BinaryTreeNode {
    func traverseInOrder(_ closure: (T) -> Void) {
        leftChild?.traverseInOrder(closure)
        closure(value)
        rightChild?.traverseInOrder(closure)
    }
    
    func traversePreOrder(_ closure: (T) -> Void) {
        closure(value)
        leftChild?.traversePreOrder(closure)
        rightChild?.traversePreOrder(closure)
    }
    
    func traversePostOrder(_ closure: (T) -> Void) {
        leftChild?.traversePostOrder(closure)
        rightChild?.traversePostOrder(closure)
        closure(value)
    }
}

extension BinaryTreeNode {
    var minNode: BinaryTreeNode {
        return leftChild?.minNode ?? self
    }
}
