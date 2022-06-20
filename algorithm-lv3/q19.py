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

def solution(gems):
    answer = []
    kind_count = len(set(gems))
    left = kind_count
    right = len(gems)

    while left <= right:
        middle = (left + right) // 2

        queue = deque()
        queue.extend(gems[:middle])

        answer = [-1, -1]
        r = gems[middle:]
        for i in range(len(r)):
            print(len(set(queue)))
            print(kind_count)
            if len(set(queue)) == kind_count: 
                answer = [i, i + middle - 1] 
                break
            
            queue.popleft()
            queue.append(r[i])

        print(answer)

        if answer[0] == -1: 
            left = middle + 1
        else: right = middle

    return answer

gems = ["1", "2", "3", "4", "3", "2", "1","5"]

print(solution(gems))