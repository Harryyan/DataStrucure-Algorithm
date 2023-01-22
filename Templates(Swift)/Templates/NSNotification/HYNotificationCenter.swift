//import Foundation
//
//private let _defaultCenter: HYNotificationCenter = HYNotificationCenter()
//
//open class HYNotificationCenter: NSObject {
//    private lazy var _nilIdentifier: ObjectIdentifier = ObjectIdentifier(_observersLock)
//    private lazy var _nilHashable: AnyHashable = AnyHashable(_nilIdentifier)
//    private let _observersLock = NSLock()
//    private var _observers: [AnyHashable: [ObjectIdentifier: [ObjectIdentifier: HYNotificationReceiver]]]
//    
//    open class var `default`: HYNotificationCenter {
//        return _defaultCenter
//    }
//    
//    public required override init() {
//        _observers = [AnyHashable: [ObjectIdentifier: [ObjectIdentifier: HYNotificationReceiver]]]()
//    }
//    
//    open func post(name aName: HYNotification.Name, object anObject: Any?, userInfo aUserInfo: [AnyHashable : Any]? = nil) {
//        let notification = HYNotification(name: aName, object: anObject, userInfo: aUserInfo)
//        post(notification)
//    }
//    
//    open func post(_ notification: HYNotification) {
//        let notificationNameIdentifier: AnyHashable = AnyHashable(notification.name)
//        let senderIdentifier: ObjectIdentifier? = notification.object.map({ ObjectIdentifier(__SwiftValue.store($0)) })
//        
//        let sendTo: [Dictionary<ObjectIdentifier, HYNotificationReceiver>.Values] = _observersLock.synchronized({
//            var retVal = [Dictionary<ObjectIdentifier, HYNotificationReceiver>.Values]()
//            
//            (_observers[_nilHashable]?[_nilIdentifier]?.values).map({ retVal.append($0) })
//            senderIdentifier.flatMap({ _observers[_nilHashable]?[$0]?.values }).map({ retVal.append($0) })
//            (_observers[notificationNameIdentifier]?[_nilIdentifier]?.values).map({ retVal.append($0) })
//            senderIdentifier.flatMap({ _observers[notificationNameIdentifier]?[$0]?.values}).map({ retVal.append($0) })
//            
//            return retVal
//        })
//        
//        sendTo.forEach { observers in
//            observers.forEach { observer in
//                guard let block = observer.block else {
//                    return
//                }
//                
//                if let queue = observer.queue, queue != OperationQueue.current {
//                    queue.addOperation { block(notification) }
//                    queue.waitUntilAllOperationsAreFinished()
//                } else {
//                    block(notification)
//                }
//            }
//        }
//    }
//    
//    open func addObserver(forName name: HYNotification.Name?,
//                          object obj: Any?,
//                          queue: OperationQueue?,
//                          using block: @escaping (HYNotification) -> Void) -> NSObjectProtocol {
//        let newObserver = HYNotificationReceiver()
//        newObserver.name = name
//        newObserver.block = block
//        newObserver.sender = __SwiftValue.store(obj)
//        newObserver.queue = queue
//        
//        let notificationNameIdentifier: AnyHashable = name.map({ AnyHashable($0) }) ?? _nilHashable
//        let senderIdentifier: ObjectIdentifier = newObserver.sender.map({ ObjectIdentifier($0) }) ?? _nilIdentifier
//        let receiverIdentifier: ObjectIdentifier = ObjectIdentifier(newObserver)
//        
//        _observersLock.synchronized({
//            _observers[notificationNameIdentifier, default: [:]][senderIdentifier, default: [:]][receiverIdentifier] = newObserver
//        })
//        
//        return newObserver
//    }
//    
//    open func addObserver(_ observer: Any, selector aSelector: Selector, name aName: HYNotification.Name?, object anObject: Any?) {
//        let name = HYNotification.Name("\(type(of: observer))")
//        let newObserver = HYNotificationReceiver()
//        newObserver.name = name
//        newObserver.selector = aSelector
//        newObserver.sender = __SwiftValue.store(obj)
//        
//        let notificationNameIdentifier: AnyHashable = name
//        let senderIdentifier: ObjectIdentifier = newObserver.sender.map({ ObjectIdentifier($0) }) ?? _nilIdentifier
//        let receiverIdentifier: ObjectIdentifier = ObjectIdentifier(newObserver)
//        
//        _observersLock.synchronized({
//            _observers[notificationNameIdentifier, default: [:]][senderIdentifier, default: [:]][receiverIdentifier] = newObserver
//        })
//    }
//    
//    open func removeObserver(_ observer: Any) {
//        removeObserver(observer, name: nil, object: nil)
//    }
//    
//    open func removeObserver(_ observer: Any, name aName: HYNotification.Name?, object: Any?) {
//        guard let observer = observer as? HYNotificationReceiver,
//              // These 2 parameters would only be useful for removing notifications added by `addObserver:selector:name:object:`
//              aName == nil || observer.name == aName,
//              object == nil || observer.sender === __SwiftValue.store(object)
//        else {
//            return
//        }
//        
//        let notificationNameIdentifier: AnyHashable = observer.name.map { AnyHashable($0) } ?? _nilHashable
//        let senderIdentifier: ObjectIdentifier = observer.sender.map { ObjectIdentifier($0) } ?? _nilIdentifier
//        let receiverIdentifier: ObjectIdentifier = ObjectIdentifier(observer)
//        
//        _observersLock.synchronized({
//            _observers[notificationNameIdentifier]?[senderIdentifier]?.removeValue(forKey: receiverIdentifier)
//            if _observers[notificationNameIdentifier]?[senderIdentifier]?.count == 0 {
//                _observers[notificationNameIdentifier]?.removeValue(forKey: senderIdentifier)
//            }
//        })
//    }
//}
//
//
//
//
//
//private class HYNotificationReceiver : NSObject {
//    fileprivate var name: HYNotification.Name?
//    fileprivate var block: ((HYNotification) -> Void)?
//    fileprivate var selector: Selector?
//    fileprivate var sender: AnyObject?
//    fileprivate var queue: OperationQueue?
//}
