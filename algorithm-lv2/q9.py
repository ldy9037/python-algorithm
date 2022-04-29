# 정렬 - H-Index
from audioop import reverse

def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    citations.append(0)

    for i in range(len(citations)):
        if i+1 >= citations[i]: 
            answer = citations [i]
            while i > answer: answer += 1
            break

    return answer

citations = [10, 10, 10, 10, 10]
print(solution(citations))

"""
최소값의 집합을 모아 그 중 최대 값을 구하는 방식

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
"""