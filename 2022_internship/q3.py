# 카카오 인턴십 - 코딩 테스트 공부

def solution(alp: int, cop: int, problems: list):
    answer = 0
 
    alp_max = max(problems, key = lambda problem: problem[0])[0]
    cop_max = max(problems, key = lambda problem: problem[1])[1]

    table = []
    for i in range(alp_max + 1):
        table.append([0] * (cop_max + 1))

        for k in range(cop_max + 1):
            a_time = 0 if alp >= i else i - alp 
            c_time = 0 if cop >= k else k - cop 
            table[i][k] = a_time + c_time

    for problem in problems:    
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem

        for i in range(alp_max + 1):
            next_alp = i + alp_rwd if i + alp_rwd <= alp_max else alp_max

            for k in range(cop_max + 1):
                if alp_req > i or cop_req > k: continue

                next_cop = k + cop_rwd if k + cop_rwd <= cop_max else cop_max
            
                if table[next_alp][next_cop] > table[i][k] + cost:
                    table[next_alp][next_cop] = table[i][k] + cost

    answer = table[alp_max][cop_max]

    return answer

alp = 0
cop = 0
#problems = 	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
problems = [[0,0,30,30,1], [5,5,1,1,10]]
print(solution(alp, cop, problems))
#13