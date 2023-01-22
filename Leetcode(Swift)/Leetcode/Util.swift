import Foundation

struct Counter {
    func count(_ str: String) -> [String: Int] {
        let letters = str.map { String($0) }
        var countedLetters = [String:Int]()
        
        letters.forEach { countedLetters[$0, default: 0] += 1 }
        
        return countedLetters
    }
    
    func inDegree(_ list: [[Int]]) -> [Int: [Int]] {
        var countDict = [Int: [Int]]()
        
        list.forEach { countDict[$0.first!, default: []].append($0.last!) }
        
        return countDict
    }
    
    func outDegree(_ list: [[Int]]) -> [Int: [Int]] {
        var countDict = [Int: [Int]]()
        
        list.forEach { countDict[$0.last!, default: []].append($0.first!) }
        
        return countDict
    }
}

extension Collection {
    func distance(to index: Index) -> Int { distance(from: startIndex, to: index) }
}

extension StringProtocol {
    func distance(of element: Element) -> Int? { firstIndex(of: element)?.distance(in: self) }
    func distance<S: StringProtocol>(of string: S) -> Int? { range(of: string)?.lowerBound.distance(in: self) }
}

extension String.Index {
    func distance<S: StringProtocol>(in string: S) -> Int { string.distance(to: self) }
}

extension Array where Element: Equatable {
    /// Remove the object from array
    ///
    /// - parameter object: The element need to remove
    ///
    /// Time Complexity: O(n)
    mutating func remove(object: Element) {
        guard let index = firstIndex(of: object) else { return }
        remove(at: index)
    }
}
