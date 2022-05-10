# 그래프 - 가장 먼 노드
import heapq

def solution(n, edge_list):
    answer = 0
    
    distances = [float("inf")] * n
    distances[0] = 0

    visited = [False] * n

    adjacent_list = [[] for _ in range(n)]
    for s, d in edge_list: 
        adjacent_list[s - 1].append((1, d - 1))
        adjacent_list[d - 1].append((1, s - 1))
    
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        distance, current = heapq.heappop(heap)
        visited[current] = True
        
        if distance > distances[current]: continue

        for next_distance, destination in adjacent_list[current]:
            if visited[destination]: continue

            total_distance = next_distance + distance
            if distances[destination] > total_distance:
                distances[destination] = total_distance

                heapq.heappush(heap,(total_distance, destination))
        
    maxium = max(distances)
    answer = distances.count(maxium)

    return answer

n = 6
edge_list = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	

print(solution(n, edge_list))