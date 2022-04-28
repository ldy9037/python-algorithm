# 힙 - 디스크 컨트롤러
# 테스트 케이스 체크 잘해야함.

import heapq

def solution(jobs):
    answer = 0
    
    jobs = sorted(jobs)

    now_time = 0
    request_heap = []
    heapq.heapify(request_heap)

    for request_time, process_time in jobs:
        answer -= request_time

        while now_time < request_time: 
            if request_heap:    
                now_time += heapq.heappop(request_heap)
                answer += now_time            
            else: 
                now_time = request_time

        heapq.heappush(request_heap, process_time)

    while request_heap:
        now_time += heapq.heappop(request_heap)
        answer += now_time            

    return answer // len(jobs)

jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
print(solution(jobs))

# return 72