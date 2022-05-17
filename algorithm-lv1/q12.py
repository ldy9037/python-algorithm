# 2021 Dev-Matching - 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    
    blind_cnt = lottos.count(0)

    lottos = set(filter(lambda number: number != 0,lottos))
    same_cnt = len(lottos & set(win_nums))

    worst = 7 - same_cnt if same_cnt > 1 else 6

    best = worst
    
    if blind_cnt != 0:
        best = worst - blind_cnt if same_cnt != 0 else worst - (blind_cnt - 1)
    
    answer = [best, worst]

    return answer

lottos = [2, 3,4,5,7,8]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))