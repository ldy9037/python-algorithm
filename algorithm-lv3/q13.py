# 그래프 - 순위
# 그래프 정렬(순위대로) 후 위에서 부터 순위확정이 가능 한 노드를 세는 방식으로 풀었으나 시간 초과됨 ㅋㅋ
from collections import deque

def solution(n, results):
    answer = 0

    parents = [[] for _ in range(n)]
    visited = [False] * n
    
    graph = [[] for _ in range(n)]
    for winner, loser in results: 
        graph[winner - 1].append(loser - 1)
        parents[loser - 1].append(winner - 1)
    
    queue = deque()
    queue.append(0)

    while queue:
        current = queue.popleft()
        visited[current] = True

        for winner in parents[current]: queue.append(winner)
        for loser in graph[current]:
            same_parents = set(parents[current]) & set(parents[loser])
            if same_parents: 
                for parent in same_parents:
                    graph[parent].remove(loser)
                    parents[loser].remove(parent)

            if visited[loser]: continue

            queue.append(loser)
    
    if not all(visited): return answer
    
    start = parents.index([])

    queue.clear()
    queue.append(start)

    while queue: 
        current = queue.popleft()
        answer += 1

        if len(parents[current]) >= 2: answer = 1
        if len(graph[current]) >= 2: break

        queue.extend(graph[current])
        
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	

print(solution(n, results))