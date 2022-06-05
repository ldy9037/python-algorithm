# 월간 코드 챌린지 - 두 개 뽑아서 더하기
from itertools import combinations

def solution(numbers):
    answer = set()
    
    for x, y in combinations(numbers, 2): answer.add(x + y)
    
    return sorted(list(answer))

numbers = [2,1,3,4,1]

print(solution(numbers))