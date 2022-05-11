# 그래프 - 순위
# 잘못 품.. 접근 자체를 잘못한 것 같음.
from collections import deque

def solution(n, results):
    answer = []

    parents = [[] for _ in range(n)]
    visited = [False] * n
    
    graph = [[] for _ in range(n)]
    for winner, loser in results: graph[winner - 1].append(loser - 1)

    while not all(visited):
        start = visited.index(False)
        
        queue = deque()
        queue.append(start)

        while queue:
            print(queue)
            current = queue.popleft()
            visited[current] = True

            for loser in graph[current]:
                same_parents = set(parents[current]) & set(parents[loser])
                if same_parents: 
                    for parent in same_parents: graph[parent].remove(loser)

                if visited[loser]: continue

                parents[loser].append(current)
                queue.append(loser)

    
    if parents.count([]) >= 2: 
        return len(answer)

    answer = range(n)

    queue = deque()
    queue.append(0)

    remove = False
    while queue:
        current = queue.popleft()
        queue.extend(parents[current])

        if remove: answer.remove(current)
        if len(parents[current]) >= 2: remove = True

    remove = False
    while queue:
        current = queue.popleft()
        queue.extend(graph[current])

        if remove: answer.remove(current)
        if len(parents[current]) >= 2: remove = True

    return len(answer)

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	

print(solution(n, results))