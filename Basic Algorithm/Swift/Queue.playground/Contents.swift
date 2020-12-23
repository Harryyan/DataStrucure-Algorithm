import Foundation

/*
 A queue is a list where you can only insert new items at the back and remove items from the front. This ensures that the first item you enqueue is also the
 first item you dequeue. First come, first serve!
 
 Why would you need this? Well, in many algorithms you want to add objects to a temporary list and pull them off this list later. Often the order in which you
 add and remove these objects matters.
 
 A queue gives you a FIFO or first-in, first-out order. The element you inserted first is the first one to come out. It is only fair! (A similar data
 structure, the stack, is LIFO or last-in first-out.)
 */

struct Queue<Element> {
    private var container: Array = [Element]()
    
    var count: Int {
        return container.count
    }
    
    var isEmpty: Bool {
        return container.isEmpty
    }
    
    var front: Element? {
        return container.first
    }
    
    mutating func enqueue(_ newElement: Element) {
        container.append(newElement)
    }
    
    mutating func dequeue() -> Element? {
        guard !isEmpty else { return nil }
        
        return container.removeFirst()
    }
}

var test = Queue<Int>()
test.enqueue(3)
test.enqueue(4)
test.enqueue(5)

test.dequeue()

print(test)
