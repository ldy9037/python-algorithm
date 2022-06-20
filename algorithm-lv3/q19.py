# 카카오 인턴십 - 보석쇼핑
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

gems = ["1", "2", "3", "4", "3", "2", "1","5"]

print(solution(gems))