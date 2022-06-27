# 스킬체크 - 거스름돈
"""
def solution(n, money):
    answer = 0

    money.sort(reverse=True)

    stack = []
    stack.append((money.pop(), n, money))

    while stack: 
        u, penny, money = stack.pop() 

        for i in range(penny // u + 1):
            n_penny = penny - (u * i)
            
            if n_penny == 0: 
                answer += 1
                continue
            
            if money: 
                n_money = money.copy()
                stack.append((n_money.pop(), n_penny, n_money))

    return answer % 1000000007
"""

def solution(n, money):
    answer = [0] * (n + 1)

    money.sort()
    for i in range(n + 1):
        if i % money[0] == 0 : answer[i] = 1

    for u in money:
        if u == money[0]: continue

        for i in range(u, n + 1):
            answer[i] = answer[i] + answer[i - u]

    return answer[n] % 1000000007

n = 5
money = [1,2,5]

print(solution(n, money))
# 4