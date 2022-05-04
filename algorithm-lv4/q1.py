# 동적계획법 - 도둑질

def solution(money):
    answer = []

    for k in range(2):
        thievery_money = [0] * len(money)

        for i in range(k,2): thievery_money[i] = max(money[k:i + 1])
        for i in range(2, len(money) - (1 - k)): thievery_money[i] = max(thievery_money[i - 1], thievery_money[i - 2] + money[i])
        
        answer.append(max(thievery_money))
    return max(answer)
    

money = [3,1,7,8,1]
print(solution(money))