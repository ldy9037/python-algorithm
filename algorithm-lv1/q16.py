# Summer/Winter Coding - 소수 만들기
from itertools import combinations

def solution(nums):
    answer = 0

    for comb in combinations(nums, 3):
        num = sum(comb)
        answer += 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0: 
                answer -= 1
                break

    return answer

nums = [1,2,3,4]	
print(solution(nums))
# 1