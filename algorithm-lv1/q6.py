# 카카오 - 실패율
# 속도가 굉장히 느림. 22번 기준 4551.61ms 나옴 / 효율성을 생각해서 다시 짜봐야겠음. 아마 count때문에 시간복잡도가 O(n^2)가 돼서 그런 듯 함. 

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