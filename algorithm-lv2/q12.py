# 탐욕법 - 조이스틱
# 그리디 방식으로 풀긴했는데 탐욕법 자체가 부분 최적해 == 전체 최적해를 성립하지 않기 때문에 반례가 있음. 이것을 어떻게 해결 할 지 차후에 고민좀 해봐야겠음. 
# 이 반례를 해결하는 법을 찾기 위해 다른 해결방법을 찾아봤는데 전부 BBBBAAAABA에서 걸림. (왼쪽 갔다가 -> 오른쪽은 고려하지 않은 솔루션들이 대부분) 
# 하지만 이 부분들까지 전부 따로 체크해주는 것은 그리디 하지도 않거니외 답에 풀이를 끼워 맞추는 느낌임. 

from collections import deque
import heapq

def alphabet_count(character):
    up_and_down_dp = (ord("Z") - ord("A")) // 2
    return ord(character) - ord("A") if up_and_down_dp > (ord(character) - ord("A")) else ord("Z") - ord(character) + 1

def next_location(location_list, cursor, name):
    location = {"left": location_list[0], "right": location_list[-1]}

    distance_heap = []
    distance_list = {"left": abs(location["left"][0] - cursor), "right":abs(location["right"][0] - cursor)}
    
    for k ,distance in distance_list.items():
        heapq.heappush(distance_heap, (distance, location[k]))
        heapq.heappush(distance_heap, (len(name) - distance, location[k]))

    return heapq.heappop(distance_heap)

def solution(name):
    answer = 0

    location_list = deque(filter(lambda location: location[0] == 0 or location[1] != "A", zip(range(len(name)), name)))
    
    cursor, character = location_list.popleft()

    while location_list:         
        answer += alphabet_count(character)

        next = next_location(location_list, cursor, name)
        
        answer += next[0]
        cursor, character = next[1]
        
        location_list.remove(next[1])

    answer += alphabet_count(character)

    return answer


name = "BBBBAAAABA"
print(solution(name))
