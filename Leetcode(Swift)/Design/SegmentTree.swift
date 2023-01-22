import Foundation

class SegmentTree {
    var tree: [Int]  // 0: no color; >1: one color; -1: multiple colors
    var mark: [Int] // lazy tag
    var data: [Int]
    var colors = 0
    
    init(number: Int) {
        tree = Array(repeating: 0, count: number * 4)
        mark = Array(repeating: 0, count: number * 4)
        data = Array(repeating: 0, count: number)
    }
    
    private func build(_ left: Int, _ right: Int, _ index: Int) {
        // Sum of intervals
//        if left == right {
//            tree[index] = data[left]
//        } else {
//            let mid = l + (r - l) / 2
//            build(l, mid, index*2)
//            build(mid+1, r, index*2+1)
//
//            tree[index] = tree[index*2] + tree[index*2+1]
//        }
    }
    
    
    /// Query
    /// - Parameters:
    ///   - cl: current interval left (tree)
    ///   - cr: current interval right (tree)
    ///   - l: target interval left
    ///   - r: target interval right
    ///   - index: node index
    private func query(_ cl: Int, _ cr: Int, _ l: Int, _ r: Int, _ index: Int) {
        if cl > r || cr < l { return }
        
        if l <= cl && r >= cr {
            if tree[index] == 0 { return }
            if tree[index] == -1 {
                let mid = cl + (cr - cl) / 2
                pushDown(index, cl, cr)
                
                query(cl, mid, l, r, index*2)
                query(mid+1, mid, l, r, index*2+1)
            } else {
                if tree[index] != 0 {
                    colors += 1
                }
            }
            
            return
        }
        
        let mid = cl + (cr - cl) / 2
        pushDown(index, cl, cr)
        
        query(cl, mid, l, r, index*2)
        query(mid+1, mid, l, r, index*2+1)
    }
    
    
    /// Update Segment Tree
    /// - Parameters:ß
    ///   - l: target interval left
    ///   - r: target interval right
    ///   - cl: current interval left (tree)
    ///   - cr: current interval right (tree)
    ///   - index: node index
    ///   - color: added color
    private func update(l: Int, r: Int, cl: Int, cr: Int, index: Int, color: Int) {
        // no overlap
        if cl > r || cr < l { return }
        
        // target interal coverred current interval
        if l <= cl && r >= cr {
            mark[index] = color
            tree[index] = color
            
            return
        }
        
        pushDown(index, cl, cr) // push down color
        
        let mid = cl + (cr - cl) / 2
        
        update(l: l, r: r, cl: cl, cr: mid, index: index*2, color: color)
        update(l: l, r: r, cl: mid+1, cr: cr, index: index*2+1, color: color)
        
        if tree[index*2] == tree[index*2+1] {
            tree[index] = tree[index*2]
        } else {
            tree[index] = -1
        }
    }
    
    
    /// Push down color to sub nodes
    /// - Parameters:
    ///   - index: node index
    ///   - l: current left index
    ///   - r: current right index
    private func pushDown(_ index: Int, _ l: Int, _ r: Int) {
        guard mark[index] != 0 else { return }
        
        mark[index*2] = mark[index]
        mark[index*2+1] = mark[index]
        
        tree[index*2] = mark[index]
        tree[index*2+1] = mark[index]
        
        mark[index] = 0
    }
}
