/*
 Given a string formula representing a chemical formula, return the count of each atom.
 
 The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
 
 One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
 
 For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
 Two formulas are concatenated together to produce another formula.
 
 For example, "H2O2He3Mg4" is also a formula.
 A formula placed in parentheses, and a count (optionally added) is also a formula.
 
 For example, "(H2O2)" and "(H2O2)3" are formulas.
 Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
 
 The test cases are generated so that all the values in the output fit in a 32-bit integer.
 */

import Foundation

class Solution_726 {
    
    func countOfAtoms(_ formula: String) -> String {
        var dict: [[String: Int]] = [[:]]
        var index = formula.startIndex
        
        while index < formula.endIndex {
            switch formula[index] {
            case "(":
                dict.append([:])
                
                formula.formIndex(after: &index)
            case ")":
                formula.formIndex(after: &index)
                
                let count = getCount(at: &index, with: formula)
                dict[dict.endIndex - 2].merge(
                    dict.popLast()!.mapValues { $0 * count },
                    uniquingKeysWith: +)
                print(dict)
            case "A"..."Z":
                dict[dict.endIndex - 1][getName(at: &index, with: formula), default: 0] += getCount(at: &index, with: formula)
                print(dict)
            default:
                break
            }
        }
        
        return dict.last!
            .sorted { $0.key < $1.key }
            .map { $0.key + ($0.value > 1 ? String($0.value) : "") }
            .joined()
    }
    
    private func getCount(at index: inout String.Index, with formula: String) -> Int {
        guard index < formula.endIndex && formula[index].isNumber else {
            return 1
        }
        
        var count = 0
        while index < formula.endIndex, let num = formula[index].wholeNumberValue {
            count = count * 10 + num
            formula.formIndex(after: &index)
        }
        
        return count
    }
    
    private func getName(at index: inout String.Index, with formula: String) -> String {
        let startIndex = index
        
        repeat {
            formula.formIndex(after: &index)
        } while index < formula.endIndex && formula[index].isLowercase
        
        return String(formula[startIndex..<index])
    }
}
