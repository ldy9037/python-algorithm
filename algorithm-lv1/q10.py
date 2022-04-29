# 완전탐색 - 모의고사
from heapq import heapify

def solution(answers):
    answer = []

    score = [0,0,0]
    giver_marking = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    length = [5, 8, 10]
    for i in range(len(answers)):
        for k in [0,1,2]:
            if answers[i] == giver_marking[k][i % length[k]]: score[k] += 1
    
    answer = list(map(lambda s: s[0] + 1 , list(filter(lambda s: s[1] == max(score),enumerate(score)))))

    return answer

answers = 	[1, 2, 3, 4, 5]
print(solution(answers))

"""
itertools.cycle 라는 함수가 있음. 이 함수는 배열을 순서대로 무한 반복 시켜주는 함수 
이 함수를 이용해서 푼 결과

from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
"""