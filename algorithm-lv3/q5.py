# 동적계획법 - N으로 표현
import math

def minimum_sum(prev_calculation):
    result = 0

    for i in range(math.ceil(len(prev_calculation))):
        case = prev_calculation[i] + prev_calculation[-1-i]
        if case < result or result == 0 : result = case

    return result
    

def solution(N, number):
    answer = 0
    calculation = [0] * 32000
    
    if N == 1: return number

    calculation[0] = 2
    calculation[1] = 3
    calculation[N - 1] = 1

    for i in range(1, 32000):
        """
        quotient, remainder = divmod(i + 1, N)
        if remainder == 0: 
            calculation[i] = quotient
            continue
        """
        count_sum = calculation[i - 1] + calculation[i]
        print(calculation)
        calculation[(i - 1) + i] = calculation[i - 1] + calculation[i] if calculation[(i - 1) + i] != 0 and calculation[(i - 1) + i] > calculation[i - 1] + calculation[i] else calculation[(i - 1) + i]
         
        calculation[i] = minimum_sum(calculation[:i]) 
    
    print(calculation)

    return answer

N = 5
number = 12
print(solution(N, number))
