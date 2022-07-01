# 팁스타운 - 단어 퍼즐
"""
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

from collections import defaultdict
from collections import deque

def solution(strs, t):
    answer = 0

    min_dict = defaultdict(int)
    for str in strs: min_dict[str] = 1

    t = deque(t)

    minimum = float("inf")
    string = ""
    while t:
        string += t.popleft()
        
        if len(string) <= 5 and string in min_dict: 
            min_dict[string] = 1
            continue
        
        b = ""
        for i in range(5):
            if string == "": break
            b = string.pop() + b

            if min_dict[string] == 0 or min_dict[b] == 0: continue

            cnt = min_dict[string] + min_dict[b] 
            if minimum == float("inf"): minimum = cnt
            if min_dict[string] == 0 or cnt < min_dict[string] :
                min_dict[string] = cnt 
            if cnt == 1 and cnt <= minimum: break

        string += b
        if not string in min_dict: min_dict[string] = 0

    answer = min_dict[string] if min_dict[string] != 0 else -1
            
    return answer
"""
from collections import deque

def solution(strs, t):
    answer = [float("inf")] * len(t)   

    string = ""
    for i in range(len(t)):
        string += t[i]
     
        for k in range(1,6):
            b = string[-k:]
            
            if b in strs:
                if b == string: 
                    answer[i] = 1
                    break
            
                answer[i] = min(answer[i], answer[i - (len(b))] + 1)
            
            if b == string: break
    
    answer = answer[-1] if answer[-1] != float("inf") else -1

    return answer



strs = 	["ab", "na", "n", "a", "bn"]
t = "nabnabn"	

print(solution(strs, t))