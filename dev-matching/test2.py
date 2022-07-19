from collections import deque
def solution(n, horizontal):
    
    answer = [] * n
    # 배열 주소 참조 방지하기 위해 loop로 2차원 배열 생성
    for i in range(n): answer.append([0] * n)

    # 시작은 [0][0]으로 고정
    answer[0][0] = 1

    # BFS를 적용하기 위해 queue 생성
    queue = deque()

    # horizontal이라면 오른쪽으로 시작 아니라면 아래로 시작
    if horizontal:queue.append((0, 1, True))
    else: queue.append((1, 0, True))    
    
    # BFS에서 현재 순서를 체크하기 위해 order 변수 생성
    order = 1
    while queue:
        order += 1
        # 큐에서 BFS 다음 정점을 꺼냄(방문), 정점 정보는 (row, col, 끝에 있는 정점인지)
        x, y, end = queue.popleft()

        # 만약 좌표가 배열을 벗어났다면 중지
        if x >= n or y >= n: break
        
        # 현재 좌표에 순번 지정
        answer[x][y] = order
        
        # 만약 현재 정점이 끝에 있는 정점이라면 (방향전환 하는 부분이라면)
        if end:
            # 방향 전환 후 시작 좌표 초기화
            n_x = 0
            n_y = 0

            # 현재 정점이 위에 존재한다면(다음 방향은 아래)
            if x == 0:  

                # 다음 시작 좌표의 col은 현재 col (아래로 이동하므로)            
                n_y = y 

                # 다음 끝점까지는 현재 col의 두배 만큼 이동해야함
                for i in range(y * 2):
                    # row를 한칸 씩 늘리면서 방문 예약(Enqueue)
                    if n_x < y: 
                        n_x += 1
                        queue.append((n_x, y, False))
                    # 한칸씩 늘리다가 row와 col이 같아지는 시점에서부터 col을 한칸씩 줄여가면서 방문 예약
                    else: 
                        n_y -= 1
                        queue.append((n_x ,n_y, False))
                # 해당 라인을 전부 방문 예약 했으므로 다음 라인으로 이동(방문) 예약 (아래로 이동/ 방향전환 준비)
                queue.append((n_x + 1 ,n_y, True))
                        
            # 현재 정점이 왼쪽에 존재한다면 (다음 방향을 오른쪽)
            if y == 0: 

                # 다음 시작 좌표의 row는 현재 row (오른쪽으로 이동하므로)            
                n_x = x

                # 마찬가지로 다음 끝점까지 이동횟수는 현재 row의 두배
                for i in range(x * 2): 
                    # col을 한칸 씩 늘리면서 방문 예약(Enqueue)
                    if n_y < x:
                        n_y += 1
                        queue.append((x, n_y, False))
                    # 한칸씩 늘리다가 row와 col이 같아지는 시점에서부터 row를 한칸씩 줄여가면서 방문 예약
                    else:
                        n_x -= 1
                        queue.append((n_x, n_y, False))
                # 해당 라인을 전부 방문 예약 했으므로 다음 라인으로 이동(방문) 예약 (오른쪽 이동/ 방향전환 준비)
                queue.append((n_x ,n_y + 1, True))
        
    return answer

n = 4 
horizontal = True

print(solution(n, horizontal))