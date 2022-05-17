# 찾아라 프로그래밍 마에스터 - 게임 맵 최단거리
# 그냥 DFS로 풀었는데 효율성에서 걸림. BFS + 이진 탐색으로 돌리면 쉽게 될 것 같음.
# 문제푸는 속도가 조금 느린듯 함
# 생각해보니 같은 곳을 이전에 방문 여부를 history로 체크하면 중복 방문 하는 경우가 생겨 성능에 문제가 생김
# 그 대신 방향에 우선 순위를 정한 후 이전에 지난 길은 벽으로 막음 (하단/우측 우선)
# 그런데 이것을 DFS로 하면 특정상황에서 너무 성능이 안좋을 것 같음. (하단 진입 후 좌측/상단 길만 존재할 경우)
# BFS로 다시 구현해보겠음.
def solution(maps):
    answer = -1

    stack = [([], (0,0))]

    while stack:
        history, current = stack.pop() 
    
        history = history + [current]
    
    
        if current == (len(maps) - 1, len(maps[0]) - 1) and (answer > len(history) or answer == -1) : 
            answer = len(history)

        arrow = {"w": (current[0], current[1] - 1), "n": (current[0] - 1, current[1]), "e": (current[0], current[1] + 1), "s": (current[0] + 1, current[1]) }
        
        for k, v in arrow.items():
            y, x = v
            if y >= 0 and y < len(maps) and x >= 0 and x < len(maps[0]) and maps[y][x]:
                maps[y][x] = 0
                stack.append((history, (y, x)))

    return answer

maps = [[1,1,1,1,1],[0,0,1,0,1],[1,1,1,0,1],[1,0,1,0,1],[1,1,1,0,1]]
print(solution(maps))