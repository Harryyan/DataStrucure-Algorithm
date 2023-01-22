import Foundation

open class HYNotification: NSObject, NSCopying, NSCoding {
    private(set) open var name: Name
    
    private(set) open var object: Any?
    
    private(set) open var userInfo: [AnyHashable : Any]?
    
    public convenience override init() {
        /* do not invoke; not a valid initializer for this class */
        fatalError()
    }
    
    public init(name: Name, object: Any?, userInfo: [AnyHashable : Any]? = nil) {
        self.name = name
        self.object = object
        self.userInfo = userInfo
    }
    
    public convenience required init?(coder aDecoder: NSCoder) {
        guard aDecoder.allowsKeyedCoding else {
            preconditionFailure("Unkeyed coding is unsupported.")
        }
        
        guard let name = aDecoder.decodeObject(of: NSString.self, forKey:"NS.name") else {
            return nil
        }
        
        let object = aDecoder.decodeObject(forKey: "NS.object")
        let userInfo = aDecoder.decodeObject(of: NSDictionary.self, forKey: "NS.userinfo")
        self.init(name: Name(rawValue: String._unconditionallyBridgeFromObjectiveC(name)), object: object as! NSObject, userInfo: nil)
    }
    
    open override func copy() -> Any {
        copy(with: nil)
    }
    
    open func copy(with zone: NSZone? = nil) -> Any {
        self
    }
    
    open func encode(with aCoder: NSCoder) {
        guard aCoder.allowsKeyedCoding else {
            preconditionFailure("Unkeyed coding is unsupported.")
        }
        
        aCoder.encode(self.name.rawValue._bridgeToObjectiveC(), forKey:"NS.name")
        aCoder.encode(self.object, forKey:"NS.object")
        aCoder.encode(self.userInfo?._bridgeToObjectiveC(), forKey:"NS.userinfo")
    }
    
    open override var description: String {
        var str = "\(type(of: self)) \(Unmanaged.passUnretained(self).toOpaque()) {"
        
        str += "name = \(self.name.rawValue)"
        if let object = self.object {
            str += "; object = \(object)"
        }
        if let userInfo = self.userInfo {
            str += "; userInfo = \(userInfo)"
        }
        str += "}"
        
        return str
    }
}

extension HYNotification {
    public struct Name : RawRepresentable, Equatable, Hashable {
        public private(set) var rawValue: String
        
        public init(_ rawValue: String) {
            self.rawValue = rawValue
        }
        
        public init(rawValue: String) {
            self.rawValue = rawValue
        }
    }
}
