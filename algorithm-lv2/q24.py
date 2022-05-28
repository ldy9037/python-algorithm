# 카카오 블라인드 - 메뉴 리뉴얼
# 잘못 접근 한 것 같음?
from collections import defaultdict
import itertools

def solution(orders, course):
    answer = []
    menu = defaultdict(int)
    
    while orders:
        current = set(orders.pop())

        for order in orders:
            intersection = set(order) & current
            if len(intersection) < course[0]: continue
            
            for length in course:
                if length > len(intersection): break
                comb = list(itertools.combinations(''.join(intersection),length))
                
                for e in comb: menu[''.join(sorted(e))] += 1
    
    
    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

print(solution(orders, course))

#["ACD", "AD", "ADE", "CD", "XYZ"]