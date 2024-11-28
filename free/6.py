from collections import defaultdict, Counter
def solution(friends: list, gifts: list) -> int:
    answer = list()
    
    give = defaultdict(list)
    take = defaultdict(list)
    
    for gift in gifts:
        g, t = gift.split()
        give[g].append(t)
        take[t].append(g)

    for i in range(len(friends)):
        count = 0
        
        for k in range(len(friends)):
            if get_count(give[friends[i]], friends[k]) > get_count(give[friends[k]], friends[i]):
                count += 1
            elif get_count(give[friends[i]], friends[k]) == get_count(give[friends[k]], friends[i]):
                if get_gift_index(friends[i], give, take) > get_gift_index(friends[k], give, take):
                    count += 1
        
        answer.append(count)
    
    return max(answer)

def get_gift_index(user: str, give: dict, take: dict ) -> int:    
    
    return len(give[user]) - len(take[user])

def get_count(users: list, rec: str) -> int:
    return Counter(users)[rec]

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends, gifts))