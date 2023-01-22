import Foundation

/*
 Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.
 
 Implement the PeekingIterator class:
 
 PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
 int next() Returns the next element in the array and moves the pointer to the next element.
 boolean hasNext() Returns true if there are still elements in the array.
 int peek() Returns the next element in the array without moving the pointer.
 Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.
 */

final class PeekingIterator {
    var iterator: IndexingIterator<Array<Int>>
    
    init(_ arr: IndexingIterator<Array<Int>>) {
        iterator = arr
    }
    
    func next() -> Int {
        let x = peek()
        iterator = iterator.dropFirst().makeIterator()  //调用next方法之后 直接丢弃第一个
        return x
    }
    
    func peek() -> Int {
        return iterator.first { _ in true } ?? 0       // 取不到值 最好是返回nil
    }
    
    func hasNext() -> Bool {
        return iterator.first { _ in true } != nil
    }
}
