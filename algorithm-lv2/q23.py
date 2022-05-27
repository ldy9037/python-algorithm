# 2021 dev-matching 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    table = [] * rows

    for k in range(rows):
        row = [columns * k + (i + 1) for i in range(columns)]
        table.append(row)

    for query in queries:
        x1, y1, x2, y2 = tuple(map(lambda n: n - 1  ,query))
        locations = [table[x1][y1], table[x2][y1], table[x1][y2], table[x2][y2]]
        
        for i in range(y2 - y1 - 1): 
            table[x1][y2 - i] = table[x1][y2 - i - 1]
            table[x2][y1 + i] = table[x2][y1 + i + 1]
            locations.extend([table[x1][y2 - i - 1], table[x2][y1 + i + 1]])
        
        for i in range(x2 - x1 - 1): 
            table[x1 + i][y1] = table[x1 + i + 1][y1]
            table[x2 - i][y2] = table[x2 - i - 1][y2]
            locations.extend([table[x1 + i + 1][y1], table[x2 - i - 1][y2]])
        
        table[x1][y1 + 1] = locations[0] 
        table[x2 - 1][y1] = locations[1]
        table[x1 + 1][y2] = locations[2]
        table[x2][y2 - 1] = locations[3]
        
        answer.append(min(locations))

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))
#[8, 10, 25]