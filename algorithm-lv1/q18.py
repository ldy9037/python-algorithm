# 월간 코드 챌린지 - 약수의 개수와 덧셈
# 제곱수를 소인수 분해하면 모든 지수는 짝수가되는 성질이 있음. 이 성질을 이용하면 제곱수의 경우 약수의 개수가 홀수임을 확인 가능함. 아래는 소인수 분해를 직접함.
from collections import Counter

def solution(left, right):
    answer = 0

    for current in range(left, right + 1):
        sm_list = []
        sm = 2

        temp = current
        while temp > 1:
            s, r = divmod(temp, sm)

            if r == 0: 
                sm_list.append(sm)
                temp = s
            else: sm += 1
        
        cnt = 1

        for k, v in dict(Counter(sm_list)).items():
            cnt *= (v + 1)    
         
        answer = answer + current if cnt % 2 == 0 else answer - current    

    return answer

left = 13
right = 17

print(solution(left, right))