import Foundation

enum BinaryTree<T: Comparable> {
    case empty
    case leaf(value: T)
    indirect case node(value: T, left: BinaryTree<T>, right: BinaryTree<T>)
    
    func inverted() -> BinaryTree<T> {
        switch self {
        case .empty:
            return .empty
        case .leaf(let value):
            return .leaf(value: value)
        case .node(let value, let left, let right):
            return .node(value: value,
                         left: right.inverted(),
                         right: left.inverted())
        }
    }
    
    // Pre-order: first look at a node, then at its left and right children.
    func traverseInPreOrder(_ process: (T?) -> Void) {
        if case let .node(value, left, right) = self {
            process(value)
            left.traverseInPreOrder(process)
            right.traverseInPreOrder(process)
        } else if case let .leaf(value) = self {
            process(value)
        } else {
            process(nil)
        }
    }
    
    //In-order (or depth-first): first look at the left child of a node, then at the node itself, and finally at its right child.
    func traverseInOrder(_ process: (T?) -> Void) {
        if case let .node(value, left, right) = self {
            left.traverseInOrder(process)
            process(value)
            right.traverseInOrder(process)
        } else if case let .leaf(value) = self {
            process(value)
        } else {
            process(nil)
        }
    }
    
    //Post-order: first look at the left and right children and process the node itself last.
    func traverseInPostOrder(_ process: (T?) -> Void) {
        if case let .node(value, left, right) = self {
            left.traverseInPostOrder(process)
            right.traverseInPostOrder(process)
            process(value)
        } else if case let .leaf(value) = self {
            process(value)
        } else {
            process(nil)
        }
    }
}

extension BinaryTree: CustomStringConvertible {
    
    public var description: String {
        switch self {
        case .empty: return ""
        case .leaf(let value): return "leaf: \(value)"
        case .node(let value, let left, let right): return "value: \(value), left = [\(left.description)], right = [\(right.description)]"
        }
    }
}

//let testNode: BinaryTree<Int> = .node(
//    value: 3,
//    left: .node(
//        value: 22,
//        left: .leaf(value: 2),
//        right:.leaf(value: 32)),
//    right: .node(
//        value: 34,
//        left: .leaf(value: 435),
//        right: .empty))

let tree: BinaryTree<Int> = .node(
    value: 4,
    left: .node(
        value: 7,
        left: .leaf(value: 2),
        right:.leaf(value: 3)),
    right: .node(
        value: 6,
        left: .leaf(value: 5),
        right: .leaf(value: 8)))
//print(tree.inverted())

tree.traverseInOrder { value in
    if let value = value {
        print(value)
    }
}
