# 이분탐색 - 입국심사
# 이분 탐색의 기준점을 얼마나 빨리 잡아내느냐의 문제.

def solution(n, times):
    answer = 0

    left = 1
    right = times[-1] * n

    while left <= right:
        middle = (left + right) // 2
        people_count = 0

        for time in times:
            people_count += middle // time

            if people_count > n: break

        if people_count >= n: right = middle - 1
        else: left = answer = middle + 1

    return answer

"""
밑에 풀이에서 이진 탐색 대신 heap을 사용한 풀이
깔끔해서 좋음. 하지만 성능은 똑같이 안좋음. 
import heapq

def solution(n, times):
    answer = 0

    times = list(map(lambda time: (time ,time), times))
    heapq.heapify(times)

    for i in range(n):
        total_time, time = heapq.heappop(times)
        total_time += time

        heapq.heappush(times, (total_time, time))

    answer = max(list(map(lambda time: time[0] - time[1], times)))

    return answer
"""

"""
기준점을 잘 못잡은 풀이, 답이긴 한데 성능이 아주아주 심각 (n 최대 1,000,000,000)
def binary_search(target, times):    
    result = 0
    left = 0
    right = len(times) - 1

    while left <= right:
        middle = (left + right) // 2

        if times[middle][1] == target: return middle
        elif times[middle][1] < target: 
            right = middle - 1
            result = middle
        else: left = result = middle + 1
    
    return result

def solution(n, times):
    answer = 0

    times = list(map(lambda time: (time,time), times))
    times.sort(reverse=True)

    for i in range(n):
    
        time, total_time = times.pop()
        total_time += time

        times.insert(binary_search(total_time, times), (time, total_time))

    answer = max(list(map(lambda time: time[1] - time[0], times)))

    return answer
"""

n = 6
times = [7, 10]

#n = 6
#times = [10,12, 4]
print(solution(n, times))