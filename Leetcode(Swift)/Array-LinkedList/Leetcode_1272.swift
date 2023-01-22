/*
 A set of real numbers can be represented as the union of several disjoint intervals,
 where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).
 
 You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above,
 where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.
 
 Return the set of real numbers with the interval toBeRemoved removed from intervals.
 In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved.
 Your answer should be a sorted list of disjoint intervals as described above.
 
 */

import Foundation

class Solution_1272 {
    
    // tc: O(n)
    // sc: O(n)
    
    func removeInterval(_ intervals: [[Int]], _ toBeRemoved: [Int]) -> [[Int]] {
        var res: [[Int]] = []
        
        for interval in intervals {
            // There are 4 different kinds of senarios of overlapped intervals
            // so checking them separately and add intervals to res
            if overlapCase1(toBeRemoved, interval) {
                res.append([toBeRemoved[1], interval[1]])
                
                continue
            }
            
            if overlapCase2(toBeRemoved, interval) {
                if toBeRemoved[0] > interval[0] {
                    res.append([interval[0], toBeRemoved[0]])
                }
                
                if toBeRemoved[1] < interval[1] {
                    res.append([toBeRemoved[1], interval[1]])
                }
                
                continue
            }
            
            if overlapCase3(toBeRemoved, interval) {
                res.append([interval[0], toBeRemoved[0]])
                
                continue
            }
            
            if overlapCase4(toBeRemoved, interval) {
                continue
            }
            
            res.append(interval)
        }
        
        return res
    }
    
    
    private func overlapCase1(_ interval1: [Int], _ interval2: [Int]) -> Bool {
        interval1[0] < interval2[0] && interval1[1] > interval2[0] && interval1[1] < interval2[1]
    }
    
    private func overlapCase2(_ interval1: [Int], _ interval2: [Int]) -> Bool {
        interval1[0] >= interval2[0] && interval1[1] <= interval2[1]
    }
    
    private func overlapCase3(_ interval1: [Int], _ interval2: [Int]) -> Bool {
        interval1[0] > interval2[0] && interval1[0] < interval2[1] && interval1[1] > interval2[1]
    }
    
    private func overlapCase4(_ interval1: [Int], _ interval2: [Int]) -> Bool {
        interval1[0] < interval2[0] && interval1[1] > interval2[1]
    }
}
