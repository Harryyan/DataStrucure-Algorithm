import Foundation

final class Logger {
    var dict = [String : Int]()
    
    func shouldPrintMessage(_ timestamp: Int, _ message: String) -> Bool {
        let result = timestamp - 10 >= dict[message] ?? -10
        if result { dict[message] = timestamp }
        
        return result
    }
}
