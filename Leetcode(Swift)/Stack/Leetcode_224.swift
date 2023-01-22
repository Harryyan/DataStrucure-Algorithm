//
//  Leetcode_224.swift
//  Leetcode
//
//  Created by Harry on 26/05/22.
//

import Foundation

class Solution_224 {

    func calculate(_ s: String) -> Int {
        var res = 0
        var num = 0
        var sign = 1
        var stack: [Int] = []
        
        for ch in s {
            if ch.isWholeNumber {
                num = 10 * num + ch.wholeNumberValue!
            } else if String(ch) == "+" || String(ch) == "-" {
                res += sign * num
                sign = String(ch) == "+" ? 1 : -1
                num = 0
            } else if String(ch) == "(" {
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            } else if String(ch) == ")" {
                res += sign * num
                num = 0
                res *= stack.removeLast()
                res += stack.removeLast()
            }
        }
        
        res += sign * num
        return res
    }
}

class Solution_224_Template {
    func calculate(_ s: String) -> Int {
        return cal(0,s).0
    }

    private func cal(_ index: Int, _ s: String) -> (Int, Int) {
        var index = index
        var num = 0
        var stack: [Int] = []
        var operand = Character("+")
        var list = Array(s)

        while index < s.count {
            if list[index].isWholeNumber {
                num = 10 * num + list[index].wholeNumberValue!
            } else if "+-*/".contains(list[index]) {
                doOpration(operand, num, &stack)
                num = 0
                operand = list[index]
            } else if String(list[index]) == "(" {
                let (value, newIndex) = cal(index+1, s)
                num = value
                index = newIndex - 1
            } else if String(list[index]) == ")"  {
                doOpration(operand, num, &stack)
                return (stack.reduce(.zero,+), index+1)
            }

            index += 1
        }

        doOpration(operand, num, &stack)
        return (stack.reduce(.zero,+), index)
    }

    private func doOpration(_ op: Character, _ value: Int, _ stack: inout [Int]) {
        if String(op) == "+" { stack.append(value) }
        if String(op) == "-" { stack.append(-value) }
        if String(op) == "*" { stack.append(stack.removeLast() * value) }
        if String(op) == "/" { stack.append(stack.removeLast() / value) }
    }
}
