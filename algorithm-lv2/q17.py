# 스킬 체크 - level2
# 스킬 체크, 그냥 DFS로 풀었는데 효율성에서 걸림. BFS + 이진 탐색으로 돌리면 쉽게 될 것 같음.
# 문제푸는 속도가 조금 느린듯 함
def solution(maps):
    answer = -1

    stack = [([], (0,0))]

    while stack:
        history, current = stack.pop() 
        
        prev_location = history[-1] if len(history) > 0 else (0,0)
        
        history = history + [current]
    
        if current == (len(maps) - 1, len(maps[0]) - 1) and (answer > len(history) or answer == -1) : 
            answer = len(history)

        arrow = {"e": (current[0], current[1] + 1), "w": (current[0], current[1] - 1), "s": (current[0] + 1, current[1]), "n": (current[0] - 1, current[1]) }
        
        for k, v in arrow.items():
            y, x = v
            if y >= 0 and y < len(maps) and x >= 0 and x < len(maps[0]):
                if not prev_location == (y, x) and maps[y][x] and not (y, x) in history: 
                    stack.append((history, (y, x)))

    

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))