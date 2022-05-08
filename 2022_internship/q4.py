# 카카오 인턴십 - 4번

import heapq


def solution(n, paths, gates, summits):
    answer = []
    last_maxium = []

    left = 1
    right = 10000000
    
    graph = [[] for _ in range(n)]

    for s, d, time in paths:
        graph[s - 1].append((d - 1, time))
        graph[d - 1].append((s - 1, time))
    
    while left <= right:
        middle = (left + right) // 2          

        maxium = []

        for gate in gates: 
            other_gates = gates.copy()
            other_gates.remove(gate)
            gate -= 1
            times = [float("inf")] * n
            visited = [False]* n
            times[gate] = 0

            heap = []
            heapq.heappush(heap, (0, gate, []))
            
            while heap:
                time, current, history = heapq.heappop(heap)
                visited[current] = True
                if (current + 1) in summits: 
                    
                    maxium.append((current + 1,max(history)))


                if times[current] < time: continue
                for destination, next_time in graph[current]: 
                    
                    if next_time > middle or (destination + 1) in other_gates or visited[current]: continue
                    total_time = time + next_time
                    
                    if total_time < times[destination]: 
                        history = history + [next_time]
                        times[destination] = total_time
                        heapq.heappush(heap, (total_time, destination, history))
        
        if len(maxium) > 0: 
            last_maxium = maxium
            right = middle -1 
        else: left = middle + 1

    last_maxium.sort()
    
    answer = list(last_maxium[0])
    
    return answer

n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3,7]
summits = [1,5]

print(solution(n, paths, gates, summits))