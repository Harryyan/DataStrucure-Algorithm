import Foundation

final class CustomStack {
    // time: 7 mins
    // sc: O(n)
    var stack: [Int] = []
    var size = 0
    var currentSize = 0

    init(_ maxSize: Int) {
        size = maxSize
    }
    
    // tc: O(1)
    func push(_ x: Int) {
        guard currentSize < size else { return }
        
        stack.append(x)
        currentSize += 1
    }
    
    // tc: O(1)
    func pop() -> Int {
        guard currentSize > 0 else { return -1 }
        
        currentSize -= 1
        
        return stack.removeLast()
    }
    
    // tc: O(n)
    // 可优化为O(1)
    // 使用另一个栈记录第k个元素增量
    // pop时再更新，属于懒加载
    func increment(_ k: Int, _ val: Int) {
        if k >= currentSize {
            stack = stack.map { $0 + val}
        } else {
            for i in 0..<k {
                stack[i] += val
            }
        }
    }
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj = CustomStack(maxSize)
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * obj.increment(k, val)
 */
