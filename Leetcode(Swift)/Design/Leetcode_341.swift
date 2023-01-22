import Foundation

class NestedInteger {
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    public func isInteger() -> Bool {
        return false
    }
    
    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    public func getInteger() -> Int {
        return 0
    }
    
    // Set this NestedInteger to hold a single integer.
    public func setInteger(value: Int){
        
    }
    
    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    public func add(elem: NestedInteger){
        
    }
    
    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    public func getList() -> [NestedInteger] {
        return []
    }
}

class NestedIterator {
    var size = 0
    var currentIndex = 0
    var res: [Int] = []
    
    init(_ nestedList: [NestedInteger]) {
        dfs(nestedList)
        
        size = res.count
    }
    
    private func dfs(_ nestedList: [NestedInteger]) {
        for item in nestedList {
            if item.isInteger() {
                res.append(item.getInteger())
            } else {
                dfs(item.getList())
            }
        }
    }
    
    func next() -> Int {
        let value = res[currentIndex]
        
        currentIndex += 1
        
        return value
    }
    
    func hasNext() -> Bool {
        currentIndex < size
    }
}
