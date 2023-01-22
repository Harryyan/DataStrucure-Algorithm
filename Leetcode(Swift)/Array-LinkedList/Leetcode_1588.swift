import Foundation

final class Solution_1588 {
    
    func sumOddLengthSubarrays(_ arr: [Int]) -> Int {
        var sum1 = 0
        var sum2 = 0
        var list: [Int] = []
        
        for (index, _) in arr.enumerated() {
            if index > 1 && index % 2 == 0 {
                list.append(index)
            }
        }
        
        for (index, value) in arr.enumerated() {
            sum1 += value
            
            if index > 1 {
                for j in list {
                    if index - j >= 0 {
                        sum2 += arr[index-j...index].sum()
                    } else {
                        break
                    }
                }
            }
        }
        
        return sum1 + sum2
    }
}

extension Sequence where Element: AdditiveArithmetic {
    func sum() -> Element { reduce(.zero, +) }
}
