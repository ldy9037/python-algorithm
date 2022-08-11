from heapq import heappop


def solution(A, B):
    answer = 0
    
    checked = [False] * len(A)
     
    for A_e, B_e in zip(A, B):
        C_e = max(A_e, B_e)
        if C_e <= len(checked):
            checked[C_e - 1] = True 
    
    print(checked)

    if not all(checked):  
        answer = checked.index(False) + 1
    else: answer = len(checked) + 1

    return answer 

A = [1,2]
B = [1,2]
print(solution(A,B))