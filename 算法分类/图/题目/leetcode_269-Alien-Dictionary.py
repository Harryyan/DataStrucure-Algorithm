from collections import defaultdict, deque
from itertools import pairwise
from typing import List

class Solution2:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = { c:0 for c in words[0] }   # 入度个数记录

        for s, t in pairwise(words):   # 字母序只能按照相邻的词比较
            for c in t:
                inDeg.setdefault(c,0)

            for u,v in zip(s,t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break    # 无需再比较
            else:
                if len(s) > len(t):   # 形如["abc", "ab"]的样例是违反定义的, 特殊判断
                    return ""     
                
        q = [u for u, d in inDeg.items() if d == 0]

        for u in q:
            for v in g[u]:  # 出度图
                inDeg[v] -= 1
                if inDeg[v] == 0: q.append(v)
        
        return ''.join(q) if len(q) == len(inDeg) else ""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def init_graph():
            g, n = defaultdict(set), len(words)
            for i in range(n - 1):
                word0, word1 = words[i], words[i + 1]
                n0, n1 = len(word0), len(word1)
                # 形如["abc", "ab"]的样例是违反定义的, 特殊判断
                if n0 > n1 and word0[:n1] == word1:
                    return None
                
                m = min(n0, n1)
                for j in range(m):
                    if word0[j] == word1[j]:
                        continue
                    # 第一对不同的字符提供序关系, 后面的字符忽略
                    g[word0[j]].add(word1[j])
                    break
            return g
        
        def count_in_degree(g):
            degree = {}
            # 将出现字符的入度初始化为0
            for word in words:
                for ch in word:  
                    degree[ch] = 0
            
            for char, charset in g.items():
                for ch in charset:
                    degree[ch] += 1
            return degree
        
        g = init_graph()
        if g is None:
            return ""
        in_degree = count_in_degree(g)
        
        queue, count = deque(), 0
        for char, degree in in_degree.items():
            count += 1
            if degree == 0:
                queue.append(char)
            
        order = ""
        while queue:
            ch = queue.popleft()
            order += ch
            
            if ch in g:
                for c in g[ch]:
                    in_degree[c] -= 1
                    if in_degree[c] == 0:
                        queue.append(c)
        return order if len(order) == count else ""