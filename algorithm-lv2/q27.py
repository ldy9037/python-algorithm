# 카카오 인턴십 - 수식 최대화
# eval이란게 있었음. cal에 적용하면 훨씬 보기 좋아질 듯

from itertools import permutations

def cal(expression, operator, i):
    result = 0
    if expression.isdigit(): result = int(expression)
    else:
        for k ,part in enumerate(expression.split(operator[i])):
            part_result = cal(part, operator, i + 1)

            if k == 0: result = part_result
            else: 
                if operator[i] == "*": result *= part_result
                elif operator[i] == "+": result += part_result
                else: result -= part_result
    
    return result


def solution(expression):
    answer = 0
    result = []

    for case in list(permutations(["*","+","-"], 3)):
        result.append(abs(cal(expression, case, 0)))

    answer = max(result)

    return answer

expression = "100-200*300-500+20"
print(solution(expression))