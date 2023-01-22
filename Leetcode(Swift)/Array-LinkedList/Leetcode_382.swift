import Foundation

final class Solution_382 {
    let head: ListNode?

    init(_ head: ListNode?) {
        self.head = head
    }
    
    func getRandom() -> Int {
        var p = head
        var reserve = 0
        var count = 0
        
        while p != nil {
            count += 1
            let rand = Int.random(in: 1 ... count)
            if rand == count {
                reserve = p!.val
            }
            
            p = p?.next
        }
        
        return reserve
    }
}
