# 월간 코드 챌린지 - 금과 은 운반하기
import math

def solution(a, b, g, s, w, t):
    left = 0
    right = ( ( 10 ** 9 ) * 2 * 2 - 1 ) * (10 ** 5)
    
    while left < right:
        middle = (left + right) // 2

        success = False
        
        max = [0, 0]
        weight = 0

        for i in range(len(t)):
            send_count = math.ceil((g[i] + s[i]) / w[i]) 
            max_count = (middle // t[i] + 1) // 2

            total_w = g[i] + s[i]
            if send_count > max_count:
                total_w = w[i] * max_count

            max[0] = max[0] + total_w if g[i] >= total_w else max[0] + g[i]
            max[1] = max[1] + total_w if s[i] >= total_w else max[1] + s[i]
            weight += total_w

            if weight >= a + b and max[0] >= a and max[1] >= b: 
                success = True
            
        if success: right = middle
        else: left = middle + 1
        
    return right


a = 2
b = 0
g = [2, 0]
s = [0, 0]
w = [2, 1]
t = [1, 1]

"""
a = 90
b = 500
g = [70,70,0]
s = [0,0,500]
w = [100,100,2]
t = [4,8,1]
"""

print(solution(a, b, g, s, w, t))
