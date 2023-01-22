/*
 Given a string s, find the length of the longest substring without repeating characters.
 */

import Foundation

final class Solution_3 {
    
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var maxCount = 0
        var array = [Character]()
        for char in s {
            if let index = array.firstIndex(of: char) {
                array.removeFirst(index + 1)
            }
            array.append(char)
            if(array.count > maxCount){
                maxCount = array.count
            }
        }
        return maxCount
    }
}
