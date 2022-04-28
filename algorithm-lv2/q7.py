# 힙 - 더 맵게
import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        min = heapq.heappop(scoville)
        if min >= K: break
        if not scoville: 
            answer = -1
            break

        heapq.heappush(scoville, min + (heapq.heappop(scoville) * 2))
        answer += 1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))