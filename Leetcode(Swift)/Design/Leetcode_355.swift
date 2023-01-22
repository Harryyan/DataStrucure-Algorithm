//
//  Leetcode_355.swift
//  Leetcode
//
//  Created by Harry on 17/05/22.
//

import Foundation

public class ListNode {
    public var userId: Int
    public var tweetId: Int
    public var next: ListNode?
    
    internal init(_ userId: Int, _ tweetId: Int, _ next: ListNode? = nil) {
        self.userId = userId
        self.tweetId = tweetId
        self.next = next
    }
}

class Twitter {
    
    var news: ListNode?
    var userMap: [Int: Set<Int>] = [:]

    init() {
        
    }
    
    func postTweet(_ userId: Int, _ tweetId: Int) {
        let node = ListNode(userId, tweetId, news)
        news = node
        
        if userMap[userId] == nil {
            var set = Set<Int>()
            set.insert(userId)
            userMap.updateValue(set, forKey: userId)
        }
    }
    
    func getNewsFeed(_ userId: Int) -> [Int] {
        var p = news
        var k = 10
        var result: [Int] = []
        guard let followers = userMap[userId] else {
            return result
        }
        
        while p != nil, k > 0 {
            if followers.contains(p!.userId) {
                result.append(p!.tweetId)
                k -= 1
            }
            p = p?.next
        }
        
        return result
    }
    
    func follow(_ followerId: Int, _ followeeId: Int) {
        if userMap[followerId] == nil {
            var set = Set<Int>()
            set.insert(followerId)
            userMap.updateValue(set, forKey: followerId)
        }
        userMap[followerId]?.insert(followeeId)
    }
    
    func unfollow(_ followerId: Int, _ followeeId: Int) {
        userMap[followerId]?.remove(followeeId)
    }
}
