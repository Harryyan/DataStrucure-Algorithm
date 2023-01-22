import Foundation

final class Solution_150 {
    func evalRPN(_ tokens: [String]) -> Int {
        var stack = [Int]()
        
        for item in tokens {
            if item == "+" || item == "-" || item == "*" || item == "/" {
                let rightV = stack.popLast()!
                let leftV = stack.popLast()!
                if item == "+" {
                    stack.append(leftV + rightV)
                } else if item == "-" {
                    stack.append(leftV - rightV)
                } else if item == "*" {
                    stack.append(leftV * rightV)
                } else {
                    stack.append(leftV / rightV)
                }
            } else {
                stack.append(Int(item)!)
            }
        }
        
        return stack.last!
    }
}
