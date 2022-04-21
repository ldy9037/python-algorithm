# 카카오 - [1차] 비밀지도 
# 코드를 짧게 작성해 보았는데 네이밍을 신경써도 가독성이 매우 떨어짐
def solution(n, arr1, arr2):
    answer = []

    answer = list(map(lambda decimal: str(bin(decimal[0] | decimal[1])).replace('0b', '').replace('1', '#').replace('0', ' ') ,zip(arr1, arr2)))
    for i in range(len(answer)):
       answer[i] = answer[i] if len(answer[i]) == n else "".join([' ' for i in range(n-len(answer[i]))]) + answer[i]

    return answer

# 문자열 앞에 문자열을 채울 수 있는 rjust 함수를 발견함. 아래처럼 작성도 가능함.
"""
def solution(n, arr1, arr2):
    answer = []

    answer = list(map(lambda decimal: str(bin(decimal[0] | decimal[1])).replace('0b', '').replace('1', '#').replace('0', ' ').rjust(n, ' ') ,zip(arr1, arr2)))

    return answer
"""

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))