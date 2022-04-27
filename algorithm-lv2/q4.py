# 스택,큐 - 프린터
from collections import deque


def solution(priorities, location):
    answer = 0
    priority_deque = deque(zip(priorities, range(len(priorities))))

    while priority_deque:
        priority, index = priority_deque.popleft()

        if not priority_deque or priority >= max(priority_deque)[0]: 
            answer += 1
            if index == location: break
        else: priority_deque.append((priority, index))

    return answer

priorities = [1, 1, 7, 1, 9, 1, 1]
location = 1

print(solution(priorities, location))

"""
any 함수를 사용해서 풀 수도 있음.
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


"""