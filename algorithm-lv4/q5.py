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
"""
from collections import defaultdict
from collections import deque

def solution(strs, t):
    answer = 0

    min_dict = defaultdict(int)
    for str in strs: min_dict[str] = 1

    t = deque(t)

    string = ""
    while t:
        string += t.popleft()
        
        
        if len(string) <= 5 and string in min_dict: 
            min_dict[string] = 1
            continue
        
        for i in range(6):
            f, b = string[:len(string) - i], string[len(string) - i:]

            if min_dict[f] == 0 or min_dict[b] == 0: continue

            cnt = min_dict[f] + min_dict[b] 
            if min_dict[string] == 0 or cnt < min_dict[string] :
                min_dict[string] = cnt 
            if cnt <= 2: break

        if not string in min_dict: min_dict[string] = 0

    answer = min_dict[string] if min_dict[string] != 0 else -1
            
    return answer


strs = 	["ab", "na", "n", "a", "bn"]
t = "nabnabn"	

print(solution(strs, t))