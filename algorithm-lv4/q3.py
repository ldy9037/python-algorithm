# Summer/Winter Coding - 지형 이동

import heapq

def solution(land, height):
    answer = 0

    visited = []
    for i in range(len(land)):
        visited.append([False] * len(land))

    heap = []
    heapq.heapify(heap)
    
    current = (0, 0)
    for i in range(len(land) ** 2 - 1):
        x, y = current 
        visited[x][y] = True

        c_cost = land[x][y]

        if x > 0 and not visited[x - 1][y]: 
            heapq.heappush(heap,(abs(c_cost - land[x - 1][y]), (x - 1, y)))
        if y > 0 and not visited[x][y - 1]: 
            heapq.heappush(heap,(abs(c_cost - land[x][y - 1]), (x, y - 1)))
        if x < len(land) - 1 and not visited[x + 1][y]:
            heapq.heappush(heap,(abs(c_cost - land[x + 1][y]), (x + 1, y)))
        if y < len(land) - 1 and not visited[x][y + 1]:
            heapq.heappush(heap,(abs(c_cost - land[x][y + 1]), (x, y + 1)))

        cost, next = heapq.heappop(heap)
        
        x, y = next
        while visited[x][y]:
            cost, next = heapq.heappop(heap)
            x, y = next
        
        answer = answer + cost if cost > height else answer
        current = next
    
    return answer

land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3

print(solution(land, height))