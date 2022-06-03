# 월간 코드 챌린지 - 3진법 뒤집기
# int 함수에 두번째 인자로 현재 진수 n을 넣으면 첫번째 인자로 넣은 값을 10진수로 변환해줌 ex) int(number, n)
from collections import deque

def solution(n):
    answer = 0

    queue = deque()
    while n >= 3:
        n, r = divmod(n, 3)
        queue.append(r)

    if n != 0: queue.append(n)

    while queue:
        num = queue.popleft()
        answer += num * (3 ** len(queue))        

    return answer

n = 45
print(solution(n))