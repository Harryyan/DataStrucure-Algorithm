#  邻接表实现图
from typing import List
from Vertex import Vertex


class Graph:
    """实现图"""

    def __init__(self):
        self.vertlist = {}
        self.count_vertex = 0

    def add_vertex(self, key):
        """在列表中添加节点"""
        self.count_vertex += 1
        self.vertlist[key] = Vertex(key)

    def get_vertex(self, i):
        """查找顶点"""
        return self.vertlist[i].get_connects() if i in self.vertlist else None

    def add_edge(self, key, nbr, weight=0):
        """添加边"""
        if key not in self.vertlist:
            self.add_vertex(key)
        if nbr not in self.vertlist:
            self.add_vertex(nbr)
            
        self.vertlist[key].add_neignbor(self.vertlist[nbr], weight)

    def get_vertex_num(self):
        """返回所有顶点数量"""
        return self.count_vertex


graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_edge("a", "b", 10)
graph.add_edge("b", "a", 10)
graph.add_edge("a", "c", 12)
graph.add_edge("b", "c", 15)

print(graph.get_vertex_num())
print(graph.get_vertex("a"))
