# 동적계획법 - 정수 삼각형
def solution(triangle):
    answer = 0

    for i, top_floor in enumerate(triangle):
        if i == len(triangle) -1: break
        next_floor = triangle[i + 1]
        max_bucket = 0
        
        for k in range(len(top_floor)):
            sum = {'left': next_floor[k] + top_floor[k], 'right': next_floor[k + 1] + top_floor[k]}
            
            next_floor[k] = sum['left'] if max_bucket < sum['left'] else max_bucket 
            max_bucket = sum['right']

        next_floor[-1] = max_bucket
        triangle[i + 1] = next_floor

        answer = max(triangle[-1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

"""
아래 처럼 푸신 분이 있음. ㅋㅋㅋㅋ
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
"""