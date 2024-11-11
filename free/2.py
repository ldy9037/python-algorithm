def solution(diffs: list, times: list, limit: int) -> int:
    level = 1 
    left = 1
    right = max(diffs)
    
    while left < right:
        level = (left + right) // 2
        
        clear = False    
        total_time = times[0]

        for i in range(1, len(diffs)):            
            total_time += solv(diffs[i], times[i], times[i - 1], level)            

        if total_time <= limit:
            clear = True

        if clear:
            right = level
        else: 
            left = level + 1    
    
    return left

def solv(diff: int, current: int, prev: int, level: int) -> int:
    result = 0
    
    if diff > level:
        result += ( current + prev ) * (diff - level)
        
    result += current
    
    return result

diffs = [1, 5, 3]
times = [2, 4, 7]
limit = 30

print(solution(diffs, times, limit))
