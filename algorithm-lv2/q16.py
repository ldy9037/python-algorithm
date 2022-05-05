# DFS/BFS - 타겟 넘버
# DFS 사용
from collections import deque


def solution(numbers, target):
    answer = 0
    
    numbers.insert(0, 0)
    stack = [(-1,0)]

    while stack:
        parent, vertex = stack.pop()   

        if parent + 2 == len(numbers):
            if vertex == target :
                answer += 1
            continue
        
        stack.append((parent + 1, vertex - numbers[parent + 2]))
        stack.append((parent + 1, vertex + numbers[parent + 2]))

    return answer

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))

"""
다른 사람들의 풀이를 보니 재밌는 풀이가 많았음.
- 재귀로 target을 줄여나가는 방식
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

- product(데카르트의 곱)을 사용해 심플하게 구현. 순열 관련된 함수는 기억해두면 쓸모가 많을 듯?
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
"""