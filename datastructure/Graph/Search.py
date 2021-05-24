from typing import List
from DS.Graph.Vertex import Vertex


from Graph import Graph

found = False

# 图： 深度优先(走迷宫)
def dfs(g: Graph, s: Vertex, t: Vertex):
    visited = [False] * g.get_vertex_num()
    visited[s] = True
    pre = [-1] * g.get_vertex_num()

    recursive_dfs(s, t, visited, pre)
    pprint(g, pre, s, t)


def recursive_dfs(g: Graph, s, t, visited, pre):
    if found:
        return

    visited[s] = True

    if s == t:
        found = True
        return

    for item in g.get_vertex(s):
        if not visited[item]:
            pre[item] = s
            recursive_dfs(g, item, t, visited, pre)


# 图 - 广度优先搜索
# 时间复杂度：O(V + E)
# 空间复杂度: O(V)


def bfs(g: Graph, s: Vertex, t: Vertex):
    if s == t:
        return

    visited = [False] * g.get_vertex_num()
    visited[s] = True
    pre = [-1] * g.get_vertex_num()
    queue = []
    queue.append[s]

    while queue:
        w = queue.pop(0)

        for item in g.get_vertex(w):
            if not visited[item]:
                pre[item] = w

                if item == t:
                    pprint(pre, s, t)
                    return

                visited[item] = True
                queue.append(item)


def pprint(pre: List, s, t):
    if pre[t] != -1 and s != t:
        pprint(pre, s, pre[t])

    print(t, end=" ")


graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_edge("a", "b", 10)
graph.add_edge("b", "a", 10)
graph.add_edge("a", "c", 12)
graph.add_edge("b", "c", 15)
