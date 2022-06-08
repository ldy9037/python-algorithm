# 카카오 블라인드 - 순위 검색
from collections import defaultdict
from itertools import combinations

def b_search(arr, v): 
    result = 0

    left = 0
    right = len(arr)

    while left < right:
        middle = (left + right) // 2
        
        if v <= arr[middle] : right = middle
        else: left = middle + 1

    result = len(arr) - left

    return result

def solution(info, query):
    answer = []

    group = defaultdict(list)

    for i in info:
        i = i.split()
        s = int(i[-1])
        i = i[0:-1]
        
        for l in range(1,5):
            for c in list(combinations(i, l)):
                group["".join(c)].append(s)
        
        group["-"].append(s)

    for k, v in group.items(): 
        v.sort()
        group[k] = v

    for q in query:
        q = q.replace("-","").replace("and", "").split()
        s = int(q[-1])
        q = q[0:-1]
        
        arr = group["".join(q)]
        if not q: arr = group["-"]

        answer.append(b_search(arr, s))

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]

#info = ["java backend junior pizza 150"] * 50000
#query = ["- and - and - and -1"] * 100000

print(solution(info, query))
