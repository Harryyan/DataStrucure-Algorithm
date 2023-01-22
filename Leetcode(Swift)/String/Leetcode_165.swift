//
//  Leetcode_165.swift
//  Leetcode
//
//  Created by Harry on 13/04/22.
//

import Foundation

class Solution_165 {
    // tc: O(n)
    // sc: O(1)
    // time: 3 + 18 | sc： O(n) -> 3 + 4
    func compareVersion(_ version1: String, _ version2: String) -> Int {
        let v1List = Array(version1)
        let v2List = Array(version2)

        var v1Pointer = 0
        var v2Pointer = 0

        while v1Pointer < version1.count || v2Pointer < version2.count {
            var v1RevisionValue = ""
            var v2RevisionValue = ""

            if v1Pointer >= version1.count {
                v1RevisionValue = "0"
            } else {
                calculatePosition(&v1Pointer, version1, v1List, &v1RevisionValue)
            }

            let v1_int_value = Int(v1RevisionValue)

            if v2Pointer >= version2.count {
                v2RevisionValue = "0"
            } else {
                calculatePosition(&v2Pointer, version2, v2List, &v2RevisionValue)
            }

            let v2_int_value = Int(v2RevisionValue)

            if v1_int_value ?? 0 < v2_int_value ?? 0 {
                return -1
            } else if v2_int_value ?? 0 < v1_int_value ?? 0 {
                return 1
            }

            v1Pointer += 1
            v2Pointer += 1
        }
        return 0
}

    private func calculatePosition(_ v1Pointer: inout Int, _ version1: String, _ v1List: [String.Element], _ v1RevisionValue: inout String) {
        while v1Pointer < version1.count && v1List[v1Pointer] == "0" {
            v1Pointer += 1
        }
        
        while v1Pointer < version1.count && v1List[v1Pointer] != "." {
            v1RevisionValue.append(v1List[v1Pointer])
            v1Pointer += 1
        }
    }
}
