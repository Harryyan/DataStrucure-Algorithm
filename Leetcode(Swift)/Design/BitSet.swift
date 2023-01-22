/*
 A Bitset is a data structure that compactly stores bits.
 
 Implement the Bitset class:
 
 Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
 void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
 void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
 void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
 boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
 boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
 int count() Returns the total number of bits in the Bitset which have value 1.
 String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.
 
 */

import Foundation

class Bitset {
    private let size: Int
    private var data: [String] = []
    private var data1: [String] = []
    private var ones: Int = 0
    
    init(_ size: Int) {
        self.size = size
        data = Array(repeating: "0", count: size)
        data1 = Array(repeating: "1", count: size)
    }
    
    func fix(_ idx: Int) {
        if data[idx] == "0" {
            data[idx] = "1"
            data1[idx] = "0"
            ones += 1
        }
    }
    
    func unfix(_ idx: Int) {
        if data[idx] == "1" {
            data[idx] = "0"
            data1[idx] = "1"
            ones -= 1
        }
    }
    
    func flip() {
        let temp = self.data
        self.data = self.data1
        self.data1 = temp
        
        ones = size - ones
    }
    
    func all() -> Bool {
        return ones == size
    }
    
    func one() -> Bool {
        return ones > 0
    }
    
    func count() -> Int {
        ones
    }
    
    func toString() -> String {
        return data.joined(separator: "")
    }
}
