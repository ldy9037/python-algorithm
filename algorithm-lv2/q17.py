# 찾아라 프로그래밍 마에스터 - 게임 맵 최단거리
from collections import deque

def solution(maps):
    answer = -1

    queue = deque()
    queue.append(([], (0,0)))

    while queue:
        history, current = queue.popleft()    
        history = history + [current]

        if current == (len(maps) - 1, len(maps[0]) - 1) and (answer > len(history) or answer == -1) : 
            answer = len(history)
            break
        
        arrow = {"w": (current[0], current[1] - 1), "n": (current[0] - 1, current[1]), "e": (current[0], current[1] + 1), "s": (current[0] + 1, current[1]) }

        for k, v in arrow.items():
            y, x = v
            if y >= 0 and y < len(maps) and x >= 0 and x < len(maps[0]) and maps[y][x]:
                maps[y][x] = 0
                queue.append((history, (y, x)))
    
    return answer

maps = [[1,1,1,1,1],[0,0,1,0,1],[1,1,1,0,1],[1,0,1,0,1],[1,1,1,0,1]]
print(solution(maps))