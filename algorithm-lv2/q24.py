# 카카오 블라인드 - 메뉴 리뉴얼
# collections.Counter 라이브러리를 사용하면 훨씬 깔끔하게 풀 수 있음. 
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
    
    maxium = dict(zip(course, [0] * len(course)))
    menu = sorted(menu.items(), key=lambda m: m[1], reverse=True)
    
    for name, count in menu:
        if maxium[len(name)] == 0: maxium[len(name)] = count
        if maxium[len(name)] == count: answer.append(name)
    
    return sorted(answer)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

print(solution(orders, course))

#["ACD", "AD", "ADE", "CD", "XYZ"]