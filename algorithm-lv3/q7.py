# 동적계획법 - 등굣길
# 1000000007 나머지 구하는 문제인 걸 감빡해서 오래걸림. 문제 잘읽자 ㅜ
def solution(m, n, puddles):
    answer = 0
    map = [[0] * m for i in range(n)]

    for i in range(n):
        for k in range(m):
            if [k + 1,i + 1] in puddles: 
                if i == 0: break
                continue
            if i == 0: 
                map[i][k] = 1
                continue
            
            map[i][k] = map[i][k - 1] + map[i - 1][k]
        
    answer = map[-1][-1] % 1000000007
    return answer

m = 4
n = 3
puddles = [[3,1],[2,3], [1,2]]

print(solution(m, n, puddles))