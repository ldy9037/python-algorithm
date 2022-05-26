# 2017 팁스타운 - 짝지어 제거하기
def solution(s):
    answer = 1
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]: stack.pop()
        else: stack.append(s[i])

    if stack: answer = 0
    return answer

s = "baabaa"
print(solution(s))