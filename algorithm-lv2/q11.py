# 완전탐색 - 카펫
from turtle import width


def solution(brown, yellow):
    answer = [0,0]
    width_plus_height = (brown - 4) / 2

    for height in range(1, int(width_plus_height // 2) + 1):
        width = int(width_plus_height - height)

        if height * width == yellow: 
            answer[0] = width + 2
            answer[1] = height + 2

    return answer

brown = 10
yellow = 2

print(solution(brown, yellow))

"""
근의 공식을 이용해서 푼 풀이도 있음. 가독성이 조금 아쉬움.
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
"""