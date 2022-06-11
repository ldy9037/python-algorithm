# 카카오 블라인드 - 후보키
from collections import deque

def solution(relation):
    answer = 0

    relation = list(map(list, zip(*relation)))
    length = len(relation[0])

    queue = deque()

    while relation:
        c = relation.pop(0)
        r = relation.copy()
        queue.append((c, r))

    while queue:
        c, r = queue.popleft()

        if len(set(c)) == length:
            answer += 1
            continue

        

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	
print(solution(relation))