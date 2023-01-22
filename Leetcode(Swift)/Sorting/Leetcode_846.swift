class Solution_846 {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        guard hand.count % groupSize == 0 else {
            return false
        }
        
        let list = hand.sorted()
        var dic: [Int: Int] = [:]
        
        list.map {
            dic[$0, default: 0] += 1
        }
        
        for num in list {
            guard dic[num] != nil else {
                continue
            }
            for i in 0..<groupSize {
                var next = num + i
                if dic[next] == nil {
                    return false
                }
                dic[next]! -= 1
                if dic[next]! == 0 {
                    dic[next] = nil
                }
            }
        }
        return true
    }
}
