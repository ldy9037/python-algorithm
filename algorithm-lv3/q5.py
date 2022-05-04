# 동적계획법 - N으로 표현
import math

def arithmetic_operation(prev_list, N):
    result = set()
    result.add(int(str(N) * (len(prev_list) + 1) ))

    for i in range(math.ceil(len(prev_list))):
        for first_calculated_value in prev_list[i]:
            for second_calculated_value in prev_list[-1-i]:
                result.add(first_calculated_value + second_calculated_value)
                result.add(abs(first_calculated_value - second_calculated_value))
                result.add(first_calculated_value * second_calculated_value)
                if first_calculated_value != 0 and second_calculated_value != 0:
                    result.add(first_calculated_value // second_calculated_value)
                    result.add(second_calculated_value // first_calculated_value)
                
    return result

def solution(N, number):
    answer = 1
    calculation = []
    
    for i in range(8):
        calculation.append(arithmetic_operation(calculation[:i], N))
        if number in calculation[-1]: break
        answer += 1

    return answer if answer <= 8 else -1

N = 5
number = 12
print(solution(N, number))
