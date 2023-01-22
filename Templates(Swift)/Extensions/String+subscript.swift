import Foundation

extension String {
    subscript(_ n: Int) -> Character {
        get {
            let idx = self.index(startIndex, offsetBy: n)
            return self[idx]
        }
        set {
            let idx = self.index(startIndex, offsetBy: n)
            self.replaceSubrange(idx...idx, with: [newValue])
        }
    }
}
