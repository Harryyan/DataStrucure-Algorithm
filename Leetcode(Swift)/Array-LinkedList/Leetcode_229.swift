//
//  Leetcode_229.swift
//  Leetcode
//
//  Created by Harry on 1/06/22.
//

import Foundation

class Solution_229 {
    func majorityElement(_ nums: [Int]) -> [Int] {
        var vote1 = 0
        var vote2 = 0
        var element1 = 0
        var element2 = 0
        var ans = [Int]()

        for num in nums {
            if vote1 > 0 && num == element1 {
                vote1 += 1
            } else if vote2 > 0 && num == element2  {
                vote2 += 1
            } else if vote1 == 0 {
                vote1 += 1
                element1 = num
            } else if vote2 == 0 {
                vote2 += 1
                element2 = num
            } else {
                vote1 -= 1
                vote2 -= 1
            }
        }

        var cnt1 = 0
        var cnt2 = 0

        for num in nums {
            if num == element1 {
                cnt1 += 1
            } else if num == element2 {
                cnt2 += 1
            }
        }

        if cnt1 > nums.count / 3 {
            ans.append(element1)
        }

        if cnt2 > nums.count / 3 {
            ans.append(element2)
        }

        return ans
    }
}
