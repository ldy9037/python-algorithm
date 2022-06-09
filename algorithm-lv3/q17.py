# 카카오 블라인드 - 자물쇠와 열쇠

def rotation(arr): 
    arr.reverse()
    return list(map(list, zip(*arr)))

def solution(key, lock):
    answer = True

    """
    for i in range(4):
        for k in range(len(key) + len(lock) - 1):
            for j in range(len(key) + len(lock) - 1):
    """    
    

    return answer

key = [
        [0, 0, 0], 
        [1, 0, 0], 
        [0, 1, 1]
    ]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))