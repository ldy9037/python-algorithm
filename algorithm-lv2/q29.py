# 월간 코드 챌린지 - 빛의 경로 사이클
def move(arrow, x, y, limit):
    row_limit, col_limit = limit
    if arrow == "e": y = y + 1 if y < col_limit - 1 else 0
    if arrow == "w": y = y - 1 if y > 0 else col_limit - 1
    if arrow == "n": x = x - 1 if x > 0 else row_limit - 1
    if arrow == "s": x = x + 1 if x < row_limit - 1 else 0

    return (x, y)

def start_location(visited):
    for i in range(len(visited)):
        for k in range(len(visited[i])):
            if not all(visited[i][k]): return (visited[i][k].index(False), i, k)
    
    return False

def cycle(grid, visited, start):
    arrow = ["n", "e", "s", "w"]
    history = [start] # arrow, x, y 0,0,0이면 동쪽으로 가서 x,y에 도착했다는 뜻
        
    while len(history) <= 1 or history[0] != history[-1]:
        p_arrow, row, col = history[-1]        
        
        arrow_index = p_arrow
        if grid[row][col] == "L": arrow_index = p_arrow - 1 if p_arrow > 0 else 3
        if grid[row][col] == "R": arrow_index = p_arrow + 1 if p_arrow < 3 else 0
        
        n_row, n_col = move(arrow[arrow_index], row, col, (len(grid), len(grid[0]))) 

        history.append((arrow_index, n_row, n_col))
        visited[n_row][n_col][arrow_index] = True 

    return (visited, len(history) - 1)

def solution(grid):
    answer = []
    
    visited = []
    for i in range(len(grid)):
        visited.append([])
        for k in range(len(grid[0])):
            visited[i].append([False] * 4)

    for i in range(len(visited)):
        for k in range(len(visited[i])):
            for j in range(4):
                if not visited[i][k][j]: 
                    visited, distance = cycle(grid, visited, (j, i, k))
                    answer.append(distance)

    return sorted(answer)

grid = ["S"]
print(solution(grid))
