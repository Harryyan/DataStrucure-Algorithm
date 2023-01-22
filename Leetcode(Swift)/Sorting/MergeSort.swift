import Foundation

final class MergeSort {
    
    func sort(_ items: [Int]) -> [Int] {
        let result = mergeSort(start: 0, end: items.count-1, items)
        
        return result
    }
    
    private func mergeSort(start: Int, end: Int, _ items: [Int]) -> [Int] {
        let n = end - start + 1
        
        if n == 1 {
            return [items[start]]
        }
        
        let mid = start + (end - start) / 2
        
        let left = mergeSort(start: start, end: mid, items)
        let right = mergeSort(start: mid + 1, end: end, items)
        
        var leftCursor = 0
        var rightCursor = 0
        var result: [Int] = []
        
        while leftCursor < left.count && rightCursor < right.count {
            if left[leftCursor] <= right[rightCursor] {
                result.append(left[leftCursor])
                leftCursor += 1
            } else {
                result.append(right[rightCursor])
                rightCursor += 1
            }
        }
        
        result += left[leftCursor..<left.count]
        result += right[rightCursor..<right.count]
        
        return result
    }
}


// Other version
func mergeSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    
    let middleIndex = array.count / 2
    
    let leftArray = mergeSort(Array(array[0..<middleIndex]))
    let rightArray = mergeSort(Array(array[middleIndex..<array.count]))
    
    return merge(leftArray, rightArray)
}

func merge<T: Comparable>(_ left: [T], _ right: [T]) -> [T] {
    var leftIndex = 0
    var rightIndex = 0
    
    var orderedArray: [T] = []
    
    while leftIndex < left.count && rightIndex < right.count {
        let leftElement = left[leftIndex]
        let rightElement = right[rightIndex]
        
        if leftElement < rightElement {
            orderedArray.append(leftElement)
            leftIndex += 1
        } else if leftElement > rightElement {
            orderedArray.append(rightElement)
            rightIndex += 1
        } else {
            orderedArray.append(leftElement)
            leftIndex += 1
            orderedArray.append(rightElement)
            rightIndex += 1
        }
    }
    
    while leftIndex < left.count {
        orderedArray.append(left[leftIndex])
        leftIndex += 1
    }
    
    while rightIndex < right.count {
        orderedArray.append(right[rightIndex])
        rightIndex += 1
    }
    
    return orderedArray
}

/*
 链表归并排序
 */
final class Solution_148 {
    func sortList(_ head: ListNode?) -> ListNode? {
        if (head == nil || head?.next == nil) {
            return head
        }
        var slow = head
        var fast = head?.next
        // 快慢指针法，使得slow指向链表的中间节点。
        while(fast != nil && fast?.next != nil){
            slow = slow?.next
            fast = fast?.next?.next
        }
        let last = slow?.next
        slow?.next = nil
        let first = sortList(head)
        let second = sortList(last)
        let res = MergeTwoList(first,second)
        return res;
    }
    
    func MergeTwoList(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        let dummpy = ListNode(-1)
        var tail = dummpy
        var list1 = list1
        var list2 = list2
        while(list1 != nil && list2 != nil){
            if(list1?.val ?? 0 < list2?.val ?? 0){
                tail.next = list1
                list1 = list1?.next
            }else{
                tail.next = list2
                list2 = list2?.next
            }
            tail = tail.next!
        }
        tail.next = (list1 != nil ? list1 : list2);
        return dummpy.next
    }
}

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}
