# Dev Matching - 다단계 칫솔 판매
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

    stack = []
    for s, a in zip(seller, amount):
        stack.append((s, a * 100))

    print(stack)

    while stack:
        s, a = stack.pop()
        
        if s == "-": continue
        
        c_index = enroll.index(s)
        
        next = referral[c_index]
        r = a // 10

        answer[c_index] += a - r

        a = r
        stack.append((next, a))

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary", "mary"]	
amount = [12, 4, 2, 5, 5, 5]

print(solution(enroll, referral, seller, amount))
# [360, 958, 108, 0, 450, 18, 180, 1080]