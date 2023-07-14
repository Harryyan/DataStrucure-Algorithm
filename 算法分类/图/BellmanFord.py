maxn = 10

class Edge:
    def __init__(self, v = 0, w = 0):
        self.v = v
        self.w = w

e = [[Edge() for i in range(maxn)] for j in range(maxn)]
dis = [0x3f3f3f3f] * maxn

def bellmanford(n, s):
    dis[s] = 0
    for i in range(1, n + 1):
        flag = False
        for u in range(1, n + 1):
            for ed in e[u]:
                v, w = ed.v, ed.w
                if dis[v] > dis[u] + w:
                    flag = True
        # 没有可以松弛的边时就停止算法
        if flag == False:
            break
    # 第 n 轮循环仍然可以松弛时说明 s 点可以抵达一个负环
    return flag
