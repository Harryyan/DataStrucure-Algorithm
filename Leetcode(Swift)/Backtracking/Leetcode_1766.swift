class Solution_1766 {
    var nums: [Int] = []
    var graph: [Int: [Int]] = [:]
    var primeDict: [Int: [Int]] = [:]
    var seen: Set<Int> = []
    var path: [Int] = []
    var depth: [Int] = [] // 每个值的深度
    var result: [Int] = []

    // tc: O(kn) - k is constant
    // sc: O(n)
    func getCoprimes(_ nums: [Int], _ edges: [[Int]]) -> [Int] {
        depth = Array(repeating:-1,count:51) // 每个值的深度
        result = Array(repeating:-1,count:nums.count)
        self.nums = nums

        // 建图
        for edge in edges {
            graph[edge[0], default:[]].append(edge[1])
            graph[edge[1], default:[]].append(edge[0])
        }

        // 预处理质数对
        for i in 1...50 {
            for j in 1...50 {
                if gcd(i,j) == 1 {
                    primeDict[i, default:[]].append(j)
                    primeDict[j, default:[]].append(i)
                }
            }
        }

        dfs(0)

        return result
    }

    private func dfs(_ node: Int) {
        var index = -1
        
        for p in primeDict[nums[node]]! {
            // 获得当前单条路径最大深度(深度数组存的是位置)
            index = max(index,depth[p])
        }

        result[node] = index == -1 ? -1 : path[index]
        let tmp = depth[nums[node]]
        depth[nums[node]] = path.count // 之后要恢复
        path.append(node)
        seen.insert(node)

        for next in graph[node] ?? [] {
            if !seen.contains(next) {
                dfs(next)
            }
        }

        depth[nums[node]] = tmp
        path.removeLast()
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        let r = a % b
        
        if r != 0 {
            return gcd(b, r)
        } else {
            return b
        }
    }
}
