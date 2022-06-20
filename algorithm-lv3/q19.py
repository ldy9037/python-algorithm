# 카카오 인턴십 - 보석쇼핑
from collections import deque

def solution(gems):
    answer = []

    current = [1, 0]

    gem_kind = set(gems)
    kind_cnt = dict(zip(gem_kind, [0] * len(gem_kind)))

    order = deque()
    complete = False

    for gem in gems:
        order.append(gem)
        kind_cnt[gem] += 1

        while kind_cnt[order[0]] > 1:
            f = order.popleft()
            kind_cnt[f] -= 1

            if kind_cnt[f] == 0: 
                order.appendleft(f)
                kind_cnt[f] += 1
            else: current[0] += 1

        current[1] += 1
        
        if complete == False:
            complete = True

            for v in kind_cnt.values():
                if v == 0: 
                    complete = False
                    break
    
        if complete: answer.append(current.copy())
            
    print(answer)
    answer.sort(key=lambda x: x[1] - x[0])
    return answer[0]

gems = 	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))
# 3,7
"""
from collections import deque

def check(gems, middle, kind_count):
    result = [0, 0]

    queue = deque()
    queue.extend(gems[:middle])

    result = [0, 0]
    r = gems[middle:]
    for i in range(len(r) + 1):
        if len(set(queue)) == kind_count: 
            result = [i + 1, i + middle] 
            break
        
        if len(r) == i: break

        queue.popleft()
        queue.append(r[i])

    return result

def solution(gems):
    answer = []
    kind_count = len(set(gems))
    left = kind_count
    right = len(gems)

    while left < right:
        middle = (left + right) // 2
        
        answer = check(gems, middle, kind_count)

        if answer[0] == 0: left = middle + 1
        else: right = middle

    answer = check(gems, left, kind_count)

    return answer
"""