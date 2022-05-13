# 그래프 - 방의 개수
from collections import defaultdict

def solution(arrows):
    answer = 0

    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    graph = defaultdict(list)

    current = (0, 0)
    for arrow in arrows:
        for i in range(2):

            x, y = current
            next_vertex = (x + move[arrow][0], y + move[arrow][1])
            if not arrow in graph[current]: 
                graph[current].append(arrow)          

                if graph[next_vertex]: 
                    answer += 1

                opposite_arrow = arrow + 4 if arrow < 4 else arrow - 4
                graph[next_vertex].append(opposite_arrow)

            current = next_vertex

    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))
#3