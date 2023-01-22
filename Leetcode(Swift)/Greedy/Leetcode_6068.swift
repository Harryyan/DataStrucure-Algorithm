//
//  Leetcode_6068.swift
//  Leetcode
//
//  Created by Harry on 16/05/22.
//

import Foundation

class Solution_6068 {
    func maximumWhiteTiles(_ tiles: [[Int]], _ carpetLen: Int) -> Int {
        var res = 0
        var cur = 0
        var r = 0
        let tiles = tiles.sorted(by: { $0[0] <= $1[0] })

        for i in 0..<tiles.count {
            while r < tiles.count && tiles[r][1] - tiles[i][0] + 1 <= carpetLen {
                cur += (tiles[r][1] - tiles[r][0] + 1)
                r += 1
            }
            
            if r < tiles.count {
                res = max(res, cur + max(0, tiles[i][0]+carpetLen-tiles[r][0]))
            } else {
                res = max(res, cur)
            }
            
            cur -= (tiles[i][1] - tiles[i][0] + 1)
        }
        
        return res
    }
}

