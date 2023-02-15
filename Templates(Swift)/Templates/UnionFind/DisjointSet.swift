final class DSU {
    var dict: [Int:Int] = [:]
    
    init(_ n: Int) {
        for i in 0..<n {
            dict[i] = i
        }
    }
    
    // Find root parent node
    // 配合路径压缩
    func find(_ a: Int) -> Int {
        guard dict[a] != nil else {
            dict[a] = a
            return a
        }
        
        if dict[a] == a {
            return a
        }
        
        dict[a] = find(dict[a]!)
        return dict[a]!
    }
    
    func union(a: Int, b: Int) {
        guard !isConnected(a: a, b: b) else { return }
        
        var parent_a = find(a)
        var parent_b = find(b)
        
        // 找较小的数作为parent
        if parent_a > parent_b {
            let temp = parent_a
            parent_a = parent_b
            parent_b = temp
        }
        
        dict[parent_b] = parent_a
    }
    
    func isConnected(a: Int, b: Int) -> Bool {
        return find(a) == find(b)
    }
}

