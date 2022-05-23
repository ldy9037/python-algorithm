# 월간 코드 챌린지 - 내적
def solution(a, b):
    answer = 0
    
    for f, s in zip(a,b):
        answer += f * s

    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]

print(solution(a,b))