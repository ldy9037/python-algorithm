# Summer/Winter Coding - 지형 이동
# MST는 자주 안짜봐서 코드가 조금 지저분한 것 같음. 
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
            heapq.heappush(heap,(abs(c_cost - land[x - 1][y]), (x,y), (x - 1, y)))
        if y > 0 and not visited[x][y - 1]: 
            heapq.heappush(heap,(abs(c_cost - land[x][y - 1]), (x,y), (x, y - 1)))
        if x < len(land) - 1 and not visited[x + 1][y]:
            heapq.heappush(heap,(abs(c_cost - land[x + 1][y]), (x,y), (x + 1, y)))
        if y < len(land) - 1 and not visited[x][y + 1]:
            heapq.heappush(heap,(abs(c_cost - land[x][y + 1]), (x,y), (x, y + 1)))

        cost, start, end = heapq.heappop(heap)
        
        x, y = end
        while visited[x][y]:
            cost, start, end = heapq.heappop(heap)
            x, y = end
        
        answer = answer + cost if cost > height else answer
        current = end
    
    return answer

land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3

print(solution(land, height))