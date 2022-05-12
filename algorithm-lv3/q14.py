# 그래프 - 순위
def solution(n, results):
    answer = 0

    table = [[0 for _ in range(n)] for _ in range(n)]

    for winner, loser in results:
        table[winner - 1][loser - 1] = 1
        table[loser - 1][winner - 1] = -1 

    for i in range(n):
        for k in range(n):
            for j in range(n):
                if table[k][i] == 1 and table[i][j] == 1 : 
                    table[k][j] = 1
                    table[j][k] = -1

    for row in table:
        if row.count(0) == 1: answer += 1

    return answer

n = 5
results = [[1, 2], [4, 5], [3, 4], [2, 3]]

print(solution(n, results))