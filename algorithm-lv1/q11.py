# 탐욕법 - 체육복
"""
import heapq

def solution(n, lost, reserve):
    answer = 0
    givers = []    

    for giver in reserve:
        if giver in lost: 
            lost.remove(giver)
        else: heapq.heappush(givers, giver) 
    
    while givers:
        giver = heapq.heappop(givers)
        if giver - 1 in lost: 
            lost.remove(giver - 1)
            continue
        if giver + 1 in lost:
            lost.remove(giver + 1)
            continue
    
    answer = n - len(lost)

    return answer

"""
"""
처음에 거르는 작업을 for + heapq를 사용했는데  remove를 사용했기 때문에 for + remove = O(n^2)가 나옴.
거르는 작업에 set을 이용하면 더 효율적으로 풀어낼 수 있음.
"""
def solution(n, lost, reserve):
    answer = 0

    givers = list(set(reserve) - set(lost)) 
    lost = list(set(lost) - set(reserve)) 

    for giver in givers:
        if giver - 1 in lost: 
            lost.remove(giver - 1)
            continue
        if giver + 1 in lost:
            lost.remove(giver + 1)
            continue

    answer = n - len(lost)

    return answer



n = 5
lost = [1,2,3,4]
reserve = [2,3,4,5]

print(solution(n, lost, reserve))
