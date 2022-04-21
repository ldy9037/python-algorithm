# 카카오 - 실패율

def solution(N, stages):
    answer = []
    failure_list = dict.fromkeys(range(1, N+1), 0)
    
    for stage in range(1, N + 1): 
        if len(stages) == 0: break
        failure_list[stage] = stages.count(stage)/len(stages)
        stages = [item for item in stages if item != stage]
    
    print(sorted(failure_list, key=lambda x : failure_list[x], reverse=True))

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))