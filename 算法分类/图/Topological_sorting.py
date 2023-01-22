from typing import List
from Graph import Graph

class Solution_Kahn:
    
    def sort(self, graph: Graph):
        queue = []
        
        for key, value in graph.inDegree.items():
            if value == 0:
                queue.append(graph.vertlist[key])
        
        while queue:
            item = queue.pop(0)
            
            print(item.id + " => ")
            
            for child in item.connect:
                graph.inDegree[child] -= 1
                
                if graph.inDegree[child] == 0:
                    queue.append[child]
    
    
graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_edge("b", "a", 10)
graph.add_edge("a", "c", 12)
graph.add_edge("b", "c", 15)
graph.buildInDegree()

solution = Solution_Kahn()
result = solution.sort(graph)