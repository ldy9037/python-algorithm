# 프로그래밍 마에스터 - 사칙연산
def cal(a, b, operator):
    return a + b if operator == "+" else a - b

"""
def solution(arr):
    answer = []

    stack = [(0, int(arr[0]), False)]

    while stack:
        i, sum, t = stack.pop()

        if i == len(arr) - 1:
            answer.append(sum)
            continue
        
        stack.append((i + 2, cal(sum, int(arr[i + 2]), arr[i + 1]), False))
        
        if arr[i - 1] == "-" or t:    
            n_operator = "+" if arr[i + 1] == "-" else "-"
            stack.append((i + 2, cal(sum, int(arr[i + 2]), n_operator), True))

    return max(answer)
"""
def solution(arr):
    maximum, minimum = 0, 0
    plus = []
    sum_list = []
    while arr:
        e = arr.pop()

        if e == "-":
            sum_list.append(-plus[-1] + sum(plus[:-1]) + maximum)
            sum_list.append(-(sum(plus) + maximum))
            sum_list.append(-sum(plus) + minimum)
            sum_list.append(-(sum(plus) + minimum))

            maximum, minimum = max(sum_list), min(sum_list)
        
            plus.clear()
            sum_list.clear() 
        elif e == "+":
            continue
        else:
            plus.append(int(e))
        
    return maximum + sum(plus)

arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
print(solution(arr))