def solution(A, B):
    answer = 0
    
    stick = [A, B]
    stick.sort()

    if A + B > 4:
        s = stick[1] // stick[0]     
        if s >= 4: answer = stick[1] // 4
        elif s == 3: answer = stick[0]
        elif s == 2: answer = stick[1] // 3
        else: answer = stick[0] // 2

    return answer 

A = 10
B = 21
print(solution(A,B))