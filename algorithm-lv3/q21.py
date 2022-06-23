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
    answer = 0
    
    left = 0
    right = (10 ** 9) * 2

    while left < right:
        middle = (left + right) // 2

        success = False
        current = {
            "gold" : a,
            "silver" : b
        }
        
        for i in range(len(t)):
            gold = g[i] if g[i] <= current["gold"] else current["gold"]
            silver = s[i] if s[i] <= current["silver"] else current["silver"]

            send_count = math.ceil((gold + silver) / w[i]) 
            max_count = (middle / t[i] + 1) // 2

            if send_count > max_count:
                total_w = w[i] * max_count
                gold = gold if total_w >= gold else total_w
                silver = total_w - gold

            current["gold"] = current["gold"] - gold if current["gold"] >= gold else 0
            current["silver"] = current["silver"] - silver if current["silver"] >= gold else 0

            if current["gold"] == 0 and current["silver"] == 0: 
                success = True
                break
        
        if success: 
            right = middle
            answer = middle
        else: left = middle + 1
        
    return answer


a = 20
b = 20
g = [20, 20]
s = [20, 0]
w = [10, 10]
t = [10, 10]

"""
a = 90
b = 500
g = [70,70,0]
s = [0,0,500]
w = [100,100,2]
t = [4,8,1]
"""

print(solution(a, b, g, s, w, t))
