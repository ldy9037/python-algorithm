# 카카오 블라인드 - 자물쇠와 열쇠
# Key를 햄버거 처럼 늘려서 xor로 비교해보았음. 의도에 맞는 풀이인지는 모르겠음.

def rotation(arr): 
    arr.reverse()
    return list(map(list, zip(*arr)))

def hamburger(key, lock):
    result = [[0] * len(key)] * len(lock)
    result.extend(key.copy())
    result.extend([[0] * len(key)] * len(lock))

    return result

def convert_list_to_binary(arr, length):
    result = [str(b) for b in arr]
    result = int("".join(result).ljust(length, "0"), 2)

    return result

def solution(key, lock):
    answer = False

    for i in range(4):
        temp = hamburger(key, lock)

        for k in range(len(key) + len(lock) + 1):
            for j in range(len(key) + len(lock) + 1):
                answer = True

                for s in range(len(lock)):
                    k_binary = convert_list_to_binary(temp[s], len(lock) + len(key))
                    l_binary = convert_list_to_binary(lock[s], len(lock))
                    
                    xor = bin(k_binary >> j ^ l_binary).replace("0b", "")
                
                    if "0" in xor.rjust(len(lock), "0")[-len(lock):]: 
                        answer = False
                        break

                if answer == True: return answer

            temp.pop(0)
        
        key = rotation(key)

    return answer

key = [
        [1, 1, 1], 
        [1, 1, 1], 
        [1, 1, 1]
    ]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

print(solution(key, lock))