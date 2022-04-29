# 완전탐색 - 소수 찾기
import itertools
import math

def isPrimeNumber(number):
    result = True
    
    if number >= 2: 
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0: 
                result = False
                break
    else: result = False
    
    return result

def solution(numbers):
    answer = 0
    permutation_set = set()

    for i in range(len(numbers)):   
        permutation_set.update(set(map(lambda number: int(''.join(number)), list(itertools.permutations(numbers, i + 1)))))
        
    
    for number in permutation_set: 
        if isPrimeNumber(number): answer += 1

    return answer

numbers = "1231" # 2
print(solution(numbers))

"""
에라스토테네스 체를 사용한 풀이. 
    def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
"""