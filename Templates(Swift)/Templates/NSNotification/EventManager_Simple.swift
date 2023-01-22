//
//  EventManager.swift
//  Templates
//
//  Created by Harry Yan on 19/10/22.
//

import Foundation

final class EventManager {
    // hash map
    private var listeners: [String: any EventListener] = [:]
    
    // singleton
    static var sharedManager = EventManager()
    
    private init() {}
    
    func subscribe(event name: String, subscriber: some EventListener) {
        listeners[name] = subscriber
    }
    
    func unSubscribe(event name: String) {
        listeners[name] = nil
    }
    
    func notify(data: String) {
        for (_,v) in listeners {
            v.update(data: data)
        }
    }
}

protocol EventListener {
    func update(data: String)
}

final class LoggingListener: EventListener {
    private var log: String = ""
    
    func update(data:String) {
        print(data)
    }
}

class Demo {
    func main() {
        let manager = EventManager.sharedManager
        let logListener = LoggingListener()
        
        manager.subscribe(event: "test", subscriber: logListener)
    }
}
