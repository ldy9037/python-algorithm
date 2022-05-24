# Summer/Winter Coding - 멀쩡한 사각형
from math import gcd

def solution(w,h):
    answer = 1

    answer = w * h - (w + h - gcd(w, h) )

    return answer

w = 8
h = 12
print(solution(w, h))