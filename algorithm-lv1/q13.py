# 월간 코드 챌린지 - 없는 숫자 더하기
def solution(numbers):
    all_sum = sum(range(10))

    return all_sum - sum(numbers)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))