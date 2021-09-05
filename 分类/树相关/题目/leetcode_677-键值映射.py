# 实现一个 MapSum 类，支持两个方法，insert 和 sum：

# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

class MapSum:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.value = 0
        self.hash_map = {}

    def insert(self, key: str, val: int) -> None:
        node = self

        if key in self.hash_map:
            o_val = self.hash_map[key]
            self.hash_map[key] = val

            val = val - o_val
        else:
            self.hash_map[key] = val

        for s in key:
            s = ord(s) - ord('a')
            if not node.children[s]:
                obj = MapSum()
                obj.value = val
                node.children[s] = obj
            else:
                node.children[s].value += val

            node = node.children[s]

        node.isEnd = True

    def sum(self, prefix: str) -> int:
        node = self
        i = 0
        n = len(prefix)
        
        for ch in prefix:
            x = ord(ch) - ord("a")
            if not node.children[x]:
                return 0
            node = node.children[x]
                
        return node.value


test = MapSum()
test.insert("apple", 3)
test.insert("app", 2)
test.insert("apple", 2)
r = test.sum("ba")

print(r)
