import Foundation

indirect enum LinkedList<T> {
    case end
    case node(element: T, next: LinkedList<T>)
}

extension LinkedList {
    
    func add(_ element: T) -> LinkedList  {
        return .node(element: element, next: self)
    }
}

extension LinkedList: Sequence {
    
    func makeIterator() -> LinkedListIterator<T> {
        return LinkedListIterator(current: self)
    }
}

struct LinkedListIterator<T>: IteratorProtocol {
    var current: LinkedList<T>
    
    mutating func next() -> T? {
        switch current {
        case let .node(element, nextNode):
            current = nextNode
            return element
        case .end:
            return nil
        }
    }
}

let list = LinkedList<Int>.end.add(3).add(2).add(1)
var it = list.makeIterator()
let a = it.next()

print(it)

let test = list.map { $0 == 1}

print(test)
