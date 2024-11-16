import copy
from collections import Counter

def solution(points: list, routes: list) -> int:
    answer = 0
    positions = list()
    
    for route in routes:
        start = getDest(points, route[0])
        time = 0
        positions.append(tuple([time] + start))

        for i in range(len(route)):
            while start != getDest(points, route[i]):
                time += 1
                start = move(start, getDest(points, route[i]))    
                positions.append(tuple([time] + start))

    counter = Counter(positions)
    
    for count in counter.values():
        if count > 1: answer += 1
    
    return answer

def move(start: list, dest: list) -> tuple:
    for i in range(2):
        if start[i] != dest[i]: 
            start[i] = start[i] + 1 if start[i] < dest[i] else start[i] - 1
            break
    
    return start

def getDest(points: list, point: int) -> list:
    return copy.deepcopy(points[point - 1])

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [4, 2], [4, 3]]
print(solution(points, routes))