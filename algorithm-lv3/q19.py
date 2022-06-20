# 카카오 인턴십 - 보석쇼핑

"""
from collections import deque

def solution(gems):
    answer = []

    current = [1, 1]
    kinds_count = len(set(gems))
    bucket = deque()
    length = 0

    for gem in gems: 
        if not gem in bucket: length += 1
        bucket.append(gem)

        if len(bucket) > 1:
            e = bucket.popleft()

            while length == len(set(bucket)): 
                current[0] += 1 
                e = bucket.popleft()

            bucket.appendleft(e)

        if length == kinds_count: 
            answer.append(current.copy())
        current[1] += 1

    answer.sort(key=lambda x: x[1] - x[0])
    
    return answer[0]
"""
from collections import deque

def check(gems, middle, kind_count):
    result = [0, 0]

    queue = deque()
    queue.extend(gems[:middle])

    result = [0, 0]
    r = gems[middle:]
    for i in range(len(r) + 1):
        if len(set(queue)) == kind_count: 
            result = [i + 1, i + middle] 
            break
        
        if len(r) == i: break

        queue.popleft()
        queue.append(r[i])

    return result

def solution(gems):
    answer = []
    kind_count = len(set(gems))
    left = kind_count
    right = len(gems)

    while left < right:
        middle = (left + right) // 2
        
        answer = check(gems, middle, kind_count)

        if answer[0] == 0: left = middle + 1
        else: right = middle

    answer = check(gems, left, kind_count)

    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(gems))