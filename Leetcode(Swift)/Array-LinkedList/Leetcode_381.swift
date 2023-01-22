import Foundation

class RandomizedCollection {
    var hashT = [Int:Int]()
    var numberOfItems = 0

    /** Initialize your data structure here. */
    init() {
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    func insert(_ val: Int) -> Bool {
        numberOfItems = numberOfItems + 1
        if let count = hashT[val] {
            hashT[val] = count + 1
            return false
        }else {
            hashT[val] = 1
            return true
        }
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    func remove(_ val: Int) -> Bool {
        if let count = hashT[val] {
            numberOfItems = numberOfItems - 1

            if count == 1 {
                hashT[val] = nil
            }else {
                hashT[val] = count - 1
            }
            
            return true
        }else {
            return false
        }
    }
    
    /** Get a random element from the collection. */
    func getRandom() -> Int {
        if (numberOfItems > 0) {
            let r = Int.random(in: 0..<numberOfItems)

            var index = 0
            for (num, count) in hashT {
                index = index + count
                if index - 1 >= r {
                    return num
                }
            }
            return 0
        }else {
            return 0
        }
    }
}
