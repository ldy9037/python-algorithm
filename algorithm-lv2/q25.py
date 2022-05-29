# 카카오 블라인드 - 괄호 변환
from collections import deque

def is_nomal(u):
    stack = []

    for current in u:
        if stack and stack[-1] + current == '()': stack.pop()
        else: stack.append(current)

    return not (stack)

def reverse(u):
    u = u[1:len(u)-1]
    u = list(u)

    for i in range(len(u)):
        u[i] = ")" if u[i] == "(" else "("
    
    return ''.join(u)

def solution(p):
    answer = ''

    u = ''
    v = deque(p) 

    while v:
        u += v.popleft()    
        if u.count("(") == u.count(")"): break

    rem = ''
    if v: rem = solution(v)

    if is_nomal(u): answer = u + rem
    else: 
        answer = "(" + rem + ")" + reverse(u)

    return answer

p = "()))((()"
print(solution(p))
