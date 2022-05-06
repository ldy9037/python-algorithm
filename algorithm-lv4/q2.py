# 이분탐색 - 징검다리
def solution(distance, rocks, n):
    answer = 0

    left = 1
    right = distance - (len(rocks) - n)

    rocks.sort()

    while left <= right:
        middle = (left + right) // 2
        
        start = 0
        removed = 0
        for rock in rocks:
            if rock - start < middle: 
                removed += 1
                continue
            else: start = rock



        if n < removed: right = answer = middle -1
        else: left = middle + 1
            

    return answer

distance = 25
rocks = [2, 14, 11, 21, 17] 
n = 2

#4

print(solution(distance, rocks, n))