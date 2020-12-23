import Foundation

/*
 A stack is like an array but with limited functionality. You can only push to add a new element to the top of the stack, pop to remove the element from the
 top, and peek at the top element without popping it off.
 
 Why would you want to do this? Well, in many algorithms you want to add objects to a temporary list at some point and then pull them off this list again at a
 later time. Often the order in which you add and remove these objects matters.
 
 A stack gives you a LIFO or last-in first-out order. The element you pushed last is the first one to come off with the next pop. (A very similar data
 structure, the queue, is FIFO or first-in first-out.)
 */

struct Stack<Element> {
    
    private var container: Array = [Element]()
    
    var isEmpty: Bool {
        return container.isEmpty
    }
    
    var count: Int {
        return container.count
    }
    
    var top: Element? {
        return container.last
    }
    
    mutating func push(_ newElement: Element) {
        container.append(newElement)
    }
    
    mutating func pop() {
        let a = container.popLast()
    }
}


var stack = Stack<Int>()
stack.push(3)
stack.push(3)
stack.push(32)

stack.pop()

print(stack)
