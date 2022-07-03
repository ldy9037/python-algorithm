from collections import deque
def solution(n, horizontal):
    answer = [] * n
    for i in range(n): answer.append([0] * n)

    answer[0][0] = 1

    queue = deque()
    if horizontal:queue.append((0, 1, True))
    else: queue.append((1, 0, True))    
    
    order = 1
    while queue:
        order += 1
        x, y, end = queue.popleft()

        if x >= n or y >= n: break
        
        answer[x][y] = order
        
        if end:
            n_x = 0
            n_y = 0

            if x == 0:              
                n_y = y
                for i in range(y * 2):
                    if n_x < y: 
                        n_x += 1
                        queue.append((n_x, y, False))
                    else: 
                        n_y -= 1
                        queue.append((n_x ,n_y, False))
                
                queue.append((n_x + 1 ,n_y, True))
                        
            if y == 0: 
                n_x = x
                for i in range(x * 2): 
                    if n_y < x:
                        n_y += 1
                        queue.append((x, n_y, False))
                    else:
                        n_x -= 1
                        queue.append((n_x, n_y, False))
                
                queue.append((n_x ,n_y + 1, True))
        
    return answer

n = 4 
horizontal = True

print(solution(n, horizontal))