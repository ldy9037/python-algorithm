# 큐,스택 - 기능개발
import math

def solution(progresses, speeds):
    answer = []

    time_queue = []

    for progress, speed in zip(progresses, speeds):
        now_time = math.ceil((100 - progress) / speed)

        if time_queue and now_time > time_queue[0]:
            answer.append(len(time_queue))
            time_queue.clear()
        
        time_queue.append(now_time)
            
    answer.append(len(time_queue))

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))