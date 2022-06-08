# 카카오 블라인드 - 순위 검색
from collections import defaultdict

def find_num(score, v):
    result = set()

    for i, s in enumerate(score):
        if s >= v: result.add(i) 
    
    return result

def solution(info, query):
    answer = []

    group = defaultdict(set)
    score = []

    for i, v in enumerate(info):
        for item in v.split():
            if item.isdigit(): score.append(int(item))
            else: group[item].add(i)

    for q in query:
        s = set()
        for i, item in enumerate(q.replace("and", "").split()):
            c = set()
            if item == "-": c = c | set(range(len(info)))
            elif item.isdigit(): c = find_num(score, int(item))
            else: c = group[item]  

            s = s | c if i == 0 else s & c

            if len(s) == 0: break

        answer.append(len(s))

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))