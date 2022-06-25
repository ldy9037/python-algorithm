# 월간 코드 챌린지 - 괄호 회전하기
# 괄호를 회전시키면서 완벽환 괄호가 되는지 확인하고 완벽한 괄호가 될 경우 부분괄호의 개수(answer)를 구함
from collections import deque

def solution(s):
    queue = deque(s)
    sub_group = []
    
    sorted = False

    for i in range(len(s)):
        if sorted: break
        
        sub_group = []
        stack = []

        for k in range(len(s)):
            bracket = queue[k]
            if stack:
                check = ord(bracket) - ord(stack[-1]) 
                
                if check == 1 or check == 2 : stack.pop()
                else: stack.append(bracket)
            else:
                if k != 0: sub_group.append(i)
                stack.append(bracket)

        if not stack: 
            sorted = True
            sub_group.append(k)
        else: queue.append(queue.popleft())

        answer = len(sub_group) if sorted else 0

    return answer

s ="))("
print(solution(s))
"""
()(
(
{{{{{{
"""
