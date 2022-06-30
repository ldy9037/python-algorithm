# 팁스타운 - 단어 퍼즐
from collections import deque

def solution(strs, t):
    answer = 0

    result = []
    stack = [(0, "", deque(t))]

    while stack:
        cnt, history, rem = stack.pop()

        string = ""
        while rem:
            string += rem.popleft()

            if string in strs: 
                stack.append((cnt + 1, history + string, rem.copy())) 

        if not rem and history == t: result.append(cnt)

    answer = min(result) if result else -1
    return answer

strs = ["ba","na","n","a"]
t = "banana"	

print(solution(strs, t))