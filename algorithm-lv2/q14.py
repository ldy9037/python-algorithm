# 탐욕법 - 구명보트
# 특이사항 없음
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))

    while people:
        answer += 1
        now_weight = people.popleft()
        while people and now_weight + people[-1] <= limit:
             now_weight += people.pop()
        
    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))