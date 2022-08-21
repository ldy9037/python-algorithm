# 카카오 - 무지의 먹방 라이브

import heapq

def solution(food_times: list, k: int) -> int:
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3
    """
    answer: int = -1

    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i))
    
    length = len(food_times)
    deleted_time = 0

    while heap:
        time, index = heapq.heappop(heap)
        time -= deleted_time

        time_sum = time * length
        if time_sum > k:
            break
            
        k -= time_sum
        deleted_time += time
        food_times[index] = 0
        length -= 1
        
    if length > 0:
        k = k % length    
        cnt = 0
        for i, time in enumerate(food_times):
            if time == 0: continue
            
            cnt += 1
            
            if cnt == k + 1:
                answer = i + 1

    return answer

food_times = [1000, 1000, 1000]
k = 3000
print(solution(food_times, k))