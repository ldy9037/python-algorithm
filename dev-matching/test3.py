def check_push(table, stack, visited, x, y):
    # 해당 지점이 물이고 방문한적이 없다면 방문 예약(push)
    if table[x][y] == 0 and not visited[x][y]: 
        # 방문 처리 (중복 방문 예약을 방지하기 위해 미리 방문 처리)
        visited[x][y] = True
        stack.append((x, y))
    
    return stack

def solution(rows, columns, lands):
    answer = []

    # DFS로 넓이를 구할 것이기 때문에 중복방문을 피하기 위해 해당 지점을 방문했는지 체크
    visited = [] * (rows)
    # 배열 주소 참조를 방지하기 위해 loop로 2차원 배열 생성
    for i in range(rows):
        visited.append([False] * (columns))

    # rows * columns 크기의 table을 생성
    # 배열 주소 참조를 방지하기 위해 loop로 2차원 배열 생성
    table = [] * rows
    for i in range(rows): table.append([0] * columns)
    # table(지도)상에 땅인 부분 1로 표시
    for x,y in lands: table[x - 1][y - 1] = 1

    # 지도의 처음 부터 탐색 시작 
    # 지도의 테두리는 바다로 구성되어 있기 때문에 테두리는 제외하고 탐색
    for i in range(rows - 2): 
        for k in range(columns - 2):
            # 이미 방문한 적이 있는 지점이거나 해당 지점이 땅일 경우는 그냥 다음 지점으로 넘어감
            if visited[i + 1][k + 1] or table[i + 1][k + 1] == 1: continue

            # 위 조건에 해당하지 않는 다면 DFS 시작 (해당 지점이 물이고 첫 방문)
            # DFS를 위해 stack 생성
            stack = []
            # 해당 지점부터 시작
            stack.append((i + 1, k + 1))
            
            # 탐색할 호수 넓이 초기화
            area = 0
            # 지금 DFS로 탐색하고 있는 영역이 호수인지 여부를 담고 있는 변수 선언
            isLake = True
            while stack: 
                # 지점 방문 (row, col)
                x, y = stack.pop()
                # 방문했음을 표시
                visited[x][y] = True
                # 호수 넓이 + 1
                area += 1

                # 호수가 테두리와 맞닿아 있다면 
                if x == 0 or y == 0 or x == rows - 1 or y == columns - 1: 
                    # 이 영역은 호수가 아님 (바다임)
                    isLake = False
                else: 
                    # 해당 지점을 기준으로 동서남북 체크 후 방문 예약
                    stack = check_push(table, stack, visited, x + 1, y)
                    stack = check_push(table, stack, visited, x, y + 1)
                    stack = check_push(table, stack, visited, x - 1, y)
                    stack = check_push(table, stack, visited, x, y - 1)

            # 탐색 결과 이 영역이 호수라면 넓이를 저장            
            if isLake: answer.append(area)    
    
    # 저장된 넓이가 존재하면 최소/최대값 return 만약에 저장된 넓이가 없다면 최소/최대 모두 -1로 return
    return [min(answer), max(answer)] if answer else [-1, -1]

rows = 5
columns = 7
lands = [[2,5],[3,3],[3,4],[3,5],[4,3]]

print(solution(rows, columns, lands))