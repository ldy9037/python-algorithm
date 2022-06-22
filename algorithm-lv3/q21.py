# 월간 코드 챌린지 - 금과 은 운반하기

def solution(a, b, g, s, w, t):
    answer = 0
    
    left = 0
    right = (10 ** 9) * 2

    while left <= right:
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
                
                time = time + t[i] if time == 0 else time + (t[i] * 2)
            
                if g_w == 0 and s_w == 0: break
            
            if t_a == a and t_b == b: 
                success = True
                break
        
        if success: 
            right = middle
            answer = middle
        else: left = middle + 1
    
    return answer

a = 90
b = 500
g = [70,70,0]
s = [0,0,500]
w = [100,100,2]
t = [4,8,1]

print(solution(a, b, g, s, w, t))
