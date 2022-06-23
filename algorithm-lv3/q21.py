# 월간 코드 챌린지 - 금과 은 운반하기
"""
def solution(a, b, g, s, w, t):
    answer = 0
    
    left = 0
    right = (10 ** 9) * 2

    while left < right:
        middle = (left + right) // 2

        success = False
        t_a, t_b = 0, 0
        for i in range(len(t)):
            time = 0
            gold, silver = g[i], s[i]
            while time < middle: 
                weight = w[i]

                g_w = weight if gold - weight > 0 else gold
                g_w = g_w if t_a + g_w < a else a - t_a
                gold -= g_w

                s_w = weight - g_w if silver - (weight - g_w) > 0 else silver
                s_w = s_w if t_b + s_w < b else b - t_b
                silver = silver - s_w

                t_a = g_w + t_a
                t_b = s_w + t_b
            
                if g_w == 0 and s_w == 0: break
                time = time + t[i] if time == 0 else time + (t[i] * 2)

            if t_a == a and t_b == b and time <= middle: 
                success = True
                break

        if success: 
            right = middle
            answer = middle
        else: left = middle + 1
        
    return answer
"""
import math

def solution(a, b, g, s, w, t):
    left = 0
    right = (10 ** 9) * 2

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
            
        if success: 
            right = middle
        else: left = middle + 1
        
    return right


a = 0
b = 0
g = [1, 0]
s = [1, 0]
w = [1, 1]
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
