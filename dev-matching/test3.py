def check_push(table, stack, visited, x, y):
    if table[x][y] == 0 and not visited[x][y]: 
        visited[x][y] = True
        stack.append((x, y))
    
    return stack

def solution(rows, columns, lands):
    answer = []

    visited = [] * (rows)
    for i in range(rows):
        visited.append([False] * (columns))

    table = [] * rows
    for i in range(rows): table.append([0] * columns)
    for x,y in lands: table[x - 1][y - 1] = 1

    for i in range(rows - 2): 
        for k in range(columns - 2):
            if visited[i + 1][k + 1] or table[i + 1][k + 1] == 1: continue

            stack = []
            stack.append((i + 1, k + 1))
            
            area = 0
            isLake = True
            while stack: 
                x, y = stack.pop()
                visited[x][y] = True
                area += 1

                if x == 0 or y == 0 or x == rows - 1 or y == columns - 1: 
                    isLake = False
                else: 
                    stack = check_push(table, stack, visited, x + 1, y)
                    stack = check_push(table, stack, visited, x, y + 1)
                    stack = check_push(table, stack, visited, x - 1, y)
                    stack = check_push(table, stack, visited, x, y - 1)
            
            if isLake: answer.append(area)    

    return [min(answer), max(answer)] if answer else [-1, -1]

rows = 5
columns = 7
lands = [[2,5],[3,3],[3,4],[3,5],[4,3]]

print(solution(rows, columns, lands))