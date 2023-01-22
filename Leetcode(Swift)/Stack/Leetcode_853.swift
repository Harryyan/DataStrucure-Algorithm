import Foundation

class Solution_853 {
    // tc: O(nlogn) - n is number of position
    // sc: O(n)
    // time: 15 mins
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        guard position.count > 1 else { return position.count  }

        var dict: [Int:Double] = [:]
        var result = 0

        for (i, p) in position.enumerated() {
            dict[p] = Double((target-p))/Double(speed[i])
        }

        var stack = dict.sorted(by: {$0.0<$1.0})

        while !stack.isEmpty {
            let car1 = stack.removeLast()
            if stack.isEmpty {
                result += 1
                break
            }

            let car2 = stack.removeLast()

            if car2.value > car1.value {
                result += 1
                stack.append(car2)
            } else {
                stack.append(car1)
            }
        }

        return result
    }
}
