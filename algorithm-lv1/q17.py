# 프로그래밍 마에스터 - 폰켓몬
def solution(nums):
    answer = 0

    choice = len(nums)/2

    nums = set(nums)
    answer = choice if len(nums) > choice else len(nums)

    return answer

nums = [3,3,3,2,2,4]
print(solution(nums))