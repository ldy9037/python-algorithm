# 월간 코드 챌린지 - 괄호 회전하기
from collections import deque

def solution(s):
    queue = deque(s)
    sub_group = []
    
    sorted = False

    for i in range(len(s)):
        if sorted: break
        
        index = 0
        sub_group = []
        stack = []

        for k in range(len(s)):
            bracket = queue[k]
            if stack:
                check = ord(bracket) - ord(stack[-1]) 
                
                if check == 1 or check == 2 : stack.pop()
                else: stack.append(bracket)
            else:
                if k != 0: sub_group.append(index)
                stack.append(bracket)

            index += 1

        if not stack: 
            sorted = True
            sub_group.append(k)
        else: queue.append(queue.popleft())

    return len(sub_group)

s = "({{}}())"
print(solution(s))