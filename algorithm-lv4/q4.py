# 프로그래밍 마에스터 - 사칙연산
def cal(a, b, operator):
    return a + b if operator == "+" else a - b

def solution(arr):
    answer = []

    stack = [("+", 0, int(arr[0]))]
    
    while stack:
        operator, i, sum = stack.pop()
        
        if i == len(arr) - 1:
            answer.append(sum)
            continue

        stack.append((arr[i + 1], i + 2, cal(sum, int(arr[i + 2]), arr[i + 1])))
        if operator == "-": 
            n_operator = "+" if operator == "-" else "-"
            stack.append((n_operator, i + 2, cal(sum, int(arr[i + 2]), n_operator)))

    return max(answer)

arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]	
print(solution(arr))