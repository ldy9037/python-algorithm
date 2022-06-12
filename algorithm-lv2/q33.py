# 카카오 블라인드 - 후보키
from collections import deque

def solution(relation):
    answer = []

    relation = list(map(list, zip(*relation)))
    length = len(relation[0])

    queue = deque()

    column = list(range(len(relation)))
    
    while column:
        c = [column.pop(0)]
        r = column.copy()
        queue.append((c, r))

    while queue:
        c, r = queue.popleft()
        
        isValid = True
        for ck in answer:
            if len(set(c) | set(ck)) == len(c): 
                isValid = False
            
        if not isValid: continue

        if len(set(zip(*list(map(lambda x: relation[x], c))))) == length:
            answer.append(c)
            continue

        while r:
            
            n = c.copy()
            n.append(r.pop(0))
            
            queue.append((n, r.copy()))
            
    return len(answer)

relation = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
print(solution(relation))
# (0),(2,3),(1,3,4)
