//
//  Leetcode_759.swift
//  Leetcode
//
//  Created by Harry on 6/05/22.
//

import Foundation

class Solution_759 {
    func employeeFreeTime(_ schedule: [[Interval]]) -> [Interval] {
        var events: [(Int, Int)] = []

        for intervals in schedule {
            for interval in intervals {
                events.append((interval.start, 1))
                events.append((interval.end, -1))
            }
        }

        events = events.sorted { $0.0 < $1.0 }
        var ans: [Interval] = []

        var prev = -1
        var count = 0

        for (index, value) in events {
            if count == 0 && prev != -1 && prev != index {
                let interval = Interval(prev, index)
                ans.append(interval)
            }

            count += value

            prev = index
        }

        return ans
    }
}
