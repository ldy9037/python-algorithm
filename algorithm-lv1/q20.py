# Summer/Winter Coding - 예산
def solution(d, budget):
    answer = 0

    d.sort()

    for i in range(len(d)):
        if budget - d[i] < 0: break
        budget -= d[i]
        answer += 1
    
    return answer

d = [1,3,2,5,4]
budget = 9

print(solution(d, budget))