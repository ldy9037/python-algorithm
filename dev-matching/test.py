def solution(grade):
    answer = 0
    
    prev = float("inf")
        
    while grade:
        m = 0
        g = grade.pop()

        if g > prev: 
            m = g - prev
            answer += m 
         
        prev = g - m
        
    return answer

grade = [3,2,3,6,4,5]

print(solution(grade))