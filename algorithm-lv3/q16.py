# Dev Matching - 다단계 칫솔 판매
# 문제 자체는 굉장히 쉬우나 범위를 생각하지 않고 예외처리를 하지 않으면 고생 할 수 있는 문제
# amount 의 범위가 100 이하이기 때문에 위로 올라가는 수수료는 최대 4번 까지만 올라감. 10000 -> 1000 -> 100 -> 10 -> 1

"""
def solution(enroll, referral, seller, amount):
    answer = []

    edge = dict(zip(enroll, list(zip(referral, [0] * len(enroll)))))

    while seller:
        current = seller.pop()
        a = amount.pop() * 100
        
        while current != "-":
            next, cumulative = edge[current]

            r = a // 10
            cumulative += a - r
        
            edge[current] = (next, cumulative)

            a = r
            current = next    

    for k, v in edge.items():answer.append(v[1])

    return answer
"""
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    c_index = dict(zip(enroll, range(len(enroll))))

    stack = []
    for s, a in zip(seller, amount):
        stack.append((s, a * 100))

    while stack:
        s, a = stack.pop()
        
        if s == "-": continue
        
        next = referral[c_index[s]]
        r = a // 10

        answer[c_index[s]] += a - r

        if r > 0:
            a = r
            stack.append((next, a))

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary", "mary"]	
amount = [12, 4, 2, 5, 5, 5]

print(solution(enroll, referral, seller, amount))
# [360, 958, 108, 0, 450, 18, 180, 1080]