# 单源最短路径

class Dijkstra:
    def startwith(self, start: int, matrix: list) -> list:
        '''
        单源最短路径实现

        Args:
            start: 起点
            matrix： 邻接矩阵，表示点和点之间的距离
        '''
        visited = [start]
        non_visited = [x for x in range(len(matrix)) if x != start]
        
        shortest_dis= matrix[start]
        
        while non_visited:
            idx = non_visited[0]

            for i in non_visited:
                if shortest_dis[i] < shortest_dis[idx]: idx = i

            non_visited.remove(idx)
            visited.append(idx)

            for i in non_visited:
                dis = shortest_dis[idx] + matrix[idx][i]

                if dis < shortest_dis[i]: shortest_dis[i] = dis

        return shortest_dis 

inf = 996
matrix = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf ,inf, 0, 4],
              [inf, inf, inf, inf ,inf, 0]]

s = Dijkstra()

r = s.startwith(0, matrix)
print(r)