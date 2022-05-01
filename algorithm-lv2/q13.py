# 탐욕법 - 큰 수 만들기

"""
그냥 문자열 그대로 비교해가면서 작은 값을 제거해주는 방식으로 구현 함. 일단 대부분의 케이스를 테스트 해보았으나 정상 통과함. 
그런데 테스트 케이스 2~10번을 통과 못 하는데 반례를 못찾겠음.

def solution(number, k):
    count = 0

    for i in range(len(number)):
        if count == k :break

        while len(number) >= (i + 2) and number[i] < number[i + 1] :
            number = number[:i] + number[i + 1:]
            if i >= 1: i -= 1

            count += 1
            if count == k: break
    
    if k - count: number = number[:(len(number) - (k - count))]

    return number
"""
# 위 풀이로 2~10번 케이스에 통과를 못함. (성능이 아니라 그냥 테스트 실패) 
# 마침 성능 개선도 할 겸 스택으로 다시 풀어서 통과함. 
def solution(number_list, k):
    stack = []
    count = 0

    for number in number_list:

        while stack and stack[-1] < number:
            if count == k: break
            stack.pop()
            count += 1

        stack.append(number)
    
    if k - count: stack = stack[:(len(stack) - (k - count))]

    return ''.join(stack)
    

number_list = "4177252841"
k = 4
print(solution(number_list, k))