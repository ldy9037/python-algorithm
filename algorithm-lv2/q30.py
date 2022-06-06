# 팁스타운 - 예상 대진표
def check_domain(a, b):
    result = [0, 0]

    exponent = 0
    while not all(result):
        for i, player in enumerate([a,b]):
            if player == 1: result[i] = 1
            if result[i] == 0 and player > 2 ** exponent and player <= 2 ** (exponent + 1): result[i] = exponent + 1

        exponent += 1

    if result[0] == result[1] and (result[1] != 1 and result[0] != 1): 
        result = check_domain(a - 2 ** (result[1] - 1), b - 2 ** (result[1] - 1))

    return result

def solution(n,a,b):
    return max(check_domain(a, b))

n, a, b= 8, (2 ** 20) -1, 2 ** 20
print(solution(n, a, b))
# 3

"""
내가 푼 방식은 각 a와 b가 2^(n-1) ~ 2^n 사이에 속하는지 체크하는 방식이였다.
다른 사람들 풀이에서 위 방식을 아주 심플하게 표현한 풀이를 찾았음. 
2의 몇승인지로 판단하는 것은 똑같음. 다만 같은 영역(2^(n-1) ~ 2^n)에 속하는 지 앞에서 부터 XOR로 체크가 가능함. (위 풀이에서 재귀 부분) 

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

"""