# DFS/BFS - 타겟 넘버(1)
# 문제를 잘못 읽어서 순서에 상관없이 target값을 만드는 방법의 수를 구함. 문제 잘 읽자..
# BFS 사용
from collections import deque
import queue

def solution(numbers, target):
    answer = set()
    queue = deque()

    queue.append(([], numbers ,0))
    
    while queue:
        history, children, parent = queue.popleft()

        if len(children) == 0 and parent == target: answer.add(tuple(history))

        history = history + [parent]
        for child in children: 
            grandson = children.copy()
            grandson.remove(child)
            
            queue.append((history,grandson, parent + child))
            queue.append((history,grandson, parent - child))                
        
    return len(answer)


numbers = [4,1,2,1]
target = 4
print(solution(numbers,target))