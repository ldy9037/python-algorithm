# 스택,큐 - 다리를 지나는 트럭
# deque를 선언하는 대신 reverse를 활용한다던가 매 loop 마다 sum을 하는 대신 현재 무게를 저장하는 변수를 선언했으면 성능이 좀 더 좋았을 듯 함. 

from queue import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge_deque = deque([], bridge_length)
    truck_weights_deque = deque(truck_weights)

    while truck_weights_deque:
        answer += 1
        
        if(bridge_deque):
            front_truck, start_time = bridge_deque.popleft()
            if answer - start_time < bridge_length: bridge_deque.appendleft((front_truck, start_time))

        next_truck = truck_weights_deque.popleft()    
        if sum(truck_weight for truck_weight, start_time in bridge_deque) + next_truck <= weight: bridge_deque.append((next_truck, answer))
        else: truck_weights_deque.appendleft(next_truck)

    return answer + bridge_length

bridge_length = 100
weight = 100
truck_weights = [10]

print(solution(bridge_length, weight, truck_weights))
