# 연습문제 - 124 나라의 숫자
def solution(n):
    answer = ''
    table = {
        1:'1', 2:'2', 3:'4'
    }
    
    while n > 0:
        s, r = divmod(n, 3)
        if r == 0: 
            s -= 1
            r = 3
        answer = table[r] + answer

        n = s

    return answer

n = 3
print(solution(n))
