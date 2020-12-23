import Foundation

/*
 
 Goal: Sort an array from low to high (or high to low).
 
 You are given an array of numbers and need to put them in the right order. The insertion sort algorithm works as follows:
 
 Put the numbers on a pile. This pile is unsorted.
 Pick a number from the pile. It doesn't really matter which one you pick, but it's easiest to pick from the top of the pile.
 Insert this number into a new array.
 Pick the next number from the unsorted pile and also insert that into the new array. It either goes before or after the first number you picked,
 so that now these two numbers are sorted.
 Again, pick the next number from the pile and insert it into the array in the proper sorted position.
 Keep doing this until there are no more numbers on the pile. You end up with an empty pile and an array that is sorted.
 That's why this is called an "insertion" sort, because you take a number from the pile and insert it in the array in its proper sorted position.
 
 Complexity: O(n^2) ; Insertion sort is actually very fast for sorting small arrays
 
 */

struct Person: Comparable {
    
    let name: String
    
    init(name: String) {
        self.name = name
    }
    
    static func < (lhs: Person, rhs: Person) -> Bool {
        return lhs.name < rhs.name
    }
    
    static func > (lhs: Person, rhs: Person) -> Bool {
        return lhs.name > rhs.name
    }
}

extension Collection where Index == Int, Element: Comparable {
    
    func sortedByInsertion(_ orderPolicy: (Element, Element) -> Bool) -> [Element] {
        var copiedArray = map{ $0 }
        guard count > 1 else { return copiedArray }
        
        for index in 1..<copiedArray.count {
            var tempIndex = index
            let currentValue = copiedArray[tempIndex]
            
            while tempIndex > 0 && orderPolicy(currentValue, copiedArray[tempIndex - 1]) {
                copiedArray[tempIndex] = copiedArray[tempIndex - 1]
                tempIndex -= 1
            }
            
            copiedArray[tempIndex] = currentValue
        }
        
        return copiedArray
    }
}

var a = Set<Int>()
a.insert(1)

let numbers = [10, -1, 3, 9, 2, 27, 8, 5, 1, 3, 0, 26]
let chars: [String] = []
let person1 = Person(name: "harry")
let person2 = Person(name: "lan")
let people = [person1, person2]

let test = numbers.sortedByInsertion(>)
let emptyTest = chars.sortedByInsertion(<)
let objTest = people.sortedByInsertion(>)
