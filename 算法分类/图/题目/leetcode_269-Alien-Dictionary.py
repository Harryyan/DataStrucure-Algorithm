from collections import defaultdict
from typing import List

# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language.
#  If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.


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
