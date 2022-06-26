# 체스판

def solution(n):
    answer = 0

    for i in range(n):
        stack = []
        
        location = []
        location.append(i)

        stack.append(location.copy())
        while stack:
            history = stack.pop()
            if len(history) == n: answer += 1

            for k in range(n):
                if abs(k - history[-1]) >= 2 and not k in history:
                    is_cross = False

                    for j in range(len(history) - 1):
                        if abs(history[j] - k) == abs(j - len(history)): 
                            is_cross = True
                            break
                    
                    if is_cross: continue
                    n_history = history.copy()
                    n_history.append(k)

                    stack.append(n_history)

    return answer

n = 5
print(solution(n))