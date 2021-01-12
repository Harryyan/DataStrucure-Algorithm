/*
 
 The classic way to speed this up is to use a binary search. The trick is to keep splitting the array in half until the value is found.
 
 For an array of size n, the performance is not O(n) as with linear search but only O(log n). To put that in perspective, binary search on an array with 1,000,000 elements only takes about 20 steps to find what you're looking for, because log_2(1,000,000) = 19.9. And for an array with a billion elements it only takes 30 steps. (Then again, when was the last time you used an array with a billion items?)
 
 Sounds great, but there is a downside to using binary search: the array must be sorted. In practice, this usually isn't a problem.
 
 Here's how binary search works:
 
 Split the array in half and determine whether the thing you're looking for, known as the search key, is in the left half or in the right half.
 How do you determine in which half the search key is? This is why you sorted the array first, so you can do a simple < or > comparison.
 If the search key is in the left half, you repeat the process there: split the left half into two even smaller pieces and look in which piece the search key
 must lie. (Likewise for when it's the right half.)
 
 This repeats until the search key is found. If the array cannot be split up any further, you must regrettably conclude that the search key is not present in
 the array.
 
 Now you know why it's called a "binary" search: in every step it splits the array into two halves. This process of divide-and-conquer is what allows it to
 quickly narrow down where the search key must be.
 
 
 Is it a problem that the array must be sorted first? It depends. Keep in mind that sorting takes time -- the combination of binary search plus sorting may be
 slower than doing a simple linear search. Binary search shines in situations where you sort just once and then do many searches.
 */


import Foundation

extension SortedArray: Collection {
    
    var startIndex: Int {
        return elements.startIndex
    }
    
    var endIndex: Int {
        return elements.endIndex
    }
    
    subscript(index: Int) -> Element {
        return elements[index]
    }
    
    func index(after i: Int) -> Int {
        return elements.index(after: i)
    }
    
    func min() -> Element? {
        return elements.first
    }
}

struct SortedArray<Element: Comparable> {
    
    var elements: [Element]
    
    init<S: Sequence>(unsorted: S) where S.Iterator.Element == Element {
        elements = unsorted.sorted()
    }
    
    mutating func insert(_ element: Element) {
        elements.insert(element, at: index(for: element))
    }
    
    func contains(element: Element) -> Bool {
        let index = self.index(for: element)
        guard index < elements.endIndex else { return false }
        
        return self[index] == element
    }
    
    private func index(for element: Element) -> Int {
        var start = elements.startIndex
        var end = elements.endIndex
        
        while start < end {
            // Using '-' to avoid overflow
            
            let middle = start + (end - start) / 2
            if elements[middle] < element {
                start = middle + 1
            } else {
                end = middle
            }
        }
        
        assert(start == end)
        return start
    }
}

var test = SortedArray<Int>(unsorted: [])
test.insert(5)
test.insert(3)

test.elements
