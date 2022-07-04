# 카카오 블라인드 - 합승 택시 요금
def solution(n, s, a, b, fares):
    answer = []

    d = [] * n
    for i in range(n): d.append([float("inf")] * n)
    for i in range(n): d[i][i] = 0
    for source, destination, f in fares: 
        d[source - 1][destination - 1] = f
        d[destination - 1][source - 1] = f

    for i in range(n):
        for k in range(n):
            for j in range(n):
                if d[k][i] + d[i][j] < d[k][j]: d[k][j] = d[k][i] + d[i][j]                
    
    for i in range(n): 
        answer.append(d[s - 1][i] + d[i][a - 1] + d[i][b - 1])

    return min(answer)
n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], 
        [3, 5, 24], 
        [5, 6, 2], 
        [3, 1, 41], 
        [5, 1, 24], 
        [4, 6, 50], 
        [2, 4, 66], 
        [2, 3, 22], 
        [1, 6, 25]]

print(solution(n, s, a, b, fares))