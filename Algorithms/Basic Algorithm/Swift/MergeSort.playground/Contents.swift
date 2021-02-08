import Foundation


/*
 
 Goal: Sort an array from low to high (or high to low)
 
 Invented in 1945 by John von Neumann, merge-sort is an efficient algorithm with a best, worst, and average time complexity of O(n log n).
 
 The merge-sort algorithm uses the divide and conquer approach which is to divide a big problem into smaller problems and solve them. I think of the merge-sort algorithm as split first and merge after.
 
 Assume you need to sort an array of n numbers in the right order. The merge-sort algorithm works as follows:
 
 Put the numbers in an unsorted pile.
 Split the pile into two. Now, you have two unsorted piles of numbers.
 Keep splitting the resulting piles until you cannot split anymore. In the end, you will have n piles with one number in each pile.
 Begin to merge the piles together by pairing them sequentially. During each merge, put the contents in sorted order. This is fairly
 easy because each individual pile is already sorted.
 
 
 Performance:
 
 The speed of the merge-sort algorithm is dependent on the size of the array it needs to sort. The larger the array, the more work it needs to do.
 
 Whether or not the initial array is sorted already does not affect the speed of the merge-sort algorithm since you will be doing the same amount splits
 and comparisons regardless of the initial order of the elements.
 
 Therefore, the time complexity for the best, worst, and average case will always be O(n log n).
 
 A disadvantage of the merge-sort algorithm is that it needs a temporary "working" array equal in size to the array being sorted. It is not an in-place sort,
 unlike for example quicksort.
 
 Most implementations of the merge-sort algorithm produce a stable sort. This means that array elements that have identical sort keys will stay in the same
 order relative to each other after sorting. This is not important for simple values such as numbers or strings, but it can be an issue when sorting more
 complex objects.
 
 */

extension Collection where Index == Int, Element: Comparable {
    
    func mergeSort(orderPolicy: (Element, Element) -> Bool) -> [Element] {
        var copiedArray = map{ $0 }
        guard count > 1 else { return copiedArray }
        
        let middleIndex = copiedArray.count / 2
        
        let leftSide = copiedArray[0..<middleIndex].mergeSort(orderPolicy: orderPolicy)
        let rightSide = copiedArray[middleIndex..<copiedArray.count].mergeSort(orderPolicy: orderPolicy)
        
        return merge(leftPile: leftSide, rightPile: rightSide, orderPolicy: orderPolicy)
    }
    
    func merge(leftPile: [Element], rightPile: [Element], orderPolicy: (Element, Element) -> Bool) -> [Element] {
        var leftIndex = 0
        var rightIndex = 0
        var orderedPile = [Element]()
        
        while leftIndex < leftPile.count && rightIndex < rightPile.count {
            if orderPolicy(leftPile[leftIndex], rightPile[rightIndex]) {
                orderedPile.append(leftPile[leftIndex])
                leftIndex += 1
            } else {
                orderedPile.append(rightPile[rightIndex])
                rightIndex += 1
            }
        }
        
        while leftIndex < leftPile.count {
            orderedPile.append(leftPile[leftIndex])
            leftIndex += 1
        }
        
        while rightIndex < rightPile.count {
            orderedPile.append(rightPile[rightIndex])
            rightIndex += 1
        }
        
        return orderedPile
    }
}

let test = [2, 1, 5, 4, 4, 9, 9, 9, 10]
test.mergeSort(orderPolicy: <)
