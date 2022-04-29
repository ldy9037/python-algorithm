# 정렬 - 가장 큰 수

from functools import reduce

def solution(numbers):
    answer = ''
    sort_numbers = []

    numbers = sorted(numbers)
    for number, index in zip(numbers, range(len(numbers))):
        number = str(number)
        
        while len(number) < 4: number += number
        sort_numbers.append((int(number[:4]),index))

    sort_numbers = sorted(sort_numbers,reverse=True)
    answer = str(int(reduce(lambda answer, number: answer + str(numbers[number[1]]) ,sort_numbers, '')))

    return answer

numbers =  [978, 97]
print(solution(numbers))


"""
처음에 작성 한 코드, 하지만 알아보기 매우 어려워서 좋은 코드라 할 수는 없겠음 
    sort_numbers = list(map(lambda number: (int(str(number[0]).ljust(4, str(number[0])[-1])), number[1]) ,zip(numbers, range(len(numbers)))))
    sort_numbers = sorted(sort_numbers,reverse=True)
    
    answer = str(int(reduce(lambda answer, number: answer + str(numbers[number[1]]) ,sort_numbers, '')))
    """


"""
문자열 sort하면 아래와 같이 작성 할 수 있음. 문자열 정렬 방식은 첫 번째 인덱스부터 ASCII 값을 비교하는 방식이고 다른 ASCII값이 나올 때까지 반복함. 
문자열 정렬 시 각 문자열을 *3 으로 이어 붙여 자릿수를 3이상으로 늘렸기 때문에 정확하게 비교 가능 함. 
문자열 sort 방식 숙지하고 있어야 할 듯 함.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
 """
