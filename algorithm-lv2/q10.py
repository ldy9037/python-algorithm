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