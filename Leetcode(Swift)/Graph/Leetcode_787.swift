/*
 There are n cities connected by some number of flights. You are given an array flights
 where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

 You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
 */

import Foundation

final class Solution_787 {
    
    func findCheapestPrice(_ n: Int, _ flights: [[Int]], _ src: Int, _ dst: Int, _ k: Int) -> Int {
        let INF = 100000
        var dist: [Int] = Array(repeating: INF, count: n)
        var dict: [Int: [(Int, Int)]] = [:]     // Adj table to save graph
        
        dist[src] = 0
        
        for flight in flights {
            let src = flight[0]
            let des = flight[1]
            let value = flight[2]
            
            if dict[src] == nil {
                dict[src] = []
                dict[src]?.append((des, value))
            } else {
                dict[src]!.append((des, value))
            }
        }
        
        var queue: [(Int, Int, Int)] = []
        queue.append((src, -1, 0))
        
        while queue.count > 0 {
            let item = queue.remove(at: 0)
            let src = item.0
            let count = item.1
            let price = item.2
            
            if count + 1 > k {
                break
            }
            
            if dict[src] != nil {
                for (des, value) in dict[src]! {
                    if dist[des] > price + value {
                        dist[des] =  price + value
                        queue.append((des, count+1, dist[des]))
                    }
                }
            }
        }

        return dist[dst] == 100000 ? -1 : dist[dst] 
    }
}
