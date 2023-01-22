import Foundation

final class Solution_71 {
    
    func simplifyPath(_ path: String) -> String {
        var stack: [String] = []
        let components = path.split(separator: "/")
        
        for item in components {
            if String(item) == ".." {
                _ = stack.popLast()
            } else if !" ..".contains(String(item)) {
                stack.append(String(item))
            }
        }
        
        return "/" + stack.joined(separator: "/")
    }
}
