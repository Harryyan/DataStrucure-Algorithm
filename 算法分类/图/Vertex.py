class Vertex:
    """顶点类，包含顶点信息及连接边"""
    
    def __init__(self, key):
        self.id = key
        self.connect = {}

    def add_neignbor(self, nbr, weight=0):
        # nbr是顶点对象所连接的另外节点，也就是顶点对象的key值
        # wight表示的权重，也就是两点之间的距离
        self.connect[nbr] = weight

    def get_connects(self):
        # 返回顶点所连接的其他点
        return [[i.id, v] for i, v in self.connect.items()]
