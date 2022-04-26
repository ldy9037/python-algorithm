# 해시 - 위장
 
"""
초기 풀이
Counter를 사용하면 쉽게 종류별 개수를 구할 수 있음. 
from collections import defaultdict

def solution(clothes):
    answer = 0
    type_list = defaultdict(list)

    for clothes_part in clothes:
        type_list[clothes_part[1]].append(clothes_part[0])

    prev_type_len = 0
    for type, clothes_part in type_list.items():
        answer += (answer + 1) * len(clothes_part)

    return answer
"""


"""
Counter를 사용해서 푼 내용. 
학창시절에 배운 경우의 수가 기억이 안나서 일단 규칙 찾아서 반복문 돌려버림.
"""
from collections import Counter

def solution(clothes):
    answer = 0
    len_list = Counter([type for name, type in clothes])

    for type, length in len_list.items():
        answer += (answer + 1) * length

    return answer

clothes = [["crowmask", "test1"], ["bluesunglasses", "test2"], ["smoky_makeup", "test3"]]
print(solution(clothes))