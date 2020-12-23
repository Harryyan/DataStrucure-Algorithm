import Foundation

enum BinarySearchTree<T: Comparable> {
    case empty
    case leaf(value: T)
    indirect case node(value: T, left: BinaryTree<T>, right: BinaryTree<T>, parent: BinaryTree<T>?)
}
