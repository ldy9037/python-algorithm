# 스택, 큐 - 주식 가격
"""
deque를 이용한 풀이
from queue import deque

def solution(prices):
    answer = []
    
    pricees_decue = deque(prices)
    
    while pricees_decue: 
        sec = 0

        price = pricees_decue.popleft()
        for next_price in pricees_decue:
            sec += 1 
            if price > next_price: break
        
        answer.append(sec)
    
    return answer
"""

"""
처음에 위 처럼 queue로만 풀었으나 stack으로 풀면 시간복잡도가 O(n)이 된다고 해서 풀어 보았음. 
시간 복잡도가 O(n)은 아닌 거 같은데 성능은 확실히 개선됨. (최악의 경우 O(n^2)로 보임)
"""
from collections import deque

def solution(prices):
    length = len(prices)
    answer = [0] * length

    prices_deque = deque(prices)
    prices_stack = []

    for i in range(length):
        now_price = prices_deque.popleft()

        while prices_stack:
            prev_index, prev_price = prices_stack.pop()
            if prev_price > now_price: answer[prev_index] = i - prev_index
            else: 
                prices_stack.append((prev_index, prev_price))
                break

        prices_stack.append((i, now_price))
    
    while prices_stack:
        prev_index, prev_price = prices_stack.pop()
        answer[prev_index] = (length -1) - prev_index

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
#[4, 3, 1, 1, 0]