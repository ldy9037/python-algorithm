# 위클리 챌린지 - 피로도
from collections import deque

def next(k, cnt, dungeons):
    result = []

    for i in range(len(dungeons)): 
        n_dungeons = dungeons.copy()
        n_dungeons.remove(dungeons[i])
        result.append((dungeons[i], n_dungeons, cnt, k))
    
    return result


def solution(k, dungeons):
    answer = []
    
    dungeons.sort()
    minimum = dungeons[0][0]

    queue = deque(next(k, 1, dungeons))


    while queue:
        c_dungeons ,r_dungeons, cnt, r_k = queue.popleft()
        
        if r_k >= c_dungeons[0]: 
            r_k -= c_dungeons[1]
        else: r_dungeons.append(c_dungeons)
        
        
        print(c_dungeons,r_dungeons)

        if r_k < minimum or len(dungeons) == cnt: 
            answer.append(len(dungeons) - len(r_dungeons))
            continue
        
        queue.extend(next(r_k, cnt + 1, r_dungeons))
    print(answer)    
    return max(answer)

k = 40
dungeons = [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]
print(solution(k, dungeons))
#4