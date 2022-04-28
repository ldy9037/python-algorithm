# 힙 - 이중우선순위큐
from heapq import heapify

import heapq

def solution(operations):
    answer = [0, 0]

    heap = []    
    status = "-1"
    for operation in operations:
        operation_type, number = operation.split()
    
        if operation_type == "I": heapq.heappush(heap, -int(status) * int(number))
        else: 
            if heap:
                if number != status: 
                    status = number
                    heap = list(map(lambda e: -e, heap))
                    heapq.heapify(heap)
                heapq.heappop(heap)
                
    if heap:
        for k, v in [(0, "1"), (1, "-1")]: answer[k] = heap[0] if status == v else int(v) * max(heap)

    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
# [6,5]

"""
힙 변경없이 max로 처리하는 코드  

import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)
    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

"""