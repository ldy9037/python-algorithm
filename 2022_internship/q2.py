# 카카오 인턴십 - 2번
from collections import deque

def solution(queue1, queue2):
    answer = 0
    q_sum = {"queue1": sum(queue1), "queue2": sum(queue2)}
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while q_sum["queue1"] != q_sum["queue2"]:
        if answer == len(queue1) + len(queue2):
            answer = -1
            break
        
        if q_sum["queue1"] > q_sum["queue2"]: 
            current = queue1.popleft() 
            queue2.append(current)
            q_sum["queue1"] -= current
            q_sum["queue2"] += current
        else: 
            current = queue2.popleft()
            queue1.append(current)
            q_sum["queue2"] -= current
            q_sum["queue1"] += current
        answer += 1

    return answer

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))